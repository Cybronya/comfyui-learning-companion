---
key: 图片生成/文生图/✨Flux All in 1 - 一站式工作流✨ V2.0_1889200614256336897.json
name: ✨Flux All in 1 - 一站式工作流✨ V2.0_1889200614256336897
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/✨Flux All in 1 - 一站式工作流✨ V2.0_1889200614256336897.json
hash: c0d3a0dc93bf751c
coverage: 0.381743
learned_at: 2026-10-10 20:59:28
nodes: [Florence2ModelLoader, FluxSamplerParams+, GetNode, FluxSamplerParams+, PreviewImage, GetNode, Anything Everywhere, Anything Everywhere, StepsAndCfg, Anything Everywhere, GetNode, FluxSamplerParams+, PreviewImage, ConditioningZeroOut, InpaintModelConditioning, GetNode, ConditioningZeroOut, PreviewImage, Anything Everywhere, Anything Everywhere, StepsAndCfg, ConditioningZeroOut, FluxGuidance, InstructPixToPixConditioning, GetNode, FluxGuidance, ConditioningZeroOut, InstructPixToPixConditioning, PreviewImage, FluxSamplerParams+, AV_VAELoader, GetNode, GetNode, ConditioningZeroOut, SetNode, ConditioningZeroOut, FluxSamplerParams+, SetNode, SetNode, FluxSamplerParams+, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, SetNode, FluxSamplerParams+, Float to String, SetNode, Anything Everywhere, StepsAndCfg, JWIntegerToString, JWIntegerToString, JWIntegerToString, DualCLIPLoader, VAEDecode, GetNode, GetNode, FluxSamplerParams+, GetNode, VAEDecode, SaveImage, VAEDecode, VAEDecode, VAEDecode, VAEDecode, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, PreviewImage, GetNode, GetNode, VAEDecode, GetNode, VAEDecode, SaveImage, FluxSamplerParams+, VAEDecode, SaveImage, SaveImage, SaveImage, SaveImage, SaveImage, SaveImage, Note, RH_Captioner, LoraLoaderModelOnly, ControlNetLoader, SaveImage, ConditioningZeroOut, UpscaleModelLoader, GetNode, ReduxAdvanced, SetNode, SaveImage, Image Comparer (rgthree), PreviewImage, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecode, CLIPTextEncode, GetNode, GetNode, StyleModelLoader, CLIPVisionLoader, ReduxAdvanced, SaveImage, FluxSamplerParams+, CLIPVisionLoader, StyleModelLoader, VAEEncode, ReduxAdvanced, LoadImage, SaveImage, ImpactGaussianBlurMask, SetNode, ShowText|pysssss, ShowText|pysssss, SetNode, SetNode, ShowText|pysssss, LoadImage, LoadImage, JWIntegerToString, SetNode, FloatSlider, Label (rgthree), Anything Everywhere, Seed_, Label (rgthree), Label (rgthree), Label (rgthree), FloatSlider, Label (rgthree), Anything Everywhere3, LoraLoader, Any Switch (rgthree), IPAdapterFluxLoader, ApplyIPAdapterFlux, Note, Note, SchedulerSelectHelper+, Any Switch (rgthree), Any Switch (rgthree), SchedulerSelectHelper+, SamplerSelectHelper+, SchedulerSelectHelper+, SamplerSelectHelper+, SchedulerSelectHelper+, SetNode, SetNode, SamplerSelectHelper+, SamplerSelectHelper+, Note, Note, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Concat Text _O, SetNode, SDXL Empty Latent Image (rgthree), GetNode, GetNode, GetNode, Any Switch (rgthree), ControlNetApplySD3, GetNode, GetNode, ControlNetLoader, SetNode, GetNode, LayerUtility: JoyCaption2, GetNode, GetNode, Florence2Run, DF_Image_scale_to_side, VAEEncode, GetNode, GetNode, VAEEncode, GetNode, InpaintModelConditioning, ImagePadForOutpaint, GetNode, GetNode, AIO_Preprocessor, AIO_Preprocessor, GetNode, GetNode, AIO_Preprocessor, VAEEncode, GetNode, UltimateSDUpscale, GetNode, ChangeImageBatchSize //Inspire, GetNode, ControlNetApplySD3, RH_LLMAPI_NODE, Fast Groups Muter (rgthree), LoadImage, Fast Groups Bypasser (rgthree), TextBox, ShowText|pysssss, Fast Groups Bypasser (rgthree), DF_DynamicPrompts_Text_Box, Fast Groups Muter (rgthree), LoraLoaderModelOnly, FluxSamplerParams+, UNETLoader, LoraLoaderModelOnly, GetNode, GetNode, AIO_Preprocessor, SetUnionControlNetType, SetUnionControlNetType]
patterns: [lora]
missing: [Concat Text _O, Float to String, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), LayerUtility: JoyCaption2, SchedulerSelectHelper+, SchedulerSelectHelper+, SchedulerSelectHelper+, SchedulerSelectHelper+, FluxSamplerParams+, FluxSamplerParams+, FluxSamplerParams+, FluxSamplerParams+, FluxSamplerParams+, FluxSamplerParams+, FluxSamplerParams+, FluxSamplerParams+, FluxSamplerParams+, FluxSamplerParams+, FluxSamplerParams+, SamplerSelectHelper+, SamplerSelectHelper+, SamplerSelectHelper+, SamplerSelectHelper+, ChangeImageBatchSize //Inspire, DF_DynamicPrompts_Text_Box, SDXL Empty Latent Image (rgthree)]
parameters: {"controlnet_strength": 0.6, "lora_name": null, "strength_clip": 1, "strength_model": 1}
discoveries: [次要节点 `Concat Text _O` 知识库中没有该节点类型的任何知识, 次要节点 `Float to String` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: JoyCaption2` 知识库中没有该节点类型的任何知识, 次要节点 `SchedulerSelectHelper+` 知识库中没有该节点类型的任何知识, 次要节点 `SchedulerSelectHelper+` 知识库中没有该节点类型的任何知识, 次要节点 `SchedulerSelectHelper+` 知识库中没有该节点类型的任何知识, 次要节点 `SchedulerSelectHelper+` 知识库中没有该节点类型的任何知识, 核心节点 `FluxSamplerParams+` 仅有 KSampler/Checkpoint 的通用知识，没有该节点自己的说明, 核心节点 `FluxSamplerParams+` 仅有 KSampler/Checkpoint 的通用知识，没有该节点自己的说明, 核心节点 `FluxSamplerParams+` 仅有 KSampler/Checkpoint 的通用知识，没有该节点自己的说明, 核心节点 `FluxSamplerParams+` 仅有 KSampler/Checkpoint 的通用知识，没有该节点自己的说明, 核心节点 `FluxSamplerParams+` 仅有 KSampler/Checkpoint 的通用知识，没有该节点自己的说明, 核心节点 `FluxSamplerParams+` 仅有 KSampler/Checkpoint 的通用知识，没有该节点自己的说明, 核心节点 `FluxSamplerParams+` 仅有 KSampler/Checkpoint 的通用知识，没有该节点自己的说明, 核心节点 `FluxSamplerParams+` 仅有 KSampler/Checkpoint 的通用知识，没有该节点自己的说明, 核心节点 `FluxSamplerParams+` 仅有 KSampler/Checkpoint 的通用知识，没有该节点自己的说明, 核心节点 `FluxSamplerParams+` 仅有 KSampler/Checkpoint 的通用知识，没有该节点自己的说明, 核心节点 `FluxSamplerParams+` 仅有 KSampler/Checkpoint 的通用知识，没有该节点自己的说明, 核心节点 `SamplerSelectHelper+` 仅有 KSampler 的通用知识，没有该节点自己的说明, 核心节点 `SamplerSelectHelper+` 仅有 KSampler 的通用知识，没有该节点自己的说明, 核心节点 `SamplerSelectHelper+` 仅有 KSampler 的通用知识，没有该节点自己的说明, 核心节点 `SamplerSelectHelper+` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `ChangeImageBatchSize //Inspire` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `DF_DynamicPrompts_Text_Box` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `SDXL Empty Latent Image (rgthree)` 仅有 VAE/Checkpoint/Resolution 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/✨Flux All in 1 - 一站式工作流✨ V2.0_1889200614256336897.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/✨Flux All in 1 - 一站式工作流✨ V2.0_1889200614256336897.json`

## 结构

**节点**（241 个）：
- `Florence2ModelLoader`
- `FluxSamplerParams+`
- `GetNode`
- `FluxSamplerParams+`
- `PreviewImage`
- `GetNode`
- `Anything Everywhere`
- `Anything Everywhere`
- `StepsAndCfg`
- `Anything Everywhere`
- `GetNode`
- `FluxSamplerParams+`
- `PreviewImage`
- `ConditioningZeroOut`
- `InpaintModelConditioning`
- `GetNode`
- `ConditioningZeroOut`
- `PreviewImage`
- `Anything Everywhere`
- `Anything Everywhere`
- `StepsAndCfg`
- `ConditioningZeroOut`
- `FluxGuidance`
- `InstructPixToPixConditioning`
- `GetNode`
- `FluxGuidance`
- `ConditioningZeroOut`
- `InstructPixToPixConditioning`
- `PreviewImage`
- `FluxSamplerParams+`
- `AV_VAELoader`
- `GetNode`
- `GetNode`
- `ConditioningZeroOut`
- `SetNode`
- `ConditioningZeroOut`
- `FluxSamplerParams+`
- `SetNode`
- `SetNode`
- `FluxSamplerParams+`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `FluxSamplerParams+`
- `Float to String`
- `SetNode`
- `Anything Everywhere`
- `StepsAndCfg`
- `JWIntegerToString`
- `JWIntegerToString`
- `JWIntegerToString`
- `DualCLIPLoader`
- `VAEDecode`
- `GetNode`
- `GetNode`
- `FluxSamplerParams+`
- `GetNode`
- `VAEDecode`
- `SaveImage`
- `VAEDecode`
- `VAEDecode`
- `VAEDecode`
- `VAEDecode`
- `VAEDecode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `VAEDecode`
- `GetNode`
- `VAEDecode`
- `SaveImage`
- `FluxSamplerParams+`
- `VAEDecode`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `Note`
- `RH_Captioner`
- `LoraLoaderModelOnly`
- `ControlNetLoader`
- `SaveImage`
- `ConditioningZeroOut`
- `UpscaleModelLoader`
- `GetNode`
- `ReduxAdvanced`
- `SetNode`
- `SaveImage`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `CLIPTextEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode`
- `CLIPTextEncode`
- `GetNode`
- `GetNode`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `ReduxAdvanced`
- `SaveImage`
- `FluxSamplerParams+`
- `CLIPVisionLoader`
- `StyleModelLoader`
- `VAEEncode`
- `ReduxAdvanced`
- `LoadImage`
- `SaveImage`
- `ImpactGaussianBlurMask`
- `SetNode`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `SetNode`
- `SetNode`
- `ShowText|pysssss`
- `LoadImage`
- `LoadImage`
- `JWIntegerToString`
- `SetNode`
- `FloatSlider`
- `Label (rgthree)`
- `Anything Everywhere`
- `Seed_`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `FloatSlider`
- `Label (rgthree)`
- `Anything Everywhere3`
- `LoraLoader`
- `Any Switch (rgthree)`
- `IPAdapterFluxLoader`
- `ApplyIPAdapterFlux`
- `Note`
- `Note`
- `SchedulerSelectHelper+`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `SchedulerSelectHelper+`
- `SamplerSelectHelper+`
- `SchedulerSelectHelper+`
- `SamplerSelectHelper+`
- `SchedulerSelectHelper+`
- `SetNode`
- `SetNode`
- `SamplerSelectHelper+`
- `SamplerSelectHelper+`
- `Note`
- `Note`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Concat Text _O`
- `SetNode`
- `SDXL Empty Latent Image (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `ControlNetApplySD3`
- `GetNode`
- `GetNode`
- `ControlNetLoader`
- `SetNode`
- `GetNode`
- `LayerUtility: JoyCaption2`
- `GetNode`
- `GetNode`
- `Florence2Run`
- `DF_Image_scale_to_side`
- `VAEEncode`
- `GetNode`
- `GetNode`
- `VAEEncode`
- `GetNode`
- `InpaintModelConditioning`
- `ImagePadForOutpaint`
- `GetNode`
- `GetNode`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `GetNode`
- `GetNode`
- `AIO_Preprocessor`
- `VAEEncode`
- `GetNode`
- `UltimateSDUpscale`
- `GetNode`
- `ChangeImageBatchSize //Inspire`
- `GetNode`
- `ControlNetApplySD3`
- `RH_LLMAPI_NODE`
- `Fast Groups Muter (rgthree)`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `TextBox`
- `ShowText|pysssss`
- `Fast Groups Bypasser (rgthree)`
- `DF_DynamicPrompts_Text_Box`
- `Fast Groups Muter (rgthree)`
- `LoraLoaderModelOnly`
- `FluxSamplerParams+`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `GetNode`
- `GetNode`
- `AIO_Preprocessor`
- `SetUnionControlNetType`
- `SetUnionControlNetType`

**识别到的模式**：lora

## 关键参数

- `controlnet_strength` = `0.6`
- `lora_name` = `None`
- `strength_clip` = `1`
- `strength_model` = `1`

## 知识

覆盖率 **38%**（92/241）

**有卡**：`Florence2ModelLoader`、`FluxSamplerParams+`、`GetNode`、`PreviewImage`、`Anything Everywhere`、`StepsAndCfg`、`ConditioningZeroOut`、`InpaintModelConditioning`、`FluxGuidance`、`InstructPixToPixConditioning`、`AV_VAELoader`、`SetNode`、`Float to String`、`JWIntegerToString`、`DualCLIPLoader`、`VAEDecode`、`SaveImage`、`Note`、`RH_Captioner`、`LoraLoaderModelOnly`、`ControlNetLoader`

**缺卡**（30）：`Concat Text _O`、`Float to String`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`LayerUtility: JoyCaption2`、`SchedulerSelectHelper+`、`SchedulerSelectHelper+`、`SchedulerSelectHelper+`、`SchedulerSelectHelper+`、`FluxSamplerParams+`、`FluxSamplerParams+`、`FluxSamplerParams+`、`FluxSamplerParams+`、`FluxSamplerParams+`、`FluxSamplerParams+`、`FluxSamplerParams+`、`FluxSamplerParams+`、`FluxSamplerParams+`、`FluxSamplerParams+`、`FluxSamplerParams+`、`SamplerSelectHelper+`、`SamplerSelectHelper+`、`SamplerSelectHelper+`、`SamplerSelectHelper+`、`ChangeImageBatchSize //Inspire`、`DF_DynamicPrompts_Text_Box`、`SDXL Empty Latent Image (rgthree)`

## 学习发现

- 次要节点 `Concat Text _O` 知识库中没有该节点类型的任何知识
- 次要节点 `Float to String` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: JoyCaption2` 知识库中没有该节点类型的任何知识
- 次要节点 `SchedulerSelectHelper+` 知识库中没有该节点类型的任何知识
- 次要节点 `SchedulerSelectHelper+` 知识库中没有该节点类型的任何知识
- 次要节点 `SchedulerSelectHelper+` 知识库中没有该节点类型的任何知识
- 次要节点 `SchedulerSelectHelper+` 知识库中没有该节点类型的任何知识
- 核心节点 `FluxSamplerParams+` 仅有 KSampler/Checkpoint 的通用知识，没有该节点自己的说明
- 核心节点 `FluxSamplerParams+` 仅有 KSampler/Checkpoint 的通用知识，没有该节点自己的说明
- 核心节点 `FluxSamplerParams+` 仅有 KSampler/Checkpoint 的通用知识，没有该节点自己的说明
- 核心节点 `FluxSamplerParams+` 仅有 KSampler/Checkpoint 的通用知识，没有该节点自己的说明
- 核心节点 `FluxSamplerParams+` 仅有 KSampler/Checkpoint 的通用知识，没有该节点自己的说明
- 核心节点 `FluxSamplerParams+` 仅有 KSampler/Checkpoint 的通用知识，没有该节点自己的说明
- 核心节点 `FluxSamplerParams+` 仅有 KSampler/Checkpoint 的通用知识，没有该节点自己的说明
- 核心节点 `FluxSamplerParams+` 仅有 KSampler/Checkpoint 的通用知识，没有该节点自己的说明
- 核心节点 `FluxSamplerParams+` 仅有 KSampler/Checkpoint 的通用知识，没有该节点自己的说明
- 核心节点 `FluxSamplerParams+` 仅有 KSampler/Checkpoint 的通用知识，没有该节点自己的说明
- 核心节点 `FluxSamplerParams+` 仅有 KSampler/Checkpoint 的通用知识，没有该节点自己的说明
- 核心节点 `SamplerSelectHelper+` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 核心节点 `SamplerSelectHelper+` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 核心节点 `SamplerSelectHelper+` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 核心节点 `SamplerSelectHelper+` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `ChangeImageBatchSize //Inspire` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `DF_DynamicPrompts_Text_Box` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `SDXL Empty Latent Image (rgthree)` 仅有 VAE/Checkpoint/Resolution 的通用知识，没有该节点自己的说明
