---
key: 平台全量/Scail-2 高阶工作流Plus V3.2版【长视频 + 多图参考 + 动作迁移 + 背景替换】_2071133720278552578.json
name: Scail-2 高阶工作流Plus V3.2版【长视频 + 多图参考 + 动作迁移 + 背景替换】_2071133720278552578
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Scail-2 高阶工作流Plus V3.2版【长视频 + 多图参考 + 动作迁移 + 背景替换】_2071133720278552578.json
hash: 39340c1411de5f5d
coverage: 0.464968
learned_at: 2026-11-14 00:57:02
nodes: [SetNode, WanAnimatePlus SetBlockSwap, WanAnimatePlus VAELoader, Note, PlaySound|pysssss, SetNode, Note, GetNode, VHS_VideoInfoLoaded, SetNode, Label (rgthree), GetNode, Label (rgthree), GetNode, VHS_VideoCombine, GetNode, GetNode, SetNode, SetNode, SetNode, Label (rgthree), GetNode, ImageResizeKJv2, SetNode, LoadImage, SetNode, VHS_VideoCombine, GetNode, SetNode, ImageResizeKJv2, ImageResizeKJv2, PreviewImage, CLIPTextEncode, CheckpointLoaderSimple, SAM3_VideoTrack, WanAnimatePlus SamplerFromSettings, GetNode, GetNode, LoadImage, LoadImage, LoadImage, ImageBatchMulti, GetNode, SetNode, GetNode, GetNode, PreviewImage, LoadImage, SCAIL2ColoredMaskV2, PreviewImage, VHS_VideoCombine, SetNode, PreviewImage, GetNode, GetNode, CheckpointLoaderSimple, LoadImage, AutoRefCollage, LoadImage, LoadImage, LoadImage, GetNode, ConvertOpenPoseKeypointsToDWPose, PoseDetectionVitPoseToDWPose, GetNode, GetNode, GetNode, RenderNLFPoses, VHS_VideoCombine, GetNode, SDPoseKeypointExtractor, NLFPredict, LoadNLFModel, CheckpointLoaderSimple, OnnxDetectionModelLoader, SetNode, ImageBatchMultiV2, CLIPVisionLoader, SetNode, GetNode, WanAnimatePlus ClipVisionEncode V2, PreviewImage, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, SetNode, Label (rgthree), ComfySwitchNodeV2, SetNode, SetNode, Int, SAM3_VideoTrack, SAM3_VideoTrack, WanAnimatePlus Decode, GetNode, GetNode, GetNode, ImageResizeKJv2, Label (rgthree), MarkdownNote, Label (rgthree), WanAnimatePlus ContextOptions, Seed (rgthree), GetNode, GetNode, Label (rgthree), Label (rgthree), Int, INTConstant, INTConstant, WanAnimatePlus ModelLoader, WanAnimatePlus SamplerSettings, Note, WanAnimatePlus BlockSwap, GetNode, WanAnimatePlus SetLoRAs, WanAnimatePlus SCAIL_2 Embeds, SetNode, SetNode, SetNode, SetNode, WanAnimatePlus LoraSelectMulti, SetNode, Fast Groups Bypasser (rgthree), GetNode, LoadImage, Any Switch (rgthree), GetNode, PrimitiveBoolean, PrimitiveBoolean, WanAnimatePlus LoraSelectMulti, FastGroupsBypassSwitch, FastGroupsBypassSwitch, LoadImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), WanVideoTextEncodeCached, Fast Groups Bypasser (rgthree), VHS_LoadVideo]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 平台全量/Scail-2 高阶工作流Plus V3.2版【长视频 + 多图参考 + 动作迁移 + 背景替换】_2071133720278552578.json

