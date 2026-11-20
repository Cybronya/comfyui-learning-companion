---
name: unknown_workflow_controlnet_inpaint_lora_12
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.883333
common_nodes: [AIO_Preprocessor, BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConstrainImage|pysssss, ControlNetApplyAdvanced, ControlNetLoader, DifferentialDiffusion, FluxGuidance, GetImageSize, GetImageSize+, Image Blank, ImageAndMaskResizeNode, ImageConcanate, ImageCrop, ImageToMask, InpaintCrop, InpaintModelConditioning, InpaintStitch, KSamplerSelect, LayerUtility: ImageAutoCrop V2, LoadImage, MaskToImage, ModelSamplingFlux, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoader, PatchModelAddDownscale, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SetUnionControlNetType, StyleModelApply, StyleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/手动换装_1927898973733044225.json, 平台全量/高清换装2.0_1927601565094547457.json, 平台全量/高清换装_1910867484965072897.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_lora_12

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/手动换装_1927898973733044225.json、平台全量/高清换装2.0_1927601565094547457.json、平台全量/高清换装_1910867484965072897.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConstrainImage|pysssss`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DifferentialDiffusion`
- `FluxGuidance`
- `GetImageSize`
- `GetImageSize+`
- `Image Blank`
- `ImageAndMaskResizeNode`
- `ImageConcanate`
- `ImageCrop`
- `ImageToMask`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `KSamplerSelect`
- `LayerUtility: ImageAutoCrop V2`
- `LoadImage`
- `MaskToImage`
- `ModelSamplingFlux`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuTextEncoderLoader`
- `PatchModelAddDownscale`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetUnionControlNetType`
- `StyleModelApply`
- `StyleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GrowMask` —— 2/3 个有
- `LayerMask: SegformerB2ClothesUltra` —— 2/3 个有
- `GroundingDinoModelLoader (segment anything)` —— 1/3 个有
- `GroundingDinoSAMSegment (segment anything)` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `SAMModelLoader (segment anything)` —— 1/3 个有
- `TextInput_` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy imageScaleDownToSize` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.5 | 0.5 - 0.7 | 3 | 83% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.5，观测区间 0.5 - 0.7，3 个样本，取值集中（一致性 83%）
