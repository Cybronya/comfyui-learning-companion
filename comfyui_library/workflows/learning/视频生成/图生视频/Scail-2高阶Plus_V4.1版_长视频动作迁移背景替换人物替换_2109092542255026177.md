---
key: 视频生成/图生视频/Scail-2高阶Plus_V4.1版_长视频动作迁移背景替换人物替换_2109092542255026177.json
name: Scail-2高阶Plus_V4.1版_长视频动作迁移背景替换人物替换_2109092542255026177
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Scail-2高阶Plus_V4.1版_长视频动作迁移背景替换人物替换_2109092542255026177.json
hash: b73fc8b1b2dd8929
coverage: 0.541985
learned_at: 2026-10-17 22:50:14
nodes: [PlaySound|pysssss, SetNode, SetNode, SetNode, WanAnimatePlus SetBlockSwap, WanAnimatePlus SetLoRAs, GetNode, GetNode, WanAnimatePlus Decode, GetNode, ImageResizeKJv2, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, WanAnimatePlus ClipVisionEncode V2, GetNode, VHS_VideoCombine, SetNode, WanAnimatePlus ContextOptions, WanAnimatePlus BlockSwap, GetNode, GetNode, GetNode, WanAnimatePlus SamplerSettings, SetNode, GetNode, SetNode, ImageResizeKJv2, SetNode, SetNode, GetNode, WanAnimatePlus SamplerFromSettings, PreviewImage, VHS_VideoCombine, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Seed (rgthree), PreviewImage, SAM3_VideoTrack, SAM3_VideoTrack, SetNode, GetNode, LoadImage, PreviewImage, SetNode, VHS_VideoCombine, Fast Groups Bypasser (rgthree), LoadImage, SetNode, FastGroupsBypassSwitch, GetNode, GetNode, Image Blank, RepeatImageBatch, WanAnimatePlus VAELoader, CLIPVisionLoader, CheckpointLoaderSimple, CLIPTextEncode, RepeatImageBatch, SAM3_TrackToMask, Image Blank, ImageCompositeMasked, SetNode, WanAnimatePlus ModelLoader, ImageResizeKJv2, SetNode, SetNode, ImageCompositeMasked, SAM3_TrackToMask, GetNode, WanVideoTextEncodeCached, GetNode, INTConstant, INTConstant, Int, Int, SetNode, SCAIL2ColoredMaskV2, WanAnimatePlus SCAIL_2 Embeds, SetNode, WanAnimatePlus LoraSelect, WanAnimatePlus LoraSelectMulti, Fast Groups Bypasser (rgthree), WanAnimatePlus SCAIL_2 TwoPhase Settings, VHS_VideoInfoLoaded, VHS_LoadVideo, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note, LoadImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "checkpoint": "sam3.1_multiplex_fp16.safetensors", "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Scail-2高阶Plus_V4.1版_长视频动作迁移背景替换人物替换_2109092542255026177.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Scail-2高阶Plus_V4.1版_长视频动作迁移背景替换人物替换_2109092542255026177.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（131 个）：
- `PlaySound|pysssss`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanAnimatePlus SetBlockSwap`
- `WanAnimatePlus SetLoRAs`
- `GetNode`
- `GetNode`
- `WanAnimatePlus Decode`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanAnimatePlus ClipVisionEncode V2`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `WanAnimatePlus ContextOptions`
- `WanAnimatePlus BlockSwap`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanAnimatePlus SamplerSettings` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanAnimatePlus SamplerFromSettings` ★核心
- `PreviewImage`
- `VHS_VideoCombine`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Seed (rgthree)`
- `PreviewImage`
- `SAM3_VideoTrack`
- `SAM3_VideoTrack`
- `SetNode`
- `GetNode`
- `LoadImage`
- `PreviewImage`
- `SetNode`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `SetNode`
- `FastGroupsBypassSwitch`
- `GetNode`
- `GetNode`
- `Image Blank`
- `RepeatImageBatch`
- `WanAnimatePlus VAELoader`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `RepeatImageBatch`
- `SAM3_TrackToMask`
- `Image Blank`
- `ImageCompositeMasked`
- `SetNode`
- `WanAnimatePlus ModelLoader`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `ImageCompositeMasked`
- `SAM3_TrackToMask`
- `GetNode`
- `WanVideoTextEncodeCached`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `Int`
- `Int`
- `SetNode`
- `SCAIL2ColoredMaskV2`
- `WanAnimatePlus SCAIL_2 Embeds`
- `SetNode`
- `WanAnimatePlus LoraSelect`
- `WanAnimatePlus LoraSelectMulti`
- `Fast Groups Bypasser (rgthree)`
- `WanAnimatePlus SCAIL_2 TwoPhase Settings`
- `VHS_VideoInfoLoaded`
- `VHS_LoadVideo`
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
- `LoadImage`
- `PreviewImage`

**识别到的模式**：text_to_image

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`
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

覆盖率 **54%**（71/131）

**有卡**：`PlaySound|pysssss`、`WanAnimatePlus SetBlockSwap`、`WanAnimatePlus SetLoRAs`、`WanAnimatePlus Decode`、`ImageResizeKJv2`、`WanAnimatePlus ClipVisionEncode V2`、`VHS_VideoCombine`、`WanAnimatePlus ContextOptions`、`WanAnimatePlus BlockSwap`、`WanAnimatePlus SamplerSettings`、`WanAnimatePlus SamplerFromSettings`、`Seed (rgthree)`、`SAM3_VideoTrack`、`LoadImage`、`FastGroupsBypassSwitch`、`Image Blank`、`RepeatImageBatch`、`WanAnimatePlus VAELoader`、`CLIPVisionLoader`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`SAM3_TrackToMask`、`ImageCompositeMasked`、`WanAnimatePlus ModelLoader`、`WanVideoTextEncodeCached`、`INTConstant`、`Int`、`SCAIL2ColoredMaskV2`、`WanAnimatePlus SCAIL_2 Embeds`、`WanAnimatePlus LoraSelect`、`WanAnimatePlus LoraSelectMulti`、`WanAnimatePlus SCAIL_2 TwoPhase Settings`、`VHS_VideoInfoLoaded`、`VHS_LoadVideo`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
