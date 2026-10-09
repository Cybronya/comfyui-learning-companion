---
key: 图片生成/文生图/😯Flux.1 Redux+cn 多参考+pose_depth姿势 姿势参考文生图_1929993539055423489.json
name: 😯Flux.1 Redux+cn 多参考+pose_depth姿势 姿势参考文生图_1929993539055423489.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/😯Flux.1 Redux+cn 多参考+pose_depth姿势 姿势参考文生图_1929993539055423489.json
hash: 07c0b8af860dd1f6
coverage: 0.35625
learned_at: 2026-10-07 22:34:23
nodes: [SetNode, SetNode, TeaCache, ConditioningZeroOut, GetNode, GetNode, SetNode, GetNode, LoraLoader, SetNode, ModelSamplingFlux, GetNode, GetNode, GetNode, RH_Translator, SetNode, easy textSwitch, SetNode, UNETLoader, CLIPTextEncode, SetNode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, SetNode, CR Text Concatenate, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, SetNode, GetNode, GetNode, GetNode, GetNode, BasicGuider, CLIPVisionLoader, CLIPVisionEncode, StyleModelLoader, GetNode, BasicScheduler, GetNode, FluxGuidance, RandomNoise, GetNode, ControlNetLoader, StyleModelApply, KSamplerSelect, GetNode, GetNode, VAEDecode, DWPreprocessor, PreviewImage, SetNode, PreviewImage, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerColor: Brightness & Contrast, LayerUtility: ImageScaleByAspectRatio V2, GetNode, RH_LLMAPI_NODE, SetNode, GetNode, ImageSmartSharpen+, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, LayerMask: MaskGrow, SetNode, LayerMask: MaskGrow, BiRefNetRMBG, LayerMask: MaskPreview, SetNode, LayerMask: MaskPreview, BackgroundScaler, SetNode, PreviewImage, SetNode, PreviewImage, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, AIO_Preprocessor, GetNode, AIO_Preprocessor, SetNode, ControlNetApplySD3, SetUnionControlNetType, GetNode, ShowText|pysssss, SetNode, PreviewImage, SetNode, SetNode, GetNode, ReduxAdvanced, GetNode, SetUnionControlNetType, RebatchLatents, GetNode, GetNode, PreviewImage, LayerMask: PersonMaskUltra V2, SaveImage, SetNode, GetNode, GetNode, StyleModelLoader, CLIPVisionLoader, SetNode, GetNode, ReduxAdvanced, LoadImage, VAEEncode, RepeatLatentBatch, easy seed, ControlNetApplySD3, INPAINT_MaskedFill, SetNode, LayerMask: MaskPreview, BiRefNetRMBG, LayerMask: MaskGrow, LayerMask: MaskGrow, PreviewImage, SamplerCustomAdvanced, InpaintCrop, SetNode, GetNode, ReduxAdvanced, GetNode, ImageSmartSharpen+, GetNode, BasicGuider, GetNode, RandomNoise, SamplerCustomAdvanced, GetNode, KSamplerSelect, GetNode, VAEEncode, GetNode, SetNode, FluxGuidance, BasicScheduler, GetNode, GetNode, VAEDecode, LoadImage, SaveImage, SaveImage, LoraLoader, RH_LLMAPI_NODE, DualCLIPLoaderGGUF, VAELoader]
patterns: [lora]
missing: [CR Text Concatenate, ImageSmartSharpen+, ImageSmartSharpen+, LayerColor: Brightness & Contrast, LayerMask: MaskGrow, LayerMask: MaskGrow, LayerMask: MaskGrow, LayerMask: MaskGrow, LayerMask: PersonMaskUltra V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, easy textSwitch, LayerMask: MaskPreview, LayerMask: MaskPreview, LayerMask: MaskPreview, easy seed]
parameters: {"controlnet_strength": 0.5000000000000001, "lora_name": "kkk-manfoot-v3-b20.safetensors", "strength_clip": 1, "strength_model": 0.5000000000000001}
discoveries: [次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `ImageSmartSharpen+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageSmartSharpen+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerColor: Brightness & Contrast` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: MaskGrow` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: MaskGrow` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: MaskGrow` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: MaskGrow` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: PersonMaskUltra V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: MaskPreview` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `LayerMask: MaskPreview` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `LayerMask: MaskPreview` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/😯Flux.1 Redux+cn 多参考+pose_depth姿势 姿势参考文生图_1929993539055423489.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1929993539055423489.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（160 个）：
- `SetNode`
- `SetNode`
- `TeaCache`
- `ConditioningZeroOut`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `LoraLoader` ★核心
- `SetNode`
- `ModelSamplingFlux`
- `GetNode`
- `GetNode`
- `GetNode`
- `RH_Translator`
- `SetNode`
- `easy textSwitch`
- `SetNode`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `CR Text Concatenate`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `BasicGuider`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `StyleModelLoader`
- `GetNode`
- `BasicScheduler`
- `GetNode`
- `FluxGuidance`
- `RandomNoise`
- `GetNode`
- `ControlNetLoader`
- `StyleModelApply`
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `DWPreprocessor`
- `PreviewImage`
- `SetNode`
- `PreviewImage`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerColor: Brightness & Contrast`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `RH_LLMAPI_NODE`
- `SetNode`
- `GetNode`
- `ImageSmartSharpen+`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `LayerMask: MaskGrow`
- `SetNode`
- `LayerMask: MaskGrow`
- `BiRefNetRMBG`
- `LayerMask: MaskPreview`
- `SetNode`
- `LayerMask: MaskPreview`
- `BackgroundScaler`
- `SetNode`
- `PreviewImage`
- `SetNode`
- `PreviewImage`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `AIO_Preprocessor`
- `GetNode`
- `AIO_Preprocessor`
- `SetNode`
- `ControlNetApplySD3` ★核心
- `SetUnionControlNetType`
- `GetNode`
- `ShowText|pysssss`
- `SetNode`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `GetNode`
- `ReduxAdvanced`
- `GetNode`
- `SetUnionControlNetType`
- `RebatchLatents`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `LayerMask: PersonMaskUltra V2`
- `SaveImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `SetNode`
- `GetNode`
- `ReduxAdvanced`
- `LoadImage`
- `VAEEncode` ★核心
- `RepeatLatentBatch`
- `easy seed`
- `ControlNetApplySD3` ★核心
- `INPAINT_MaskedFill`
- `SetNode`
- `LayerMask: MaskPreview`
- `BiRefNetRMBG`
- `LayerMask: MaskGrow`
- `LayerMask: MaskGrow`
- `PreviewImage`
- `SamplerCustomAdvanced` ★核心
- `InpaintCrop`
- `SetNode`
- `GetNode`
- `ReduxAdvanced`
- `GetNode`
- `ImageSmartSharpen+`
- `GetNode`
- `BasicGuider`
- `GetNode`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `VAEEncode` ★核心
- `GetNode`
- `SetNode`
- `FluxGuidance`
- `BasicScheduler`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `LoadImage`
- `SaveImage`
- `SaveImage`
- `LoraLoader` ★核心
- `RH_LLMAPI_NODE`
- `DualCLIPLoaderGGUF`
- `VAELoader`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `kkk-manfoot-v3-b20.safetensors`
- `strength_model` = `0.5000000000000001`
- `strength_clip` = `1`
- `controlnet_strength` = `0.5000000000000001`

## 知识

覆盖率 **36%**（57/160）

**有卡**：`TeaCache`、`ConditioningZeroOut`、`LoraLoader`、`ModelSamplingFlux`、`RH_Translator`、`UNETLoader`、`CLIPTextEncode`、`BasicGuider`、`CLIPVisionLoader`、`CLIPVisionEncode`、`StyleModelLoader`、`BasicScheduler`、`FluxGuidance`、`RandomNoise`、`ControlNetLoader`、`StyleModelApply`、`KSamplerSelect`、`VAEDecode`、`DWPreprocessor`、`RH_LLMAPI_NODE`、`BiRefNetRMBG`、`BackgroundScaler`、`AIO_Preprocessor`、`ControlNetApplySD3`、`SetUnionControlNetType`、`ReduxAdvanced`、`RebatchLatents`、`SaveImage`、`LoadImage`、`VAEEncode`、`RepeatLatentBatch`、`INPAINT_MaskedFill`、`SamplerCustomAdvanced`、`InpaintCrop`、`DualCLIPLoaderGGUF`、`VAELoader`

**缺卡**（19）：`CR Text Concatenate`、`ImageSmartSharpen+`、`ImageSmartSharpen+`、`LayerColor: Brightness & Contrast`、`LayerMask: MaskGrow`、`LayerMask: MaskGrow`、`LayerMask: MaskGrow`、`LayerMask: MaskGrow`、`LayerMask: PersonMaskUltra V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy textSwitch`、`LayerMask: MaskPreview`、`LayerMask: MaskPreview`、`LayerMask: MaskPreview`、`easy seed`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、ControlNetLoader、SetUnionControlNetType

## 学习发现

- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageSmartSharpen+` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageSmartSharpen+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerColor: Brightness & Contrast` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: MaskGrow` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: MaskGrow` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: MaskGrow` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: MaskGrow` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: PersonMaskUltra V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: MaskPreview` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `LayerMask: MaskPreview` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `LayerMask: MaskPreview` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
