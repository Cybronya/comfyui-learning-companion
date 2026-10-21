---
name: text_to_image_sampler_clip_unet_152
type: Text To Image
frequency: 2
level: weak
coverage: 0.884
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1973209775687208961.json, 图片生成/文生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清直出_2083015619733180417.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_152

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1973209775687208961.json、图片生成/文生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清直出_2083015619733180417.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `ImageStitch` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `RunningHub Deepcleaner` —— 1/2 个有
- `SeedVR2` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1344 | - | 2 | 57% |
| 高度 | 1052 | - | 2 | 97% |
| 采样步数 | 14 | - | 2 | 57% |
| Prompt 约束强度(CFG) | 1.25 | - | 2 | 80% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1344，样本不足，未给区间，2 个样本
- 高度 中位数 1052，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
- 采样步数 中位数 14，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1.25，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
