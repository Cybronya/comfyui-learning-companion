---
key: 视频生成/图生视频/Infinite talk动态加强（Lightx2v+Rcm）_1981983249872371714.json
name: Infinite talk动态加强（Lightx2v+Rcm）_1981983249872371714.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1981983249872371714.json
hash: c0f4a8b46c3f0d70
coverage: 0.866667
learned_at: 2026-10-15 22:32:39
nodes: [CLIPVisionLoader, PreviewAny, WanVideoModelLoader, MultiTalkWav2VecEmbeds, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, LayerUtility: ImageScaleByAspectRatio V2, AudioSeparation, JWInteger, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, JWFloat, MultiTalkModelLoader, MarkdownNote, Note, WanVideoVAELoader, Note, LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoImageToVideoMultiTalk, WanVideoClipVisionEncode, WanVideoSampler, WanVideoDecode, VHS_VideoCombine, LoadImage, AudioCrop, LoadAudio, CR Prompt Text, JWInteger]
patterns: []
missing: []
---

# 视频生成/图生视频/Infinite talk动态加强（Lightx2v+Rcm）_1981983249872371714.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1981983249872371714.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（30 个）：
- `CLIPVisionLoader`
- `PreviewAny`
- `WanVideoModelLoader`
- `MultiTalkWav2VecEmbeds`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `AudioSeparation`
- `JWInteger`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `JWFloat`
- `MultiTalkModelLoader`
- `MarkdownNote`
- `Note`
- `WanVideoVAELoader`
- `Note`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoClipVisionEncode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `LoadImage`
- `AudioCrop`
- `LoadAudio`
- `CR Prompt Text`
- `JWInteger`

## 知识

覆盖率 **87%**（26/30）

**有卡**：`CLIPVisionLoader`、`WanVideoModelLoader`、`MultiTalkWav2VecEmbeds`、`DownloadAndLoadWav2VecModel`、`GetImageSizeAndCount`、`LayerUtility: ImageScaleByAspectRatio V2`、`AudioSeparation`、`JWInteger`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`JWFloat`、`MultiTalkModelLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoImageToVideoMultiTalk`、`WanVideoClipVisionEncode`、`WanVideoSampler`、`WanVideoDecode`、`VHS_VideoCombine`、`LoadImage`、`AudioCrop`、`LoadAudio`、`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
