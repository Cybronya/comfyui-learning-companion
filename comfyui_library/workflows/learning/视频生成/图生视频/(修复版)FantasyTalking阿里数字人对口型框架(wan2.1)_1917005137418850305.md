---
key: 视频生成/图生视频/(修复版)FantasyTalking阿里数字人对口型框架(wan2.1)_1917005137418850305.json
name: (修复版)FantasyTalking阿里数字人对口型框架(wan2.1)_1917005137418850305.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1917005137418850305.json
hash: ce70eb6dbbcdddcf
coverage: 0.7
learned_at: 2026-10-15 22:29:39
nodes: [WanVideoSampler, MarkdownNote, PreviewImage, SetNode, GetNode, WanVideoTeaCache, WanVideoDecode, GetNode, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, WanVideoTextEncode, ImageResizeKJ, SetNode, FantasyTalkingWav2VecEmbeds, GetNode, ImageConcanate, INTConstant, CLIPVisionLoader, LoadWanVideoT5TextEncoder, Note, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoModelLoader, WanVideoVAELoader, DownloadAndLoadWav2VecModel, FantasyTalkingModelLoader, Note, Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], Text Multiline, CreateCFGScheduleFloatList, Note, VHS_VideoCombine, VHS_VideoCombine, Reroute, Reroute, LoadAudio, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/(修复版)FantasyTalking阿里数字人对口型框架(wan2.1)_1917005137418850305.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1917005137418850305.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（40 个）：
- `WanVideoSampler` ★核心
- `MarkdownNote`
- `PreviewImage`
- `SetNode`
- `GetNode`
- `WanVideoTeaCache`
- `WanVideoDecode`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `WanVideoClipVisionEncode`
- `WanVideoTextEncode`
- `ImageResizeKJ`
- `SetNode`
- `FantasyTalkingWav2VecEmbeds`
- `GetNode`
- `ImageConcanate`
- `INTConstant`
- `CLIPVisionLoader`
- `LoadWanVideoT5TextEncoder`
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `DownloadAndLoadWav2VecModel`
- `FantasyTalkingModelLoader`
- `Note`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Text Multiline`
- `CreateCFGScheduleFloatList`
- `Note`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Reroute`
- `Reroute`
- `LoadAudio`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **70%**（28/40）

**有卡**：`WanVideoSampler`、`WanVideoTeaCache`、`WanVideoDecode`、`WanVideoImageToVideoEncode`、`WanVideoClipVisionEncode`、`WanVideoTextEncode`、`ImageResizeKJ`、`FantasyTalkingWav2VecEmbeds`、`ImageConcanate`、`INTConstant`、`CLIPVisionLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoVAELoader`、`DownloadAndLoadWav2VecModel`、`FantasyTalkingModelLoader`、`Primitive integer [Crystools]`、`Text Multiline`、`CreateCFGScheduleFloatList`、`VHS_VideoCombine`、`LoadAudio`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
