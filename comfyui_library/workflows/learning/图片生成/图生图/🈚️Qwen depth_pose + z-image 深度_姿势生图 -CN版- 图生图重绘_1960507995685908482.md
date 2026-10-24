---
key: 图片生成/图生图/🈚️Qwen depth_pose + z-image 深度_姿势生图 -CN版- 图生图重绘_1960507995685908482.json
name: 🈚️Qwen depth_pose + z-image 深度_姿势生图 -CN版- 图生图重绘_1960507995685908482
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/🈚️Qwen depth_pose + z-image 深度_姿势生图 -CN版- 图生图重绘_1960507995685908482.json
hash: 7f37e3e1b4a87b76
coverage: 0.581818
learned_at: 2026-10-23 13:38:40
nodes: [PreviewImage, SetNode, SetNode, SetNode, easy cleanGpuUsed, LayerMask: SegmentAnythingUltra, GetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, RebatchLatents, CLIPTextEncode, ControlNetLoader, RH_LLMAPI_NODE, RH_LLMAPI_NODE, ShowText|pysssss, RepeatLatentBatch, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CFGNorm, ModelSamplingAuraFlow, CLIPLoader, CFGZeroStar, LoraLoaderModelOnly, UNETLoader, CLIPTextEncode, ConditioningZeroOut, VAEDecode, CLIPLoader, VAELoader, VAEEncode, UNETLoader, SetNode, LoraLoaderModelOnly, GetNode, GetNode, GetNode, JWInteger, SetNode, JWInteger, SetNode, Int, Note, SetNode, LayerColor: Brightness & Contrast, PreviewImage, SetNode, GetNode, GetNode, GetNode, ImpactSwitch, GetNode, ModelPassThrough, easy textSwitch, SetNode, LayerUtility: ImageScaleByAspectRatio V2, easy cleanGpuUsed, KSamplerSelect, BasicScheduler, SamplerCustom, DetailDaemonSamplerNode, GetNode, CLIPTextEncode, ConditioningZeroOut, SetUnionControlNetType, SetNode, LayerUtility: ImageScaleByAspectRatio V2, DWPreprocessor, AIO_Preprocessor, BackgroundScaler, PreviewImage, SetNode, SetNode, SetNode, LayerUtility: CropByMask V2, easy cleanGpuUsed, easy cleanGpuUsed, RepeatLatentBatch, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, ImageSmartSharpen+, RebatchLatents, easy seed, CR Text Concatenate, CR Text, easy imageRemBg, Anything Everywhere3, SetNode, GetNode, GetNode, SetNode, SetNode, SetNode, LoadImage, LoadImage, SaveImage, PreviewImage, KSampler, ControlNetApplySD3, EmptyLatentImage, GetNode, GetNode]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "controlnet_strength": 0.8000000000000002, "denoise": 0.37000000000000005, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 1030454734910631, "steps": 4, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/🈚️Qwen depth_pose + z-image 深度_姿势生图 -CN版- 图生图重绘_1960507995685908482.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/🈚️Qwen depth_pose + z-image 深度_姿势生图 -CN版- 图生图重绘_1960507995685908482.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（110 个）：
- `PreviewImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `LayerMask: SegmentAnythingUltra`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `RebatchLatents`
- `CLIPTextEncode` ★核心
- `ControlNetLoader`
- `RH_LLMAPI_NODE`
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `RepeatLatentBatch`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `CFGZeroStar`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `JWInteger`
- `SetNode`
- `JWInteger`
- `SetNode`
- `Int`
- `Note`
- `SetNode`
- `LayerColor: Brightness & Contrast`
- `PreviewImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImpactSwitch`
- `GetNode`
- `ModelPassThrough`
- `easy textSwitch`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy cleanGpuUsed`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SamplerCustom` ★核心
- `DetailDaemonSamplerNode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `SetUnionControlNetType`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `DWPreprocessor`
- `AIO_Preprocessor`
- `BackgroundScaler`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `LayerUtility: CropByMask V2`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `RepeatLatentBatch`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageSmartSharpen+`
- `RebatchLatents`
- `easy seed`
- `CR Text Concatenate`
- `CR Text`
- `easy imageRemBg`
- `Anything Everywhere3`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `PreviewImage`
- `KSampler` ★核心
- `ControlNetApplySD3` ★核心
- `EmptyLatentImage` ★核心
- `GetNode`
- `GetNode`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `1030454734910631`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.37000000000000005`
- `controlnet_strength` = `0.8000000000000002`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **58%**（64/110）

**有卡**：`easy cleanGpuUsed`、`LayerMask: SegmentAnythingUltra`、`LayerUtility: ImageScaleByAspectRatio V2`、`RebatchLatents`、`CLIPTextEncode`、`ControlNetLoader`、`RH_LLMAPI_NODE`、`RepeatLatentBatch`、`VAELoader`、`LoraLoaderModelOnly`、`CFGNorm`、`ModelSamplingAuraFlow`、`CLIPLoader`、`CFGZeroStar`、`UNETLoader`、`ConditioningZeroOut`、`VAEDecode`、`VAEEncode`、`JWInteger`、`Int`、`LayerColor: Brightness & Contrast`、`ModelPassThrough`、`easy textSwitch`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustom`、`DetailDaemonSamplerNode`、`SetUnionControlNetType`、`DWPreprocessor`、`AIO_Preprocessor`、`BackgroundScaler`、`LayerUtility: CropByMask V2`、`ImageSmartSharpen+`、`easy seed`、`CR Text Concatenate`、`CR Text`、`easy imageRemBg`、`LoadImage`、`SaveImage`、`KSampler`、`ControlNetApplySD3`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
