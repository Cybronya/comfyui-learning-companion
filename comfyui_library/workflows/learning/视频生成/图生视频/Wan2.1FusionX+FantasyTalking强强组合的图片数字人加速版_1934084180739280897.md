---
key: 视频生成/图生视频/Wan2.1FusionX+FantasyTalking强强组合的图片数字人加速版_1934084180739280897.json
name: Wan2.1FusionX+FantasyTalking强强组合的图片数字人加速版_1934084180739280897.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1FusionX+FantasyTalking强强组合的图片数字人加速版_1934084180739280897.json
hash: 48ada989a373fb61
coverage: 1
learned_at: 2026-10-15 22:30:16
nodes: [WanVideoDecode, WanVideoTextEncode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoBlockSwap, FantasyTalkingModelLoader, DownloadAndLoadWav2VecModel, ImageResizeKJ, WanVideoClipVisionEncode, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoContextOptions, FantasyTalkingWav2VecEmbeds, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoTeaCache, VHS_VideoCombine, LoadImage, CLIPVisionLoader, SeargeFloatConstant, LoadAudio, INTConstant]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1FusionX+FantasyTalking强强组合的图片数字人加速版_1934084180739280897.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1934084180739280897.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（22 个）：
- `WanVideoDecode`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `FantasyTalkingModelLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJ`
- `WanVideoClipVisionEncode`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoContextOptions`
- `FantasyTalkingWav2VecEmbeds`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoTeaCache`
- `VHS_VideoCombine`
- `LoadImage`
- `CLIPVisionLoader`
- `SeargeFloatConstant`
- `LoadAudio`
- `INTConstant`

## 知识

覆盖率 **100%**（22/22）

**有卡**：`WanVideoDecode`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`FantasyTalkingModelLoader`、`DownloadAndLoadWav2VecModel`、`ImageResizeKJ`、`WanVideoClipVisionEncode`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoContextOptions`、`FantasyTalkingWav2VecEmbeds`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`WanVideoTeaCache`、`VHS_VideoCombine`、`LoadImage`、`CLIPVisionLoader`、`SeargeFloatConstant`、`LoadAudio`、`INTConstant`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
