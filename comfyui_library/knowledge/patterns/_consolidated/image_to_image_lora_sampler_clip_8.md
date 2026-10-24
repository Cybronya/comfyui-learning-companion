---
name: image_to_image_lora_sampler_clip_8
type: Image To Image
frequency: 16
level: moderate
coverage: 0.894125
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ImageScaleBy, KSampler, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, RH_Captioner, ReferenceLatent, RunningHub Deepcleaner, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: ["图片生成/图生图/人像超高清修复Ultra-High-Definition Portrait Retouching,_2098940600866394114.json", "图片生成/图生图/人像超高清修复Ultra-High-Definition_Portrait_Retouching,_2099339782718574593.json", "图片生成/图生图/人像超高清修复Ultra-High-Definition_Portrait_Retouching,_2099671450700570625.json", 图片生成/图生图/人像超高清修复_2041837002299023362.json, 图片生成/图生图/人像超高清修复五官锐化细节重生_2105578771867856898.json, 图片生成/图生图/人像超高清修复五官锐化细节重生_2108015810252992513.json, 图片生成/图生图/人像高清放大-无偏移-重绘+真实化_2027587184131317762.json, 图片生成/图生图/图生图---Flux2 Klein控油+高清放大+增强细节_2047571214654251010.json, 图片生成/图生图/控油+高清放大+增强细节- 邻家AI大女孩_2044317203054469122.json, 图片生成/图生图/无损修复去AI感 Flux 2-klein9b_2064244264825090050.json, 图片生成/图生图/曾经像素低模糊不清的照片有救了！Flux2 Klein控油+高清放大+增强细节_2019672759852339202.json, 图片生成/图生图/模糊图片修复+放大 增补原图细节_2070051923562156034.json, 图片生成/图生图/模糊图片修复+放大_增补原图细节_2096873219700645889.json, 图片生成/图生图/模糊图片修复+放大_增补原图细节_2097166080690184193.json, 图片生成/图生图/洗图去AI感_2095684072474501121.json, 图片生成/图生图/高清修复+去AI感 Flux 2-klein9b_2015799392439115778.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_8

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/人像超高清修复Ultra-High-Definition Portrait Retouching,_2098940600866394114.json、图片生成/图生图/人像超高清修复Ultra-High-Definition_Portrait_Retouching,_2099339782718574593.json、图片生成/图生图/人像超高清修复Ultra-High-Definition_Portrait_Retouching,_2099671450700570625.json、图片生成/图生图/人像超高清修复_2041837002299023362.json、图片生成/图生图/人像超高清修复五官锐化细节重生_2105578771867856898.json…）

- **类型**：Image To Image
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ImageScaleBy`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `RH_Captioner`
- `ReferenceLatent`
- `RunningHub Deepcleaner`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 15/16 个有
- `Image Comparer (rgthree)` —— 13/16 个有
- `CR Prompt Text` —— 10/16 个有
- `EmptyFlux2LatentImage` —— 10/16 个有
- `GetImageSize` —— 10/16 个有
- `easy cleanGpuUsed` —— 7/16 个有
- `ColorMatch` —— 6/16 个有
- `Fast Groups Bypasser (rgthree)` —— 6/16 个有
- `LatentUpscaleBy` —— 6/16 个有
- `workflow>高清节点` —— 6/16 个有
- `Float` —— 3/16 个有
- `Int` —— 3/16 个有
- `GrowMask` —— 1/16 个有
- `ImageUpscaleWithModel` —— 1/16 个有
- `InvertMask` —— 1/16 个有
- `JoinImageWithAlpha` —— 1/16 个有
- `LayerMask: BiRefNetUltraV2` —— 1/16 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/16 个有
- `Upscale Model Loader` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 15 | 16 | 0% |
| 采样算法 | euler_ancestral | - | 16 | 38% |
| 调度器 | simple | - | 16 | 56% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 15，16 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler_ancestral，16 个样本，一致性 38%
- 调度器 最常用 simple，16 个样本，一致性 56%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 15，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 高发问题（16/16 个样本）：Steps较低可能导致细节不足
