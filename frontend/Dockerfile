# Use Node.js as a builder for the frontend
FROM node:14 AS builder

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy all frontend files
COPY . .

# Use Nginx to serve the frontend
FROM nginx:latest AS production
COPY --from=builder /app /usr/share/nginx/html
EXPOSE 80

