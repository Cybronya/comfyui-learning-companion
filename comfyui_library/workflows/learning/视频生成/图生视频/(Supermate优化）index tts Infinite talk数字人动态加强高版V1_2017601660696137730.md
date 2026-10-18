---
key: 视频生成/图生视频/(Supermate优化）index tts Infinite talk数字人动态加强高版V1_2017601660696137730.json
name: (Supermate优化）index tts Infinite talk数字人动态加强高版V1_2017601660696137730.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(Supermate优化）index tts Infinite talk数字人动态加强高版V1_2017601660696137730.json
hash: 6de8e932e4ae8efb
coverage: 0.769231
learned_at: 2026-10-15 22:34:50
nodes: [Note, DownloadAndLoadWav2VecModel, JWInteger, WanVideoImageToVideoMultiTalk, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, GetImageSizeAndCount, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoVAELoader, WanVideoTextEncode, Note, Note, VHS_VideoCombine, LoadWanVideoT5TextEncoder, WanVideoModelLoader, MarkdownNote, Note, WanVideoBlockSwap, WanVideoLoraSelect, MultiTalkModelLoader, WanVideoLoraSelect, JWFloat, Reroute, PreviewAny, AudioSeparation, AudioCrop, SaveAudio, LoadAudio, easy downloadIndexTTSAndLoadModel, Note, MultiTalkWav2VecEmbeds, Note, WanVideoDecode, WanVideoSampler, LoadImage, CR Prompt Text, easy indexTTSGenerateSimple, Label (rgthree)]
patterns: []
missing: []
---

# 视频生成/图生视频/(Supermate优化）index tts Infinite talk数字人动态加强高版V1_2017601660696137730.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2017601660696137730.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（39 个）：
- `Note`
- `DownloadAndLoadWav2VecModel`
- `JWInteger`
- `WanVideoImageToVideoMultiTalk`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `GetImageSizeAndCount`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `MarkdownNote`
- `Note`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `WanVideoLoraSelect`
- `JWFloat`
- `Reroute`
- `PreviewAny`
- `AudioSeparation`
- `AudioCrop`
- `SaveAudio`
- `LoadAudio`
- `easy downloadIndexTTSAndLoadModel`
- `Note`
- `MultiTalkWav2VecEmbeds`
- `Note`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `LoadImage`
- `CR Prompt Text`
- `easy indexTTSGenerateSimple`
- `Label (rgthree)`

## 知识

覆盖率 **77%**（30/39）

**有卡**：`DownloadAndLoadWav2VecModel`、`JWInteger`、`WanVideoImageToVideoMultiTalk`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageSizeAndCount`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoVAELoader`、`WanVideoTextEncode`、`VHS_VideoCombine`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`JWFloat`、`AudioSeparation`、`AudioCrop`、`SaveAudio`、`LoadAudio`、`easy downloadIndexTTSAndLoadModel`、`MultiTalkWav2VecEmbeds`、`WanVideoDecode`、`WanVideoSampler`、`LoadImage`、`CR Prompt Text`、`easy indexTTSGenerateSimple`、`Label (rgthree)`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
