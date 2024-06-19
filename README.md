[![cas:local CI](https://github.com/emakeiv/content_analysis_service/actions/workflows/local_ci_conf.yml/badge.svg)](https://github.com/emakeiv/content_analysis_service/actions/workflows/local_ci_conf.yml)

# Content Analysis Service

## Overview
This project aims to analyze and improve TV content data by performing various data cleaning, processing, and analysis tasks.

## Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/emakeiv/content_analysis_service.git
   cd content_analysis_service

2. **Build Docker Image**:
   ```bash
   docker build -t cas_app .

2. **Run service container**:
  ```bash
  docker run -p 80:80 cas+_app



