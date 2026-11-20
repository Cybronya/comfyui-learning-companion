---
name: unknown_workflow_lora_sampler_clip_15
type: Unknown Workflow
frequency: 22
level: moderate
coverage: 0.955818
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/剪纸风格-myshell_1967455683580923905.json, 图片生成/文生图/剪纸风格_1963167950662512641.json, 图片生成/文生图/动漫出图Qwen工作流_2019691912264945666.json, 图片生成/文生图/动漫出图Qwen工作流_2053018053553737730.json, 图片生成/文生图/千问-qwen-lora-文生图工作流_1960181642029641729.json, 图片生成/文生图/帝企鹅工作流_1980164055954526209.json, 图片生成/文生图/文生图合集_2038775252657905666.json, 图片生成/文生图/文生图合集_2049394125358764034.json, 图片生成/文生图/文生图合集（3种风格）_2038265960213258242.json, 图片生成/文生图/炼狱杏寿郎_1981285976733638658.json, 图片生成/文生图/简单手绘风格_1962501732217536513.json, 图片生成/文生图/红潮造相ZImage+LoRA文生图+VAE增加细节_2009818930566664194.json, 图片生成/文生图/赛博玄幻修仙者｜墨渊·文生图_2093285763407507458.json, 图片生成/文生图/赛博玄幻修仙者｜燕青·文生图_2093374844577599489.json, 图片生成/文生图/造相-Z-Image-Turbo-文生图工作流_2052340397992624130.json, 图片生成/文生图/阿清的AI模特文生图_2000461829648379906.json, 图片生成/文生图/陶器工作流_2071425077450727425.json, 图片生成/文生图/静帧画面工作流_2025778505488801793.json, 平台全量/赛博玄幻·湘灵 女主｜文生图_2093230034579447809.json, 平台全量/赛博玄幻修仙者｜场景设计器_2093573794328829954.json, 平台全量/赛博玄幻修仙者｜文生图_2092997570682515457.json, 平台全量/赛博玄幻修仙者｜通用修仙题材 文生图_2093683753389486081.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_15

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/文生图/剪纸风格-myshell_1967455683580923905.json、图片生成/文生图/剪纸风格_1963167950662512641.json、图片生成/文生图/动漫出图Qwen工作流_2019691912264945666.json、图片生成/文生图/动漫出图Qwen工作流_2053018053553737730.json、图片生成/文生图/千问-qwen-lora-文生图工作流_1960181642029641729.json…）

- **类型**：Unknown Workflow
- **样本数**：22
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 22 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 2/22 个有
- `PathchSageAttentionKJ` —— 2/22 个有
- `ShellAgentPluginInputText` —— 1/22 个有
- `ShellAgentPluginSaveImage` —— 1/22 个有
- `StringFunction|pysssss` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | 4 - 40 | 22 | 42% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 22 | 55% |
| 采样算法 | euler | - | 22 | 100% |
| 调度器 | simple | - | 22 | 55% |
| 重绘幅度 | 1 | 1 - 1 | 22 | 100% |
| LoRA 模型强度 | 1.25 | - | 2 | 80% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/22 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，观测区间 4 - 40，22 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，22 个样本
- 采样算法 最常用 euler，22 个样本，一致性 100%
- 调度器 最常用 simple，22 个样本，一致性 55%
- 重绘幅度 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1.25，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（14/22 个样本）：Steps较低可能导致细节不足
