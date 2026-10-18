---
key: 视频生成/图生视频/InfiniteTalk-wan-双人-index tts_1958085210749415426.json
name: InfiniteTalk-wan-双人-index tts_1958085210749415426.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/InfiniteTalk-wan-双人-index tts_1958085210749415426.json
hash: d27146e6414df3a4
coverage: 0.939394
learned_at: 2026-10-15 22:31:20
nodes: [LoadWanVideoT5TextEncoder, DownloadAndLoadWav2VecModel, AudioCrop, WanVideoDecode, AudioCrop, StringToInt, WanVideoTorchCompileSettings, WanVideoVAELoader, StringToInt, MaskPreview, WanVideoBlockSwap, CLIPVisionLoader, WanVideoModelLoader, MathExpression|pysssss, PrimitiveNode, PrimitiveNode, AudioSeparation, AudioSeparation, LoadAudio, LoadAudio, PreviewAudio, WanVideoTextEncode, ImageResizeKJv2, WanVideoClipVisionEncode, MaskPreview, SeparateMasks, WanVideoSampler, LoadImage, MultiTalkWav2VecEmbeds, MultiTalkModelLoader, WanVideoLoraSelect, WanVideoImageToVideoMultiTalk, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/InfiniteTalk-wan-双人-index tts_1958085210749415426.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1958085210749415426.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（33 个）：
- `LoadWanVideoT5TextEncoder`
- `DownloadAndLoadWav2VecModel`
- `AudioCrop`
- `WanVideoDecode`
- `AudioCrop`
- `StringToInt`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `StringToInt`
- `MaskPreview`
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `WanVideoModelLoader`
- `MathExpression|pysssss`
- `PrimitiveNode`
- `PrimitiveNode`
- `AudioSeparation`
- `AudioSeparation`
- `LoadAudio`
- `LoadAudio`
- `PreviewAudio`
- `WanVideoTextEncode`
- `ImageResizeKJv2`
- `WanVideoClipVisionEncode`
- `MaskPreview`
- `SeparateMasks`
- `WanVideoSampler` ★核心
- `LoadImage`
- `MultiTalkWav2VecEmbeds`
- `MultiTalkModelLoader`
- `WanVideoLoraSelect`
- `WanVideoImageToVideoMultiTalk`
- `VHS_VideoCombine`

## 知识

覆盖率 **94%**（31/33）

**有卡**：`LoadWanVideoT5TextEncoder`、`DownloadAndLoadWav2VecModel`、`AudioCrop`、`WanVideoDecode`、`StringToInt`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`MaskPreview`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoModelLoader`、`MathExpression|pysssss`、`AudioSeparation`、`LoadAudio`、`PreviewAudio`、`WanVideoTextEncode`、`ImageResizeKJv2`、`WanVideoClipVisionEncode`、`SeparateMasks`、`WanVideoSampler`、`LoadImage`、`MultiTalkWav2VecEmbeds`、`MultiTalkModelLoader`、`WanVideoLoraSelect`、`WanVideoImageToVideoMultiTalk`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
