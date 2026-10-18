---
key: 视频生成/图生视频/🥱表情复刻+对口型工作流【FantasyPortrait+Multitalk】🥱_1956623622469287937.json
name: 🥱表情复刻+对口型工作流【FantasyPortrait+Multitalk】🥱_1956623622469287937.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/🥱表情复刻+对口型工作流【FantasyPortrait+Multitalk】🥱_1956623622469287937.json
hash: cd1bf5fbb1412a5a
coverage: 0.886364
learned_at: 2026-10-15 22:31:14
nodes: [ImageConcatMulti, WanVideoDecode, WanVideoImageToVideoEncode, ImageConcatMulti, WanVideoTorchCompileSettings, ToInt, SoundFlow_GetLength, ImageResizeKJv2, CR Text, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, SetNode, SimpleMath+, CLIPVisionLoader, WanVideoAddFantasyPortrait, WanVideoClipVisionEncode, WanVideoTextEncodeCached, ImageResizeKJv2, VHS_VideoCombine, VHS_VideoCombine, AudioSeparation, DownloadAndLoadWav2VecModel, easy showAnything, SoundFlow_Fade, MultiTalkWav2VecEmbeds, SimpleMath+, FantasyPortraitFaceDetector, VHS_VideoInfo, GetNode, WanVideoSampler, MarkdownNote, Note Plus (mtb), LoadImage, VHS_LoadVideo, GetNode, WanVideoVAELoader, FantasyPortraitModelLoader, WanVideoModelLoader, WanVideoLoraSelect, MultiTalkModelLoader, ImpactInt, ImpactInt, ImpactInt]
patterns: []
missing: []
---

# 视频生成/图生视频/🥱表情复刻+对口型工作流【FantasyPortrait+Multitalk】🥱_1956623622469287937.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1956623622469287937.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（44 个）：
- `ImageConcatMulti`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `ImageConcatMulti`
- `WanVideoTorchCompileSettings`
- `ToInt`
- `SoundFlow_GetLength`
- `ImageResizeKJv2`
- `CR Text`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `SetNode`
- `SimpleMath+`
- `CLIPVisionLoader`
- `WanVideoAddFantasyPortrait`
- `WanVideoClipVisionEncode`
- `WanVideoTextEncodeCached`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `AudioSeparation`
- `DownloadAndLoadWav2VecModel`
- `easy showAnything`
- `SoundFlow_Fade`
- `MultiTalkWav2VecEmbeds`
- `SimpleMath+`
- `FantasyPortraitFaceDetector`
- `VHS_VideoInfo`
- `GetNode`
- `WanVideoSampler` ★核心
- `MarkdownNote`
- `Note Plus (mtb)`
- `LoadImage`
- `VHS_LoadVideo`
- `GetNode`
- `WanVideoVAELoader`
- `FantasyPortraitModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`

## 知识

覆盖率 **89%**（39/44）

**有卡**：`ImageConcatMulti`、`WanVideoDecode`、`WanVideoImageToVideoEncode`、`WanVideoTorchCompileSettings`、`ToInt`、`SoundFlow_GetLength`、`ImageResizeKJv2`、`CR Text`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`SimpleMath+`、`CLIPVisionLoader`、`WanVideoAddFantasyPortrait`、`WanVideoClipVisionEncode`、`WanVideoTextEncodeCached`、`VHS_VideoCombine`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`SoundFlow_Fade`、`MultiTalkWav2VecEmbeds`、`FantasyPortraitFaceDetector`、`VHS_VideoInfo`、`WanVideoSampler`、`Note Plus (mtb)`、`LoadImage`、`VHS_LoadVideo`、`WanVideoVAELoader`、`FantasyPortraitModelLoader`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`ImpactInt`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、WanVideoLoraSelect
