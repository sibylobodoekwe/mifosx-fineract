FROM node:14-slim

WORKDIR /app

# Clone the Mifos X Web App repository
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/openMF/web-app.git .

# Install dependencies
RUN npm install

# Build the application
RUN npm run build

# Expose the application
EXPOSE 80

# Start the application
CMD ["npm", "start"]