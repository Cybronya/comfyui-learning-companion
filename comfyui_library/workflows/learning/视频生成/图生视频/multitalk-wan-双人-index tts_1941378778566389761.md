---
key: 视频生成/图生视频/multitalk-wan-双人-index tts_1941378778566389761.json
name: multitalk-wan-双人-index tts_1941378778566389761.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1941378778566389761.json
hash: 72233b6e21937750
coverage: 0.955556
learned_at: 2026-10-15 22:30:35
nodes: [LoadWanVideoT5TextEncoder, DownloadAndLoadWav2VecModel, AudioCrop, WanVideoDecode, VHS_VideoCombine, LayerUtility: PurgeVRAM V2, IndexTTSRun, LayerUtility: PurgeVRAM V2, LoadAudio, String Literal, LoadAudio, PreviewAudio, PreviewAudio, AudioCrop, StringToInt, MultiTalkModelLoader, WanVideoTorchCompileSettings, WanVideoVAELoader, StringToInt, MaskPreview, WanVideoBlockSwap, WanVideoImageToVideoMultiTalk, CLIPVisionLoader, WanVideoModelLoader, MathExpression|pysssss, PrimitiveNode, PrimitiveNode, AudioSeparation, AudioSeparation, LoadAudio, LoadAudio, PreviewAudio, WanVideoTextEncode, ImageResizeKJv2, AudioSeparation, PreviewAudio, IndexTTSRun, WanVideoClipVisionEncode, MaskPreview, SeparateMasks, WanVideoLoraSelect, WanVideoSampler, String Literal, MultiTalkWav2VecEmbeds, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/multitalk-wan-双人-index tts_1941378778566389761.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1941378778566389761.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（45 个）：
- `LoadWanVideoT5TextEncoder`
- `DownloadAndLoadWav2VecModel`
- `AudioCrop`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM V2`
- `IndexTTSRun`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `String Literal`
- `LoadAudio`
- `PreviewAudio`
- `PreviewAudio`
- `AudioCrop`
- `StringToInt`
- `MultiTalkModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `StringToInt`
- `MaskPreview`
- `WanVideoBlockSwap`
- `WanVideoImageToVideoMultiTalk`
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
- `AudioSeparation`
- `PreviewAudio`
- `IndexTTSRun`
- `WanVideoClipVisionEncode`
- `MaskPreview`
- `SeparateMasks`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `String Literal`
- `MultiTalkWav2VecEmbeds`
- `LoadImage`

## 知识

覆盖率 **96%**（43/45）

**有卡**：`LoadWanVideoT5TextEncoder`、`DownloadAndLoadWav2VecModel`、`AudioCrop`、`WanVideoDecode`、`VHS_VideoCombine`、`LayerUtility: PurgeVRAM V2`、`IndexTTSRun`、`LoadAudio`、`String Literal`、`PreviewAudio`、`StringToInt`、`MultiTalkModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`MaskPreview`、`WanVideoBlockSwap`、`WanVideoImageToVideoMultiTalk`、`CLIPVisionLoader`、`WanVideoModelLoader`、`MathExpression|pysssss`、`AudioSeparation`、`WanVideoTextEncode`、`ImageResizeKJv2`、`WanVideoClipVisionEncode`、`SeparateMasks`、`WanVideoLoraSelect`、`WanVideoSampler`、`MultiTalkWav2VecEmbeds`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
