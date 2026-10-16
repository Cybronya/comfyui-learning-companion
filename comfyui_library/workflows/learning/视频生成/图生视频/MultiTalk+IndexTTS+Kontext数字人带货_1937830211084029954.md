---
key: 视频生成/图生视频/MultiTalk+IndexTTS+Kontext数字人带货_1937830211084029954.json
name: MultiTalk+IndexTTS+Kontext数字人带货_1937830211084029954.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1937830211084029954.json
hash: 46761c04ba503f4e
coverage: 0.942857
learned_at: 2026-10-15 22:30:29
nodes: [LoadWanVideoT5TextEncoder, WanVideoClipVisionEncode, WanVideoDecode, AudioSeparation, CLIPVisionLoader, AudioCrop, WanVideoTorchCompileSettings, WanVideoLoraSelect, MultiTalkModelLoader, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoModelLoader, MultiTalkWav2VecEmbeds, DownloadAndLoadWav2VecModel, WanVideoVAELoader, WanVideoBlockSwap, VHS_VideoCombine, PreviewImage, ImageConcanate, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, RH_ComfyFluxKontext, LoadImage, LoadImage, RH_Translator, WanVideoTextEncode, String Literal, INTConstant, ImageResizeKJv2, LayerUtility: PurgeVRAM V2, PreviewAudio, IndexTTSRun, String Literal, LoadAudio]
patterns: []
missing: []
---

# 视频生成/图生视频/MultiTalk+IndexTTS+Kontext数字人带货_1937830211084029954.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1937830211084029954.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（35 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `AudioSeparation`
- `CLIPVisionLoader`
- `AudioCrop`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `MultiTalkWav2VecEmbeds`
- `DownloadAndLoadWav2VecModel`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `PreviewImage`
- `ImageConcanate`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `RH_ComfyFluxKontext`
- `LoadImage`
- `LoadImage`
- `RH_Translator`
- `WanVideoTextEncode`
- `String Literal`
- `INTConstant`
- `ImageResizeKJv2`
- `LayerUtility: PurgeVRAM V2`
- `PreviewAudio`
- `IndexTTSRun`
- `String Literal`
- `LoadAudio`

## 知识

覆盖率 **94%**（33/35）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoClipVisionEncode`、`WanVideoDecode`、`AudioSeparation`、`CLIPVisionLoader`、`AudioCrop`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`WanVideoModelLoader`、`MultiTalkWav2VecEmbeds`、`DownloadAndLoadWav2VecModel`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`ImageConcanate`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`RH_ComfyFluxKontext`、`LoadImage`、`RH_Translator`、`WanVideoTextEncode`、`String Literal`、`INTConstant`、`ImageResizeKJv2`、`LayerUtility: PurgeVRAM V2`、`PreviewAudio`、`IndexTTSRun`、`LoadAudio`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
