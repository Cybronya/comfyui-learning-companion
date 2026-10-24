---
name: text_to_image_lora_sampler_clip_270
type: Text To Image
frequency: 7
level: weak
coverage: 0.916
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen_image_文生图_1977747366285561858.json, 图片生成/文生图/Qwen千问 _ 文生图_1953804613029908482.json, 图片生成/文生图/Qwen文生图-正负提示词_1989381394365378562.json, 图片生成/文生图/Qwen文生图_1975417957952172034.json, 图片生成/文生图/Qwen文生图基础工作流_1989984703535083522.json, 图片生成/文生图/Z-Image Turbo _ 文生图_1916516546913435650.json, 图片生成/文生图/qwen海报编辑设计_1955679085127241729.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_270

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Qwen_image_文生图_1977747366285561858.json、图片生成/文生图/Qwen千问 _ 文生图_1953804613029908482.json、图片生成/文生图/Qwen文生图-正负提示词_1989381394365378562.json、图片生成/文生图/Qwen文生图_1975417957952172034.json、图片生成/文生图/Qwen文生图基础工作流_1989984703535083522.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 5/7 个有
- `ConditioningZeroOut` —— 4/7 个有
- `PathchSageAttentionKJ` —— 4/7 个有
- `easy cleanGpuUsed` —— 4/7 个有
- `Anything Everywhere3` —— 3/7 个有
- `JjkText` —— 2/7 个有
- `Anything Everywhere` —— 1/7 个有
- `CR Latent Batch Size` —— 1/7 个有
- `DifferentialDiffusion` —— 1/7 个有
- `LayerUtility: TextJoin` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `RHHiddenNodes` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 35 | 7 | 35% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 7 | 27% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 512 | 512 - 1080 | 7 | 64% |
| 高度 | 512 | 512 - 1720 | 7 | 45% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 35，7 个样本，取值分散，一致性仅 35%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，7 个样本，取值分散，一致性仅 27%
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 1080，7 个样本
- 高度 中位数 512，观测区间 512 - 1720，7 个样本，取值分散，一致性仅 45%
- 高发问题（11/7 个样本）：Steps较低可能导致细节不足
