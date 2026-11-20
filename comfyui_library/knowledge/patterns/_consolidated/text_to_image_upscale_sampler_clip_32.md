---
name: text_to_image_upscale_sampler_clip_32
type: Text To Image
frequency: 4
level: moderate
coverage: 0.906
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageUpscaleWithModel, KSampler, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/iL出图Zimage质感_2035518069124108290.json, 图片生成/文生图/krea2_turbo文生图+Lora+四倍高清放大_2080125976993947650.json, 图片生成/文生图/摄影-文生图-Z-image-turbo_2096447342345015297.json, 图片生成/文生图/摸鱼仙人-anima-preview2_2033441061263122433.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_32

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/iL出图Zimage质感_2035518069124108290.json、图片生成/文生图/krea2_turbo文生图+Lora+四倍高清放大_2080125976993947650.json、图片生成/文生图/摄影-文生图-Z-image-turbo_2096447342345015297.json、图片生成/文生图/摸鱼仙人-anima-preview2_2033441061263122433.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ImageUpscaleWithModel`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `FaceDetailer` —— 2/4 个有
- `UltralyticsDetectorProvider` —— 2/4 个有
- `VAEEncode` —— 2/4 个有
- `CheckpointLoaderSimple` —— 1/4 个有
- `ImageFromBatch` —— 1/4 个有
- `ImageScaleBy` —— 1/4 个有
- `LayerColor: Brightness & Contrast` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有
- `TextInput_` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 12 | 4 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 4 | 19% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 0.8 | 0.3 - 1 | 4 | 59% |
| 宽度 | 864 | 720 - 1080 | 4 | 85% |
| 高度 | 1248 | 1152 - 1920 | 4 | 78% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 12，4 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，4 个样本，取值分散，一致性仅 19%
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 0.8，观测区间 0.3 - 1，4 个样本
- 宽度 中位数 864，观测区间 720 - 1080，4 个样本，取值集中（一致性 85%）
- 高度 中位数 1248，观测区间 1152 - 1920，4 个样本
