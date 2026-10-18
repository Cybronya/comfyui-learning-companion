---
key: 视频生成/图生视频/Digital Avatars for E-commerce InfiniteTalk +数字人带货_2095704577696948225.json
name: Digital Avatars for E-commerce InfiniteTalk +数字人带货_2095704577696948225
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Digital Avatars for E-commerce InfiniteTalk +数字人带货_2095704577696948225.json
hash: 51adf2807cebb605
coverage: 0.942857
learned_at: 2026-10-17 01:09:16
nodes: [LoadWanVideoT5TextEncoder, WanVideoClipVisionEncode, WanVideoDecode, CLIPVisionLoader, WanVideoSampler, WanVideoModelLoader, DownloadAndLoadWav2VecModel, WanVideoVAELoader, WanVideoBlockSwap, ImageConcanate, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, WanVideoTextEncode, INTConstant, ImageResizeKJv2, LayerUtility: PurgeVRAM V2, PreviewAudio, MultiTalkWav2VecEmbeds, AudioSeparation, WanVideoImageToVideoMultiTalk, MultiTalkModelLoader, WanVideoLoraSelect, VHS_VideoCombine, LoadImage, PreviewImage, RH_ComfyFluxKontext, IndexTTSRun, String Literal, String Literal, LoadAudio, LoadImage, WanVideoTorchCompileSettings, AudioCrop, RH_Translator]
patterns: []
missing: []
---

# 视频生成/图生视频/Digital Avatars for E-commerce InfiniteTalk +数字人带货_2095704577696948225.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Digital Avatars for E-commerce InfiniteTalk +数字人带货_2095704577696948225.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（35 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `CLIPVisionLoader`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `DownloadAndLoadWav2VecModel`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `ImageConcanate`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `WanVideoTextEncode`
- `INTConstant`
- `ImageResizeKJv2`
- `LayerUtility: PurgeVRAM V2`
- `PreviewAudio`
- `MultiTalkWav2VecEmbeds`
- `AudioSeparation`
- `WanVideoImageToVideoMultiTalk`
- `MultiTalkModelLoader`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`
- `LoadImage`
- `PreviewImage`
- `RH_ComfyFluxKontext`
- `IndexTTSRun`
- `String Literal`
- `String Literal`
- `LoadAudio`
- `LoadImage`
- `WanVideoTorchCompileSettings`
- `AudioCrop`
- `RH_Translator`

## 知识

覆盖率 **94%**（33/35）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoClipVisionEncode`、`WanVideoDecode`、`CLIPVisionLoader`、`WanVideoSampler`、`WanVideoModelLoader`、`DownloadAndLoadWav2VecModel`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`ImageConcanate`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`WanVideoTextEncode`、`INTConstant`、`ImageResizeKJv2`、`LayerUtility: PurgeVRAM V2`、`PreviewAudio`、`MultiTalkWav2VecEmbeds`、`AudioSeparation`、`WanVideoImageToVideoMultiTalk`、`MultiTalkModelLoader`、`WanVideoLoraSelect`、`VHS_VideoCombine`、`LoadImage`、`RH_ComfyFluxKontext`、`IndexTTSRun`、`String Literal`、`LoadAudio`、`WanVideoTorchCompileSettings`、`AudioCrop`、`RH_Translator`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
