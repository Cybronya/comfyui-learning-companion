---
name: text_to_image_controlnet_upscale_sampler_8
type: Text To Image
frequency: 2
level: weak
coverage: 0.496
common_nodes: [Anything Everywhere3, BasicGuider, BasicScheduler, BboxDetectorSEGS, CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DetailerForEach, DualCLIPLoader, EmptyLatentImage, Fast Groups Bypasser (rgthree), Float, GetNode, Image Comparer (rgthree), ImageResizeKJ, ImpactSegsAndMask, ImpactSwitch, Int, KSampler, KSamplerSelect, LoadImage, MaskPreview+, ModelSamplingFlux, OpenposePreprocessor, PlaySound|pysssss, PortraitMaster, PreviewImage, RandomNoise, SAMDetectorCombined, SAMLoader, SamplerCustomAdvanced, SaveImage, SetNode, ShowText|pysssss, TextInput_, UNETLoader, UltimateSDUpscale, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/多角度一致性写实人物_PuLID换脸_1838619374977531905.json, 平台全量/多角度一致性写实人物_基础版_1837756005856821249.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_upscale_sampler_8

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/多角度一致性写实人物_PuLID换脸_1838619374977531905.json、平台全量/多角度一致性写实人物_基础版_1837756005856821249.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：50%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `BasicGuider`
- `BasicScheduler`
- `BboxDetectorSEGS`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DetailerForEach`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Float`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageResizeKJ`
- `ImpactSegsAndMask`
- `ImpactSwitch`
- `Int`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `MaskPreview+`
- `ModelSamplingFlux`
- `OpenposePreprocessor`
- `PlaySound|pysssss`
- `PortraitMaster`
- `PreviewImage`
- `RandomNoise`
- `SAMDetectorCombined`
- `SAMLoader`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `TextInput_`
- `UNETLoader`
- `UltimateSDUpscale`
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ApplyPulidAdvanced` —— 1/2 个有
- `Automatic CFG` —— 1/2 个有
- `ColorMatch` —— 1/2 个有
- `CropFaces` —— 1/2 个有
- `DepthAnything_V2` —— 1/2 个有
- `DetectFaces` —— 1/2 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 1/2 个有
- `FaceAnalysisModels` —— 1/2 个有
- `FaceBoundingBox` —— 1/2 个有
- `FeatherMask` —— 1/2 个有
- `ImageToMask` —— 1/2 个有
- `InpaintModelConditioning` —— 1/2 个有
- `InstantIDFaceAnalysis` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PulidEvaClipLoader` —— 1/2 个有
- `PulidModelLoader` —— 1/2 个有
- `WarpFacesBack` —— 1/2 个有
- `easy imageChooser` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.9 | - | 2 | 89% |
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 2 | - | 2 | 100% |
| 采样算法 | dpmpp_sde | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
