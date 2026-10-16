---
key: 视频生成/图生视频/MultiTalk+LightX2v Rank64+AniWan双人加速版极限动态质量版V1（KJ）_1945360751139934210.json
name: MultiTalk+LightX2v Rank64+AniWan双人加速版极限动态质量版V1（KJ）_1945360751139934210.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1945360751139934210.json
hash: 82d255b5209f944f
coverage: 1
learned_at: 2026-10-15 22:30:41
nodes: [WanVideoDecode, LoadWanVideoT5TextEncoder, DownloadAndLoadWav2VecModel, WanVideoBlockSwap, WanVideoVAELoader, LoadAudio, WanVideoTextEncode, MultiTalkModelLoader, WanVideoClipVisionEncode, CLIPVisionLoader, SaveAudio, LoadImage, AudioCrop, CR Prompt Text, JWStringToInteger, JWStringToInteger, AudioSeparation, MathExpression|pysssss, LoadAudio, AudioCrop, MultiTalkWav2VecEmbeds, ImageResizeKJv2, AudioSeparation, SeparateMasks, MaskPreview+, WanVideoImageToVideoMultiTalk, CR Prompt Text, WanVideoModelLoader, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, VHS_VideoCombine, WanVideoLoraSelect, WanVideoSampler, WanVideoFreeInitArgs]
patterns: []
missing: []
---

# 视频生成/图生视频/MultiTalk+LightX2v Rank64+AniWan双人加速版极限动态质量版V1（KJ）_1945360751139934210.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1945360751139934210.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（35 个）：
- `WanVideoDecode`
- `LoadWanVideoT5TextEncoder`
- `DownloadAndLoadWav2VecModel`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `LoadAudio`
- `WanVideoTextEncode`
- `MultiTalkModelLoader`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `SaveAudio`
- `LoadImage`
- `AudioCrop`
- `CR Prompt Text`
- `JWStringToInteger`
- `JWStringToInteger`
- `AudioSeparation`
- `MathExpression|pysssss`
- `LoadAudio`
- `AudioCrop`
- `MultiTalkWav2VecEmbeds`
- `ImageResizeKJv2`
- `AudioSeparation`
- `SeparateMasks`
- `MaskPreview+`
- `WanVideoImageToVideoMultiTalk`
- `CR Prompt Text`
- `WanVideoModelLoader`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `WanVideoFreeInitArgs`

## 知识

覆盖率 **100%**（35/35）

**有卡**：`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`DownloadAndLoadWav2VecModel`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`LoadAudio`、`WanVideoTextEncode`、`MultiTalkModelLoader`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`SaveAudio`、`LoadImage`、`AudioCrop`、`CR Prompt Text`、`JWStringToInteger`、`AudioSeparation`、`MathExpression|pysssss`、`MultiTalkWav2VecEmbeds`、`ImageResizeKJv2`、`SeparateMasks`、`MaskPreview+`、`WanVideoImageToVideoMultiTalk`、`WanVideoModelLoader`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`WanVideoSampler`、`WanVideoFreeInitArgs`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
