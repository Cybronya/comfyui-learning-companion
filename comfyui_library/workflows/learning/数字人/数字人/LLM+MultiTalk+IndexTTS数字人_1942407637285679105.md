---
key: 数字人/数字人/LLM+MultiTalk+IndexTTS数字人_1942407637285679105.json
name: LLM+MultiTalk+IndexTTS数字人_1942407637285679105
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LLM+MultiTalk+IndexTTS数字人_1942407637285679105.json
hash: 93251782cadb6f85
coverage: 0.966667
learned_at: 2026-10-26 01:55:41
nodes: [LoadWanVideoT5TextEncoder, WanVideoClipVisionEncode, WanVideoDecode, AudioSeparation, CLIPVisionLoader, WanVideoLoraSelect, MultiTalkModelLoader, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoModelLoader, MultiTalkWav2VecEmbeds, DownloadAndLoadWav2VecModel, WanVideoVAELoader, WanVideoBlockSwap, WanVideoTextEncode, VHS_VideoCombine, String Literal, LayerUtility: PurgeVRAM V2, LLMLoader, AudioCrop, WanVideoTorchCompileSettings, ImageResizeKJv2, INTConstant, IndexTTSRun, LoadAudio, ShowText, LLMSampler, LoadImage, PrimitiveStringMultiline, PreviewAudio]
patterns: []
missing: []
---

# 数字人/数字人/LLM+MultiTalk+IndexTTS数字人_1942407637285679105.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LLM+MultiTalk+IndexTTS数字人_1942407637285679105.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（30 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `AudioSeparation`
- `CLIPVisionLoader`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `MultiTalkWav2VecEmbeds`
- `DownloadAndLoadWav2VecModel`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `String Literal`
- `LayerUtility: PurgeVRAM V2`
- `LLMLoader`
- `AudioCrop`
- `WanVideoTorchCompileSettings`
- `ImageResizeKJv2`
- `INTConstant`
- `IndexTTSRun`
- `LoadAudio`
- `ShowText`
- `LLMSampler` ★核心
- `LoadImage`
- `PrimitiveStringMultiline`
- `PreviewAudio`

## 知识

覆盖率 **97%**（29/30）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoClipVisionEncode`、`WanVideoDecode`、`AudioSeparation`、`CLIPVisionLoader`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`WanVideoModelLoader`、`MultiTalkWav2VecEmbeds`、`DownloadAndLoadWav2VecModel`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoTextEncode`、`VHS_VideoCombine`、`String Literal`、`LayerUtility: PurgeVRAM V2`、`LLMLoader`、`AudioCrop`、`WanVideoTorchCompileSettings`、`ImageResizeKJv2`、`INTConstant`、`IndexTTSRun`、`LoadAudio`、`ShowText`、`LLMSampler`、`LoadImage`、`PreviewAudio`

**用到的条目**：LoadImage、WanVideoSampler、LLMSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
