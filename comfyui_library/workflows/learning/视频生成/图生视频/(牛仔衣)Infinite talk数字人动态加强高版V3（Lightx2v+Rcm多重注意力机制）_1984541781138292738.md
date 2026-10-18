---
key: 视频生成/图生视频/(牛仔衣)Infinite talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1984541781138292738.json
name: (牛仔衣)Infinite talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1984541781138292738.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(牛仔衣)Infinite talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1984541781138292738.json
hash: 555338f7ad5a37b8
coverage: 0.771429
learned_at: 2026-10-15 22:32:49
nodes: [MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, Note, Note, Note, Note, Note, AudioSeparation, CR Prompt Text, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, Note, WanVideoModelLoader, WanVideoTextEncode, WanVideoSampler, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoLoraSelect, MultiTalkModelLoader, JWFloat, MultiTalkWav2VecEmbeds, JWInteger, JWInteger, VHS_VideoCombine, LoadImage, AudioCrop, LoadAudio, WanVideoDecode, VHS_VideoCombine, WanVideoBlockSwap]
patterns: []
missing: []
---

# 视频生成/图生视频/(牛仔衣)Infinite talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1984541781138292738.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1984541781138292738.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（35 个）：
- `MarkdownNote`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoT5TextEncoder`
- `CLIPVisionLoader`
- `PreviewAny`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `AudioSeparation`
- `CR Prompt Text`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `Note`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `JWFloat`
- `MultiTalkWav2VecEmbeds`
- `JWInteger`
- `JWInteger`
- `VHS_VideoCombine`
- `LoadImage`
- `AudioCrop`
- `LoadAudio`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`

## 知识

覆盖率 **77%**（27/35）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`AudioSeparation`、`CR Prompt Text`、`DownloadAndLoadWav2VecModel`、`GetImageSizeAndCount`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`JWFloat`、`MultiTalkWav2VecEmbeds`、`JWInteger`、`VHS_VideoCombine`、`LoadImage`、`AudioCrop`、`LoadAudio`、`WanVideoDecode`、`WanVideoBlockSwap`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
