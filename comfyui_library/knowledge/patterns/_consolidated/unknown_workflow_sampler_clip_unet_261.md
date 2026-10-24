---
name: unknown_workflow_sampler_clip_unet_261
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9818
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLux1.D（2.5d头像框）_2062090702082891778.json, 图片生成/文生图/Flux.1文生图工作流_2100500167958024193.json, 图片生成/文生图/Flux_Krea_t2i_1960596890238746626.json, 图片生成/文生图/Newbie Image 文生图_2025554845473705985.json, 图片生成/文生图/flux1文生图-头像-2D（金属边框）_2059557977534849025.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_261

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/FLux1.D（2.5d头像框）_2062090702082891778.json、图片生成/文生图/Flux.1文生图工作流_2100500167958024193.json、图片生成/文生图/Flux_Krea_t2i_1960596890238746626.json、图片生成/文生图/Newbie Image 文生图_2025554845473705985.json、图片生成/文生图/flux1文生图-头像-2D（金属边框）_2059557977534849025.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxGuidance` —— 3/5 个有
- `DeepTranslatorTextNode` —— 2/5 个有
- `LoraLoader` —— 2/5 个有
- `StringFunction|pysssss` —— 2/5 个有
- `CR Text` —— 1/5 个有
- `ImageScaleBy` —— 1/5 个有
- `ImageUpscaleWithModel` —— 1/5 个有
- `RescaleCFG` —— 1/5 个有
- `UpscaleModelLoader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.65 | - | 2 | 77% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 25 | 20 - 30 | 5 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 5 | 18% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.65，样本不足，未给区间，2 个样本
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 20 - 30，5 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，5 个样本，取值分散，一致性仅 18%
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
