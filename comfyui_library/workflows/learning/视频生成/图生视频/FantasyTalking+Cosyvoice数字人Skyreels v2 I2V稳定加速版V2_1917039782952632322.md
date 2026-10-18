---
key: 视频生成/图生视频/FantasyTalking+Cosyvoice数字人Skyreels v2 I2V稳定加速版V2_1917039782952632322.json
name: FantasyTalking+Cosyvoice数字人Skyreels v2 I2V稳定加速版V2_1917039782952632322.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/FantasyTalking+Cosyvoice数字人Skyreels v2 I2V稳定加速版V2_1917039782952632322.json
hash: a1298684aaea89c5
coverage: 0.75
learned_at: 2026-10-15 22:29:39
nodes: [LoadAudio, PreviewAudio, PreviewAudio, LoadAudio, NTCosyVoiceZeroShotSampler, NTCosyVoiceInstruct2Sampler, NTCosyVoiceCrossLingualSampler, PreviewAudio, LoadImage, CLIPVisionLoader, WanVideoClipVisionEncode, SetNode, WanVideoImageToVideoEncode, GetNode, SetNode, WanVideoTextEncode, DownloadAndLoadWav2VecModel, WanVideoVAELoader, FantasyTalkingModelLoader, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoBlockSwap, WanVideoDecode, GetNode, GetNode, VHS_VideoCombine, WanVideoTeaCache, CreateCFGScheduleFloatList, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, FantasyTalkingWav2VecEmbeds, JWInteger, JWInteger, JWInteger, LoadAudio, Note, Note, Note, Note, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/FantasyTalking+Cosyvoice数字人Skyreels v2 I2V稳定加速版V2_1917039782952632322.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1917039782952632322.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（40 个）：
- `LoadAudio`
- `PreviewAudio`
- `PreviewAudio`
- `LoadAudio`
- `NTCosyVoiceZeroShotSampler` ★核心
- `NTCosyVoiceInstruct2Sampler` ★核心
- `NTCosyVoiceCrossLingualSampler` ★核心
- `PreviewAudio`
- `LoadImage`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `SetNode`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `SetNode`
- `WanVideoTextEncode`
- `DownloadAndLoadWav2VecModel`
- `WanVideoVAELoader`
- `FantasyTalkingModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoTeaCache`
- `CreateCFGScheduleFloatList`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `FantasyTalkingWav2VecEmbeds`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `LoadAudio`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`

## 知识

覆盖率 **75%**（30/40）

**有卡**：`LoadAudio`、`PreviewAudio`、`NTCosyVoiceZeroShotSampler`、`NTCosyVoiceInstruct2Sampler`、`NTCosyVoiceCrossLingualSampler`、`LoadImage`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`WanVideoTextEncode`、`DownloadAndLoadWav2VecModel`、`WanVideoVAELoader`、`FantasyTalkingModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoTeaCache`、`CreateCFGScheduleFloatList`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`FantasyTalkingWav2VecEmbeds`、`JWInteger`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、NTCosyVoiceCrossLingualSampler、NTCosyVoiceInstruct2Sampler、NTCosyVoiceZeroShotSampler、LoadWanVideoT5TextEncoder、WanVideoDecode
