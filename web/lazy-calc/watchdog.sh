#!/bin/bash

# Configuration
MAX_RETRIES=5
RETRY_DELAY=3
PORT=8000
SERVICE_NAME="FastAPI Service"
LOG_FILE="/app/watchdog.log"

# Handle SIGTERM gracefully
cleanup() {
    log_message "Shutting down gracefully..."
    pkill -f "uvicorn backend.main:app"
    exit 0
}

trap cleanup SIGTERM SIGINT

log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S'): $1" | tee -a "$LOG_FILE"
}

check_service() {
    # Check for any defunct processes
    if ps aux | grep "[d]efunct" > /dev/null; then
        log_message "Defunct processes found - service needs restart"
        return 1
    fi
    
    log_message "No defunct processes found - service is running normally"
    return 0
}

start_service() {
    log_message "Starting $SERVICE_NAME..."
    uvicorn backend.main:app --host 0.0.0.0 --port $PORT --reload > /app/uvicorn.log 2>&1 &
    UVICORN_PID=$!
    log_message "Started uvicorn with PID: $UVICORN_PID"
    sleep 2
    
    # Verify if process is still running
    if ps -p $UVICORN_PID > /dev/null; then
        log_message "Service started successfully"
        return 0
    else
        log_message "Service failed to start properly"
        return 1
    fi
}

stop_service() {
    log_message "Stopping any existing service processes..."
    pkill -f "uvicorn backend.main:app"
    # Clean up any defunct processes
    pkill -9 -f "uvicorn backend.main:app"
    sleep 1
}

monitor_service() {
    local retry_count=0
    
    while true; do
        if ! check_service; then
            log_message "Service needs attention!"
            log_message "Recent uvicorn logs:"
            tail -n 5 /app/uvicorn.log >> "$LOG_FILE"
            
            stop_service
            if start_service; then
                log_message "Service restarted successfully"
                retry_count=0
            else
                ((retry_count++))
                log_message "Failed restart attempt $retry_count of $MAX_RETRIES"
                
                if [ $retry_count -ge $MAX_RETRIES ]; then
                    log_message "Maximum retry attempts reached. Manual intervention required."
                    log_message "Full uvicorn logs:"
                    cat /app/uvicorn.log >> "$LOG_FILE"
                    exit 1
                fi
                
                sleep $RETRY_DELAY
            fi
        fi
        
        sleep 2
    done
}

# Ensure clean log files at startup
echo "" > "$LOG_FILE"
echo "" > /app/uvicorn.log

log_message "Watchdog starting up..."
log_message "Initial service start..."

if start_service; then
    log_message "Initial service start successful"
    monitor_service
else
    log_message "Initial service start failed"
    exit 1
fi

