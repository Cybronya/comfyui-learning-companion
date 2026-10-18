---
key: 视频生成/图生视频/MultiTalk+AniWan单人KJ（UNI3C运镜 手持） 浮云_1998778583533412354.json
name: MultiTalk+AniWan单人KJ（UNI3C运镜 手持） 浮云_1998778583533412354.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MultiTalk+AniWan单人KJ（UNI3C运镜 手持） 浮云_1998778583533412354.json
hash: 8ae94f1c0d87b4cc
coverage: 0.723404
learned_at: 2026-10-15 22:33:34
nodes: [DownloadAndLoadWav2VecModel, easy showAnything, easy cleanGpuUsed, WanVideoDecode, MultiTalkWav2VecEmbeds, LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoImageToVideoEncode, easy showAnything, AudioSeparation, VHS_VideoCombine, easy showAnything, easy showAnything, AudioCrop, JWIntegerToString, MultiTalkModelLoader, CLIPVisionLoader, WanVideoSampler, LayerUtility: PurgeVRAM, JWInteger, Note, Note, Note, Note, Note, Note, ImageResizeKJ, WanVideoClipVisionEncode, WanVideoVAELoader, WanVideoEncode, WanVideoUni3C_ControlnetLoader, LayerUtility: ImageScaleByAspectRatio V2, Note, WanVideoBlockSwap, TextInput_, WanVideoLoraSelect, WanVideoModelLoader, JWInteger, PrimitiveFloat, LoadImage, LoadAudio, PrimitiveInt, WanVideoUni3C_embeds, VHS_LoadVideo, SimpleMath+, Audio Duration (mtb), SimpleMath+]
patterns: []
missing: []
---

# 视频生成/图生视频/MultiTalk+AniWan单人KJ（UNI3C运镜 手持） 浮云_1998778583533412354.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1998778583533412354.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（47 个）：
- `DownloadAndLoadWav2VecModel`
- `easy showAnything`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `MultiTalkWav2VecEmbeds`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `WanVideoImageToVideoEncode`
- `easy showAnything`
- `AudioSeparation`
- `VHS_VideoCombine`
- `easy showAnything`
- `easy showAnything`
- `AudioCrop`
- `JWIntegerToString`
- `MultiTalkModelLoader`
- `CLIPVisionLoader`
- `WanVideoSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `ImageResizeKJ`
- `WanVideoClipVisionEncode`
- `WanVideoVAELoader`
- `WanVideoEncode`
- `WanVideoUni3C_ControlnetLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `WanVideoBlockSwap`
- `TextInput_`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `JWInteger`
- `PrimitiveFloat`
- `LoadImage`
- `LoadAudio`
- `PrimitiveInt`
- `WanVideoUni3C_embeds`
- `VHS_LoadVideo`
- `SimpleMath+`
- `Audio Duration (mtb)`
- `SimpleMath+`

## 知识

覆盖率 **72%**（34/47）

**有卡**：`DownloadAndLoadWav2VecModel`、`easy cleanGpuUsed`、`WanVideoDecode`、`MultiTalkWav2VecEmbeds`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoImageToVideoEncode`、`AudioSeparation`、`VHS_VideoCombine`、`AudioCrop`、`JWIntegerToString`、`MultiTalkModelLoader`、`CLIPVisionLoader`、`WanVideoSampler`、`LayerUtility: PurgeVRAM`、`JWInteger`、`ImageResizeKJ`、`WanVideoClipVisionEncode`、`WanVideoVAELoader`、`WanVideoEncode`、`WanVideoUni3C_ControlnetLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoBlockSwap`、`TextInput_`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`LoadImage`、`LoadAudio`、`WanVideoUni3C_embeds`、`VHS_LoadVideo`、`SimpleMath+`、`Audio Duration (mtb)`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoUni3C_ControlnetLoader、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
