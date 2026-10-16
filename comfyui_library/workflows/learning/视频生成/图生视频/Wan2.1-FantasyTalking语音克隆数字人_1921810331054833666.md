---
key: 视频生成/图生视频/Wan2.1-FantasyTalking语音克隆数字人_1921810331054833666.json
name: Wan2.1-FantasyTalking语音克隆数字人_1921810331054833666.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1921810331054833666.json
hash: 7bce33d9dffe446f
coverage: 0.823529
learned_at: 2026-10-15 22:29:44
nodes: [WanVideoVAELoader, DownloadAndLoadWav2VecModel, FantasyTalkingModelLoader, FantasyTalkingWav2VecEmbeds, GetNode, LoadWanVideoT5TextEncoder, SetNode, VHS_VideoInfo, WanVideoClipVisionEncode, CLIPVisionLoader, SparkTTSClone, SaveAudio, GetNode, WanVideoImageToVideoEncode, GetNode, WanVideoContextOptions, VHS_VideoCombine, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoModelLoader, WanVideoBlockSwap, PreviewImage, VHS_LoadVideo, WanVideoSampler, WanVideoDecode, Int, ImageResizeKJ, CR Text, LoadImage, WanVideoTextEncode, Int, WanVideoTeaCache, AudioSeparation, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1-FantasyTalking语音克隆数字人_1921810331054833666.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1921810331054833666.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（34 个）：
- `WanVideoVAELoader`
- `DownloadAndLoadWav2VecModel`
- `FantasyTalkingModelLoader`
- `FantasyTalkingWav2VecEmbeds`
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `VHS_VideoInfo`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `SparkTTSClone`
- `SaveAudio`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `WanVideoContextOptions`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `PreviewImage`
- `VHS_LoadVideo`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `Int`
- `ImageResizeKJ`
- `CR Text`
- `LoadImage`
- `WanVideoTextEncode`
- `Int`
- `WanVideoTeaCache`
- `AudioSeparation`
- `Note`

## 知识

覆盖率 **82%**（28/34）

**有卡**：`WanVideoVAELoader`、`DownloadAndLoadWav2VecModel`、`FantasyTalkingModelLoader`、`FantasyTalkingWav2VecEmbeds`、`LoadWanVideoT5TextEncoder`、`VHS_VideoInfo`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`SparkTTSClone`、`SaveAudio`、`WanVideoImageToVideoEncode`、`WanVideoContextOptions`、`VHS_VideoCombine`、`easy cleanGpuUsed`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`VHS_LoadVideo`、`WanVideoSampler`、`WanVideoDecode`、`Int`、`ImageResizeKJ`、`CR Text`、`LoadImage`、`WanVideoTextEncode`、`WanVideoTeaCache`、`AudioSeparation`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
