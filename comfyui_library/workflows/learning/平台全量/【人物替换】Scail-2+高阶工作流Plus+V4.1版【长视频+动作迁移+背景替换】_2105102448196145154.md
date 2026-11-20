---
key: 平台全量/【人物替换】Scail-2+高阶工作流Plus+V4.1版【长视频+动作迁移+背景替换】_2105102448196145154.json
name: 【人物替换】Scail-2+高阶工作流Plus+V4.1版【长视频+动作迁移+背景替换】_2105102448196145154
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【人物替换】Scail-2+高阶工作流Plus+V4.1版【长视频+动作迁移+背景替换】_2105102448196145154.json
hash: 421c990128da8cf4
coverage: 0.419643
learned_at: 2026-11-14 01:22:59
nodes: [Note, PlaySound|pysssss, SetNode, SetNode, SetNode, WanAnimatePlus SetBlockSwap, WanAnimatePlus SetLoRAs, Note, GetNode, GetNode, WanAnimatePlus Decode, GetNode, ImageResizeKJv2, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, Note, GetNode, WanAnimatePlus ClipVisionEncode V2, GetNode, VHS_VideoCombine, SetNode, WanAnimatePlus ContextOptions, WanAnimatePlus BlockSwap, GetNode, GetNode, GetNode, WanAnimatePlus SamplerSettings, SetNode, GetNode, SetNode, ImageResizeKJv2, SetNode, GetNode, SetNode, GetNode, WanAnimatePlus SamplerFromSettings, PreviewImage, VHS_VideoCombine, VHS_VideoInfoLoaded, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Seed (rgthree), PreviewImage, SAM3_VideoTrack, SAM3_VideoTrack, SetNode, GetNode, LoadImage, PreviewImage, SetNode, VHS_VideoCombine, Fast Groups Bypasser (rgthree), LoadImage, SetNode, FastGroupsBypassSwitch, GetNode, GetNode, Image Blank, RepeatImageBatch, WanAnimatePlus VAELoader, CLIPVisionLoader, CheckpointLoaderSimple, CLIPTextEncode, RepeatImageBatch, SAM3_TrackToMask, Image Blank, ImageCompositeMasked, SetNode, VHS_LoadVideo, ImageResizeKJv2, SetNode, SetNode, ImageCompositeMasked, SAM3_TrackToMask, GetNode, WanVideoTextEncodeCached, GetNode, INTConstant, INTConstant, Int, Int, SetNode, SCAIL2ColoredMaskV2, MarkdownNote, WanAnimatePlus SCAIL_2 Embeds, SetNode, MarkdownNote, WanAnimatePlus LoraSelect, WanAnimatePlus LoraSelectMulti, Fast Groups Bypasser (rgthree), MarkdownNote, WanAnimatePlus SCAIL_2 TwoPhase Settings, WanAnimatePlus ModelLoader]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 平台全量/【人物替换】Scail-2+高阶工作流Plus+V4.1版【长视频+动作迁移+背景替换】_2105102448196145154.json

> 来源文件 `comfyui_library/workflows/平台全量/【人物替换】Scail-2+高阶工作流Plus+V4.1版【长视频+动作迁移+背景替换】_2105102448196145154.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（112 个）：
- `Note`
- `PlaySound|pysssss`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanAnimatePlus SetBlockSwap`
- `WanAnimatePlus SetLoRAs`
- `Note`
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
- `Note`
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
- `GetNode`
- `SetNode`
- `GetNode`
- `WanAnimatePlus SamplerFromSettings` ★核心
- `PreviewImage`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
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
- `VHS_LoadVideo`
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
- `MarkdownNote`
- `WanAnimatePlus SCAIL_2 Embeds`
- `SetNode`
- `MarkdownNote`
- `WanAnimatePlus LoraSelect`
- `WanAnimatePlus LoraSelectMulti`
- `Fast Groups Bypasser (rgthree)`
- `MarkdownNote`
- `WanAnimatePlus SCAIL_2 TwoPhase Settings`
- `WanAnimatePlus ModelLoader`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **42%**（47/112）

**有卡**：`PlaySound|pysssss`、`WanAnimatePlus SetBlockSwap`、`WanAnimatePlus SetLoRAs`、`WanAnimatePlus Decode`、`ImageResizeKJv2`、`WanAnimatePlus ClipVisionEncode V2`、`VHS_VideoCombine`、`WanAnimatePlus ContextOptions`、`WanAnimatePlus BlockSwap`、`WanAnimatePlus SamplerSettings`、`WanAnimatePlus SamplerFromSettings`、`VHS_VideoInfoLoaded`、`Seed (rgthree)`、`SAM3_VideoTrack`、`LoadImage`、`FastGroupsBypassSwitch`、`Image Blank`、`RepeatImageBatch`、`WanAnimatePlus VAELoader`、`CLIPVisionLoader`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`SAM3_TrackToMask`、`ImageCompositeMasked`、`VHS_LoadVideo`、`WanVideoTextEncodeCached`、`INTConstant`、`Int`、`SCAIL2ColoredMaskV2`、`WanAnimatePlus SCAIL_2 Embeds`、`WanAnimatePlus LoraSelect`、`WanAnimatePlus LoraSelectMulti`、`WanAnimatePlus SCAIL_2 TwoPhase Settings`、`WanAnimatePlus ModelLoader`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、Seed (rgthree)、WanAnimatePlus SamplerFromSettings、WanAnimatePlus SamplerSettings、WanAnimatePlus ClipVisionEncode V2、WanAnimatePlus Decode
