---
key: 视频生成/图生视频/目前最新最火InfiniteTalk数字人对口型，适合口播唱歌 V1.0_1961819630828503041.json
name: 目前最新最火InfiniteTalk数字人对口型，适合口播唱歌 V1.0_1961819630828503041.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/目前最新最火InfiniteTalk数字人对口型，适合口播唱歌 V1.0_1961819630828503041.json
hash: a91c794230155511
coverage: 1
learned_at: 2026-10-15 22:31:29
nodes: [WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoVAELoader, DownloadAndLoadWav2VecModel, LoadWanVideoT5TextEncoder, AudioSeparation, WanVideoClipVisionEncode, WanVideoTextEncode, Audio Duration (mtb), MultiTalkModelLoader, WanVideoSampler, WanVideoModelLoader, SimpleMath+, WanVideoLoraSelect, ImageFromBatch+, WanVideoDecode, CLIPVisionLoader, WanVideoImageToVideoMultiTalk, MultiTalkWav2VecEmbeds, SimpleMath+, LoadImage, CR Text, ImageResizeKJv2, VHS_VideoCombine, LoadAudio, AudioCrop, VHS_LoadVideo, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/目前最新最火InfiniteTalk数字人对口型，适合口播唱歌 V1.0_1961819630828503041.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1961819630828503041.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（28 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `DownloadAndLoadWav2VecModel`
- `LoadWanVideoT5TextEncoder`
- `AudioSeparation`
- `WanVideoClipVisionEncode`
- `WanVideoTextEncode`
- `Audio Duration (mtb)`
- `MultiTalkModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `SimpleMath+`
- `WanVideoLoraSelect`
- `ImageFromBatch+`
- `WanVideoDecode`
- `CLIPVisionLoader`
- `WanVideoImageToVideoMultiTalk`
- `MultiTalkWav2VecEmbeds`
- `SimpleMath+`
- `LoadImage`
- `CR Text`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `LoadAudio`
- `AudioCrop`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（28/28）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`DownloadAndLoadWav2VecModel`、`LoadWanVideoT5TextEncoder`、`AudioSeparation`、`WanVideoClipVisionEncode`、`WanVideoTextEncode`、`Audio Duration (mtb)`、`MultiTalkModelLoader`、`WanVideoSampler`、`WanVideoModelLoader`、`SimpleMath+`、`WanVideoLoraSelect`、`ImageFromBatch+`、`WanVideoDecode`、`CLIPVisionLoader`、`WanVideoImageToVideoMultiTalk`、`MultiTalkWav2VecEmbeds`、`LoadImage`、`CR Text`、`ImageResizeKJv2`、`VHS_VideoCombine`、`LoadAudio`、`AudioCrop`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
