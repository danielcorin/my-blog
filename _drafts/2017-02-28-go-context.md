---
layout: post
title:  "Setting values with Go context"
date:   2017-02-28 20:30:00
categories: code
---

The use of `context` in Go can help you pass metadata through your program with helpful, related information about a call.

{% highlight go %}
package main

import (
    "context"
    "fmt"
)

type MyHandler interface {
    MessageUser(context.Context, string, string, string) bool
}

type myHandler struct {
    Environment string
    Service     myService
    Logger logger
}

func (handler myHandler) MessageUser(
    ctx context.Context,
    fromUser string,
    toUser string,
    message string,
) bool {
    return handler.Service.SendMessage(ctx, fromUser, toUser, message)
}

type MyService interface {
    SendMessage(context.Context, string, string, string) bool
}

type myService struct {
    Gateway myGateway
}

func (service myService) SendMessage(
    ctx context.Context,
    fromUser string,
    toUser string,
    message string,
) bool {
    return service.Gateway.TweetAtUser(ctx, fromUser, toUser, message)
}

type MyGateway interface {
    EmailUser(context.Context, string, string, string) bool
}

type myGateway struct{}

func (gateway myGateway) TweetAtUser(
    ctx context.Context,
    fromUser string,
    toUser string,
    message string,
) bool {
    fmt.Printf("Sending email from %s to %s\n", fromUser, toUser)
    fmt.Printf("Message: %s\n", message)
    return true
}

func main() {
    myGateway := myGateway{}
    myService := myService{
        Gateway: myGateway,
    }
    myHandler := myHandler{
        Environment: "dev",
        Service:     myService,
    }
    ctx := context.TODO()
    myHandler.MessageUser(ctx, "@danielcorin", "@golang", "Hi, Gopher")
}
{% endhighlight %}
https://play.golang.org/p/9lKmUGvukF