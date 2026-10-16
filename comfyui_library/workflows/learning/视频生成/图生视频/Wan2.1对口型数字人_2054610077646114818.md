---
key: 视频生成/图生视频/Wan2.1对口型数字人_2054610077646114818.json
name: Wan2.1对口型数字人_2054610077646114818.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2054610077646114818.json
hash: 385b012ca192cbe9
coverage: 0.958333
learned_at: 2026-10-15 22:37:50
nodes: [VHS_VideoCombine, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoDecode, WanVideoSampler, GetImageSizeAndCount, WanVideoClipVisionEncode, WanVideoImageToVideoMultiTalk, PreviewAny, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoTextEncodeCached, DownloadAndLoadWav2VecModel, MultiTalkWav2VecEmbeds, AudioSeparation, JWInteger, JWInteger, WanVideoVAELoader, CLIPVisionLoader, MultiTalkModelLoader, LoadImage, LoadAudio, ImageResizeKJv2, AudioCrop]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1对口型数字人_2054610077646114818.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2054610077646114818.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（24 个）：
- `VHS_VideoCombine`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `GetImageSizeAndCount`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoMultiTalk`
- `PreviewAny`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoTextEncodeCached`
- `DownloadAndLoadWav2VecModel`
- `MultiTalkWav2VecEmbeds`
- `AudioSeparation`
- `JWInteger`
- `JWInteger`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `MultiTalkModelLoader`
- `LoadImage`
- `LoadAudio`
- `ImageResizeKJv2`
- `AudioCrop`

## 知识

覆盖率 **96%**（23/24）

**有卡**：`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoDecode`、`WanVideoSampler`、`GetImageSizeAndCount`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoMultiTalk`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoTextEncodeCached`、`DownloadAndLoadWav2VecModel`、`MultiTalkWav2VecEmbeds`、`AudioSeparation`、`JWInteger`、`WanVideoVAELoader`、`CLIPVisionLoader`、`MultiTalkModelLoader`、`LoadImage`、`LoadAudio`、`ImageResizeKJv2`、`AudioCrop`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、CLIPVisionLoader
