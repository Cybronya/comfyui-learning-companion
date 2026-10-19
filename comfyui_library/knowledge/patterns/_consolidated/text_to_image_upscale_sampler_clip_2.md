---
name: text_to_image_upscale_sampler_clip_2
type: Text To Image
frequency: 2
level: weak
coverage: 0.9645
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, ImageUpscaleWithModel, KSampler, SaveImage, UpscaleModelLoader, VAEDecode]
problems: []
missing: [CR Text]
members: [图片生成/文生图/1934952424287182850.json, 图片生成/文生图/1934957385754550274.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1934952424287182850.json、图片生成/文生图/1934957385754550274.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `ImageUpscaleWithModel`
- `KSampler`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `FaceDetailer` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `UltralyticsDetectorProvider` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 6.25 | - | 2 | 72% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 616 | - | 2 | 83% |
| 高度 | 896 | - | 2 | 57% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6.25，样本不足，未给区间，2 个样本
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 616，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
- 高度 中位数 896，样本不足，未给区间，2 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
