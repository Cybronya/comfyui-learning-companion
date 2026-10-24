---
name: text_to_image_upscale_sampler_clip_33
type: Text To Image
frequency: 3
level: moderate
coverage: 0.799667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageUpscaleWithModel, KSampler, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/iL出图Zimage质感_2035518069124108290.json, 图片生成/文生图/摸鱼仙人-anima-preview2_2033441061263122433.json, 图片生成/文生图/文生图+图生图+基础放大课堂教学_2038512641508904962.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_33

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/iL出图Zimage质感_2035518069124108290.json、图片生成/文生图/摸鱼仙人-anima-preview2_2033441061263122433.json、图片生成/文生图/文生图+图生图+基础放大课堂教学_2038512641508904962.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ImageUpscaleWithModel`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `FaceDetailer` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `UltralyticsDetectorProvider` —— 2/3 个有
- `ImageScaleBy` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有
- `TextInput_` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 12 | 3 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 3 | 24% |
| 采样算法 | euler_ancestral | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 0.6 | 0.3 - 0.7 | 3 | 68% |
| 宽度 | 832 | 720 - 1280 | 3 | 74% |
| 高度 | 1280 | 1216 - 1920 | 3 | 78% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 12，3 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，3 个样本，取值分散，一致性仅 24%
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 0.6，观测区间 0.3 - 0.7，3 个样本
- 宽度 中位数 832，观测区间 720 - 1280，3 个样本
- 高度 中位数 1280，观测区间 1216 - 1920，3 个样本
