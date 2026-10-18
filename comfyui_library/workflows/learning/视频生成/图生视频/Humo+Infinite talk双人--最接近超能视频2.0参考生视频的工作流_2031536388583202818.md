---
key: 视频生成/图生视频/Humo+Infinite talk双人--最接近超能视频2.0参考生视频的工作流_2031536388583202818.json
name: Humo+Infinite talk双人--最接近超能视频2.0参考生视频的工作流_2031536388583202818.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Humo+Infinite talk双人--最接近超能视频2.0参考生视频的工作流_2031536388583202818.json
hash: 296cb4e1ebd94632
coverage: 0.9875
learned_at: 2026-10-15 22:35:31
nodes: [RecordAudio, Display Int (rgthree), AudioSeparation, WanVideoCombineEmbeds, easy int, ToInt, SoundFlow_GetLength, WanVideoImageToVideoMultiTalk, SoundFlow_GetLength, ToInt, AudioSeparation, easy int, ImageFromBatch, WanVideoDecode, VHS_VideoCombine, PreviewAudio, HuMoEmbeds, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoCombineEmbeds, ToInt, AudioSeparation, Display Int (rgthree), WanVideoDecode, ImageFromBatch, SimpleMath+, SimpleMath+, MultiTalkWav2VecEmbeds, MultiTalkWav2VecEmbeds, MultiTalkWav2VecEmbeds, HuMoEmbeds, WanVideoImageToVideoMultiTalk, HuMoEmbeds, ImageResizeKJv2, easy imageRemBg, ImageAddMulti, WanVideoCombineEmbeds, VHS_VideoCombine, ImageBatchMulti, WanVideoSampler, WanVideoSampler, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoBlockSwap, ImageFromBatch, ImageConcanate, ImageConcanate, VHS_VideoCombine, WanVideoLoraSelect, WanVideoModelLoader, MultiTalkModelLoader, WhisperModelLoader, Wav2VecModelLoader, WanVideoVAELoader, LoadWanVideoT5TextEncoder, PreviewImage, ImageResizeKJv2, easy imageRemBg, INTConstant, INTConstant, SoundFlow_GetLength, VHS_VideoCombine, AudioConcat, AudioConcat, PreviewAudio, LoadImage, LoadImage, PreviewAudio, Display Int (rgthree), easy int, SimpleMath+, SoundFlow_TrimAudio, SoundFlow_TrimAudio, WanVideoTextEncode, PreviewAudio, VHS_VideoCombine, SoundFlow_TrimAudio, WanVideoTextEncode, LoadAudio, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/Humo+Infinite talk双人--最接近超能视频2.0参考生视频的工作流_2031536388583202818.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2031536388583202818.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（80 个）：
- `RecordAudio`
- `Display Int (rgthree)`
- `AudioSeparation`
- `WanVideoCombineEmbeds`
- `easy int`
- `ToInt`
- `SoundFlow_GetLength`
- `WanVideoImageToVideoMultiTalk`
- `SoundFlow_GetLength`
- `ToInt`
- `AudioSeparation`
- `easy int`
- `ImageFromBatch`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `PreviewAudio`
- `HuMoEmbeds`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoCombineEmbeds`
- `ToInt`
- `AudioSeparation`
- `Display Int (rgthree)`
- `WanVideoDecode`
- `ImageFromBatch`
- `SimpleMath+`
- `SimpleMath+`
- `MultiTalkWav2VecEmbeds`
- `MultiTalkWav2VecEmbeds`
- `MultiTalkWav2VecEmbeds`
- `HuMoEmbeds`
- `WanVideoImageToVideoMultiTalk`
- `HuMoEmbeds`
- `ImageResizeKJv2`
- `easy imageRemBg`
- `ImageAddMulti`
- `WanVideoCombineEmbeds`
- `VHS_VideoCombine`
- `ImageBatchMulti`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `ImageFromBatch`
- `ImageConcanate`
- `ImageConcanate`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `MultiTalkModelLoader`
- `WhisperModelLoader`
- `Wav2VecModelLoader`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `ImageResizeKJv2`
- `easy imageRemBg`
- `INTConstant`
- `INTConstant`
- `SoundFlow_GetLength`
- `VHS_VideoCombine`
- `AudioConcat`
- `AudioConcat`
- `PreviewAudio`
- `LoadImage`
- `LoadImage`
- `PreviewAudio`
- `Display Int (rgthree)`
- `easy int`
- `SimpleMath+`
- `SoundFlow_TrimAudio`
- `SoundFlow_TrimAudio`
- `WanVideoTextEncode`
- `PreviewAudio`
- `VHS_VideoCombine`
- `SoundFlow_TrimAudio`
- `WanVideoTextEncode`
- `LoadAudio`
- `WanVideoTextEncode`

## 知识

覆盖率 **99%**（79/80）

**有卡**：`RecordAudio`、`Display Int (rgthree)`、`AudioSeparation`、`WanVideoCombineEmbeds`、`easy int`、`ToInt`、`SoundFlow_GetLength`、`WanVideoImageToVideoMultiTalk`、`ImageFromBatch`、`WanVideoDecode`、`VHS_VideoCombine`、`PreviewAudio`、`HuMoEmbeds`、`SimpleMath+`、`MultiTalkWav2VecEmbeds`、`ImageResizeKJv2`、`easy imageRemBg`、`ImageAddMulti`、`ImageBatchMulti`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`ImageConcanate`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`MultiTalkModelLoader`、`WhisperModelLoader`、`Wav2VecModelLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`INTConstant`、`AudioConcat`、`LoadImage`、`SoundFlow_TrimAudio`、`WanVideoTextEncode`、`LoadAudio`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、ImageResizeKJv2
