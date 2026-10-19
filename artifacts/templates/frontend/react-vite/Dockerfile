FROM node:18-alpine

LABEL "com.gmc.navin3d"="smnavin65@gmail.com"

LABEL version="0.1"

WORKDIR /usr/frontend

COPY ./dist ./dist
RUN npm install -g serve

EXPOSE 3000

CMD ["serve", "-l", "3000", "-s", "dist"]
