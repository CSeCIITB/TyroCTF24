# Dockerfile
FROM --platform=linux/amd64 nginx:alpine

# Copy custom Nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy your static files
COPY index.html /usr/share/nginx/html/index.html
COPY static/ /usr/share/nginx/html/static/
COPY most_secure_folder/ /usr/share/nginx/html/most_secure_folder/
COPY robots.txt /usr/share/nginx/html/robots.txt
COPY .git /usr/share/nginx/html/.git

EXPOSE 80
