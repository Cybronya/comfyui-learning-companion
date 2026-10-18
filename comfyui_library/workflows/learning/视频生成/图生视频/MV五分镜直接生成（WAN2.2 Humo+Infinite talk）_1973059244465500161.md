---
key: 视频生成/图生视频/MV五分镜直接生成（WAN2.2 Humo+Infinite talk）_1973059244465500161.json
name: MV五分镜直接生成（WAN2.2 Humo+Infinite talk）_1973059244465500161.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MV五分镜直接生成（WAN2.2 Humo+Infinite talk）_1973059244465500161.json
hash: b0865516c53b7aa3
coverage: 1
learned_at: 2026-10-15 22:32:02
nodes: [SoundFlow_GetLength, ToInt, RecordAudio, Display Int (rgthree), AudioSeparation, MultiTalkWav2VecEmbeds, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoCombineEmbeds, WanVideoImageToVideoMultiTalk, easy int, Display Int (rgthree), AudioSeparation, WanVideoCombineEmbeds, easy int, ToInt, SoundFlow_GetLength, WanVideoImageToVideoMultiTalk, MultiTalkWav2VecEmbeds, ToInt, Display Int (rgthree), AudioSeparation, MultiTalkWav2VecEmbeds, WanVideoCombineEmbeds, WanVideoImageToVideoMultiTalk, PreviewAudio, PreviewAudio, WanVideoSampler, SimpleMath+, ImageFromBatch, SimpleMath+, ImageFromBatch, SimpleMath+, WanVideoDecode, WanVideoDecode, WanVideoDecode, ImageFromBatch, WanVideoSampler, VHS_VideoCombine, WanVideoLoraSelect, MultiTalkModelLoader, WanVideoTextEncode, easy int, SoundFlow_GetLength, Display Int (rgthree), WanVideoCombineEmbeds, WanVideoDecode, SoundFlow_GetLength, ToInt, easy int, HuMoEmbeds, HuMoEmbeds, VHS_VideoCombine, VHS_VideoCombine, Wav2VecModelLoader, AudioSeparation, SimpleMath+, MultiTalkWav2VecEmbeds, HuMoEmbeds, Display Int (rgthree), ImageFromBatch, ImageBatchMulti, WanVideoDecode, ImageFromBatch, WanVideoModelLoader, WanVideoSampler, WanVideoCombineEmbeds, WhisperModelLoader, SoundFlow_GetLength, ToInt, easy int, SimpleMath+, MultiTalkWav2VecEmbeds, HuMoEmbeds, VHS_VideoCombine, VHS_VideoCombine, WanVideoTextEncode, WanVideoVAELoader, AudioSeparation, LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoSampler, PreviewAudio, HuMoEmbeds, VHS_VideoCombine, LoadAudio, WanVideoImageToVideoMultiTalk, WanVideoImageToVideoMultiTalk, WanVideoTextEncode, WanVideoTextEncode, INTConstant, LoadImage, INTConstant, ImageResizeKJv2, easy imageRemBg, ImageResizeKJv2, easy imageRemBg, ImageBatchMulti, LoadImage, PreviewAudio, PreviewAudio, SoundFlow_TrimAudio, SoundFlow_TrimAudio, SoundFlow_TrimAudio, SoundFlow_TrimAudio, SoundFlow_TrimAudio, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/MV五分镜直接生成（WAN2.2 Humo+Infinite talk）_1973059244465500161.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1973059244465500161.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（107 个）：
- `SoundFlow_GetLength`
- `ToInt`
- `RecordAudio`
- `Display Int (rgthree)`
- `AudioSeparation`
- `MultiTalkWav2VecEmbeds`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoCombineEmbeds`
- `WanVideoImageToVideoMultiTalk`
- `easy int`
- `Display Int (rgthree)`
- `AudioSeparation`
- `WanVideoCombineEmbeds`
- `easy int`
- `ToInt`
- `SoundFlow_GetLength`
- `WanVideoImageToVideoMultiTalk`
- `MultiTalkWav2VecEmbeds`
- `ToInt`
- `Display Int (rgthree)`
- `AudioSeparation`
- `MultiTalkWav2VecEmbeds`
- `WanVideoCombineEmbeds`
- `WanVideoImageToVideoMultiTalk`
- `PreviewAudio`
- `PreviewAudio`
- `WanVideoSampler` ★核心
- `SimpleMath+`
- `ImageFromBatch`
- `SimpleMath+`
- `ImageFromBatch`
- `SimpleMath+`
- `WanVideoDecode`
- `WanVideoDecode`
- `WanVideoDecode`
- `ImageFromBatch`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `WanVideoTextEncode`
- `easy int`
- `SoundFlow_GetLength`
- `Display Int (rgthree)`
- `WanVideoCombineEmbeds`
- `WanVideoDecode`
- `SoundFlow_GetLength`
- `ToInt`
- `easy int`
- `HuMoEmbeds`
- `HuMoEmbeds`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Wav2VecModelLoader`
- `AudioSeparation`
- `SimpleMath+`
- `MultiTalkWav2VecEmbeds`
- `HuMoEmbeds`
- `Display Int (rgthree)`
- `ImageFromBatch`
- `ImageBatchMulti`
- `WanVideoDecode`
- `ImageFromBatch`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoCombineEmbeds`
- `WhisperModelLoader`
- `SoundFlow_GetLength`
- `ToInt`
- `easy int`
- `SimpleMath+`
- `MultiTalkWav2VecEmbeds`
- `HuMoEmbeds`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `AudioSeparation`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `PreviewAudio`
- `HuMoEmbeds`
- `VHS_VideoCombine`
- `LoadAudio`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoTextEncode`
- `WanVideoTextEncode`
- `INTConstant`
- `LoadImage`
- `INTConstant`
- `ImageResizeKJv2`
- `easy imageRemBg`
- `ImageResizeKJv2`
- `easy imageRemBg`
- `ImageBatchMulti`
- `LoadImage`
- `PreviewAudio`
- `PreviewAudio`
- `SoundFlow_TrimAudio`
- `SoundFlow_TrimAudio`
- `SoundFlow_TrimAudio`
- `SoundFlow_TrimAudio`
- `SoundFlow_TrimAudio`
- `WanVideoTextEncode`

## 知识

覆盖率 **100%**（107/107）

**有卡**：`SoundFlow_GetLength`、`ToInt`、`RecordAudio`、`Display Int (rgthree)`、`AudioSeparation`、`MultiTalkWav2VecEmbeds`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoCombineEmbeds`、`WanVideoImageToVideoMultiTalk`、`easy int`、`PreviewAudio`、`WanVideoSampler`、`SimpleMath+`、`ImageFromBatch`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`WanVideoTextEncode`、`HuMoEmbeds`、`Wav2VecModelLoader`、`ImageBatchMulti`、`WanVideoModelLoader`、`WhisperModelLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`LoadAudio`、`INTConstant`、`LoadImage`、`ImageResizeKJv2`、`easy imageRemBg`、`SoundFlow_TrimAudio`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、ImageResizeKJv2
