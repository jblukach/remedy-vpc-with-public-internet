#!/usr/bin/env python3
import os

import aws_cdk as cdk

from remedy_vpc_with_public_internet.remedy_vpc_with_public_internet_stack import RemedyVpcWithPublicInternetStack

app = cdk.App()

RemedyVpcWithPublicInternetStack(
    app, 'RemedyVpcWithPublicInternetStack',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = os.getenv('CDK_DEFAULT_REGION')
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

cdk.Tags.of(app).add('vpc-with-public-internet','vpc-with-public-internet')

app.synth()
