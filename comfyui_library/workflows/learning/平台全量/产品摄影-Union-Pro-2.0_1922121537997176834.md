---
key: 平台全量/产品摄影-Union-Pro-2.0_1922121537997176834.json
name: 产品摄影-Union-Pro-2.0_1922121537997176834
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/产品摄影-Union-Pro-2.0_1922121537997176834.json
hash: b10f5b91dc490265
coverage: 0.852273
learned_at: 2026-11-14 01:35:10
nodes: [InpaintModelConditioning, ConditioningZeroOut, VAELoader, KSamplerSelect, BasicScheduler, BasicGuider, RandomNoise, ModelSamplingFlux, FluxGuidance, DifferentialDiffusion, GetImageSize+, SetUnionControlNetType, ACN_AdvancedControlNetApplySingle_v2, AIO_Preprocessor, PreviewImage, ACN_AdvancedControlNetApplySingle_v2, SetUnionControlNetType, SamplerCustomAdvanced, SetUnionControlNetType, DualCLIPLoader, LayerMask: LoadFlorence2Model, PreviewImage, PreviewImage, LayerMask: ObjectDetectorFL2, LayerMask: SAM2Ultra, Int, MaskToImage, PreviewImage, InpaintModelConditioning, ConditioningZeroOut, VAEDecode, VAELoader, KSamplerSelect, BasicScheduler, BasicGuider, ModelSamplingFlux, FluxGuidance, DifferentialDiffusion, GetImageSize+, SetUnionControlNetType, ACN_AdvancedControlNetApplySingle_v2, AIO_Preprocessor, PreviewImage, ACN_AdvancedControlNetApplySingle_v2, SetUnionControlNetType, SamplerCustomAdvanced, ACN_AdvancedControlNetApplySingle_v2, AIO_Preprocessor, SetUnionControlNetType, ACN_AdvancedControlNetApplySingle_v2, DualCLIPLoader, SetUnionControlNetType, LayerMask: LoadFlorence2Model, AIO_Preprocessor, AIO_Preprocessor, PreviewImage, PreviewImage, LayerMask: SAM2Ultra, Int, GrowMaskWithBlur, ImageResizeKJ, PreviewImage, MaskToImage, PreviewImage, UNETLoader, ControlNetLoader, LayerMask: ObjectDetectorFL2, CLIPTextEncode, PreviewImage, ACN_AdvancedControlNetApplySingle_v2, ACN_AdvancedControlNetApplySingle_v2, AIO_Preprocessor, AIO_Preprocessor, AIO_Preprocessor, SetUnionControlNetType, ImageResizeKJ, CLIPTextEncode, GrowMaskWithBlur, ControlNetLoader, UNETLoader, PreviewImage, RandomNoise, VAEDecode, SaveImage, LoadImage, PreviewImage, PreviewImage, LoadImage]
patterns: []
missing: []
parameters: {"controlnet_strength": 0.30000000000000004}
---

# 平台全量/产品摄影-Union-Pro-2.0_1922121537997176834.json

> 来源文件 `comfyui_library/workflows/平台全量/产品摄影-Union-Pro-2.0_1922121537997176834.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（88 个）：
- `InpaintModelConditioning`
- `ConditioningZeroOut`
- `VAELoader`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `BasicGuider`
- `RandomNoise`
- `ModelSamplingFlux`
- `FluxGuidance`
- `DifferentialDiffusion`
- `GetImageSize+`
- `SetUnionControlNetType`
- `ACN_AdvancedControlNetApplySingle_v2` ★核心
- `AIO_Preprocessor`
- `PreviewImage`
- `ACN_AdvancedControlNetApplySingle_v2` ★核心
- `SetUnionControlNetType`
- `SamplerCustomAdvanced` ★核心
- `SetUnionControlNetType`
- `DualCLIPLoader`
- `LayerMask: LoadFlorence2Model`
- `PreviewImage`
- `PreviewImage`
- `LayerMask: ObjectDetectorFL2`
- `LayerMask: SAM2Ultra`
- `Int`
- `MaskToImage`
- `PreviewImage`
- `InpaintModelConditioning`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `VAELoader`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `BasicGuider`
- `ModelSamplingFlux`
- `FluxGuidance`
- `DifferentialDiffusion`
- `GetImageSize+`
- `SetUnionControlNetType`
- `ACN_AdvancedControlNetApplySingle_v2` ★核心
- `AIO_Preprocessor`
- `PreviewImage`
- `ACN_AdvancedControlNetApplySingle_v2` ★核心
- `SetUnionControlNetType`
- `SamplerCustomAdvanced` ★核心
- `ACN_AdvancedControlNetApplySingle_v2` ★核心
- `AIO_Preprocessor`
- `SetUnionControlNetType`
- `ACN_AdvancedControlNetApplySingle_v2` ★核心
- `DualCLIPLoader`
- `SetUnionControlNetType`
- `LayerMask: LoadFlorence2Model`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `PreviewImage`
- `PreviewImage`
- `LayerMask: SAM2Ultra`
- `Int`
- `GrowMaskWithBlur`
- `ImageResizeKJ`
- `PreviewImage`
- `MaskToImage`
- `PreviewImage`
- `UNETLoader` ★核心
- `ControlNetLoader`
- `LayerMask: ObjectDetectorFL2`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `ACN_AdvancedControlNetApplySingle_v2` ★核心
- `ACN_AdvancedControlNetApplySingle_v2` ★核心
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `SetUnionControlNetType`
- `ImageResizeKJ`
- `CLIPTextEncode` ★核心
- `GrowMaskWithBlur`
- `ControlNetLoader`
- `UNETLoader` ★核心
- `PreviewImage`
- `RandomNoise`
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `PreviewImage`
- `PreviewImage`
- `LoadImage`

## 关键参数

- `controlnet_strength` = `0.30000000000000004`

## 知识

覆盖率 **85%**（75/88）

**有卡**：`InpaintModelConditioning`、`ConditioningZeroOut`、`VAELoader`、`KSamplerSelect`、`BasicScheduler`、`BasicGuider`、`RandomNoise`、`ModelSamplingFlux`、`FluxGuidance`、`DifferentialDiffusion`、`GetImageSize+`、`SetUnionControlNetType`、`ACN_AdvancedControlNetApplySingle_v2`、`AIO_Preprocessor`、`SamplerCustomAdvanced`、`DualCLIPLoader`、`LayerMask: LoadFlorence2Model`、`LayerMask: ObjectDetectorFL2`、`LayerMask: SAM2Ultra`、`Int`、`MaskToImage`、`VAEDecode`、`GrowMaskWithBlur`、`ImageResizeKJ`、`UNETLoader`、`ControlNetLoader`、`CLIPTextEncode`、`SaveImage`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、ACN_AdvancedControlNetApplySingle_v2、ControlNetLoader
