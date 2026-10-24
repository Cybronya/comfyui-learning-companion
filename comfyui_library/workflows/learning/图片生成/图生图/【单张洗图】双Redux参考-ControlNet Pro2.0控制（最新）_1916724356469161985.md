---
key: 图片生成/图生图/【单张洗图】双Redux参考-ControlNet Pro2.0控制（最新）_1916724356469161985.json
name: 【单张洗图】双Redux参考-ControlNet Pro2.0控制（最新）_1916724356469161985
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【单张洗图】双Redux参考-ControlNet Pro2.0控制（最新）_1916724356469161985.json
hash: ca8391244d6e4d40
coverage: 0.790698
learned_at: 2026-10-23 11:49:44
nodes: [RandomNoise, EmptyLatentImage, Image Comparer (rgthree), KSamplerSelect, BasicScheduler, CLIPVisionLoader, StyleModelLoader, BasicGuider, SamplerCustomAdvanced, LoadImage, CR Text Concatenate, PreviewImage, AIO_Preprocessor, SetUnionControlNetType, ControlNetLoader, ReduxAdvanced, CLIPTextEncodeFlux, Note, CR Text, LTXVPromptEnhancer, VAEDecode, PreviewImage, ImageResize+, ReduxAdvanced, ImageCASharpening+, ACN_AdvancedControlNetApplySingle_v2, CheckpointLoaderSimple, Anything Everywhere, LTXVPromptEnhancerLoader, Anything Everywhere, VAELoader, DualCLIPLoader, Note, CM_IntToBool, CR String To Number, Note, LoraLoader, StringConstant, Int, Anything Everywhere, SaveImage, LayerColor: ColorAdapter, ImpactConditionalBranch]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "checkpoint": "麦橘超然majicFlus_v1_liblib.safetensors", "controlnet_strength": 0.4000000000000001, "height": 960, "lora_name": "F.1-【暗影幽梦】情绪氛围冷艳感_V1.safetensors", "strength_clip": 1, "strength_model": 1.0000000000000002, "width": 720}
---

# 图片生成/图生图/【单张洗图】双Redux参考-ControlNet Pro2.0控制（最新）_1916724356469161985.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【单张洗图】双Redux参考-ControlNet Pro2.0控制（最新）_1916724356469161985.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `RandomNoise`
- `EmptyLatentImage` ★核心
- `Image Comparer (rgthree)`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `CLIPVisionLoader`
- `StyleModelLoader`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `LoadImage`
- `CR Text Concatenate`
- `PreviewImage`
- `AIO_Preprocessor`
- `SetUnionControlNetType`
- `ControlNetLoader`
- `ReduxAdvanced`
- `CLIPTextEncodeFlux` ★核心
- `Note`
- `CR Text`
- `LTXVPromptEnhancer`
- `VAEDecode` ★核心
- `PreviewImage`
- `ImageResize+`
- `ReduxAdvanced`
- `ImageCASharpening+`
- `ACN_AdvancedControlNetApplySingle_v2` ★核心
- `CheckpointLoaderSimple` ★核心
- `Anything Everywhere`
- `LTXVPromptEnhancerLoader`
- `Anything Everywhere`
- `VAELoader`
- `DualCLIPLoader`
- `Note`
- `CM_IntToBool`
- `CR String To Number`
- `Note`
- `LoraLoader` ★核心
- `StringConstant`
- `Int`
- `Anything Everywhere`
- `SaveImage`
- `LayerColor: ColorAdapter`
- `ImpactConditionalBranch`

**识别到的模式**：lora

## 关键参数

- `width` = `720`
- `height` = `960`
- `batch_size` = `1`
- `controlnet_strength` = `0.4000000000000001`
- `checkpoint` = `麦橘超然majicFlus_v1_liblib.safetensors`
- `lora_name` = `F.1-【暗影幽梦】情绪氛围冷艳感_V1.safetensors`
- `strength_model` = `1.0000000000000002`
- `strength_clip` = `1`

## 知识

覆盖率 **79%**（34/43）

**有卡**：`RandomNoise`、`EmptyLatentImage`、`KSamplerSelect`、`BasicScheduler`、`CLIPVisionLoader`、`StyleModelLoader`、`BasicGuider`、`SamplerCustomAdvanced`、`LoadImage`、`CR Text Concatenate`、`AIO_Preprocessor`、`SetUnionControlNetType`、`ControlNetLoader`、`ReduxAdvanced`、`CLIPTextEncodeFlux`、`CR Text`、`LTXVPromptEnhancer`、`VAEDecode`、`ImageResize+`、`ImageCASharpening+`、`ACN_AdvancedControlNetApplySingle_v2`、`CheckpointLoaderSimple`、`LTXVPromptEnhancerLoader`、`VAELoader`、`DualCLIPLoader`、`CM_IntToBool`、`CR String To Number`、`LoraLoader`、`StringConstant`、`Int`、`SaveImage`、`LayerColor: ColorAdapter`、`ImpactConditionalBranch`

**用到的条目**：VAEDecode、VAELoader、CheckpointLoaderSimple、EmptyLatentImage、LoadImage、ControlNetLoader、SetUnionControlNetType、ACN_AdvancedControlNetApplySingle_v2
