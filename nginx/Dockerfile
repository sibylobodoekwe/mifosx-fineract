# Use the official nginx image as base
FROM nginx:stable-alpine

# Install necessary packages for SSL
RUN apk add --no-cache openssl

# Remove default nginx configuration
RUN rm /etc/nginx/conf.d/default.conf

# Create directory for SSL certificates
RUN mkdir -p /etc/ssl/private \
    && mkdir -p /etc/ssl/certs

# Copy nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Set proper permissions
RUN chmod 600 /etc/ssl/private/* \
    && chmod 644 /etc/ssl/certs/*

# Create nginx user if not exists
RUN adduser -D -H -u 1000 -s /sbin/nologin www-data

# Set proper ownership
RUN chown -R www-data:www-data /var/cache/nginx \
    && chown -R www-data:www-data /var/log/nginx \
    && chown -R www-data:www-data /etc/nginx/conf.d

# Create directory for nginx pid file
RUN mkdir -p /run/nginx \
    && chown -R www-data:www-data /run/nginx

# Update nginx configuration permissions
RUN chown -R www-data:www-data /etc/nginx/nginx.conf

# Set working directory
WORKDIR /etc/nginx

# Expose ports
EXPOSE 80 443

# Switch to non-root user
USER www-data

# Start nginx
CMD ["nginx", "-g", "daemon off;"]