---
name: image_to_image_sampler_clip_checkpoint_13
type: Image To Image
frequency: 3
level: moderate
coverage: 0.8
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ICLightConditioning, KSampler, LoadAndApplyICLightUnet, LoadImage, MaskToImage, PreviewImage, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/IC-Light V2官方工作流_1930184992649854977.json, 图片生成/图生图/iclight1.5打光_1904110598605676545.json, 平台全量/IC-linght全系打光_2017418690014224385.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_checkpoint_13

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/IC-Light V2官方工作流_1930184992649854977.json、图片生成/图生图/iclight1.5打光_1904110598605676545.json、平台全量/IC-linght全系打光_2017418690014224385.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ICLightConditioning`
- `KSampler`
- `LoadAndApplyICLightUnet`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `CreateShapeMask` —— 2/3 个有
- `GrowMaskWithBlur` —— 2/3 个有
- `ImageResize+` —— 2/3 个有
- `RemapMaskRange` —— 2/3 个有
- `BRIAAI Matting` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageScale` —— 1/3 个有
- `ImageScaleBy` —— 1/3 个有
- `MaskBlur+` —— 1/3 个有
- `RemapImageRange` —— 1/3 个有
- `RepeatLatentBatch` —— 1/3 个有
- `VAELoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 30 | 3 | 84% |
| Prompt 约束强度(CFG) | 3.5 | 2.05 - 8 | 3 | 44% |
| 采样算法 | dpmpp_2m | - | 3 | 67% |
| 调度器 | karras | - | 3 | 67% |
| 重绘幅度 | 0.94 | 0.9 - 1 | 3 | 96% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 30，3 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 2.05 - 8，3 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 dpmpp_2m，3 个样本，一致性 67%
- 调度器 最常用 karras，3 个样本，一致性 67%
- 重绘幅度 中位数 0.94，观测区间 0.9 - 1，3 个样本，取值集中（一致性 96%）
