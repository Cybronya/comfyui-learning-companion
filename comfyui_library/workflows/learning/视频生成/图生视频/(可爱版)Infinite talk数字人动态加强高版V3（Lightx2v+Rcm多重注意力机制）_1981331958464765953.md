---
key: 视频生成/图生视频/(可爱版)Infinite talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1981331958464765953.json
name: (可爱版)Infinite talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1981331958464765953.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(可爱版)Infinite talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1981331958464765953.json
hash: 1ca9e2c7327ace97
coverage: 0.771429
learned_at: 2026-10-15 22:32:37
nodes: [MarkdownNote, MultiTalkWav2VecEmbeds, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, MultiTalkModelLoader, WanVideoVAELoader, WanVideoClipVisionEncode, Note, Note, Note, Note, WanVideoBlockSwap, Note, AudioSeparation, CR Prompt Text, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, Note, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoTextEncode, WanVideoSampler, WanVideoImageToVideoMultiTalk, JWInteger, VHS_VideoCombine, AudioCrop, JWInteger, LoadImage, LoadAudio, JWFloat, WanVideoDecode, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/(可爱版)Infinite talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1981331958464765953.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1981331958464765953.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（35 个）：
- `MarkdownNote`
- `MultiTalkWav2VecEmbeds`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoT5TextEncoder`
- `CLIPVisionLoader`
- `PreviewAny`
- `MultiTalkModelLoader`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `Note`
- `Note`
- `Note`
- `Note`
- `WanVideoBlockSwap`
- `Note`
- `AudioSeparation`
- `CR Prompt Text`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `Note`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoMultiTalk`
- `JWInteger`
- `VHS_VideoCombine`
- `AudioCrop`
- `JWInteger`
- `LoadImage`
- `LoadAudio`
- `JWFloat`
- `WanVideoDecode`
- `VHS_VideoCombine`

## 知识

覆盖率 **77%**（27/35）

**有卡**：`MultiTalkWav2VecEmbeds`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`MultiTalkModelLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`WanVideoBlockSwap`、`AudioSeparation`、`CR Prompt Text`、`DownloadAndLoadWav2VecModel`、`GetImageSizeAndCount`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`JWInteger`、`VHS_VideoCombine`、`AudioCrop`、`LoadImage`、`LoadAudio`、`JWFloat`、`WanVideoDecode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
