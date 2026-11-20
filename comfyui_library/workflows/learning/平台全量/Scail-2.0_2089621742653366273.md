---
key: 平台全量/Scail-2.0_2089621742653366273.json
name: Scail-2.0_2089621742653366273
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Scail-2.0_2089621742653366273.json
hash: 058fea8e1a293bee
coverage: 0.425926
learned_at: 2026-11-14 00:57:04
nodes: [PlaySound|pysssss, WanAnimatePlus SetBlockSwap, WanAnimatePlus SetLoRAs, GetNode, GetNode, GetNode, ImageResizeKJv2, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, Note, GetNode, WanAnimatePlus ClipVisionEncode V2, GetNode, VHS_VideoCombine, SetNode, WanAnimatePlus ContextOptions, WanAnimatePlus BlockSwap, GetNode, GetNode, GetNode, WanAnimatePlus SamplerSettings, SetNode, GetNode, SetNode, SetNode, PreviewImage, VHS_VideoInfoLoaded, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Seed (rgthree), SAM3_VideoTrack, SAM3_VideoTrack, SetNode, GetNode, PreviewImage, SetNode, GetNode, GetNode, Image Blank, RepeatImageBatch, WanAnimatePlus VAELoader, CLIPVisionLoader, CheckpointLoaderSimple, CLIPTextEncode, RepeatImageBatch, SAM3_TrackToMask, Image Blank, ImageCompositeMasked, SetNode, ImageResizeKJv2, ImageCompositeMasked, SAM3_TrackToMask, GetNode, GetNode, INTConstant, INTConstant, Int, Int, WanAnimatePlus SCAIL_2 Embeds, SetNode, WanAnimatePlus LoraSelect, WanAnimatePlus LoraSelectMulti, WanAnimatePlus SCAIL_2 TwoPhase Settings, PreviewImage, GetNode, SetNode, WanAnimatePlus Decode, SetNode, SetNode, SetNode, SetNode, SCAIL2ColoredMaskV2, VHS_VideoCombine, SetNode, SetNode, Fast Groups Bypasser (rgthree), GetNode, Note, Fast Groups Bypasser (rgthree), WanAnimatePlus ModelLoader, GetNode, ImageResizeKJv2, LoadImage, SetNode, VHS_VideoCombine, MarkdownNote, GetNode, SetNode, GetNode, WanAnimatePlus SamplerFromSettings, VHS_LoadVideo, LoadImage, WanVideoTextEncodeCached]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 平台全量/Scail-2.0_2089621742653366273.json

> 来源文件 `comfyui_library/workflows/平台全量/Scail-2.0_2089621742653366273.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（108 个）：
- `PlaySound|pysssss`
- `WanAnimatePlus SetBlockSwap`
- `WanAnimatePlus SetLoRAs`
- `GetNode`
- `GetNode`
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
- `SetNode`
- `PreviewImage`
- `VHS_VideoInfoLoaded`
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
- `Seed (rgthree)`
- `SAM3_VideoTrack`
- `SAM3_VideoTrack`
- `SetNode`
- `GetNode`
- `PreviewImage`
- `SetNode`
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
- `ImageResizeKJv2`
- `ImageCompositeMasked`
- `SAM3_TrackToMask`
- `GetNode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `Int`
- `Int`
- `WanAnimatePlus SCAIL_2 Embeds`
- `SetNode`
- `WanAnimatePlus LoraSelect`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus SCAIL_2 TwoPhase Settings`
- `PreviewImage`
- `GetNode`
- `SetNode`
- `WanAnimatePlus Decode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SCAIL2ColoredMaskV2`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `WanAnimatePlus ModelLoader`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `SetNode`
- `VHS_VideoCombine`
- `MarkdownNote`
- `GetNode`
- `SetNode`
- `GetNode`
- `WanAnimatePlus SamplerFromSettings` ★核心
- `VHS_LoadVideo`
- `LoadImage`
- `WanVideoTextEncodeCached`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **43%**（46/108）

**有卡**：`PlaySound|pysssss`、`WanAnimatePlus SetBlockSwap`、`WanAnimatePlus SetLoRAs`、`ImageResizeKJv2`、`WanAnimatePlus ClipVisionEncode V2`、`VHS_VideoCombine`、`WanAnimatePlus ContextOptions`、`WanAnimatePlus BlockSwap`、`WanAnimatePlus SamplerSettings`、`VHS_VideoInfoLoaded`、`Seed (rgthree)`、`SAM3_VideoTrack`、`Image Blank`、`RepeatImageBatch`、`WanAnimatePlus VAELoader`、`CLIPVisionLoader`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`SAM3_TrackToMask`、`ImageCompositeMasked`、`INTConstant`、`Int`、`WanAnimatePlus SCAIL_2 Embeds`、`WanAnimatePlus LoraSelect`、`WanAnimatePlus LoraSelectMulti`、`WanAnimatePlus SCAIL_2 TwoPhase Settings`、`WanAnimatePlus Decode`、`SCAIL2ColoredMaskV2`、`WanAnimatePlus ModelLoader`、`LoadImage`、`WanAnimatePlus SamplerFromSettings`、`VHS_LoadVideo`、`WanVideoTextEncodeCached`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、Seed (rgthree)、WanAnimatePlus SamplerFromSettings、WanAnimatePlus SamplerSettings、WanAnimatePlus ClipVisionEncode V2、WanAnimatePlus Decode
