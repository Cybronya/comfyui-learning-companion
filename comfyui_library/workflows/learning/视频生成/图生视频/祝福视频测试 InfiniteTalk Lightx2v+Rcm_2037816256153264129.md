---
key: 视频生成/图生视频/祝福视频测试 InfiniteTalk Lightx2v+Rcm_2037816256153264129.json
name: 祝福视频测试 InfiniteTalk Lightx2v+Rcm_2037816256153264129.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/祝福视频测试 InfiniteTalk Lightx2v+Rcm_2037816256153264129.json
hash: 9ff534325cf4278c
coverage: 0.923077
learned_at: 2026-10-15 22:35:59
nodes: [WanVideoTextEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoLoraSelect, JWFloat, WanVideoDecode, WanVideoSampler, WanVideoVAELoader, AudioCrop, DownloadAndLoadWav2VecModel, LoadWanVideoT5TextEncoder, WanVideoClipVisionEncode, WanVideoModelLoader, CLIPVisionLoader, LayerUtility: ImageScaleByAspectRatio V2, AudioSeparation, JWInteger, LoadAudio, Note, VHS_VideoCombine, CR Prompt Text, MultiTalkModelLoader, LoadImage, PreviewImage, MultiTalkWav2VecEmbeds]
patterns: []
missing: []
---

# 视频生成/图生视频/祝福视频测试 InfiniteTalk Lightx2v+Rcm_2037816256153264129.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2037816256153264129.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（26 个）：
- `WanVideoTextEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `JWFloat`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `AudioCrop`
- `DownloadAndLoadWav2VecModel`
- `LoadWanVideoT5TextEncoder`
- `WanVideoClipVisionEncode`
- `WanVideoModelLoader`
- `CLIPVisionLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `AudioSeparation`
- `JWInteger`
- `LoadAudio`
- `Note`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `MultiTalkModelLoader`
- `LoadImage`
- `PreviewImage`
- `MultiTalkWav2VecEmbeds`

## 知识

覆盖率 **92%**（24/26）

**有卡**：`WanVideoTextEncode`、`WanVideoImageToVideoMultiTalk`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`JWFloat`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoVAELoader`、`AudioCrop`、`DownloadAndLoadWav2VecModel`、`LoadWanVideoT5TextEncoder`、`WanVideoClipVisionEncode`、`WanVideoModelLoader`、`CLIPVisionLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`AudioSeparation`、`JWInteger`、`LoadAudio`、`VHS_VideoCombine`、`CR Prompt Text`、`MultiTalkModelLoader`、`LoadImage`、`MultiTalkWav2VecEmbeds`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
