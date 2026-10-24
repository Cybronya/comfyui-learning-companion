---
key: 图片生成/图生图/Wanvideo_Multitalk_Kijai_1936153809884205058.json
name: Wanvideo_Multitalk_Kijai_1936153809884205058
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wanvideo_Multitalk_Kijai_1936153809884205058.json
hash: 34c6a9e89356d99f
coverage: 1
learned_at: 2026-10-23 11:28:28
nodes: [CreateCFGScheduleFloatList, AudioSeparation, WanVideoTorchCompileSettings, CLIPVisionLoader, AudioCrop, MultiTalkModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoBlockSwap, LoadAudio, WanVideoClipVisionEncode, DownloadAndLoadWav2VecModel, WanVideoSampler, WanVideoContextOptions, WanVideoVAELoader, WanVideoDecode, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoEncode, VHS_DuplicateImages, LoadWanVideoT5TextEncoder, INTConstant, WanVideoTextEncode, WanVideoImageToVideoEncode, LoadImage, VHS_VideoCombine, ImageResizeKJv2, MultiTalkWav2VecEmbeds]
patterns: []
missing: []
---

# 图片生成/图生图/Wanvideo_Multitalk_Kijai_1936153809884205058.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wanvideo_Multitalk_Kijai_1936153809884205058.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（28 个）：
- `CreateCFGScheduleFloatList`
- `AudioSeparation`
- `WanVideoTorchCompileSettings`
- `CLIPVisionLoader`
- `AudioCrop`
- `MultiTalkModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `LoadAudio`
- `WanVideoClipVisionEncode`
- `DownloadAndLoadWav2VecModel`
- `WanVideoSampler` ★核心
- `WanVideoContextOptions`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoEncode`
- `VHS_DuplicateImages`
- `LoadWanVideoT5TextEncoder`
- `INTConstant`
- `WanVideoTextEncode`
- `WanVideoImageToVideoEncode`
- `LoadImage`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `MultiTalkWav2VecEmbeds`

## 知识

覆盖率 **100%**（28/28）

**有卡**：`CreateCFGScheduleFloatList`、`AudioSeparation`、`WanVideoTorchCompileSettings`、`CLIPVisionLoader`、`AudioCrop`、`MultiTalkModelLoader`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`LoadAudio`、`WanVideoClipVisionEncode`、`DownloadAndLoadWav2VecModel`、`WanVideoSampler`、`WanVideoContextOptions`、`WanVideoVAELoader`、`WanVideoDecode`、`WanVideoUni3C_ControlnetLoader`、`WanVideoUni3C_embeds`、`WanVideoEncode`、`VHS_DuplicateImages`、`LoadWanVideoT5TextEncoder`、`INTConstant`、`WanVideoTextEncode`、`WanVideoImageToVideoEncode`、`LoadImage`、`VHS_VideoCombine`、`ImageResizeKJv2`、`MultiTalkWav2VecEmbeds`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
