---
key: 视频生成/图生视频/Infinite talk数字人动态加强高版（Lightx2v+Rcm多重注意力机制）_1984675339228102657.json
name: Infinite talk数字人动态加强高版（Lightx2v+Rcm多重注意力机制）_1984675339228102657.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Infinite talk数字人动态加强高版（Lightx2v+Rcm多重注意力机制）_1984675339228102657.json
hash: e608c9e832cf0981
coverage: 0.882353
learned_at: 2026-10-15 22:32:49
nodes: [WanVideoLoraSelect, MultiTalkModelLoader, LoadImage, AudioSeparation, WanVideoImageToVideoMultiTalk, WanVideoClipVisionEncode, LoadImage, WanVideoSampler, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionLoader, WanVideoVAELoader, Note, MarkdownNote, LoadWanVideoT5TextEncoder, ToInt, Int, DownloadAndLoadWav2VecModel, SimpleMath+, easy showAnything, CR Prompt Text, PreviewAny, MultiTalkWav2VecEmbeds, WanVideoTextEncode, RH_GetAudioDuration, GetImageSizeAndCount, JWFloat, WanVideoDecode, VHS_VideoCombine, LoadAudio, AudioCrop, WanVideoModelLoader, WanVideoLoraSelect, WanVideoBlockSwap, JWInteger]
patterns: []
missing: []
---

# 视频生成/图生视频/Infinite talk数字人动态加强高版（Lightx2v+Rcm多重注意力机制）_1984675339228102657.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1984675339228102657.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（34 个）：
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `LoadImage`
- `AudioSeparation`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoClipVisionEncode`
- `LoadImage`
- `WanVideoSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `Note`
- `MarkdownNote`
- `LoadWanVideoT5TextEncoder`
- `ToInt`
- `Int`
- `DownloadAndLoadWav2VecModel`
- `SimpleMath+`
- `easy showAnything`
- `CR Prompt Text`
- `PreviewAny`
- `MultiTalkWav2VecEmbeds`
- `WanVideoTextEncode`
- `RH_GetAudioDuration`
- `GetImageSizeAndCount`
- `JWFloat`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `LoadAudio`
- `AudioCrop`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `JWInteger`

## 知识

覆盖率 **88%**（30/34）

**有卡**：`WanVideoLoraSelect`、`MultiTalkModelLoader`、`LoadImage`、`AudioSeparation`、`WanVideoImageToVideoMultiTalk`、`WanVideoClipVisionEncode`、`WanVideoSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`ToInt`、`Int`、`DownloadAndLoadWav2VecModel`、`SimpleMath+`、`CR Prompt Text`、`MultiTalkWav2VecEmbeds`、`WanVideoTextEncode`、`RH_GetAudioDuration`、`GetImageSizeAndCount`、`JWFloat`、`WanVideoDecode`、`VHS_VideoCombine`、`LoadAudio`、`AudioCrop`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`JWInteger`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
