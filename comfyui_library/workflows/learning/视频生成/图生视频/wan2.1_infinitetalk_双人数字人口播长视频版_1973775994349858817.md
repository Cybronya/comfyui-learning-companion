---
key: 视频生成/图生视频/wan2.1_infinitetalk_双人数字人口播长视频版_1973775994349858817.json
name: wan2.1_infinitetalk_双人数字人口播长视频版_1973775994349858817.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1973775994349858817.json
hash: 96601099d4753ceb
coverage: 0.909091
learned_at: 2026-10-15 22:32:04
nodes: [WanVideoDecode, WanVideoLoraSelect, MultiTalkModelLoader, VHS_VideoCombine, AudioSeparation, WanVideoSampler, WanVideoImageToVideoMultiTalk, Reroute, Int, Int, LoadImage, GetNode, CR Text, SetNode, WanVideoBlockSwap, WanVideoModelLoader, WanVideoClipVisionEncode, WanVideoVAELoader, CLIPVisionLoader, LoadWanVideoT5TextEncoder, WanVideoTextEncode, ImageResizeKJv2, MultiTalkWav2VecEmbeds, AudioSeparation, LoadAudio, AudioCrop, LoadAudio, AudioCrop, LoadAudio, AudioCrop, MathExpression|pysssss, JWInteger, DownloadAndLoadWav2VecModel]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1_infinitetalk_双人数字人口播长视频版_1973775994349858817.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1973775994349858817.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（33 个）：
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `VHS_VideoCombine`
- `AudioSeparation`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoMultiTalk`
- `Reroute`
- `Int`
- `Int`
- `LoadImage`
- `GetNode`
- `CR Text`
- `SetNode`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoClipVisionEncode`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `ImageResizeKJv2`
- `MultiTalkWav2VecEmbeds`
- `AudioSeparation`
- `LoadAudio`
- `AudioCrop`
- `LoadAudio`
- `AudioCrop`
- `LoadAudio`
- `AudioCrop`
- `MathExpression|pysssss`
- `JWInteger`
- `DownloadAndLoadWav2VecModel`

## 知识

覆盖率 **91%**（30/33）

**有卡**：`WanVideoDecode`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`VHS_VideoCombine`、`AudioSeparation`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`Int`、`LoadImage`、`CR Text`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoClipVisionEncode`、`WanVideoVAELoader`、`CLIPVisionLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`ImageResizeKJv2`、`MultiTalkWav2VecEmbeds`、`LoadAudio`、`AudioCrop`、`MathExpression|pysssss`、`JWInteger`、`DownloadAndLoadWav2VecModel`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
