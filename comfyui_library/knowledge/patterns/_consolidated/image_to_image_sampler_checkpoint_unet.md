---
name: image_to_image_sampler_checkpoint_unet
type: Image To Image
frequency: 4
level: weak
coverage: 0.767
common_nodes: [CheckpointLoaderSimple, ImageScaleBy, KSampler, LoadImage, SUPIR_conditioner, SUPIR_decode, SUPIR_encode, SUPIR_first_stage, SUPIR_model_loader_v2, SUPIR_sample, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/27.tonnie- Krea人像写实高清放大（supir放大）（线下跑费资源）_2001054119471312897.json, 图片生成/图生图/32.tonnie-最强Wan2.2写实人像高清放大_2003192990376108033.json, 图片生成/图生图/Flux2-Klein-9B-图像修复高清放大_2012343124554686465.json, 图片生成/图生图/Qwen-edit-2511-图像高清放大修复_2012364787153379329.json]
source: knowledge_consolidation
---

# image_to_image_sampler_checkpoint_unet

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/27.tonnie- Krea人像写实高清放大（supir放大）（线下跑费资源）_2001054119471312897.json、图片生成/图生图/32.tonnie-最强Wan2.2写实人像高清放大_2003192990376108033.json、图片生成/图生图/Flux2-Klein-9B-图像修复高清放大_2012343124554686465.json、图片生成/图生图/Qwen-edit-2511-图像高清放大修复_2012364787153379329.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 4 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `ImageScaleBy`
- `KSampler`
- `LoadImage`
- `SUPIR_conditioner`
- `SUPIR_decode`
- `SUPIR_encode`
- `SUPIR_first_stage`
- `SUPIR_model_loader_v2`
- `SUPIR_sample`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 3/4 个有
- `CLIPTextEncode` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `FluxKontextImageScale` —— 2/4 个有
- `CFGNorm` —— 1/4 个有
- `DualCLIPLoader` —— 1/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `FluxGuidance` —— 1/4 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/4 个有
- `ModelSamplingAuraFlow` —— 1/4 个有
- `ModelSamplingSD3` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `ReferenceLatent` —— 1/4 个有
- `TextEncodeQwenImageEditPlus` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 10 | 4 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 4 | 33% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 0.665 | 0.2 - 1 | 4 | 41% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 10，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，4 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 0.665，观测区间 0.2 - 1，4 个样本，取值分散，一致性仅 41%
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
