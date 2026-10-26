---
name: image_to_image_upscale_lora_sampler_6
type: Image To Image
frequency: 19
level: strong
coverage: 0.904158
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EditTextEncode_EditUtils, Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, Flux2KleinOutputExtractor_EditUtils, Flux2Scheduler, FluxKVCache, GetImageSize, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAEEncodeTiled, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/完美换装+双采高清直出【御川0805】】_2084911316422189057.json, 图片生成/图生图/新版人像高清放大，皮肤nice_2082286371208777729.json, 图片生成/图生图/新版人像高清放大，皮肤nice【0721】_2113792779288662018.json, 图片生成/图生图/新版人像高清放大，皮肤nice【御川0721】_2079468772016087041.json, 图片生成/图生图/新版人像高清放大，皮肤nice【御川0721】_2113796151311953921.json, 图片生成/图生图/新版人像高清放大，皮肤nice【御川0721】_2113807003230494722.json, 图片生成/图生图/新版人像高清放大，皮肤增强_2083573713554989058.json, 图片生成/图生图/男生大头优化4K_2097262151164588033.json, 图片生成/图生图/高清修复 4k细节-Krea2最新工作流_2074820750917328897.json, 图片生成/图生图/高清修复 4k细节-Krea2最新工作流_2077028032933613569.json, 图片生成/图生图/高清修复 4k细节-Krea2最新工作流_2077343497681727490.json, 图片生成/图生图/高清修复 4k细节-Krea2最新工作流_2077826236499456001.json, 图片生成/图生图/高清修复 4k细节-Krea2最新工作流_2078025500471160834.json, 图片生成/图生图/高清修复 4k细节-Krea2最新工作流_2078073501503811585.json, 图片生成/图生图/高清修复+4k细节-Krea2 自然真实 修复细节 最新工作流 极致美学_2076542796521099266.json, 图片生成/图生图/高清修复4k细节_2076124143707312129.json, 图片生成/图生图/高清修复_4k细节-Krea2最新工作流_2092621636909486081.json, 图片生成/图生图/高清细节修复 去除AI感_2087433012127555586.json, 视频生成/图生视频/Krea2高清修复+4k细节+去除AI塑料感-最新工作流_2079739645310619650.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_6

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/完美换装+双采高清直出【御川0805】】_2084911316422189057.json、图片生成/图生图/新版人像高清放大，皮肤nice_2082286371208777729.json、图片生成/图生图/新版人像高清放大，皮肤nice【0721】_2113792779288662018.json、图片生成/图生图/新版人像高清放大，皮肤nice【御川0721】_2079468772016087041.json、图片生成/图生图/新版人像高清放大，皮肤nice【御川0721】_2113796151311953921.json…）

- **类型**：Image To Image
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 19 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EditTextEncode_EditUtils`
- `Flux2KleinConfigPreparer_EditUtils`
- `Flux2KleinModelConfig_EditUtils`
- `Flux2KleinOutputExtractor_EditUtils`
- `Flux2Scheduler`
- `FluxKVCache`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAEEncodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `easy cleanGpuUsed` —— 18/19 个有
- `easy imageColorMatch` —— 18/19 个有
- `Anything Everywhere3` —— 11/19 个有
- `LatentColorMatchSimple` —— 11/19 个有
- `PreviewImage` —— 8/19 个有
- `EmptyImage` —— 3/19 个有
- `CFGNorm` —— 1/19 个有
- `CR Text` —— 1/19 个有
- `CheckpointLoaderSimple` —— 1/19 个有
- `EmptySD3LatentImage` —— 1/19 个有
- `GroundingDinoModelLoader_SDPose` —— 1/19 个有
- `ModelSamplingAuraFlow` —— 1/19 个有
- `SDPoseOODLoader` —— 1/19 个有
- `SDPoseOODProcessor` —— 1/19 个有
- `TextEncodeQwenImageEditPlus` —— 1/19 个有
- `YOLOModelLoader` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 19 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 19 | 100% |
| 采样算法 | euler_ancestral | - | 19 | 100% |
| 调度器 | kl_optimal | - | 19 | 100% |
| 重绘幅度 | 0.4 | 0.3 - 0.4 | 19 | 94% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，19 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，19 个样本，一致性 100%
- 调度器 最常用 kl_optimal，19 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.3 - 0.4，19 个样本，取值集中（一致性 94%）
- 高发问题（21/19 个样本）：Steps较低可能导致细节不足
