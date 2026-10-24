---
name: text_to_image_lora_sampler_clip_222
type: Text To Image
frequency: 8
level: strong
coverage: 0.853125
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, ImageScaleBy, JjkText, KSampler, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux-2-Klei洗图去AI感高清修复细节增强图生图处理工具_2102135996421853185.json, 图片生成/图生图/Flux-2-Klei洗图去AI感高清修复细节增强，告别塑料感图生图方案_2103562807370412034.json, 图片生成/图生图/Flux2 Klein控油图生图精修｜高清放大增强细节_2094892914123034625.json, 图片生成/图生图/Flux2 Klein洗图去AI感 高清修复细节增强告别塑料感_2099567091627155458.json, 图片生成/图生图/控油高清放大增强细节｜Flux2 Klein图生图_2092881657077526529.json, 图片生成/图生图/高清放大增强细节｜Flux2 Klein控油图生图精修_2092692856954773506.json, 图片生成/图生图/高清放大增强细节｜Flux2_Klein控油图生图精修_2094592387850002434.json, 图片生成/图生图/高清放大增强细节｜Flux2_Klein控油图生图精修_2094724625912647681.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_222

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Flux-2-Klei洗图去AI感高清修复细节增强图生图处理工具_2102135996421853185.json、图片生成/图生图/Flux-2-Klei洗图去AI感高清修复细节增强，告别塑料感图生图方案_2103562807370412034.json、图片生成/图生图/Flux2 Klein控油图生图精修｜高清放大增强细节_2094892914123034625.json、图片生成/图生图/Flux2 Klein洗图去AI感 高清修复细节增强告别塑料感_2099567091627155458.json、图片生成/图生图/控油高清放大增强细节｜Flux2 Klein图生图_2092881657077526529.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `ImageScaleBy`
- `JjkText`
- `KSampler`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 6/8 个有
- `CR Prompt Text` —— 5/8 个有
- `GetImageSize` —— 5/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/8 个有
- `PreviewImage` —— 5/8 个有
- `RH_Captioner` —— 5/8 个有
- `RunningHub Deepcleaner` —— 5/8 个有
- `Float` —— 3/8 个有
- `GetNode` —— 3/8 个有
- `Image Comparer (rgthree)` —— 3/8 个有
- `ImageResize+` —— 3/8 个有
- `RHHiddenNodes` —— 3/8 个有
- `SetNode` —— 3/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（17/8 个样本）：Steps较低可能导致细节不足
