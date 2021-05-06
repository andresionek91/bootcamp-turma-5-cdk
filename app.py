#!/usr/bin/env python3
import os

from aws_cdk import core
from bootcamp_cdk_turma_5.bootcamp_cdk_turma_5_stack import BootcampCdkTurma5Stack


app = core.App()
BootcampCdkTurma5Stack(app, "BootcampCdkTurma5Stack")
app.synth()
