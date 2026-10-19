---
key: 数字人/数字人/音频趋动 infinite talk wan2.1_2015430092859645953.json
name: 音频趋动 infinite talk wan2.1_2015430092859645953
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/音频趋动 infinite talk wan2.1_2015430092859645953.json
hash: 861aff9ad188d5be
coverage: 0.592593
learned_at: 2026-10-18 19:07:53
nodes: [GetImageRangeFromBatch, WanVideoEncode, GetImageSizeAndCount, GetNode, GetNode, PreviewAny, SetNode, Note, SetNode, CLIPVisionLoader, SetNode, Note, WanVideoDecode, WanVideoBlockSwap, ImageFromBatch, ColorMatch, WanVideoTextEncodeCached, WanVideoVAELoader, WanVideoLoraSelect, WanVideoImageToVideoMultiTalk, WanVideoClipVisionEncode, GetNode, GetNode, Note, INTConstant, SetNode, Note, Note, GetNode, LayerUtility: ImageScaleByAspectRatio V2, ImageFromBatch, Note, VHS_LoadVideo, Note, Note, DownloadAndLoadWav2VecModel, MultiTalkWav2VecEmbeds, INTConstant, PreviewAudio, GetNode, CR Text, WanVideoSampler, WanVideoLoraSelect, WanVideoModelLoader, MultiTalkModelLoader, AudioSeparation, SetNode, LoadImage, LoadAudio, TrimAudioDuration, PreviewAudio, GetNode, SetNode, VHS_VideoCombine]
patterns: []
missing: []
---

# 数字人/数字人/音频趋动 infinite talk wan2.1_2015430092859645953.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/音频趋动 infinite talk wan2.1_2015430092859645953.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（54 个）：
- `GetImageRangeFromBatch`
- `WanVideoEncode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `PreviewAny`
- `SetNode`
- `Note`
- `SetNode`
- `CLIPVisionLoader`
- `SetNode`
- `Note`
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `ImageFromBatch`
- `ColorMatch`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `Note`
- `INTConstant`
- `SetNode`
- `Note`
- `Note`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageFromBatch`
- `Note`
- `VHS_LoadVideo`
- `Note`
- `Note`
- `DownloadAndLoadWav2VecModel`
- `MultiTalkWav2VecEmbeds`
- `INTConstant`
- `PreviewAudio`
- `GetNode`
- `CR Text`
- `WanVideoSampler` ★核心
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `MultiTalkModelLoader`
- `AudioSeparation`
- `SetNode`
- `LoadImage`
- `LoadAudio`
- `TrimAudioDuration`
- `PreviewAudio`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`

## 知识

覆盖率 **59%**（32/54）

**有卡**：`GetImageRangeFromBatch`、`WanVideoEncode`、`GetImageSizeAndCount`、`CLIPVisionLoader`、`WanVideoDecode`、`WanVideoBlockSwap`、`ImageFromBatch`、`ColorMatch`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoImageToVideoMultiTalk`、`WanVideoClipVisionEncode`、`INTConstant`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_LoadVideo`、`DownloadAndLoadWav2VecModel`、`MultiTalkWav2VecEmbeds`、`PreviewAudio`、`CR Text`、`WanVideoSampler`、`WanVideoModelLoader`、`MultiTalkModelLoader`、`AudioSeparation`、`LoadImage`、`LoadAudio`、`TrimAudioDuration`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode、WanVideoLoraSelect
