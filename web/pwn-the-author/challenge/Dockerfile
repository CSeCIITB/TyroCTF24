FROM node:20

WORKDIR /app

COPY bot.js app.js index.ejs fetch.html /app
COPY package.json package-lock.json /app

RUN npm install
RUN apt-get update
RUN npx playwright install --with-deps chromium

ENV FLAG="tyroCTF{54m351t3_15_n0n3_53cur3}"
ENV HOST="https://iitbtrustlab-pwn-the-author.chals.io/"

CMD ["node", "app.js"]
EXPOSE 3000
