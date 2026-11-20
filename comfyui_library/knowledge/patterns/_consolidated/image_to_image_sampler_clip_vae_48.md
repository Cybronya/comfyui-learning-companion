---
name: image_to_image_sampler_clip_vae_48
type: Image To Image
frequency: 4
level: strong
coverage: 0.933
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, ImageResizeKJv2, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Flux-2-klein-9B六合一工作流合集_2012415580581662721.json, 图片生成/文生图/Klein-9B-NewAsia六合一工作流合集_2060296922392514562.json, 平台全量/换装换脸多图编辑 加强版 保持图像一致性Flux2-Klein-9B Consis_2052928033895526401.json, 平台全量/自然换脸换装Klein-9B+Consis多图编辑 保持图像一致性_2056244081130557441.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_48

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Flux-2-klein-9B六合一工作流合集_2012415580581662721.json、图片生成/文生图/Klein-9B-NewAsia六合一工作流合集_2060296922392514562.json、平台全量/换装换脸多图编辑 加强版 保持图像一致性Flux2-Klein-9B Consis_2052928033895526401.json、平台全量/自然换脸换装Klein-9B+Consis多图编辑 保持图像一致性_2056244081130557441.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `Get Image Size` —— 2/4 个有
- `LayerUtility: FluxKontextImageScale` —— 2/4 个有
- `Qwen3_VQA` —— 2/4 个有
- `QwenMultiangleCameraNode` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `CheckpointLoaderSimple` —— 1/4 个有
- `FluxKontextImageScale` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5.5 | 5 - 6 | 4 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5.5，观测区间 5 - 6，4 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（16/4 个样本）：Steps较低可能导致细节不足
