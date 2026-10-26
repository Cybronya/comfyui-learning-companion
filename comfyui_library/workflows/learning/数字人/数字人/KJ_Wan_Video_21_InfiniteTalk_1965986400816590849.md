---
key: 数字人/数字人/KJ_Wan_Video_21_InfiniteTalk_1965986400816590849.json
name: KJ_Wan_Video_21_InfiniteTalk_1965986400816590849
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/KJ_Wan_Video_21_InfiniteTalk_1965986400816590849.json
hash: f723b6ccb4d4f63b
coverage: 0.564516
learned_at: 2026-10-26 01:55:36
nodes: [SetNode, DownloadAndLoadWav2VecModel, MultiTalkWav2VecEmbeds, WanVideoVAELoader, GetNode, CLIPVisionLoader, Note, ImageResizeKJv2, GetImageSizeAndCount, WanVideoClipVisionEncode, GetNode, WanVideoImageToVideoMultiTalk, Note, MarkdownNote, PreviewAny, GetNode, SetNode, MultiTalkModelLoader, MultiTalkModelLoader, WanVideoLoraSelect, WanVideoModelLoader, GetNode, LoadImage, WanVideoLoraSelect, GetNode, Audio Duration (mtb), easy showAnything, easy showAnything, MathExpression|pysssss, easy mathInt, easy showAnything, CeilNode, WanVideoTorchCompileSettings, SetNode, SetNode, WanVideoTextEncodeCached, Note, easy mathInt, VHS_VideoCombine, WanVideoModelLoader, easy showAnything, easy showAnything, easy showAnything, SetNode, SetNode, SetNode, Int, Int, Int, SetNode, AudioSeparation, CR Text, WanVideoDecode, GetNode, WanVideoSampler, GetNode, GetNode, CM_IntToFloat, LoadAudioFromUrl, WanVideoBlockSwap, LoadImage, LoadAudio]
patterns: []
missing: []
---

# 数字人/数字人/KJ_Wan_Video_21_InfiniteTalk_1965986400816590849.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/KJ_Wan_Video_21_InfiniteTalk_1965986400816590849.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（62 个）：
- `SetNode`
- `DownloadAndLoadWav2VecModel`
- `MultiTalkWav2VecEmbeds`
- `WanVideoVAELoader`
- `GetNode`
- `CLIPVisionLoader`
- `Note`
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `WanVideoClipVisionEncode`
- `GetNode`
- `WanVideoImageToVideoMultiTalk`
- `Note`
- `MarkdownNote`
- `PreviewAny`
- `GetNode`
- `SetNode`
- `MultiTalkModelLoader`
- `MultiTalkModelLoader`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `GetNode`
- `LoadImage`
- `WanVideoLoraSelect`
- `GetNode`
- `Audio Duration (mtb)`
- `easy showAnything`
- `easy showAnything`
- `MathExpression|pysssss`
- `easy mathInt`
- `easy showAnything`
- `CeilNode`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `SetNode`
- `WanVideoTextEncodeCached`
- `Note`
- `easy mathInt`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `SetNode`
- `SetNode`
- `SetNode`
- `Int`
- `Int`
- `Int`
- `SetNode`
- `AudioSeparation`
- `CR Text`
- `WanVideoDecode`
- `GetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `CM_IntToFloat`
- `LoadAudioFromUrl`
- `WanVideoBlockSwap`
- `LoadImage`
- `LoadAudio`

## 知识

覆盖率 **56%**（35/62）

**有卡**：`DownloadAndLoadWav2VecModel`、`MultiTalkWav2VecEmbeds`、`WanVideoVAELoader`、`CLIPVisionLoader`、`ImageResizeKJv2`、`GetImageSizeAndCount`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoMultiTalk`、`MultiTalkModelLoader`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`LoadImage`、`Audio Duration (mtb)`、`MathExpression|pysssss`、`easy mathInt`、`CeilNode`、`WanVideoTorchCompileSettings`、`WanVideoTextEncodeCached`、`VHS_VideoCombine`、`Int`、`AudioSeparation`、`CR Text`、`WanVideoDecode`、`WanVideoSampler`、`CM_IntToFloat`、`LoadAudioFromUrl`、`WanVideoBlockSwap`、`LoadAudio`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、CLIPVisionLoader
