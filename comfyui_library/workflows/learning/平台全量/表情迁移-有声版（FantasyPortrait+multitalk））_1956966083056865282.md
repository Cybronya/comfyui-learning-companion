---
key: 平台全量/表情迁移-有声版（FantasyPortrait+multitalk））_1956966083056865282.json
name: 表情迁移-有声版（FantasyPortrait+multitalk））_1956966083056865282
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/表情迁移-有声版（FantasyPortrait+multitalk））_1956966083056865282.json
hash: 1c92b1ed74d0bbbc
coverage: 0.869565
learned_at: 2026-11-14 02:33:36
nodes: [MultiTalkWav2VecEmbeds, DownloadAndLoadWav2VecModel, easy showAnything, WanVideoVAELoader, WanVideoModelLoader, WanVideoAddFantasyPortrait, MultiTalkModelLoader, FantasyPortraitModelLoader, WanVideoBlockSwap, WanVideoTorchCompileSettings, SoundFlow_GetLength, SimpleMath+, ToInt, SoundFlow_Fade, VHS_VideoInfo, SetNode, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoSetBlockSwap, FantasyPortraitFaceDetector, ImageResizeKJv2, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoTextEncodeCached, ImageResizeKJv2, WanVideoSampler, GetNode, WanVideoDecode, WanVideoImageToVideoEncode, GetNode, ImageConcatMulti, ImageConcatMulti, PrimitiveStringMultiline, VHS_VideoCombine, Fast Groups Bypasser (rgthree), VHS_LoadVideo, VHS_VideoCombine, CM_IntToFloat, CM_IntBinaryOperation, JWInteger, LoadImage, JWInteger, JWInteger, JWInteger, JWInteger, CM_IntBinaryOperation]
patterns: []
missing: []
---

# 平台全量/表情迁移-有声版（FantasyPortrait+multitalk））_1956966083056865282.json

> 来源文件 `comfyui_library/workflows/平台全量/表情迁移-有声版（FantasyPortrait+multitalk））_1956966083056865282.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（46 个）：
- `MultiTalkWav2VecEmbeds`
- `DownloadAndLoadWav2VecModel`
- `easy showAnything`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoAddFantasyPortrait`
- `MultiTalkModelLoader`
- `FantasyPortraitModelLoader`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `SoundFlow_GetLength`
- `SimpleMath+`
- `ToInt`
- `SoundFlow_Fade`
- `VHS_VideoInfo`
- `SetNode`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `FantasyPortraitFaceDetector`
- `ImageResizeKJv2`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoTextEncodeCached`
- `ImageResizeKJv2`
- `WanVideoSampler` ★核心
- `GetNode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `CM_IntToFloat`
- `CM_IntBinaryOperation`
- `JWInteger`
- `LoadImage`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `CM_IntBinaryOperation`

## 知识

覆盖率 **87%**（40/46）

**有卡**：`MultiTalkWav2VecEmbeds`、`DownloadAndLoadWav2VecModel`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoAddFantasyPortrait`、`MultiTalkModelLoader`、`FantasyPortraitModelLoader`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`SoundFlow_GetLength`、`SimpleMath+`、`ToInt`、`SoundFlow_Fade`、`VHS_VideoInfo`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`FantasyPortraitFaceDetector`、`ImageResizeKJv2`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoImageToVideoEncode`、`ImageConcatMulti`、`VHS_VideoCombine`、`VHS_LoadVideo`、`CM_IntToFloat`、`CM_IntBinaryOperation`、`JWInteger`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelect
