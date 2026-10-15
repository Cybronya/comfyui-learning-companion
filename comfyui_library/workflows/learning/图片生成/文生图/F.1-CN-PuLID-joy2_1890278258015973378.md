---
key: 图片生成/文生图/F.1-CN-PuLID-joy2_1890278258015973378.json
name: F.1-CN-PuLID-joy2_1890278258015973378
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/F.1-CN-PuLID-joy2_1890278258015973378.json
hash: e695c5de3726b581
coverage: 0.652632
learned_at: 2026-10-15 22:26:16
nodes: [PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Text Concatenate (JPS), CLIPTextEncodeFlux, Any Switch (rgthree), Mute / Bypass Repeater (rgthree), Reroute, ApplyPulidFlux, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Fast Bypasser (rgthree), VAELoader, easy cleanGpuUsed, EmptyLatentImage, ConstrainImage|pysssss, GetImageSize, EmptyLatentImage, Mute / Bypass Repeater (rgthree), Reroute, Mute / Bypass Repeater (rgthree), LoadImage, Mute / Bypass Repeater (rgthree), LoadImage, Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Reroute, Reroute, Reroute, Reroute, Fast Bypasser (rgthree), Fast Bypasser (rgthree), KSampler, Reroute, LoraLoader, LoraLoader, Fast Bypasser (rgthree), Fast Bypasser (rgthree), Joy_caption_two, easy showAnything, Fast Bypasser (rgthree), Fast Bypasser (rgthree), VAEDecode, TextInput_, SaveImage, CLIPTextEncode, LayerUtility: ColorPicker, LayerUtility: ImageRemoveAlpha, PreviewImage, Fast Bypasser (rgthree), Mute / Bypass Repeater (rgthree), AIO_Preprocessor, PreviewImage, ControlNetApplyAdvanced, Reroute, Reroute, DWPreprocessor, PreviewImage, Canny, Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), PreviewImage, Fast Bypasser (rgthree), Reroute, Reroute, Reroute, ControlNetApplyAdvanced, SetShakkerLabsUnionControlNetType, Fast Bypasser (rgthree), ControlNetApplyAdvanced, Fast Bypasser (rgthree), Fast Bypasser (rgthree), LoadImage, LayerMask: SegmentAnythingUltra V2, ControlNetLoader, UNETLoader, DualCLIPLoader, LoraLoader, PulidFluxModelLoader, Joy_caption_two_load]
patterns: [text_to_image, lora]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "controlnet_strength": 0.8, "denoise": 1, "height": 1024, "lora_name": "秋日森林_秋天女孩_V1.0.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 732946905914755, "steps": 20, "strength_clip": 1, "strength_model": 0.8, "width": 768}
---

# 图片生成/文生图/F.1-CN-PuLID-joy2_1890278258015973378.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/F.1-CN-PuLID-joy2_1890278258015973378.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（95 个）：
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Text Concatenate (JPS)`
- `CLIPTextEncodeFlux` ★核心
- `Any Switch (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Reroute`
- `ApplyPulidFlux`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Fast Bypasser (rgthree)`
- `VAELoader`
- `easy cleanGpuUsed`
- `EmptyLatentImage` ★核心
- `ConstrainImage|pysssss`
- `GetImageSize`
- `EmptyLatentImage` ★核心
- `Mute / Bypass Repeater (rgthree)`
- `Reroute`
- `Mute / Bypass Repeater (rgthree)`
- `LoadImage`
- `Mute / Bypass Repeater (rgthree)`
- `LoadImage`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `KSampler` ★核心
- `Reroute`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `Joy_caption_two`
- `easy showAnything`
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `VAEDecode` ★核心
- `TextInput_`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `LayerUtility: ColorPicker`
- `LayerUtility: ImageRemoveAlpha`
- `PreviewImage`
- `Fast Bypasser (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `AIO_Preprocessor`
- `PreviewImage`
- `ControlNetApplyAdvanced` ★核心
- `Reroute`
- `Reroute`
- `DWPreprocessor`
- `PreviewImage`
- `Canny`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `PreviewImage`
- `Fast Bypasser (rgthree)`
- `Reroute`
- `Reroute`
- `Reroute`
- `ControlNetApplyAdvanced` ★核心
- `SetShakkerLabsUnionControlNetType`
- `Fast Bypasser (rgthree)`
- `ControlNetApplyAdvanced` ★核心
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `LoadImage`
- `LayerMask: SegmentAnythingUltra V2`
- `ControlNetLoader`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LoraLoader` ★核心
- `PulidFluxModelLoader`
- `Joy_caption_two_load`

**识别到的模式**：text_to_image、lora

## 关键参数

- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `732946905914755`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `秋日森林_秋天女孩_V1.0.safetensors`
- `strength_model` = `0.8`
- `strength_clip` = `1`
- `controlnet_strength` = `0.8`

## 知识

覆盖率 **65%**（62/95）

**有卡**：`PulidFluxEvaClipLoader`、`PulidFluxInsightFaceLoader`、`Mute / Bypass Repeater (rgthree)`、`Text Concatenate (JPS)`、`CLIPTextEncodeFlux`、`ApplyPulidFlux`、`Fast Bypasser (rgthree)`、`VAELoader`、`easy cleanGpuUsed`、`EmptyLatentImage`、`ConstrainImage|pysssss`、`GetImageSize`、`LoadImage`、`KSampler`、`LoraLoader`、`Joy_caption_two`、`VAEDecode`、`TextInput_`、`SaveImage`、`CLIPTextEncode`、`LayerUtility: ColorPicker`、`LayerUtility: ImageRemoveAlpha`、`AIO_Preprocessor`、`ControlNetApplyAdvanced`、`DWPreprocessor`、`Canny`、`SetShakkerLabsUnionControlNetType`、`LayerMask: SegmentAnythingUltra V2`、`ControlNetLoader`、`UNETLoader`、`DualCLIPLoader`、`PulidFluxModelLoader`、`Joy_caption_two_load`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced
