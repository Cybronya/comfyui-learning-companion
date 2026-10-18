---
key: 视频生成/图生视频/Lip-syncing + Emotional Voice-over对口型+情感口播++数字人_2097495815702007810.json
name: Lip-syncing + Emotional Voice-over对口型+情感口播++数字人_2097495815702007810
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Lip-syncing + Emotional Voice-over对口型+情感口播++数字人_2097495815702007810.json
hash: 665c3527ce24e3f7
coverage: 0.866667
learned_at: 2026-10-17 01:28:03
nodes: [WanVideoLoraSelect, PlaySound|pysssss, GetNode, WanVideoModelLoader, WanVideoBlockSwap, CLIPVisionLoader, GetImageRangeFromBatch, LoadWanVideoT5TextEncoder, WanVideoLoraSelect, WanVideoVAELoader, WanVideoClipVisionEncode, LayerUtility: ImageScaleByAspectRatio V2, MultiTalkModelLoader, AudioSeparation, WanVideoImageToVideoMultiTalk, WanVideoSampler, WanVideoDecode, AudioCrop, SetNode, Audio Duration (mtb), MathExpression|pysssss, SetNode, MathExpression|pysssss, DownloadAndLoadWav2VecModel, MultiTalkWav2VecEmbeds, SetNode, WanVideoTextEncode, LoadAudio, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Lip-syncing + Emotional Voice-over对口型+情感口播++数字人_2097495815702007810.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Lip-syncing + Emotional Voice-over对口型+情感口播++数字人_2097495815702007810.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（30 个）：
- `WanVideoLoraSelect`
- `PlaySound|pysssss`
- `GetNode`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `GetImageRangeFromBatch`
- `LoadWanVideoT5TextEncoder`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MultiTalkModelLoader`
- `AudioSeparation`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `AudioCrop`
- `SetNode`
- `Audio Duration (mtb)`
- `MathExpression|pysssss`
- `SetNode`
- `MathExpression|pysssss`
- `DownloadAndLoadWav2VecModel`
- `MultiTalkWav2VecEmbeds`
- `SetNode`
- `WanVideoTextEncode`
- `LoadAudio`
- `VHS_VideoCombine`
- `LoadImage`

## 知识

覆盖率 **87%**（26/30）

**有卡**：`WanVideoLoraSelect`、`PlaySound|pysssss`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`GetImageRangeFromBatch`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`MultiTalkModelLoader`、`AudioSeparation`、`WanVideoImageToVideoMultiTalk`、`WanVideoSampler`、`WanVideoDecode`、`AudioCrop`、`Audio Duration (mtb)`、`MathExpression|pysssss`、`DownloadAndLoadWav2VecModel`、`MultiTalkWav2VecEmbeds`、`WanVideoTextEncode`、`LoadAudio`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
