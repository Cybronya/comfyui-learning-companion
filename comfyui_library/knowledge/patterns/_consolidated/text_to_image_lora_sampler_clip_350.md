---
name: text_to_image_lora_sampler_clip_350
type: Text To Image
frequency: 6
level: moderate
coverage: 0.757167
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetImageSize, ImageMergeTileList, KSampler, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveInt, ResizeImageMaskNode, SaveImage, SeedVR2Conditioning, SeedVR2PostProcessing, SeedVR2Preprocess, SplitImageToTileList, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/HerRAW-v0.1 配套工作流_2088951905115533314.json, 图片生成/文生图/HerRAW-v0.1 配套工作流_2105122285165301761.json, 图片生成/文生图/VividMuse HerRAW-v0.1配套｜文生图人像写真直出_2089416825527431169.json, 图片生成/文生图/文生图Krea2_2095491303940386817.json, 图片生成/文生图/文生图Z-Image_2095484115935125506.json, 平台全量/SeedVR2分块放大高清放大｜大图空间维度缩小单次处理规模_2090063710214774785.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_350

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/HerRAW-v0.1 配套工作流_2088951905115533314.json、图片生成/文生图/HerRAW-v0.1 配套工作流_2105122285165301761.json、图片生成/文生图/VividMuse HerRAW-v0.1配套｜文生图人像写真直出_2089416825527431169.json、图片生成/文生图/文生图Krea2_2095491303940386817.json、图片生成/文生图/文生图Z-Image_2095484115935125506.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetImageSize`
- `ImageMergeTileList`
- `KSampler`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `SaveImage`
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
- `ConditioningZeroOut` —— 5/6 个有
- `Fast Groups Bypasser (rgthree)` —— 5/6 个有
- `KSamplerAdvanced` —— 5/6 个有
- `PrimitiveStringMultiline` —— 5/6 个有
- `ResolutionSelector` —— 5/6 个有
- `Seed (rgthree)` —— 5/6 个有
- `PreviewImage` —— 4/6 个有
- `ImageScale` —— 3/6 个有
- `JjkText` —— 2/6 个有
- `solarL_SaveImagesToZip` —— 2/6 个有
- `孤海注释` —— 2/6 个有
- `GetNode` —— 1/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `ImageBlend` —— 1/6 个有
- `ImageBlur` —— 1/6 个有
- `JoinImageWithAlpha` —— 1/6 个有
- `LoadImage` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `SetNode` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 80 - 512 | 6 | 45% |
| 高度 | 512 | 80 - 512 | 6 | 45% |
| 采样步数 | randomize | - | 6 | 33% |
| Prompt 约束强度(CFG) | 8 | 4.5 - 8 | 6 | 76% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | ddim | - | 6 | 33% |
| 重绘幅度 | beta | - | 6 | 33% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 80 - 512，6 个样本，取值分散，一致性仅 45%
- 高度 中位数 512，观测区间 80 - 512，6 个样本，取值分散，一致性仅 45%
- 采样步数 最常用 randomize，6 个样本，一致性 33%
- Prompt 约束强度(CFG) 中位数 8，观测区间 4.5 - 8，6 个样本
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 ddim，6 个样本，一致性 33%
- 重绘幅度 最常用 beta，6 个样本，一致性 33%
- 高发问题（8/6 个样本）：Steps较低可能导致细节不足