> 来源文件 `comfyui_library/workflows/平台全量/Scail-2 高阶工作流Plus V3.2版【长视频 + 多图参考 + 动作迁移 + 背景替换】_2071133720278552578.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（157 个）：
- `SetNode`
- `WanAnimatePlus SetBlockSwap`
- `WanAnimatePlus VAELoader`
- `Note`
- `PlaySound|pysssss`
- `SetNode`
- `Note`
- `GetNode`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `Label (rgthree)`
- `GetNode`
- `Label (rgthree)`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Label (rgthree)`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `LoadImage`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `SetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `SAM3_VideoTrack`
- `WanAnimatePlus SamplerFromSettings` ★核心
- `GetNode`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ImageBatchMulti`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `LoadImage`
- `SCAIL2ColoredMaskV2`
- `PreviewImage`
- `VHS_VideoCombine`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `AutoRefCollage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `GetNode`
- `ConvertOpenPoseKeypointsToDWPose`
- `PoseDetectionVitPoseToDWPose`
- `GetNode`
- `GetNode`
- `GetNode`
- `RenderNLFPoses`
- `VHS_VideoCombine`
- `GetNode`
- `SDPoseKeypointExtractor`
- `NLFPredict`
- `LoadNLFModel`
- `CheckpointLoaderSimple` ★核心
- `OnnxDetectionModelLoader`
- `SetNode`
- `ImageBatchMultiV2`
- `CLIPVisionLoader`
- `SetNode`
- `GetNode`
- `WanAnimatePlus ClipVisionEncode V2`
- `PreviewImage`
- `SetNode`
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
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `Label (rgthree)`
- `ComfySwitchNodeV2`
- `SetNode`
- `SetNode`
- `Int`
- `SAM3_VideoTrack`
- `SAM3_VideoTrack`
- `WanAnimatePlus Decode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `Label (rgthree)`
- `MarkdownNote`
- `Label (rgthree)`
- `WanAnimatePlus ContextOptions`
- `Seed (rgthree)`
- `GetNode`
- `GetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `Int`
- `INTConstant`
- `INTConstant`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus SamplerSettings` ★核心
- `Note`
- `WanAnimatePlus BlockSwap`
- `GetNode`
- `WanAnimatePlus SetLoRAs`
- `WanAnimatePlus SCAIL_2 Embeds`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanAnimatePlus LoraSelectMulti`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `LoadImage`
- `Any Switch (rgthree)`
- `GetNode`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `WanAnimatePlus LoraSelectMulti`
- `FastGroupsBypassSwitch`
- `FastGroupsBypassSwitch`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `WanVideoTextEncodeCached`
- `Fast Groups Bypasser (rgthree)`
- `VHS_LoadVideo`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **46%**（73/157）

**有卡**：`WanAnimatePlus SetBlockSwap`、`WanAnimatePlus VAELoader`、`PlaySound|pysssss`、`VHS_VideoInfoLoaded`、`Label (rgthree)`、`VHS_VideoCombine`、`ImageResizeKJv2`、`LoadImage`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`SAM3_VideoTrack`、`WanAnimatePlus SamplerFromSettings`、`ImageBatchMulti`、`SCAIL2ColoredMaskV2`、`AutoRefCollage`、`ConvertOpenPoseKeypointsToDWPose`、`PoseDetectionVitPoseToDWPose`、`RenderNLFPoses`、`SDPoseKeypointExtractor`、`NLFPredict`、`LoadNLFModel`、`OnnxDetectionModelLoader`、`ImageBatchMultiV2`、`CLIPVisionLoader`、`WanAnimatePlus ClipVisionEncode V2`、`ComfySwitchNodeV2`、`Int`、`WanAnimatePlus Decode`、`WanAnimatePlus ContextOptions`、`Seed (rgthree)`、`INTConstant`、`WanAnimatePlus ModelLoader`、`WanAnimatePlus SamplerSettings`、`WanAnimatePlus BlockSwap`、`WanAnimatePlus SetLoRAs`、`WanAnimatePlus SCAIL_2 Embeds`、`WanAnimatePlus LoraSelectMulti`、`PrimitiveBoolean`、`FastGroupsBypassSwitch`、`WanVideoTextEncodeCached`、`VHS_LoadVideo`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ConvertOpenPoseKeypointsToDWPose、Seed (rgthree)、WanAnimatePlus SamplerFromSettings、WanAnimatePlus SamplerSettings、WanAnimatePlus ClipVisionEncode V2
