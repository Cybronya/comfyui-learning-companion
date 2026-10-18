---
key: 视频生成/图生视频/MultiTalk单人KJ高质量加速稳定版(无clipvision版)_1936345879362310145.json
name: MultiTalk单人KJ高质量加速稳定版(无clipvision版)_1936345879362310145.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MultiTalk单人KJ高质量加速稳定版(无clipvision版)_1936345879362310145.json
hash: 32478e866b97f9ce
coverage: 0.692308
learned_at: 2026-10-15 22:30:26
nodes: [DownloadAndLoadWav2VecModel, easy showAnything, easy cleanGpuUsed, WanVideoDecode, MultiTalkWav2VecEmbeds, LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoImageToVideoEncode, Audio Duration (mtb), easy showAnything, AudioSeparation, VHS_VideoCombine, easy showAnything, SimpleMath+, SimpleMath+, easy showAnything, AudioCrop, JWIntegerToString, WanVideoBlockSwap, WanVideoLoraSelect, MultiTalkModelLoader, WanVideoModelLoader, CLIPVisionLoader, WanVideoSampler, LayerUtility: PurgeVRAM, WanVideoVAELoader, LoadImage, JWInteger, LoadAudio, PrimitiveInt, TextInput_, PrimitiveFloat, Note, Note, Note, Note, Note, Note, LayerUtility: ImageScaleByAspectRatio V2]
patterns: []
missing: []
---

# 视频生成/图生视频/MultiTalk单人KJ高质量加速稳定版(无clipvision版)_1936345879362310145.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1936345879362310145.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `DownloadAndLoadWav2VecModel`
- `easy showAnything`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `MultiTalkWav2VecEmbeds`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `WanVideoImageToVideoEncode`
- `Audio Duration (mtb)`
- `easy showAnything`
- `AudioSeparation`
- `VHS_VideoCombine`
- `easy showAnything`
- `SimpleMath+`
- `SimpleMath+`
- `easy showAnything`
- `AudioCrop`
- `JWIntegerToString`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `WanVideoModelLoader`
- `CLIPVisionLoader`
- `WanVideoSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `WanVideoVAELoader`
- `LoadImage`
- `JWInteger`
- `LoadAudio`
- `PrimitiveInt`
- `TextInput_`
- `PrimitiveFloat`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`

## 知识

覆盖率 **69%**（27/39）

**有卡**：`DownloadAndLoadWav2VecModel`、`easy cleanGpuUsed`、`WanVideoDecode`、`MultiTalkWav2VecEmbeds`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoImageToVideoEncode`、`Audio Duration (mtb)`、`AudioSeparation`、`VHS_VideoCombine`、`SimpleMath+`、`AudioCrop`、`JWIntegerToString`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`WanVideoModelLoader`、`CLIPVisionLoader`、`WanVideoSampler`、`LayerUtility: PurgeVRAM`、`WanVideoVAELoader`、`LoadImage`、`JWInteger`、`LoadAudio`、`TextInput_`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoLoraSelect
