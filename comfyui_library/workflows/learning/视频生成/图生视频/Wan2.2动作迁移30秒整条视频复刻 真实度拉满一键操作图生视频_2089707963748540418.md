---
key: 视频生成/图生视频/Wan2.2动作迁移30秒整条视频复刻 真实度拉满一键操作图生视频_2089707963748540418.json
name: Wan2.2动作迁移30秒整条视频复刻 真实度拉满一键操作图生视频_2089707963748540418
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2动作迁移30秒整条视频复刻 真实度拉满一键操作图生视频_2089707963748540418.json
hash: ccbd344aa50fa4b3
coverage: 0.623288
learned_at: 2026-10-16 22:02:16
nodes: [GetNode, WanVideoTorchCompileSettings, GetNode, GetNode, GetNode, PrimitiveNode, GetNode, LoadWanVideoT5TextEncoder, SetNode, SetNode, GetNode, GetNode, WanVideoSetLoRAs, WanVideoSetLoRAs, Int, Int, WanVideoVAELoader, Primitive float [Crystools], PrimitiveNode, WanVideoBlockSwap, LoadImage, ImageResizeKJv2, GetNode, GetImageSizeAndCount, PreviewImage, ImageResizeKJv2, GetNode, GetNode, Reroute, GetNode, GetNode, PrimitiveNode, GetNode, SetNode, GetImageRangeFromBatch, Reroute, GetNode, RepeatImageBatch, GetImageSizeAndCount, SetNode, Primitive integer [Crystools], ControlNextGetPoses, SetNode, SetNode, GetNode, WanVideoImageToVideoEncode, SimpleMath+, GetNode, Primitive integer [Crystools], VHS_VideoInfoLoaded, Primitive integer [Crystools], SetNode, SimpleMath+, SimpleMath+, SimpleMath+, ImpactSwitch, SetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, ColorMatch, ImageFromBatch, RHHiddenNodes, Text Multiline, SimpleMath+, RHHiddenNodes, GetNode, easy forLoopStart, RHHiddenNodes, GetNode, GetNode, GetNode, easy forLoopEnd, ImageBatchMulti, ImageConcatMulti, WanVideoSLG, ColorMatch, GetNode, Primitive float [Crystools], PrimitiveNode, RHHiddenNodes, GetNode, GetNode, WanVideoControlEmbeds, GetNode, GetNode, GetNode, Text Concatenate, RH_Captioner, GetNode, SetNode, Text Multiline, GetNode, WanVideoTextEncode, SetNode, ShowText|pysssss, ImpactSwitch, WanVideoEncode, WanVideoSampler, WanVideoSampler, ImageConcatMulti, WanVideoSLG, WanVideoEncode, WanVideoControlEmbeds, VHS_VideoCombine, WanVideoImageToVideoEncode, WanVideoSampler, ImageFromBatch, SetNode, WanVideoDecode, GetNode, WanVideoSampler, WanVideoDecode, ImageResizeKJ, Primitive integer [Crystools], VHS_LoadVideo, LoadImage, easy showAnything, LoadImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2动作迁移30秒整条视频复刻 真实度拉满一键操作图生视频_2089707963748540418.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Wan2.2动作迁移30秒整条视频复刻 真实度拉满一键操作图生视频_2089707963748540418.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（146 个）：
- `GetNode`
- `WanVideoTorchCompileSettings`
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveNode`
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `Int`
- `Int`
- `WanVideoVAELoader`
- `Primitive float [Crystools]`
- `PrimitiveNode`
- `WanVideoBlockSwap`
- `LoadImage`
- `ImageResizeKJv2`
- `GetNode`
- `GetImageSizeAndCount`
- `PreviewImage`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `Reroute`
- `GetNode`
- `GetNode`
- `PrimitiveNode`
- `GetNode`
- `SetNode`
- `GetImageRangeFromBatch`
- `Reroute`
- `GetNode`
- `RepeatImageBatch`
- `GetImageSizeAndCount`
- `SetNode`
- `Primitive integer [Crystools]`
- `ControlNextGetPoses`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `SimpleMath+`
- `GetNode`
- `Primitive integer [Crystools]`
- `VHS_VideoInfoLoaded`
- `Primitive integer [Crystools]`
- `SetNode`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `ImpactSwitch`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ColorMatch`
- `ImageFromBatch`
- `RHHiddenNodes`
- `Text Multiline`
- `SimpleMath+`
- `RHHiddenNodes`
- `GetNode`
- `easy forLoopStart`
- `RHHiddenNodes`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy forLoopEnd`
- `ImageBatchMulti`
- `ImageConcatMulti`
- `WanVideoSLG`
- `ColorMatch`
- `GetNode`
- `Primitive float [Crystools]`
- `PrimitiveNode`
- `RHHiddenNodes`
- `GetNode`
- `GetNode`
- `WanVideoControlEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `Text Concatenate`
- `RH_Captioner`
- `GetNode`
- `SetNode`
- `Text Multiline`
- `GetNode`
- `WanVideoTextEncode`
- `SetNode`
- `ShowText|pysssss`
- `ImpactSwitch`
- `WanVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `ImageConcatMulti`
- `WanVideoSLG`
- `WanVideoEncode`
- `WanVideoControlEmbeds`
- `VHS_VideoCombine`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `ImageFromBatch`
- `SetNode`
- `WanVideoDecode`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `ImageResizeKJ`
- `Primitive integer [Crystools]`
- `VHS_LoadVideo`
- `LoadImage`
- `easy showAnything`
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

覆盖率 **62%**（91/146）

**有卡**：`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`WanVideoSetLoRAs`、`Int`、`WanVideoVAELoader`、`Primitive float [Crystools]`、`WanVideoBlockSwap`、`LoadImage`、`ImageResizeKJv2`、`GetImageSizeAndCount`、`GetImageRangeFromBatch`、`RepeatImageBatch`、`Primitive integer [Crystools]`、`ControlNextGetPoses`、`WanVideoImageToVideoEncode`、`SimpleMath+`、`VHS_VideoInfoLoaded`、`VHS_VideoCombine`、`ColorMatch`、`ImageFromBatch`、`RHHiddenNodes`、`Text Multiline`、`easy forLoopStart`、`easy forLoopEnd`、`ImageBatchMulti`、`ImageConcatMulti`、`WanVideoSLG`、`WanVideoControlEmbeds`、`Text Concatenate`、`RH_Captioner`、`WanVideoTextEncode`、`WanVideoEncode`、`WanVideoSampler`、`WanVideoDecode`、`ImageResizeKJ`、`VHS_LoadVideo`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
