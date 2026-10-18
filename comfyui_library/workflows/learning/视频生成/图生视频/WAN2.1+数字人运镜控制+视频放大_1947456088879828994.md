---
key: 视频生成/图生视频/WAN2.1+数字人运镜控制+视频放大_1947456088879828994.json
name: WAN2.1+数字人运镜控制+视频放大_1947456088879828994.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.1+数字人运镜控制+视频放大_1947456088879828994.json
hash: dbb7472af39de4d2
coverage: 0.942857
learned_at: 2026-10-15 22:30:45
nodes: [WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoLoraSelect, MultiTalkModelLoader, WanVideoModelLoader, WanVideoVAELoader, CLIPVisionLoader, WanVideoClipVisionEncode, Reroute, WanVideoContextOptions, MultiTalkWav2VecEmbeds, DownloadAndLoadWav2VecModel, AudioSeparation, WanVideoTextEncode, AudioCrop, ImageResizeKJv2, WanVideoSampler, LoadAudio, PT_KeyframeCamera, RepeatImageBatch, INTConstant, PreviewImage, WanVideoImageToVideoEncode, LoadWanVideoT5TextEncoder, ImageUpscaleWithModel, RIFE VFI, UpscaleModelLoader, WanVideoDecode, VHS_VideoCombine, WanVideoEncode, WanVideoUni3C_embeds, WanVideoUni3C_ControlnetLoader, LoadImage, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.1+数字人运镜控制+视频放大_1947456088879828994.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1947456088879828994.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（35 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `Reroute`
- `WanVideoContextOptions`
- `MultiTalkWav2VecEmbeds`
- `DownloadAndLoadWav2VecModel`
- `AudioSeparation`
- `WanVideoTextEncode`
- `AudioCrop`
- `ImageResizeKJv2`
- `WanVideoSampler` ★核心
- `LoadAudio`
- `PT_KeyframeCamera`
- `RepeatImageBatch`
- `INTConstant`
- `PreviewImage`
- `WanVideoImageToVideoEncode`
- `LoadWanVideoT5TextEncoder`
- `ImageUpscaleWithModel`
- `RIFE VFI`
- `UpscaleModelLoader`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoEncode`
- `WanVideoUni3C_embeds`
- `WanVideoUni3C_ControlnetLoader`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **94%**（33/35）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`WanVideoModelLoader`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoContextOptions`、`MultiTalkWav2VecEmbeds`、`DownloadAndLoadWav2VecModel`、`AudioSeparation`、`WanVideoTextEncode`、`AudioCrop`、`ImageResizeKJv2`、`WanVideoSampler`、`LoadAudio`、`PT_KeyframeCamera`、`RepeatImageBatch`、`INTConstant`、`WanVideoImageToVideoEncode`、`LoadWanVideoT5TextEncoder`、`ImageUpscaleWithModel`、`RIFE VFI`、`UpscaleModelLoader`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoEncode`、`WanVideoUni3C_embeds`、`WanVideoUni3C_ControlnetLoader`、`LoadImage`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
