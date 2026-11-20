---
name: unknown_workflow_sampler_clip_unet_545
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.947
common_nodes: [ApplyPulidFlux, BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, FluxGuidance, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, ModelSamplingFlux, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/FLUX_Redux  + 风格迁移_1955297581578555393.json, 平台全量/PuLID + Redux 🐯🐻🐨一人风格百变效果 🐯🐻🐨_1960382206545899521.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_545

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/FLUX_Redux  + 风格迁移_1955297581578555393.json、平台全量/PuLID + Redux 🐯🐻🐨一人风格百变效果 🐯🐻🐨_1960382206545899521.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LoadImage`
- `ModelSamplingFlux`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `InstructPixToPixConditioning` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PIP_图像联结` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `easy imageConcat` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
