---
name: text_to_image_upscale_latent_upscale_face_detailer_2
type: Text To Image
frequency: 2
level: weak
coverage: 0.8105
common_nodes: [CLIPSetLastLayer, CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, FaceDetailer, Fast Groups Bypasser (rgthree), ImageUpscaleWithModel, KSampler, LatentUpscaleBy, PreviewImage, SAMLoader, SaveImage, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/文生图/RF预测(Rectified Flow )_2004349648317939713.json, 图片生成/文生图/摸鱼仙人-基础文生图_1994032235412127745.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_face_detailer_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/RF预测(Rectified Flow )_2004349648317939713.json、图片生成/文生图/摸鱼仙人-基础文生图_1994032235412127745.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `FaceDetailer`
- `Fast Groups Bypasser (rgthree)`
- `ImageUpscaleWithModel`
- `KSampler`
- `LatentUpscaleBy`
- `PreviewImage`
- `SAMLoader`
- `SaveImage`
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 1/2 个有
- `ModelSamplingSD3` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1536 | - | 2 | 100% |
| 采样步数 | 25 | - | 2 | 80% |
| Prompt 约束强度(CFG) | 5 | - | 2 | 80% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.65 | - | 2 | 46% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 5，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.65，样本不足，未给区间，2 个样本，取值分散，一致性仅 46%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
