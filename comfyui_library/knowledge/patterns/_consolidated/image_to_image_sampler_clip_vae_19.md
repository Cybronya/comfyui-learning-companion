---
name: image_to_image_sampler_clip_vae_19
type: Image To Image
frequency: 9
level: strong
coverage: 0.983556
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2.0单图编辑（GGUF加速版）_1993841057280573442.json, 图片生成/图生图/Flux2.0多图编辑工作流_1993686011580448770.json, 图片生成/图生图/Flux2DEV多图编辑_1993664042084532225.json, 图片生成/图生图/Flux2单图编辑加速版_1994696141314854914.json, 图片生成/图生图/Flux2图生图_图像编辑_1993490262106324993.json, 图片生成/图生图/Klein-9B-换头一键封神！_2034251935917805570.json, 图片生成/图生图/Klein-true-V2-单图编辑+一致性lora_2047831635298619393.json, 图片生成/图生图/flux-2-klein-单-多图编辑_2014322675694444546.json, 图片生成/图生图/flux2 dev双图编辑【全能图片V1平替】_2000078046042484738.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_19

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Flux2.0单图编辑（GGUF加速版）_1993841057280573442.json、图片生成/图生图/Flux2.0多图编辑工作流_1993686011580448770.json、图片生成/图生图/Flux2DEV多图编辑_1993664042084532225.json、图片生成/图生图/Flux2单图编辑加速版_1994696141314854914.json、图片生成/图生图/Flux2图生图_图像编辑_1993490262106324993.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/9 个有
- `UNETLoader` —— 8/9 个有
- `ConditioningZeroOut` —— 6/9 个有
- `EmptyFlux2LatentImage` —— 6/9 个有
- `FluxGuidance` —— 6/9 个有
- `ImageScaleToTotalPixels` —— 3/9 个有
- `LoraLoaderModelOnly` —— 2/9 个有
- `ModelPatchTorchSettings` —— 2/9 个有
- `PathchSageAttentionKJ` —— 2/9 个有
- `CR Prompt Text` —— 1/9 个有
- `Flux2Scheduler` —— 1/9 个有
- `ImageConcanate` —— 1/9 个有
- `PrimitiveInt` —— 1/9 个有
- `PrimitiveStringMultiline` —— 1/9 个有
- `UnetLoaderGGUF` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 6 - 20 | 9 | 64% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 6 - 20，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
