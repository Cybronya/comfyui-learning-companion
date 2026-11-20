---
key: 平台全量/写实动作迁移｜视频人物替换主体替换wan2.2_2090843725713993729.json
name: 写实动作迁移｜视频人物替换主体替换wan2.2_2090843725713993729
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/写实动作迁移｜视频人物替换主体替换wan2.2_2090843725713993729.json
hash: a9ea3336c635f1f6
coverage: 0.648352
learned_at: 2026-11-14 01:43:09
nodes: [GetNode, GetNode, SetNode, GetNode, CLIPVisionLoader, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, OnnxDetectionModelLoader, DrawViTPose, WanVideoClipVisionEncode, GetNode, WanVideoSampler, GetNode, Textbox, ImpactInt, Int, SetNode, SetNode, WanVideoModelLoader, MathExpression|pysssss, ImageResizeKJv2, SetNode, SetNode, SetNode, DownloadAndLoadSAM2Model, GrowMask, BlockifyMask, SetNode, DrawMaskOnImage, Sam2Segmentation, WanVideoAnimateEmbeds, WanVideoLoraSelectMulti, WanVideoTextEncodeCached, WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, LayerUtility: ImageScaleByAspectRatio V2, ImageFromBatch, WanVideoVAELoader, SetNode, WanVideoTorchCompileSettings, WanVideoBlockSwap, PoseAndFaceDetection, WanVideoDecode, ImageFromBatch, VHS_VideoCombine, VHS_LoadVideo, LoadImage, ImpactInt, SetNode, SetNode, PreviewImage, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/写实动作迁移｜视频人物替换主体替换wan2.2_2090843725713993729.json

> 来源文件 `comfyui_library/workflows/平台全量/写实动作迁移｜视频人物替换主体替换wan2.2_2090843725713993729.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（91 个）：
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `OnnxDetectionModelLoader`
- `DrawViTPose`
- `WanVideoClipVisionEncode`
- `GetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `Textbox`
- `ImpactInt`
- `Int`
- `SetNode`
- `SetNode`
- `WanVideoModelLoader`
- `MathExpression|pysssss`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `SetNode`
- `DownloadAndLoadSAM2Model`
- `GrowMask`
- `BlockifyMask`
- `SetNode`
- `DrawMaskOnImage`
- `Sam2Segmentation`
- `WanVideoAnimateEmbeds`
- `WanVideoLoraSelectMulti`
- `WanVideoTextEncodeCached`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageFromBatch`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `PoseAndFaceDetection`
- `WanVideoDecode`
- `ImageFromBatch`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`
- `ImpactInt`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **65%**（59/91）

**有卡**：`CLIPVisionLoader`、`OnnxDetectionModelLoader`、`DrawViTPose`、`WanVideoClipVisionEncode`、`WanVideoSampler`、`Textbox`、`ImpactInt`、`Int`、`WanVideoModelLoader`、`MathExpression|pysssss`、`ImageResizeKJv2`、`DownloadAndLoadSAM2Model`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`Sam2Segmentation`、`WanVideoAnimateEmbeds`、`WanVideoLoraSelectMulti`、`WanVideoTextEncodeCached`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageFromBatch`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`PoseAndFaceDetection`、`WanVideoDecode`、`VHS_VideoCombine`、`VHS_LoadVideo`、`LoadImage`、`ImageConcatMulti`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、EmptyLatentImage、LayerUtility: ImageScaleByAspectRatio V2

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
