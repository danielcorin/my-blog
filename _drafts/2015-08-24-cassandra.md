---
layout: post
title:  "Cassandra"
date:   2015-08-22 21:59:48
categories: code
---

Cassandra has gained traction in enterprise computing for its horizontal scalability and capacity for high data write rates. The ability to quickly build Cassandra clusters that can receive and store data injected at a high volume has perpetuated the demand for analytics at a comparable scale. However, a distributed database such as Cassandra requires tradeoffs in consistency (all nodes see the same data at the same time), availibilty (all requests receive a response indicating success or failure) and partition tolerance (system continues to operate in spite of splits due to network or hardware failure). These tradeoffs are summarized as the CAP theorem. However, the notion of tradeoffs in these database properties described by the CAP theorem is a nuance worth noting. We are not forced to sacrifice consistency entirely in favor of availibility and partition tolerance. These chioces can be made with fine granularity at the system level as discussed in Eric Brewer's paper, [CAP Twelve Years Later: How the "Rules" Have Changed](http://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed).

> Exploring these nuances requires pushing the traditional way of dealing with partitions, which is the fundamental challenge. Because partitions are rare, CAP should allow perfect C and A most of the time, but when partitions are present or perceived, a strategy that detects partitions and explicitly accounts for them is in order. This strategy should have three steps: detect partitions, enter an explicit partition mode that can limit some operations, and initiate a recovery process to restore consistency and compensate for mistakes made during a partition.

When designing a database, partition tolerance is often a system requirement. Stakeholders will justifiably require 100% uptime for their business critical systems. The implementation challenge for a distributed database then shifts to tradeoffs in availability and consistency _during_ a system partition. As Brewer mentions, specific behaviors should be defined for the identification of and performance during a system partition. To summarize, we generally assume partition tolerance is a requirement and then work to identify the tradeoffs we can make in availability and consistency. A few questions we might ask to determine this are:

- is a timely response more important than a strictly "correct" one?
- is it acceptable to have conflicting data in the system?
- 

A bank might require that a transaction be committed and propagated across the entire system before an additional transaction can be processed. This use case requires consistency over availability to prevent fraud and maintain a consistent representation of business critical data. In contrast, Instagram uses Cassandra to serve users' activity feeds. Since far less risk management is involved in handling Instagram statistics compared to bank transactions, this Cassandra cluster performs were high availability with the tradeoff of degraded consistency during system partitions. In summary, the tradeoffs you make in you Cassandra database are often dictated by your specific use case and business requirements. There is no perfect distributed database solution but making smart, strategic compromises allows your system to acheive levels performance that could not be attained with relational databases.

