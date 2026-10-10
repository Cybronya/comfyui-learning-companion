---
key: 视频生成/文生视频/Infinite+talk数字人动态加强高版V3.5_1991175069309448194.json
name: Infinite+talk数字人动态加强高版V3.5_1991175069309448194
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Infinite+talk数字人动态加强高版V3.5_1991175069309448194.json
hash: f852f2bc0511470b
coverage: 0.714286
learned_at: 2026-10-11 02:57:36
nodes: [MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, Note, Note, Note, Note, Note, AudioSeparation, GetImageSizeAndCount, Note, WanVideoModelLoader, WanVideoTextEncode, WanVideoSampler, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, MultiTalkModelLoader, JWFloat, MultiTalkWav2VecEmbeds, WanVideoBlockSwap, JWInteger, WanVideoDecode, VHS_VideoCombine, VHS_VideoCombine, CR Prompt Text, LoadImage, LoadAudio, WanVideoLoraSelect, AudioCrop, JWInteger, DownloadAndLoadWav2VecModel]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, CR Prompt Text]
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Infinite+talk数字人动态加强高版V3.5_1991175069309448194.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Infinite+talk数字人动态加强高版V3.5_1991175069309448194.json`

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
- `GetImageSizeAndCount`
- `Note`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `JWFloat`
- `MultiTalkWav2VecEmbeds`
- `WanVideoBlockSwap`
- `JWInteger`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `LoadImage`
- `LoadAudio`
- `WanVideoLoraSelect`
- `AudioCrop`
- `JWInteger`
- `DownloadAndLoadWav2VecModel`

## 知识

覆盖率 **71%**（25/35）

**有卡**：`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`AudioSeparation`、`GetImageSizeAndCount`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`JWFloat`、`MultiTalkWav2VecEmbeds`、`WanVideoBlockSwap`、`JWInteger`、`WanVideoDecode`、`VHS_VideoCombine`、`LoadImage`、`LoadAudio`、`AudioCrop`、`DownloadAndLoadWav2VecModel`

**缺卡**（2）：`LayerUtility: ImageScaleByAspectRatio V2`、`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
