---
name: text_to_image_sampler_clip_unet_168
type: Text To Image
frequency: 3
level: strong
coverage: 0.960667
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptyLatentImage, FluxKontextImageScale, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen-Edit 多图融合｜电商海报_1958013536578547713.json, 图片生成/图生图/Qwen-edit IP形象三视图_1970744457626873858.json, 图片生成/图生图/Qwen-edit单图参考_1970746794273632258.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_168

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen-Edit 多图融合｜电商海报_1958013536578547713.json、图片生成/图生图/Qwen-edit IP形象三视图_1970744457626873858.json、图片生成/图生图/Qwen-edit单图参考_1970746794273632258.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptyLatentImage`
- `FluxKontextImageScale`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageCropByRatio` —— 2/3 个有
- `LoadImageFromUrl` —— 2/3 个有
- `Note Plus (mtb)` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `VAEEncode` —— 1/3 个有
- `easy imageConcat` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 2.5 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1536 | 960 - 1536 | 3 | 80% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 2.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1536，观测区间 960 - 1536，3 个样本
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
