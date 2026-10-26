---
key: 数字人/数字人/CWPS_TTS+数字人-1.1_2056673235961470977.json
name: CWPS_TTS+数字人-1.1_2056673235961470977
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/CWPS_TTS+数字人-1.1_2056673235961470977.json
hash: 38c41449bcacf82b
coverage: 0.871795
learned_at: 2026-10-26 01:54:04
nodes: [LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, WanVideoClipVisionEncode, GetImageSizeAndCount, WanVideoTextEncode, WanVideoSampler, WanVideoImageToVideoMultiTalk, WanVideoBlockSwap, WanVideoModelLoader, CLIPVisionLoader, WanVideoVAELoader, WanVideoDecode, Reroute, DownloadAndLoadWav2VecModel, MultiTalkWav2VecEmbeds, PreviewAny, VHS_VideoCombine, Note, Note, JWFloat, WanVideoLoraSelect, WanVideoLoraSelect, MultiTalkModelLoader, JWInteger, LoadImage, easy indexTTSEmotionAudio, Audio Duration (mtb), easy showAnything, JWInteger, SimpleMath+, AudioSeparation, AudioCrop, SimpleMath+, easy downloadIndexTTSAndLoadModel, LoadAudio, LoadAudio, CR Prompt Text, CR Prompt Text, easy indexTTSGenerate]
patterns: []
missing: []
---

# 数字人/数字人/CWPS_TTS+数字人-1.1_2056673235961470977.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/CWPS_TTS+数字人-1.1_2056673235961470977.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoT5TextEncoder`
- `WanVideoClipVisionEncode`
- `GetImageSizeAndCount`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoMultiTalk`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `Reroute`
- `DownloadAndLoadWav2VecModel`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `JWFloat`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `JWInteger`
- `LoadImage`
- `easy indexTTSEmotionAudio`
- `Audio Duration (mtb)`
- `easy showAnything`
- `JWInteger`
- `SimpleMath+`
- `AudioSeparation`
- `AudioCrop`
- `SimpleMath+`
- `easy downloadIndexTTSAndLoadModel`
- `LoadAudio`
- `LoadAudio`
- `CR Prompt Text`
- `CR Prompt Text`
- `easy indexTTSGenerate`

## 知识

覆盖率 **87%**（34/39）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`WanVideoClipVisionEncode`、`GetImageSizeAndCount`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoDecode`、`DownloadAndLoadWav2VecModel`、`MultiTalkWav2VecEmbeds`、`VHS_VideoCombine`、`JWFloat`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`JWInteger`、`LoadImage`、`easy indexTTSEmotionAudio`、`Audio Duration (mtb)`、`SimpleMath+`、`AudioSeparation`、`AudioCrop`、`easy downloadIndexTTSAndLoadModel`、`LoadAudio`、`CR Prompt Text`、`easy indexTTSGenerate`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
