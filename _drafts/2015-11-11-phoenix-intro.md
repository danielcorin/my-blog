---
layout: post
title:  "Phoenix Introduction"
date:   2015-11-11 17:28:00
categories: code
---

Pull the container from Docker hub if you don't have it

    docker pull postgres

To start a Postgres db container for testing
    
    docker run --name my-pg -p 5432:5432 -e POSTGRES_PASSWORD=<your_pass> -d postgres