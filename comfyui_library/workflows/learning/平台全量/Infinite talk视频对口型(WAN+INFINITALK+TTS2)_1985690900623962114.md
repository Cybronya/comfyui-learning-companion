---
key: 平台全量/Infinite talk视频对口型(WAN+INFINITALK+TTS2)_1985690900623962114.json
name: Infinite talk视频对口型(WAN+INFINITALK+TTS2)_1985690900623962114
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Infinite talk视频对口型(WAN+INFINITALK+TTS2)_1985690900623962114.json
hash: 8530e0fc91cedbbd
coverage: 0.807692
learned_at: 2026-11-14 00:32:37
nodes: [INTConstant, SetNode, INTConstant, ToInt, easy showAnything, DownloadAndLoadWav2VecModel, MultiTalkWav2VecEmbeds, SetNode, RH_GetAudioDuration, WanVideoDecode, Anything Everywhere, WanVideoVAELoader, WanVideoBlockSwap, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, INTConstant, easy showAnything, SimpleMath+, GetNode, GetNode, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoEncode, GetNode, SimpleMath+, SetNode, WanVideoSampler, VHS_VideoCombine, easy cleanGpuUsed, ImageResizeKJv2, WanVideoModelLoader, WanVideoTextEncode, WanVideoImageToVideoMultiTalk, VHS_LoadVideo, easy cleanGpuUsed, intToFloat _O, AudioSeparation, SaveAudio, LoadAudio, CR Prompt Text, IndexTTS2Run, LoadAudio, CR Prompt Text, VHS_LoadVideo, AudioCrop, easy showAnything, SaveAudio, CR Index, VHS_VideoInfo, Switch, PreviewAudio]
patterns: []
missing: []
---

# 平台全量/Infinite talk视频对口型(WAN+INFINITALK+TTS2)_1985690900623962114.json

> 来源文件 `comfyui_library/workflows/平台全量/Infinite talk视频对口型(WAN+INFINITALK+TTS2)_1985690900623962114.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（52 个）：
- `INTConstant`
- `SetNode`
- `INTConstant`
- `ToInt`
- `easy showAnything`
- `DownloadAndLoadWav2VecModel`
- `MultiTalkWav2VecEmbeds`
- `SetNode`
- `RH_GetAudioDuration`
- `WanVideoDecode`
- `Anything Everywhere`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `INTConstant`
- `easy showAnything`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoEncode`
- `GetNode`
- `SimpleMath+`
- `SetNode`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `ImageResizeKJv2`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `WanVideoImageToVideoMultiTalk`
- `VHS_LoadVideo`
- `easy cleanGpuUsed`
- `intToFloat _O`
- `AudioSeparation`
- `SaveAudio`
- `LoadAudio`
- `CR Prompt Text`
- `IndexTTS2Run`
- `LoadAudio`
- `CR Prompt Text`
- `VHS_LoadVideo`
- `AudioCrop`
- `easy showAnything`
- `SaveAudio`
- `CR Index`
- `VHS_VideoInfo`
- `Switch`
- `PreviewAudio`

## 知识

覆盖率 **81%**（42/52）

**有卡**：`INTConstant`、`ToInt`、`DownloadAndLoadWav2VecModel`、`MultiTalkWav2VecEmbeds`、`RH_GetAudioDuration`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`MultiTalkModelLoader`、`SimpleMath+`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoEncode`、`WanVideoSampler`、`VHS_VideoCombine`、`easy cleanGpuUsed`、`ImageResizeKJv2`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoImageToVideoMultiTalk`、`VHS_LoadVideo`、`intToFloat _O`、`AudioSeparation`、`SaveAudio`、`LoadAudio`、`CR Prompt Text`、`IndexTTS2Run`、`AudioCrop`、`CR Index`、`VHS_VideoInfo`、`Switch`、`PreviewAudio`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect
