# Workflow 分析输出模板（workflow_template）

> Agent 每分析一个 workflow，都按本模板生成报告。`<!-- -->` 为填写提示，正文照写。

# Workflow名称


## 基本信息

名称:

来源:

用途:


---

# 一、整体流程


输入

↓

模型处理

↓

采样

↓

后处理

↓

输出

<!-- 按实际链路填写，标注节点与数据类型，如：
LoadImage(IMAGE) → VAEEncode(LATENT) → KSampler(high noise) → KSampler(low noise) → VAEDecode(IMAGE) → VHS_VideoCombine(VIDEO) -->

---

# 二、核心节点

<!-- 每个关键节点一张卡。禁止只报节点名，必须回答"为什么存在 / 解决什么问题 / 与其他节点关系 / 是否可替换" -->

## Node:

类型:

作用:

为什么需要:

输入:

输出:


---

# 三、模型组成


Checkpoint:

VAE:

Text Encoder:

LoRA:

<!-- 视频流补充：Diffusion Model（fp8/精度）、CLIP Vision、专属视频 VAE；没有的项写"无" -->

---

# 四、关键参数


Steps:

CFG:

Sampler:

Resolution:

<!-- 视频流补充：帧数(frames) / 帧率(fps) / 时长 -->

---

# 五、工作流特点


优势:

缺点:

适合场景:


---

# 六、可优化方向


显存优化:

速度优化:

质量优化:

<!-- 每条建议都要有依据（引用具体节点/参数），没有则写"暂无" -->

---

# 七、相似Workflow

<!-- 对照 memory/workflow_index.json 中已分析的工作流；没有相似项写"暂无" -->

已有:

区别:

---

> 报告完成后必须做两件事：
> 1. 把本工作流的索引（路径、用途概述、节点统计、日期）追加到 `memory/workflow_index.json`
> 2. 分析中新学到的节点/模型/原理 → 在 `knowledge/` 对应目录建卡 → `memory/learning_records.md` 记一笔
