---
name: unknown_workflow_upscale_sampler_clip_10
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.846
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, Flux2Scheduler, FluxKontextImageScale, GroundingDinoModelLoader_SDPose, ImageScaleBy, KSamplerSelect, LoadImage, PreviewImage, RandomNoise, ReferenceLatent, SDPoseOODLoader, SDPoseOODProcessor, SamplerCustomAdvanced, SamplerEulerAncestral, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageSize, easy showAnything, easy sleep]
problems: []
missing: []
members: [图片生成/图生图/flux2-klein-二次元服装真人试穿_2113795408454578177.json, 图片生成/图生图/flux2-klein-二次元服装真人试穿_2113933618732163074.json, 图片生成/图生图/flux2-klein-二次元服装真人试穿_2113955999886438401.json, 图片生成/图生图/人物换装flux2  服装真人试穿 Character Costume Changes_2116343676086603778.json, 平台全量/Flux2 Klein 9B 产品服饰完美迁移保留细节 多图编辑+高清放大_2025030710775517186.json, 平台全量/flux2-klein-cosplay-角色扮演_2026885285010739202.json, 平台全量/flux2-klein-二次元服装真人试穿_2023783089570320386.json, 平台全量/flux2-klein-二次元服装真人试穿_2117515624976052226.json, 平台全量/flux2-klein-二次元服装真人试穿_2117539839628365825.json, 平台全量/flux2-klein-二次元服装真人试穿_2117855434324406273.json, 视频生成/图生视频/人物换装flux2_服装真人试穿_Character_Costume_Changes_2116382633553907714.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_10

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/flux2-klein-二次元服装真人试穿_2113795408454578177.json、图片生成/图生图/flux2-klein-二次元服装真人试穿_2113933618732163074.json、图片生成/图生图/flux2-klein-二次元服装真人试穿_2113955999886438401.json、图片生成/图生图/人物换装flux2  服装真人试穿 Character Costume Changes_2116343676086603778.json、平台全量/Flux2 Klein 9B 产品服饰完美迁移保留细节 多图编辑+高清放大_2025030710775517186.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
- `FluxKontextImageScale`
- `GroundingDinoModelLoader_SDPose`
- `ImageScaleBy`
- `KSamplerSelect`
- `LoadImage`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SamplerCustomAdvanced`
- `SamplerEulerAncestral`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageSize`
- `easy showAnything`
- `easy sleep`

**可变部分**（部分 workflow 才有）：
- `ClothesSegment` —— 10/11 个有
- `EmptyLatentImage` —— 10/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/11 个有
- `EmptyImage` —— 1/11 个有
- `LayerMask: LoadSegmentAnythingModels` —— 1/11 个有
- `LayerMask: MaskGrow` —— 1/11 个有
- `LayerMask: SegmentAnythingUltra V3` —— 1/11 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/11 个有
- `SetLatentNoiseMask` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 10 | 100% |
| 高度 | 512 | 512 - 512 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，10 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，10 个样本，取值集中（一致性 100%）
