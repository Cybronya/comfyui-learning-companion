---
name: text_to_image_lora_sampler_clip_400
type: Text To Image
frequency: 5
level: moderate
coverage: 0.8316
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize, ImageMergeTileList, KSampler, KSamplerAdvanced, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, ResizeImageMaskNode, ResolutionSelector, SaveImage, Seed (rgthree), SeedVR2Conditioning, SeedVR2PostProcessing, SeedVR2Preprocess, SplitImageToTileList, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/HerRAW-v0.1 配套工作流_2088951905115533314.json, 图片生成/文生图/HerRAW-v0.1 配套工作流_2105122285165301761.json, 图片生成/文生图/VividMuse HerRAW-v0.1配套｜文生图人像写真直出_2089416825527431169.json, 图片生成/文生图/文生图Krea2_2095491303940386817.json, 图片生成/文生图/文生图Z-Image_2095484115935125506.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_400

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/HerRAW-v0.1 配套工作流_2088951905115533314.json、图片生成/文生图/HerRAW-v0.1 配套工作流_2105122285165301761.json、图片生成/文生图/VividMuse HerRAW-v0.1配套｜文生图人像写真直出_2089416825527431169.json、图片生成/文生图/文生图Krea2_2095491303940386817.json、图片生成/文生图/文生图Z-Image_2095484115935125506.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `ImageMergeTileList`
- `KSampler`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `ResizeImageMaskNode`
- `ResolutionSelector`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2Conditioning`
- `SeedVR2PostProcessing`
- `SeedVR2Preprocess`
- `SplitImageToTileList`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 3/5 个有
- `ImageScale` —— 2/5 个有
- `JjkText` —— 1/5 个有
- `solarL_SaveImagesToZip` —— 1/5 个有
- `孤海注释` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 80 - 512 | 5 | 59% |
| 高度 | 512 | 80 - 512 | 5 | 59% |
| 采样步数 | randomize | - | 5 | 40% |
| Prompt 约束强度(CFG) | 8 | 4.5 - 8 | 5 | 81% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | ddim | - | 5 | 40% |
| 重绘幅度 | beta | - | 5 | 40% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 80 - 512，5 个样本
- 高度 中位数 512，观测区间 80 - 512，5 个样本
- 采样步数 最常用 randomize，5 个样本，一致性 40%
- Prompt 约束强度(CFG) 中位数 8，观测区间 4.5 - 8，5 个样本，取值集中（一致性 81%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 ddim，5 个样本，一致性 40%
- 重绘幅度 最常用 beta，5 个样本，一致性 40%
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足
