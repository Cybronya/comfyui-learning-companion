---
name: text_to_image_lora_sampler_clip_519
type: Text To Image
frequency: 3
level: strong
coverage: 0.891333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImageSize, Image Comparer (rgthree), JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, ResizeImageMaskNode, SaveImage, SetLatentNoiseMask, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAEEncode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1局部放大重绘流｜细节区域精准修复_2108051790385209345.json, 图片生成/图生图/Qwen Image 2.1零偏移单多图局部遮罩编辑重绘工作流，局部重绘图生图方案_2107941927051161602.json, 图片生成/图生图/Qwen Image 2.1零偏移单多图局部遮罩编辑重绘工作流，局部重绘图生图方案_2107943545071030273.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_519

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1局部放大重绘流｜细节区域精准修复_2108051790385209345.json、图片生成/图生图/Qwen Image 2.1零偏移单多图局部遮罩编辑重绘工作流，局部重绘图生图方案_2107941927051161602.json、图片生成/图生图/Qwen Image 2.1零偏移单多图局部遮罩编辑重绘工作流，局部重绘图生图方案_2107943545071030273.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `ResizeImageMaskNode`
- `SaveImage`
- `SetLatentNoiseMask`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 2/3 个有
- `RHHiddenNodes` —— 2/3 个有
- `WujiCleaner` —— 2/3 个有
- `WujiUpscaler2` —— 2/3 个有
- `LayerUtility: CropByMask V2` —— 1/3 个有
- `LayerUtility: ImageScaleRestore V2` —— 1/3 个有
- `LayerUtility: RestoreCropBox` —— 1/3 个有
- `SaveImageAdvanced` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（5/3 个样本）：Steps较低可能导致细节不足
