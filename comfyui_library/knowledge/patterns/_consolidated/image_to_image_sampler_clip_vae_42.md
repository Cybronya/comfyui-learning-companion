---
name: image_to_image_sampler_clip_vae_42
type: Image To Image
frequency: 2
level: weak
coverage: 0.7205
common_nodes: [CLIPTextEncode, Display Any (rgthree), Image Comparer (rgthree), KSampler, LoadImage, PreviewImage, SaveImage, Text Concatenate, VAEDecode, VAEEncode, WD14Tagger|pysssss, ttN text, workflow/模型]
problems: []
missing: []
members: [图片生成/图生图/将你的照片来变成黏土风格吧！_1892079729086783490.json, 图片生成/图生图/照片批量像素化_1892166474004602881.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_42

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/将你的照片来变成黏土风格吧！_1892079729086783490.json、图片生成/图生图/照片批量像素化_1892166474004602881.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：72%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `Display Any (rgthree)`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `Text Concatenate`
- `VAEDecode`
- `VAEEncode`
- `WD14Tagger|pysssss`
- `ttN text`
- `workflow/模型`

**可变部分**（部分 workflow 才有）：
- `IPAdapterAdvanced` —— 1/2 个有
- `IPAdapterFaceID` —— 1/2 个有
- `IPAdapterUnifiedLoader` —— 1/2 个有
- `IPAdapterUnifiedLoaderFaceID` —— 1/2 个有
- `Image Pixelate` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `ImageResizeKJ` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 5 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 0.58 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 0.58，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
