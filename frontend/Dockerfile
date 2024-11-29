# Use the official Nginx image as the base
FROM nginx:alpine

# Copy the static content (HTML, JS) into Nginx's HTML directory
COPY index.html /usr/share/nginx/html/
COPY app.js /usr/share/nginx/html/

# Expose port 80
EXPOSE 80

