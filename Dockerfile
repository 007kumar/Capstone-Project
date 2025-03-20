FROM nginx:alpine

RUN apk update && apk upgrade && rm -rf /var/cache/apk/*

COPY html/index.html /usr/share/nginx/html/

# Expose port
EXPOSE 80

# Start Nginx service
CMD ["nginx", "-g", "daemon off;"]
