# L-SHACSO
Success History Adaptive Competitive Swarm Optimizer with Linear Population Reduction: Performance Benchmarking and Application in Eye Disease Detection  

## Highlights  
• We equip Success History Adaptation and Linear Population Reduction to CSO and develop L-SHACSO.  
• Comprehensive numerical experiments in CEC benchmarks and engineering problems confirm the competitiveness of L-SHACSO.  
• The sensitivity experiments are conducted to demonstrate the robustness of L-SHACSO.  
• We further integrate L-SHACSO into DenseNet and ELM to propose DenseNet-L-SHACSO-ELM for eye disease detection.  

## Abstract
Eye disease detection has achieved significant advancements thanks to artificial intelligence (AI) techniques. However, the construction of high-accuracy predictive models still faces challenges, and one reason is the deficiency of the optimizer. This paper presents an efficient optimizer named Success History Adaptive Competitive Swarm Optimizer with Linear Population Reduction (L-SHACSO). Inspired by the effective success history adaptation scheme and linear population reduction strategy in Differential Evolution (DE), we introduce these techniques into CSO to enable the automatic and intelligent adjustment of hyper-parameters during optimization thereby balancing exploration and exploitation across different phases. To thoroughly investigate the performance of L-SHACSO, we conduct extensive numerical experiments on CEC2017, CEC2020, CEC2022, and eight engineering problems. State-of-the-art optimizers including jSO and L-SHADE-cnEpSin and recently proposed metaheuristic algorithms (MAs) such as RIME and the Parrot Optimizer (PO) are employed as competitors. Experimental results confirm the superiority of L-SHACSO across various optimization tasks. Furthermore, we integrate L-SHACSO into DenseNet and Extreme Learning Machine (ELM) and propose DenseNet-L-SHACSO-ELM for eye disease detection, where the features extracted by the pre-trained DenseNet are fed into L-SHACSO-optimized ELM for classification. Experiments on public datasets confirm the feasibility and effectiveness of our proposed model, which has great potential in real-world scenarios. The source code of this research is available at https://github.com/RuiZhong961230/L-SHACSO.

## Citation
@article{Zhong:25,  
title = {Success History Adaptive Competitive Swarm Optimizer with Linear Population Reduction: Performance benchmarking and application in eye disease detection},  
journal = {Computers in Biology and Medicine},  
volume = {186},  
pages = {109587},  
year = {2025},  
issn = {0010-4825},  
doi = {https://doi.org/10.1016/j.compbiomed.2024.109587 },  
author = {Rui Zhong and Zhongmin Wang and Abdelazim G. Hussien and Essam H. Houssein and Ibrahim Al-Shourbaji and Mohamed A. Elseify and Jun Yu}  
}


## Datasets and Libraries
CEC benchmarks and Engineering problems are provided by opfunu==1.0.0 and enoppy=0.1.1 libraries, respectively, Deep learning models are provided by the Pytorch library, and the eye disease detection dataset is downloaded from https://www.kaggle.com/datasets/gunavenkatdoddi/eye-diseases-classification.
