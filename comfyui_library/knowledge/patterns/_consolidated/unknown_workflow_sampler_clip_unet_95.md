---
name: unknown_workflow_sampler_clip_unet_95
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.989
common_nodes: [CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLux1.D（2.5d头像框）_2062090702082891778.json, 图片生成/文生图/Flux.1文生图工作流_2100500167958024193.json, 图片生成/文生图/Qwen Image 2512 平铺商品摄影｜LoRA 商品棚拍_2091542940056375297.json, 图片生成/文生图/Qwen_Image_2512_商业商品摄影_LoRA｜单品棚拍_2100057678470012930.json, 图片生成/文生图/Qwen_Image_2512_商业商品摄影_LoRA｜单品棚拍_2100137995608346626.json, 图片生成/文生图/Z-image-base蛋挞质感增强_2026161469645135874.json, 图片生成/文生图/flux1文生图-头像-2D（金属边框）_2059557977534849025.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_95

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/FLux1.D（2.5d头像框）_2062090702082891778.json、图片生成/文生图/Flux.1文生图工作流_2100500167958024193.json、图片生成/文生图/Qwen Image 2512 平铺商品摄影｜LoRA 商品棚拍_2091542940056375297.json、图片生成/文生图/Qwen_Image_2512_商业商品摄影_LoRA｜单品棚拍_2100057678470012930.json、图片生成/文生图/Qwen_Image_2512_商业商品摄影_LoRA｜单品棚拍_2100137995608346626.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 6/7 个有
- `CLIPLoader` —— 4/7 个有
- `DualCLIPLoader` —— 3/7 个有
- `FluxGuidance` —— 3/7 个有
- `DeepTranslatorTextNode` —— 2/7 个有
- `StringFunction|pysssss` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `ImageScaleBy` —— 1/7 个有
- `ImageUpscaleWithModel` —— 1/7 个有
- `ModelSamplingAuraFlow` —— 1/7 个有
- `UpscaleModelLoader` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.9 | 0.5 - 1 | 6 | 75% |
| LoRA 文本强度 | 1 | 1 - 1 | 6 | 100% |
| 采样步数 | 20 | 20 - 30 | 7 | 81% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 7 | 45% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.9，观测区间 0.5 - 1，6 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 20 - 30，7 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，7 个样本，取值分散，一致性仅 45%
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
