---
name: image_to_image_sampler_clip_unet_81
type: Image To Image
frequency: 7
level: moderate
coverage: 0.869286
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ImageResize+, ImageScaleBy, KSampler, KSamplerAdvanced, LoadImage, ModelSamplingAuraFlow, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2 Klein 8K 完美高清修复+放大_2019215002783195137.json, 图片生成/图生图/Flux2-Klein 高清修复+细节还原+8K 放大_2040437717317718018.json, 图片生成/图生图/Flux2-Klein 高清修复+细节还原+8K 放大_2041331980343713793.json, 图片生成/图生图/flux-2-klei洗图 去Ai感 高清修复 细节增强 告别塑料感_2098998012981899265.json, 图片生成/图生图/蒜香卡普v1 Flux2-Klein 高清修复+细节还原+8K 放大 颜色匹配_2041546360595423233.json, 平台全量/老照片修复+图片高清放大 FLUX.2-klein-9b+Zimage高清修复细节 去除AI感极致_2031937095199100930.json, 平台全量/老照片修复+高清放大flux-2-kleir_2015773629597880321.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_81

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein 8K 完美高清修复+放大_2019215002783195137.json、图片生成/图生图/Flux2-Klein 高清修复+细节还原+8K 放大_2040437717317718018.json、图片生成/图生图/Flux2-Klein 高清修复+细节还原+8K 放大_2041331980343713793.json、图片生成/图生图/flux-2-klei洗图 去Ai感 高清修复 细节增强 告别塑料感_2098998012981899265.json、图片生成/图生图/蒜香卡普v1 Flux2-Klein 高清修复+细节还原+8K 放大 颜色匹配_2041546360595423233.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `RunningHub Deepcleaner` —— 6/7 个有
- `RHHiddenNodes` —— 5/7 个有
- `SetNode` —— 5/7 个有
- `GetImageSize+` —— 4/7 个有
- `Image Comparer (rgthree)` —— 4/7 个有
- `ImageCASharpening+` —— 4/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/7 个有
- `PrimitiveFloat` —— 4/7 个有
- `TTP_Image_Assy` —— 4/7 个有
- `EmptyFlux2LatentImage` —— 3/7 个有
- `Float` —— 3/7 个有
- `LoraLoaderModelOnly` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `RH_Captioner` —— 2/7 个有
- `ColorMatchV2` —— 1/7 个有
- `GetNode` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 7 | 13% |
| 采样算法 | 1 | - | 7 | 43% |
| 调度器 | simple | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，7 个样本，取值分散，一致性仅 13%
- 采样算法 最常用 1，7 个样本，一致性 43%
- 调度器 最常用 simple，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
