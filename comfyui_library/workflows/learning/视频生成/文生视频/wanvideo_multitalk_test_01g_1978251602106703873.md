---
key: 视频生成/文生视频/wanvideo_multitalk_test_01g_1978251602106703873.json
name: wanvideo_multitalk_test_01g_1978251602106703873
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wanvideo_multitalk_test_01g_1978251602106703873.json
hash: 447607b3ecb91077
coverage: 0.933333
learned_at: 2026-10-10 23:09:59
nodes: [WanVideoDecode, CreateCFGScheduleFloatList, WanVideoSampler, WanVideoImageToVideoEncode, WanVideoModelLoader, VHS_DuplicateImages, WanVideoVAELoader, CLIPVisionLoader, WanVideoContextOptions, WanVideoLoraSelect, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoClipVisionEncode, MultiTalkModelLoader, WanVideoEncode, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, MultiTalkWav2VecEmbeds, DownloadAndLoadWav2VecModel, LoadWanVideoT5TextEncoder, AudioCrop, VHS_VideoCombine, AudioSeparation, Note, INTConstant, WanVideoTextEncode, LoadAudio, LoadImage, ImageResizeKJv2, Note]
patterns: []
missing: []
---

# 视频生成/文生视频/wanvideo_multitalk_test_01g_1978251602106703873.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wanvideo_multitalk_test_01g_1978251602106703873.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（30 个）：
- `WanVideoDecode`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `VHS_DuplicateImages`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `WanVideoContextOptions`
- `WanVideoLoraSelect`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `MultiTalkModelLoader`
- `WanVideoEncode`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `MultiTalkWav2VecEmbeds`
- `DownloadAndLoadWav2VecModel`
- `LoadWanVideoT5TextEncoder`
- `AudioCrop`
- `VHS_VideoCombine`
- `AudioSeparation`
- `Note`
- `INTConstant`
- `WanVideoTextEncode`
- `LoadAudio`
- `LoadImage`
- `ImageResizeKJv2`
- `Note`

## 知识

覆盖率 **93%**（28/30）

**有卡**：`WanVideoDecode`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`WanVideoImageToVideoEncode`、`WanVideoModelLoader`、`VHS_DuplicateImages`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoContextOptions`、`WanVideoLoraSelect`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoClipVisionEncode`、`MultiTalkModelLoader`、`WanVideoEncode`、`WanVideoUni3C_ControlnetLoader`、`WanVideoUni3C_embeds`、`MultiTalkWav2VecEmbeds`、`DownloadAndLoadWav2VecModel`、`LoadWanVideoT5TextEncoder`、`AudioCrop`、`VHS_VideoCombine`、`AudioSeparation`、`INTConstant`、`WanVideoTextEncode`、`LoadAudio`、`LoadImage`、`ImageResizeKJv2`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
