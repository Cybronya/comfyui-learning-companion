---
key: 视频生成/图生视频/InfiniteTalk+IndexTTS+Kontext数字人带货_1958084173951094786.json
name: InfiniteTalk+IndexTTS+Kontext数字人带货_1958084173951094786.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1958084173951094786.json
hash: 35cd6499ae0c9089
coverage: 0.942857
learned_at: 2026-10-15 22:31:20
nodes: [LoadWanVideoT5TextEncoder, WanVideoClipVisionEncode, WanVideoDecode, CLIPVisionLoader, AudioCrop, WanVideoTorchCompileSettings, WanVideoSampler, WanVideoModelLoader, DownloadAndLoadWav2VecModel, WanVideoVAELoader, WanVideoBlockSwap, PreviewImage, ImageConcanate, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, RH_ComfyFluxKontext, LoadImage, LoadImage, RH_Translator, WanVideoTextEncode, String Literal, INTConstant, ImageResizeKJv2, LayerUtility: PurgeVRAM V2, PreviewAudio, IndexTTSRun, String Literal, LoadAudio, MultiTalkWav2VecEmbeds, AudioSeparation, WanVideoImageToVideoMultiTalk, MultiTalkModelLoader, WanVideoLoraSelect, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/InfiniteTalk+IndexTTS+Kontext数字人带货_1958084173951094786.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1958084173951094786.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（35 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `CLIPVisionLoader`
- `AudioCrop`
- `WanVideoTorchCompileSettings`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `DownloadAndLoadWav2VecModel`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
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
- `MultiTalkWav2VecEmbeds`
- `AudioSeparation`
- `WanVideoImageToVideoMultiTalk`
- `MultiTalkModelLoader`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`

## 知识

覆盖率 **94%**（33/35）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoClipVisionEncode`、`WanVideoDecode`、`CLIPVisionLoader`、`AudioCrop`、`WanVideoTorchCompileSettings`、`WanVideoSampler`、`WanVideoModelLoader`、`DownloadAndLoadWav2VecModel`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`ImageConcanate`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`RH_ComfyFluxKontext`、`LoadImage`、`RH_Translator`、`WanVideoTextEncode`、`String Literal`、`INTConstant`、`ImageResizeKJv2`、`LayerUtility: PurgeVRAM V2`、`PreviewAudio`、`IndexTTSRun`、`LoadAudio`、`MultiTalkWav2VecEmbeds`、`AudioSeparation`、`WanVideoImageToVideoMultiTalk`、`MultiTalkModelLoader`、`WanVideoLoraSelect`、`VHS_VideoCombine`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
