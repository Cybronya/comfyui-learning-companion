---
name: image_to_image_lora_sampler_unet_34
type: Image To Image
frequency: 13
level: moderate
coverage: 0.922615
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/3D转绘-Qwen-Image-Edit图像编辑-Comfy官方_1970486961637105665.json, 图片生成/图生图/3D转绘-Qwen-Image-Edit图像编辑-Comfy官方_2018211066441900034.json, 图片生成/图生图/51.tonnie-Qwen Edit 下一个镜头（效果不好）_2007931488599281666.json, 图片生成/图生图/57.tonnie-2509换脸_2008688247454568450.json, 图片生成/图生图/67.tonnie--2511改背景、换角度_2009983274596179970.json, 图片生成/图生图/68.tonnie-2511位移、质量下降及色差_2009989683740155905.json, 图片生成/图生图/FireRed Image edit_2030887570980212737.json, 图片生成/图生图/Qwen-image-2509-人物镜头多角度展示_1995104571196366850.json, 图片生成/图生图/Qwen-image-2511-Multiple-Angles-LoRA_2013960041979715586.json, 图片生成/图生图/Qwen-image-2511-人物镜头多角度展示_2006023840396218370.json, 图片生成/图生图/WH-AI-Studio-千问2511-一键人物镜头多角度展示（人物固定版）_2021135812963864577.json, 图片生成/图生图/WH-AI-Studio-千问2511-一键人物镜头多角度展示（脸部跟随版）_2015620861742555138.json, 图片生成/图生图/ygd生图-多图生成多角度-QwenEdit_1988117156808269826.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_34

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/3D转绘-Qwen-Image-Edit图像编辑-Comfy官方_1970486961637105665.json、图片生成/图生图/3D转绘-Qwen-Image-Edit图像编辑-Comfy官方_2018211066441900034.json、图片生成/图生图/51.tonnie-Qwen Edit 下一个镜头（效果不好）_2007931488599281666.json、图片生成/图生图/57.tonnie-2509换脸_2008688247454568450.json、图片生成/图生图/67.tonnie--2511改背景、换角度_2009983274596179970.json…）

- **类型**：Image To Image
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImageEditPlus` —— 12/13 个有
- `Text Multiline` —— 9/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/13 个有
- `easy promptLine` —— 7/13 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 6/13 个有
- `ConditioningZeroOut` —— 5/13 个有
- `ImageScaleToTotalPixels` —— 4/13 个有
- `AddLabel` —— 3/13 个有
- `ImageResizeKJv2` —— 2/13 个有
- `ImageStitch` —— 2/13 个有
- `PreviewImage` —— 2/13 个有
- `Fast Groups Bypasser (rgthree)` —— 1/13 个有
- `GetImageSizeAndCount` —— 1/13 个有
- `InpaintCrop` —— 1/13 个有
- `InpaintStitch` —— 1/13 个有
- `Int` —— 1/13 个有
- `SetNode` —— 1/13 个有
- `easy seed` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 13 | 60% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 13 | 56% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，13 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，13 个样本
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（7/13 个样本）：Steps较低可能导致细节不足
