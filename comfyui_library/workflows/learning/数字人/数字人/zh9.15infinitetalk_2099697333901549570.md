---
key: 数字人/数字人/zh9.15infinitetalk_2099697333901549570.json
name: zh9.15infinitetalk_2099697333901549570
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/zh9.15infinitetalk_2099697333901549570.json
hash: b9857f23fadaefce
coverage: 0.745098
learned_at: 2026-10-19 00:19:16
nodes: [SaveAudio, INTConstant, SetNode, INTConstant, easy showAnything, easy cleanGpuUsed, DownloadAndLoadWav2VecModel, MultiTalkWav2VecEmbeds, SetNode, WanVideoDecode, WanVideoBlockSwap, ImageResizeKJv2, easy showAnything, SimpleMath+, WanVideoImageToVideoMultiTalk, GetNode, GetNode, CLIPVisionLoader, easy cleanGpuUsed, SimpleMath+, SetNode, WanVideoSampler, MultiTalkModelLoader, WanVideoClipVisionEncode, AudioSeparation, WanVideoModelLoader, ToInt, GetNode, WanVideoLoraSelect, ToFloat, Audio Duration (mtb), PrimitiveInt, BasicMath, SaveAudio, LoadWanVideoT5TextEncoder, easy showAnything, VHS_VideoInfo, AudioCrop, WanVideoContextOptions, MarkdownNote, VHS_VideoCombine, WanVideoEncode, SaveVideo, CreateVideo, WanVideoVAELoader, Anything Everywhere, WanVideoTextEncode, JjkText, INTConstant, LoadAudio, VHS_LoadVideo]
patterns: []
missing: []
---

# 数字人/数字人/zh9.15infinitetalk_2099697333901549570.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/zh9.15infinitetalk_2099697333901549570.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（51 个）：
- `SaveAudio`
- `INTConstant`
- `SetNode`
- `INTConstant`
- `easy showAnything`
- `easy cleanGpuUsed`
- `DownloadAndLoadWav2VecModel`
- `MultiTalkWav2VecEmbeds`
- `SetNode`
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `ImageResizeKJv2`
- `easy showAnything`
- `SimpleMath+`
- `WanVideoImageToVideoMultiTalk`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `easy cleanGpuUsed`
- `SimpleMath+`
- `SetNode`
- `WanVideoSampler` ★核心
- `MultiTalkModelLoader`
- `WanVideoClipVisionEncode`
- `AudioSeparation`
- `WanVideoModelLoader`
- `ToInt`
- `GetNode`
- `WanVideoLoraSelect`
- `ToFloat`
- `Audio Duration (mtb)`
- `PrimitiveInt`
- `BasicMath`
- `SaveAudio`
- `LoadWanVideoT5TextEncoder`
- `easy showAnything`
- `VHS_VideoInfo`
- `AudioCrop`
- `WanVideoContextOptions`
- `MarkdownNote`
- `VHS_VideoCombine`
- `WanVideoEncode`
- `SaveVideo`
- `CreateVideo`
- `WanVideoVAELoader`
- `Anything Everywhere`
- `WanVideoTextEncode`
- `JjkText`
- `INTConstant`
- `LoadAudio`
- `VHS_LoadVideo`

## 知识

覆盖率 **75%**（38/51）

**有卡**：`SaveAudio`、`INTConstant`、`easy cleanGpuUsed`、`DownloadAndLoadWav2VecModel`、`MultiTalkWav2VecEmbeds`、`WanVideoDecode`、`WanVideoBlockSwap`、`ImageResizeKJv2`、`SimpleMath+`、`WanVideoImageToVideoMultiTalk`、`CLIPVisionLoader`、`WanVideoSampler`、`MultiTalkModelLoader`、`WanVideoClipVisionEncode`、`AudioSeparation`、`WanVideoModelLoader`、`ToInt`、`WanVideoLoraSelect`、`ToFloat`、`Audio Duration (mtb)`、`BasicMath`、`LoadWanVideoT5TextEncoder`、`VHS_VideoInfo`、`AudioCrop`、`WanVideoContextOptions`、`VHS_VideoCombine`、`WanVideoEncode`、`SaveVideo`、`CreateVideo`、`WanVideoVAELoader`、`WanVideoTextEncode`、`LoadAudio`、`VHS_LoadVideo`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoEncode、WanVideoLoraSelect
