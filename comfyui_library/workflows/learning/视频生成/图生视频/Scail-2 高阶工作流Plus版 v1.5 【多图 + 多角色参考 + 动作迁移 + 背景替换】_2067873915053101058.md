---
key: 视频生成/图生视频/Scail-2 高阶工作流Plus版 v1.5 【多图 + 多角色参考 + 动作迁移 + 背景替换】_2067873915053101058.json
name: Scail-2 高阶工作流Plus版 v1.5 【多图 + 多角色参考 + 动作迁移 + 背景替换】_2067873915053101058.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2067873915053101058.json
hash: c9a728c3886e7928
coverage: 0.458333
learned_at: 2026-10-15 22:40:14
nodes: [SetNode, WanAnimatePlus ClipVisionEncode, SetNode, WanAnimatePlus SetBlockSwap, GetNode, Note, WanAnimatePlus SetLoRAs, SetNode, WanAnimatePlus VAELoader, CLIPVisionLoader, WanAnimatePlus LoraSelectMulti, Note, PlaySound|pysssss, SetNode, Note, GetNode, GetNode, VHS_VideoInfoLoaded, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, WanAnimatePlus Decode, GetNode, VHS_VideoCombine, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, Label (rgthree), GetNode, GetNode, SetNode, WanVideoContextOptions, VHS_VideoCombine, SetNode, Int, Int, ImageResizeKJv2, ImageResizeKJv2, PreviewImage, CLIPTextEncode, GetNode, GetNode, CheckpointLoaderSimple, SetNode, SAM3_VideoTrack, GetNode, GetNode, WanAnimatePlus SamplerFromSettings, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LoadImage, LoadImage, LoadImage, LoadImage, ImageBatchMulti, WanAnimatePlus SamplerSettings, WanAnimatePlus SCAIL_2 Embeds, GetNode, SetNode, GetNode, GetNode, ImageResizeKJv2, LoadImage, SetNode, SetNode, WanVideoTorchCompileSettings, SetNode, GetNode, GetNode, CheckpointLoaderSimple, Label (rgthree), WanAnimatePlus ModelLoader, Seed (rgthree), LoadImage, WanAnimatePlus BlockSwap, LoadImage, LoadImage, LoadImage, LoadImage, AutoRefCollage, PreviewImage, FastGroupsBypassSwitch, SetNode, ImageResizeKJv2, Fast Groups Bypasser (rgthree), PrimitiveBoolean, Fast Groups Bypasser (rgthree), SAM3_VideoTrack, PreviewImage, SCAIL2ColoredMaskV2, PreviewImage, SAM3_VideoTrack, VHS_VideoCombine, GetNode, LoadImage, VHS_LoadVideo, SimpleMath+, SetNode, INTConstant, INTConstant, WanVideoTextEncodeCached, JjkText]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 视频生成/图生视频/Scail-2 高阶工作流Plus版 v1.5 【多图 + 多角色参考 + 动作迁移 + 背景替换】_2067873915053101058.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2067873915053101058.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（120 个）：
- `SetNode`
- `WanAnimatePlus ClipVisionEncode`
- `SetNode`
- `WanAnimatePlus SetBlockSwap`
- `GetNode`
- `Note`
- `WanAnimatePlus SetLoRAs`
- `SetNode`
- `WanAnimatePlus VAELoader`
- `CLIPVisionLoader`
- `WanAnimatePlus LoraSelectMulti`
- `Note`
- `PlaySound|pysssss`
- `SetNode`
- `Note`
- `GetNode`
- `GetNode`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanAnimatePlus Decode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Label (rgthree)`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoContextOptions`
- `VHS_VideoCombine`
- `SetNode`
- `Int`
- `Int`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `CheckpointLoaderSimple` ★核心
- `SetNode`
- `SAM3_VideoTrack`
- `GetNode`
- `GetNode`
- `WanAnimatePlus SamplerFromSettings` ★核心
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
- `GetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ImageBatchMulti`
- `WanAnimatePlus SamplerSettings` ★核心
- `WanAnimatePlus SCAIL_2 Embeds`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `SetNode`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `GetNode`
- `GetNode`
- `CheckpointLoaderSimple` ★核心
- `Label (rgthree)`
- `WanAnimatePlus ModelLoader`
- `Seed (rgthree)`
- `LoadImage`
- `WanAnimatePlus BlockSwap`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `AutoRefCollage`
- `PreviewImage`
- `FastGroupsBypassSwitch`
- `SetNode`
- `ImageResizeKJv2`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveBoolean`
- `Fast Groups Bypasser (rgthree)`
- `SAM3_VideoTrack`
- `PreviewImage`
- `SCAIL2ColoredMaskV2`
- `PreviewImage`
- `SAM3_VideoTrack`
- `VHS_VideoCombine`
- `GetNode`
- `LoadImage`
- `VHS_LoadVideo`
- `SimpleMath+`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `WanVideoTextEncodeCached`
- `JjkText`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **46%**（55/120）

**有卡**：`WanAnimatePlus ClipVisionEncode`、`WanAnimatePlus SetBlockSwap`、`WanAnimatePlus SetLoRAs`、`WanAnimatePlus VAELoader`、`CLIPVisionLoader`、`WanAnimatePlus LoraSelectMulti`、`PlaySound|pysssss`、`VHS_VideoInfoLoaded`、`WanAnimatePlus Decode`、`VHS_VideoCombine`、`Label (rgthree)`、`WanVideoContextOptions`、`Int`、`ImageResizeKJv2`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`SAM3_VideoTrack`、`WanAnimatePlus SamplerFromSettings`、`LoadImage`、`ImageBatchMulti`、`WanAnimatePlus SamplerSettings`、`WanAnimatePlus SCAIL_2 Embeds`、`WanVideoTorchCompileSettings`、`WanAnimatePlus ModelLoader`、`Seed (rgthree)`、`WanAnimatePlus BlockSwap`、`AutoRefCollage`、`FastGroupsBypassSwitch`、`PrimitiveBoolean`、`SCAIL2ColoredMaskV2`、`VHS_LoadVideo`、`SimpleMath+`、`INTConstant`、`WanVideoTextEncodeCached`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、Seed (rgthree)、WanAnimatePlus SamplerFromSettings、WanAnimatePlus SamplerSettings、WanVideoTextEncodeCached、WanAnimatePlus ClipVisionEncode
