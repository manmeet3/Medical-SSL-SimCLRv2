# Overview
This directory contains the original implementation of simclrv2 cloned from https://github.com/google-research/simclr

The code was ran as-is for 3 phases:
1. Unlabeled pretraining (weights saved in pretraining_chkpts folder)
2. Supervised finetuning the linear head (weights saved in finetuning_chkpts folder)
3. Self-training/distillation of task predictions (See colab notebooks)


![Simclrv2 Architecture](https://miro.medium.com/max/1770/1*Co4X6v8d2i0w0e7VMhLYOQ.jpeg)



