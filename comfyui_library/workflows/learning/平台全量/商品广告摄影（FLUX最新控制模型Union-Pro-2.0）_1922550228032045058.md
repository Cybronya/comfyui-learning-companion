---
key: 平台全量/商品广告摄影（FLUX最新控制模型Union-Pro-2.0）_1922550228032045058.json
name: 商品广告摄影（FLUX最新控制模型Union-Pro-2.0）_1922550228032045058
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/商品广告摄影（FLUX最新控制模型Union-Pro-2.0）_1922550228032045058.json
hash: 2fd8ecc06e11f1f8
coverage: 0.852273
learned_at: 2026-11-14 01:52:36
nodes: [ConditioningZeroOut, VAELoader, KSamplerSelect, BasicScheduler, ModelSamplingFlux, DifferentialDiffusion, GetImageSize+, SetUnionControlNetType, ACN_AdvancedControlNetApplySingle_v2, AIO_Preprocessor, PreviewImage, SetUnionControlNetType, SetUnionControlNetType, DualCLIPLoader, PreviewImage, PreviewImage, MaskToImage, ConditioningZeroOut, VAEDecode, VAELoader, KSamplerSelect, BasicScheduler, BasicGuider, ModelSamplingFlux, FluxGuidance, DifferentialDiffusion, GetImageSize+, SetUnionControlNetType, ACN_AdvancedControlNetApplySingle_v2, AIO_Preprocessor, PreviewImage, ACN_AdvancedControlNetApplySingle_v2, SetUnionControlNetType, ACN_AdvancedControlNetApplySingle_v2, AIO_Preprocessor, SetUnionControlNetType, ACN_AdvancedControlNetApplySingle_v2, DualCLIPLoader, SetUnionControlNetType, AIO_Preprocessor, AIO_Preprocessor, PreviewImage, PreviewImage, PreviewImage, MaskToImage, PreviewImage, UNETLoader, ControlNetLoader, PreviewImage, ACN_AdvancedControlNetApplySingle_v2, ACN_AdvancedControlNetApplySingle_v2, AIO_Preprocessor, ImageResizeKJ, UNETLoader, PreviewImage, RandomNoise, VAEDecode, SaveImage, LayerMask: LoadFlorence2Model, LayerMask: ObjectDetectorFL2, LayerMask: SAM2Ultra, PreviewImage, Int, GrowMaskWithBlur, CLIPTextEncode, SetUnionControlNetType, AIO_Preprocessor, ControlNetLoader, InpaintModelConditioning, ACN_AdvancedControlNetApplySingle_v2, AIO_Preprocessor, FluxGuidance, RandomNoise, BasicGuider, SamplerCustomAdvanced, PreviewImage, LoadImage, PreviewImage, LayerMask: SAM2Ultra, CLIPTextEncode, LoadImage, SamplerCustomAdvanced, ImageResizeKJ, Int, GrowMaskWithBlur, InpaintModelConditioning, LayerMask: ObjectDetectorFL2, LayerMask: LoadFlorence2Model]
patterns: []
missing: []
parameters: {"controlnet_strength": 0.5}
---

# 平台全量/商品广告摄影（FLUX最新控制模型Union-Pro-2.0）_1922550228032045058.json

> 来源文件 `comfyui_library/workflows/平台全量/商品广告摄影（FLUX最新控制模型Union-Pro-2.0）_1922550228032045058.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（88 个）：
- `ConditioningZeroOut`
- `VAELoader`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `ModelSamplingFlux`
- `DifferentialDiffusion`
- `GetImageSize+`
- `SetUnionControlNetType`
- `ACN_AdvancedControlNetApplySingle_v2` ★核心
- `AIO_Preprocessor`
- `PreviewImage`
- `SetUnionControlNetType`
- `SetUnionControlNetType`
- `DualCLIPLoader`
- `PreviewImage`
- `PreviewImage`
- `MaskToImage`
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
- `ACN_AdvancedControlNetApplySingle_v2` ★核心
- `AIO_Preprocessor`
- `SetUnionControlNetType`
- `ACN_AdvancedControlNetApplySingle_v2` ★核心
- `DualCLIPLoader`
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `MaskToImage`
- `PreviewImage`
- `UNETLoader` ★核心
- `ControlNetLoader`
- `PreviewImage`
- `ACN_AdvancedControlNetApplySingle_v2` ★核心
- `ACN_AdvancedControlNetApplySingle_v2` ★核心
- `AIO_Preprocessor`
- `ImageResizeKJ`
- `UNETLoader` ★核心
- `PreviewImage`
- `RandomNoise`
- `VAEDecode` ★核心
- `SaveImage`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: ObjectDetectorFL2`
- `LayerMask: SAM2Ultra`
- `PreviewImage`
- `Int`
- `GrowMaskWithBlur`
- `CLIPTextEncode` ★核心
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `ControlNetLoader`
- `InpaintModelConditioning`
- `ACN_AdvancedControlNetApplySingle_v2` ★核心
- `AIO_Preprocessor`
- `FluxGuidance`
- `RandomNoise`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `PreviewImage`
- `LoadImage`
- `PreviewImage`
- `LayerMask: SAM2Ultra`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `SamplerCustomAdvanced` ★核心
- `ImageResizeKJ`
- `Int`
- `GrowMaskWithBlur`
- `InpaintModelConditioning`
- `LayerMask: ObjectDetectorFL2`
- `LayerMask: LoadFlorence2Model`

## 关键参数

- `controlnet_strength` = `0.5`

## 知识

覆盖率 **85%**（75/88）

**有卡**：`ConditioningZeroOut`、`VAELoader`、`KSamplerSelect`、`BasicScheduler`、`ModelSamplingFlux`、`DifferentialDiffusion`、`GetImageSize+`、`SetUnionControlNetType`、`ACN_AdvancedControlNetApplySingle_v2`、`AIO_Preprocessor`、`DualCLIPLoader`、`MaskToImage`、`VAEDecode`、`BasicGuider`、`FluxGuidance`、`UNETLoader`、`ControlNetLoader`、`ImageResizeKJ`、`RandomNoise`、`SaveImage`、`LayerMask: LoadFlorence2Model`、`LayerMask: ObjectDetectorFL2`、`LayerMask: SAM2Ultra`、`Int`、`GrowMaskWithBlur`、`CLIPTextEncode`、`InpaintModelConditioning`、`SamplerCustomAdvanced`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、ACN_AdvancedControlNetApplySingle_v2、ControlNetLoader
