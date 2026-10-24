---
key: 图片生成/图生图/😯F.1 Redux+cn 多参考+pose_depth-v1-姿势参考_人物参考_姿势迁移_1914026393066270722.json
name: 😯F.1 Redux+cn 多参考+pose_depth-v1-姿势参考_人物参考_姿势迁移_1914026393066270722
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/😯F.1 Redux+cn 多参考+pose_depth-v1-姿势参考_人物参考_姿势迁移_1914026393066270722.json
hash: 02b794b31fddb1d1
coverage: 0.496403
learned_at: 2026-10-23 13:39:55
nodes: [GetNode, GetNode, GetNode, GetNode, SetUnionControlNetType, GetNode, SetUnionControlNetType, SetNode, GetNode, BasicGuider, CLIPVisionLoader, CLIPVisionEncode, StyleModelLoader, GetNode, BasicScheduler, SetNode, SetNode, SetNode, TeaCache, ConditioningZeroOut, GetNode, GetNode, SetNode, GetNode, GetNode, DWPreprocessor, PreviewImage, SetNode, PreviewImage, AIO_Preprocessor, SetNode, LoraLoader, SetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, SetNode, SetNode, LayerUtility: CropByMask V2, PreviewImage, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, FluxGuidance, GetNode, GetNode, RandomNoise, SamplerCustomAdvanced, GetNode, BackgroundScaler, PreviewImage, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerColor: Brightness & Contrast, ControlNetLoader, ModelSamplingFlux, GetNode, GetNode, ControlNetApplySD3, easy cleanGpuUsed, LayerMask: SegmentAnythingUltra, easy cleanGpuUsed, StyleModelApply, GetNode, GetNode, RH_Translator, CR Text Concatenate, SetNode, easy textSwitch, SetNode, VAELoader, UNETLoader, CLIPTextEncode, GetNode, SetNode, KSamplerSelect, RH_LLMAPI_NODE, GetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, BiRefNetRMBG, LayerUtility: ImageScaleByAspectRatio V2, RepeatLatentBatch, RebatchLatents, GetNode, GetNode, VAEEncode, SetNode, StyleModelLoader, CLIPVisionLoader, easy seed, ShowText|pysssss, GetNode, SetNode, GetNode, GetNode, LayerMask: PersonMaskUltra V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, LayerUtility: CropByMask V2, GetNode, ReduxAdvanced, MaskPreview+, LoraLoader, DualCLIPLoaderGGUF, ReduxAdvanced, ControlNetApplySD3, LoadImage, LoadImage, BasicGuider, GetNode, RandomNoise, SamplerCustomAdvanced, GetNode, KSamplerSelect, GetNode, VAEEncode, VAEDecode, GetNode, SetNode, SetNode, FluxGuidance, BasicScheduler, GetNode, GetNode, VAEDecode, SaveImage, SaveImage, ImageSmartSharpen+, GetNode, ImageSmartSharpen+, GetNode, RH_LLMAPI_NODE, GetNode]
patterns: [lora]
missing: []
parameters: {"controlnet_strength": 0.5000000000000001, "lora_name": "kkk-manfoot-v3-b20.safetensors", "strength_clip": 1, "strength_model": 0.5000000000000001}
---

# 图片生成/图生图/😯F.1 Redux+cn 多参考+pose_depth-v1-姿势参考_人物参考_姿势迁移_1914026393066270722.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/😯F.1 Redux+cn 多参考+pose_depth-v1-姿势参考_人物参考_姿势迁移_1914026393066270722.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（139 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetUnionControlNetType`
- `GetNode`
- `SetUnionControlNetType`
- `SetNode`
- `GetNode`
- `BasicGuider`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `StyleModelLoader`
- `GetNode`
- `BasicScheduler`
- `SetNode`
- `SetNode`
- `SetNode`
- `TeaCache`
- `ConditioningZeroOut`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `DWPreprocessor`
- `PreviewImage`
- `SetNode`
- `PreviewImage`
- `AIO_Preprocessor`
- `SetNode`
- `LoraLoader` ★核心
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `SetNode`
- `SetNode`
- `LayerUtility: CropByMask V2`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `FluxGuidance`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `BackgroundScaler`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerColor: Brightness & Contrast`
- `ControlNetLoader`
- `ModelSamplingFlux`
- `GetNode`
- `GetNode`
- `ControlNetApplySD3` ★核心
- `easy cleanGpuUsed`
- `LayerMask: SegmentAnythingUltra`
- `easy cleanGpuUsed`
- `StyleModelApply`
- `GetNode`
- `GetNode`
- `RH_Translator`
- `CR Text Concatenate`
- `SetNode`
- `easy textSwitch`
- `SetNode`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetNode`
- `KSamplerSelect` ★核心
- `RH_LLMAPI_NODE`
- `GetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `BiRefNetRMBG`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RepeatLatentBatch`
- `RebatchLatents`
- `GetNode`
- `GetNode`
- `VAEEncode` ★核心
- `SetNode`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `easy seed`
- `ShowText|pysssss`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LayerMask: PersonMaskUltra V2`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `LayerUtility: CropByMask V2`
- `GetNode`
- `ReduxAdvanced`
- `MaskPreview+`
- `LoraLoader` ★核心
- `DualCLIPLoaderGGUF`
- `ReduxAdvanced`
- `ControlNetApplySD3` ★核心
- `LoadImage`
- `LoadImage`
- `BasicGuider`
- `GetNode`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `FluxGuidance`
- `BasicScheduler`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `ImageSmartSharpen+`
- `GetNode`
- `ImageSmartSharpen+`
- `GetNode`
- `RH_LLMAPI_NODE`
- `GetNode`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `kkk-manfoot-v3-b20.safetensors`
- `strength_model` = `0.5000000000000001`
- `strength_clip` = `1`
- `controlnet_strength` = `0.5000000000000001`

## 知识

覆盖率 **50%**（69/139）

**有卡**：`SetUnionControlNetType`、`BasicGuider`、`CLIPVisionLoader`、`CLIPVisionEncode`、`StyleModelLoader`、`BasicScheduler`、`TeaCache`、`ConditioningZeroOut`、`DWPreprocessor`、`AIO_Preprocessor`、`LoraLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: CropByMask V2`、`FluxGuidance`、`RandomNoise`、`SamplerCustomAdvanced`、`BackgroundScaler`、`LayerColor: Brightness & Contrast`、`ControlNetLoader`、`ModelSamplingFlux`、`ControlNetApplySD3`、`easy cleanGpuUsed`、`LayerMask: SegmentAnythingUltra`、`StyleModelApply`、`RH_Translator`、`CR Text Concatenate`、`easy textSwitch`、`VAELoader`、`UNETLoader`、`CLIPTextEncode`、`KSamplerSelect`、`RH_LLMAPI_NODE`、`BiRefNetRMBG`、`RepeatLatentBatch`、`RebatchLatents`、`VAEEncode`、`easy seed`、`LayerMask: PersonMaskUltra V2`、`ReduxAdvanced`、`MaskPreview+`、`DualCLIPLoaderGGUF`、`LoadImage`、`VAEDecode`、`SaveImage`、`ImageSmartSharpen+`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、ControlNetLoader、SetUnionControlNetType
