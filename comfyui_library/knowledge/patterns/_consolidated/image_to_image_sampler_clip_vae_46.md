---
name: image_to_image_sampler_clip_vae_46
type: Image To Image
frequency: 2
level: weak
coverage: 0.957
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Get Image Size, ImageResizeKJv2, KSampler, LayerUtility: FluxKontextImageScale, LoadImage, Qwen3_VQA, QwenMultiangleCameraNode, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Flux-2-klein-9B六合一工作流合集_2012415580581662721.json, 图片生成/文生图/Klein-9B-NewAsia六合一工作流合集_2060296922392514562.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_46

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Flux-2-klein-9B六合一工作流合集_2012415580581662721.json、图片生成/文生图/Klein-9B-NewAsia六合一工作流合集_2060296922392514562.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Get Image Size`
- `ImageResizeKJv2`
- `KSampler`
- `LayerUtility: FluxKontextImageScale`
- `LoadImage`
- `Qwen3_VQA`
- `QwenMultiangleCameraNode`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `FluxKontextImageScale` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `UNETLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（12/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
