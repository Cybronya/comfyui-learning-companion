---
name: unknown_workflow_lora_sampler_unet_262
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.885333
common_nodes: [CLIPLoader, CR Text, CR Text Replace, EmptyLatentImage, ExtractLinesByIndex, ImageScale, ImageScaleToTotalPixels, JWStringConcat, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, Qwen3_VQA, SaveImage, Text Multiline, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy convertAnything, easy promptList, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/分镜图自动提示词_2001210347631542273.json, 图片生成/图生图/分镜图自动提示词_2041194194231894018.json, 平台全量/一键生成分镜图 全能图片2.0（适配15秒视频） Gemini 3_2034511187613851650.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_262

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/分镜图自动提示词_2001210347631542273.json、图片生成/图生图/分镜图自动提示词_2041194194231894018.json、平台全量/一键生成分镜图 全能图片2.0（适配15秒视频） Gemini 3_2034511187613851650.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CR Text`
- `CR Text Replace`
- `EmptyLatentImage`
- `ExtractLinesByIndex`
- `ImageScale`
- `ImageScaleToTotalPixels`
- `JWStringConcat`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `Qwen3_VQA`
- `SaveImage`
- `Text Multiline`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy convertAnything`
- `easy promptList`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `ImpactInt` —— 1/3 个有
- `ImpactMakeImageBatch` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LayerUtility: NanoBananaImageScale` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/3 个有
- `Repeater|pysssss` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `easy promptConcat` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1536 | 1536 - 1536 | 3 | 100% |
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
