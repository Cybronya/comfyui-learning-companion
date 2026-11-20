---
name: image_to_image_sampler_clip_vae_47
type: Image To Image
frequency: 4
level: strong
coverage: 0.74025
common_nodes: [CLIPTextEncode, Display Any (rgthree), Image Comparer (rgthree), KSampler, LoadImage, SaveImage, Text Concatenate, VAEDecode, VAEEncode, WD14Tagger|pysssss, ttN text]
problems: []
missing: []
members: [图片生成/图生图/将你的照片来变成黏土风格吧！_1892079729086783490.json, 图片生成/图生图/照片批量像素化_1892166474004602881.json, 平台全量/图片转像素风 _ Image To Pixel Style_1864561925345460225.json, 平台全量/轻黏土风格化_1846189877489451010.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_47

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/将你的照片来变成黏土风格吧！_1892079729086783490.json、图片生成/图生图/照片批量像素化_1892166474004602881.json、平台全量/图片转像素风 _ Image To Pixel Style_1864561925345460225.json、平台全量/轻黏土风格化_1846189877489451010.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `Display Any (rgthree)`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `Text Concatenate`
- `VAEDecode`
- `VAEEncode`
- `WD14Tagger|pysssss`
- `ttN text`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `CheckpointLoaderSimple` —— 2/4 个有
- `IPAdapterAdvanced` —— 2/4 个有
- `IPAdapterFaceID` —— 2/4 个有
- `IPAdapterUnifiedLoader` —— 2/4 个有
- `IPAdapterUnifiedLoaderFaceID` —— 2/4 个有
- `Image Pixelate` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `workflow/模型` —— 2/4 个有
- `ImageResizeKJ` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 5 | 5 - 5 | 4 | 100% |
| 采样算法 | euler_ancestral | - | 4 | 100% |
| 调度器 | normal | - | 4 | 100% |
| 重绘幅度 | 0.58 | 0.58 - 0.58 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 5 - 5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 100%
- 重绘幅度 中位数 0.58，观测区间 0.58 - 0.58，4 个样本，取值集中（一致性 100%）
