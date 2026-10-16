---
key: 视频生成/图生视频/wan2.2动作迁移打造真实感视频 真人级动作复刻效果_2094816106904113154.json
name: wan2.2动作迁移打造真实感视频 真人级动作复刻效果_2094816106904113154
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2动作迁移打造真实感视频 真人级动作复刻效果_2094816106904113154.json
hash: 672ab1b25ecda9bf
coverage: 0.693069
learned_at: 2026-10-17 00:02:52
nodes: [GetNode, WanVideoTorchCompileSettings, WanVideoBlockSwap, SimpleMath+, GetNode, GetNode, GetNode, SetNode, SetNode, SimpleMath+, VHS_VideoInfoLoaded, ImageResizeKJv2, ControlNextGetPoses, GetNode, WanVideoControlEmbeds, Reroute, GetNode, PreviewImage, WanVideoEncode, VHS_VideoCombine, ImageResizeKJv2, GetImageSizeAndCount, SetNode, SetNode, SimpleMath+, Text Multiline, PrimitiveNode, GetNode, WanVideoSLG, GetNode, GetNode, RH_Captioner, Text Concatenate, WanVideoTextEncode, LoadWanVideoT5TextEncoder, SetNode, SetNode, SetNode, SetNode, GetNode, WanVideoImageToVideoEncode, SetNode, GetNode, GetNode, WanVideoSetLoRAs, WanVideoSetLoRAs, Int, Int, ImpactSwitch, VHS_VideoCombine, VHS_VideoCombine, ImageFromBatch, WanVideoDecode, RHHiddenNodes, VHS_VideoCombine, ColorMatch, ImageConcatMulti, WanVideoSetBlockSwap, WanVideoSetBlockSwap, ShowText|pysssss, WanVideoVAELoader, Primitive float [Crystools], WanVideoSampler, VHS_LoadVideo, Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], RHHiddenNodes, WanVideoSampler, RHHiddenNodes, PrimitiveNode, LoadImage, ImageResizeKJ, LoadImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/wan2.2动作迁移打造真实感视频 真人级动作复刻效果_2094816106904113154.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/wan2.2动作迁移打造真实感视频 真人级动作复刻效果_2094816106904113154.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（101 个）：
- `GetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `VHS_VideoInfoLoaded`
- `ImageResizeKJv2`
- `ControlNextGetPoses`
- `GetNode`
- `WanVideoControlEmbeds`
- `Reroute`
- `GetNode`
- `PreviewImage`
- `WanVideoEncode`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `Text Multiline`
- `PrimitiveNode`
- `GetNode`
- `WanVideoSLG`
- `GetNode`
- `GetNode`
- `RH_Captioner`
- `Text Concatenate`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `Int`
- `Int`
- `ImpactSwitch`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageFromBatch`
- `WanVideoDecode`
- `RHHiddenNodes`
- `VHS_VideoCombine`
- `ColorMatch`
- `ImageConcatMulti`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `ShowText|pysssss`
- `WanVideoVAELoader`
- `Primitive float [Crystools]`
- `WanVideoSampler` ★核心
- `VHS_LoadVideo`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `RHHiddenNodes`
- `WanVideoSampler` ★核心
- `RHHiddenNodes`
- `PrimitiveNode`
- `LoadImage`
- `ImageResizeKJ`
- `LoadImage`
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
- `CLIPTextEncode` ★核心
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

覆盖率 **69%**（70/101）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`SimpleMath+`、`VHS_VideoInfoLoaded`、`ImageResizeKJv2`、`ControlNextGetPoses`、`WanVideoControlEmbeds`、`WanVideoEncode`、`VHS_VideoCombine`、`GetImageSizeAndCount`、`Text Multiline`、`WanVideoSLG`、`RH_Captioner`、`Text Concatenate`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoImageToVideoEncode`、`WanVideoSetLoRAs`、`Int`、`ImageFromBatch`、`WanVideoDecode`、`RHHiddenNodes`、`ColorMatch`、`ImageConcatMulti`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`Primitive float [Crystools]`、`WanVideoSampler`、`VHS_LoadVideo`、`Primitive integer [Crystools]`、`LoadImage`、`ImageResizeKJ`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
