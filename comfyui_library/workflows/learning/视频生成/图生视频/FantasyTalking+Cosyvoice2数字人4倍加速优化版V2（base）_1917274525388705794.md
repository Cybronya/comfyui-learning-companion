---
key: 视频生成/图生视频/FantasyTalking+Cosyvoice2数字人4倍加速优化版V2（base）_1917274525388705794.json
name: FantasyTalking+Cosyvoice2数字人4倍加速优化版V2（base）_1917274525388705794.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1917274525388705794.json
hash: b8857fd56db235eb
coverage: 0.833333
learned_at: 2026-10-15 22:29:39
nodes: [LoadAudio, PreviewAudio, PreviewAudio, LoadAudio, NTCosyVoiceZeroShotSampler, NTCosyVoiceInstruct2Sampler, NTCosyVoiceCrossLingualSampler, PreviewAudio, LoadImage, CLIPVisionLoader, WanVideoClipVisionEncode, MarkdownNote, Note, SetNode, GetNode, WanVideoImageToVideoEncode, GetNode, SetNode, GetNode, WanVideoTextEncode, DownloadAndLoadWav2VecModel, FantasyTalkingWav2VecEmbeds, WanVideoVAELoader, FantasyTalkingModelLoader, CreateCFGScheduleFloatList, WanVideoSLG, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, WanVideoDecode, WanVideoSampler, WanVideoTeaCache, WanVideoModelLoader, WanVideoContextOptions, VHS_VideoCombine, JWInteger, JWInteger, JWInteger, LoadAudio, CR Prompt Text]
patterns: []
missing: []
---

# 视频生成/图生视频/FantasyTalking+Cosyvoice2数字人4倍加速优化版V2（base）_1917274525388705794.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1917274525388705794.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（42 个）：
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
- `MarkdownNote`
- `Note`
- `SetNode`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `SetNode`
- `GetNode`
- `WanVideoTextEncode`
- `DownloadAndLoadWav2VecModel`
- `FantasyTalkingWav2VecEmbeds`
- `WanVideoVAELoader`
- `FantasyTalkingModelLoader`
- `CreateCFGScheduleFloatList`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoTeaCache`
- `WanVideoModelLoader`
- `WanVideoContextOptions`
- `VHS_VideoCombine`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `LoadAudio`
- `CR Prompt Text`

## 知识

覆盖率 **83%**（35/42）

**有卡**：`LoadAudio`、`PreviewAudio`、`NTCosyVoiceZeroShotSampler`、`NTCosyVoiceInstruct2Sampler`、`NTCosyVoiceCrossLingualSampler`、`LoadImage`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`WanVideoTextEncode`、`DownloadAndLoadWav2VecModel`、`FantasyTalkingWav2VecEmbeds`、`WanVideoVAELoader`、`FantasyTalkingModelLoader`、`CreateCFGScheduleFloatList`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoExperimentalArgs`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoTeaCache`、`WanVideoModelLoader`、`WanVideoContextOptions`、`VHS_VideoCombine`、`JWInteger`、`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、NTCosyVoiceCrossLingualSampler、NTCosyVoiceInstruct2Sampler、NTCosyVoiceZeroShotSampler、LoadWanVideoT5TextEncoder、WanVideoDecode
