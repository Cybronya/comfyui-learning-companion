---
key: 视频生成/图生视频/【AI播草机】WAN2.2首帧+Multitalk口型视频生成_2033528799509352449.json
name: 【AI播草机】WAN2.2首帧+Multitalk口型视频生成_2033528799509352449.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【AI播草机】WAN2.2首帧+Multitalk口型视频生成_2033528799509352449.json
hash: cbe7230d498db51a
coverage: 0.971429
learned_at: 2026-10-15 22:35:40
nodes: [DownloadAndLoadWav2VecModel, StringConcatenate, WanVideoModelLoader, WanVideoModelLoader, WanVideoTorchCompileSettings, GetImageRangeFromBatch, WanVideoDecode, easy cleanGpuUsed, WanVideoVAELoader, MultiTalkWav2VecEmbeds, easy cleanGpuUsed, easy cleanGpuUsed, BasicMath, WanVideoTextEncode, MultiTalkModelLoader, WanVideoImageToVideoEncode, BasicMath, INTConstant, INTConstant, easy showAnything, ToFloat, ToInt, VHS_VideoCombine, INTConstant, INTConstant, SaveImage, WanVideoSampler, WanVideoSampler, LoadWanVideoT5TextEncoder, CLIPVisionLoader, WanVideoClipVisionEncode, LoadImage, FloatConstant, StringConcatenate, LoadAudio]
patterns: []
missing: []
---

# 视频生成/图生视频/【AI播草机】WAN2.2首帧+Multitalk口型视频生成_2033528799509352449.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2033528799509352449.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（35 个）：
- `DownloadAndLoadWav2VecModel`
- `StringConcatenate`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `GetImageRangeFromBatch`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `WanVideoVAELoader`
- `MultiTalkWav2VecEmbeds`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `BasicMath`
- `WanVideoTextEncode`
- `MultiTalkModelLoader`
- `WanVideoImageToVideoEncode`
- `BasicMath`
- `INTConstant`
- `INTConstant`
- `easy showAnything`
- `ToFloat`
- `ToInt`
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `SaveImage`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `LoadWanVideoT5TextEncoder`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `LoadImage`
- `FloatConstant`
- `StringConcatenate`
- `LoadAudio`

## 知识

覆盖率 **97%**（34/35）

**有卡**：`DownloadAndLoadWav2VecModel`、`StringConcatenate`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`GetImageRangeFromBatch`、`WanVideoDecode`、`easy cleanGpuUsed`、`WanVideoVAELoader`、`MultiTalkWav2VecEmbeds`、`BasicMath`、`WanVideoTextEncode`、`MultiTalkModelLoader`、`WanVideoImageToVideoEncode`、`INTConstant`、`ToFloat`、`ToInt`、`VHS_VideoCombine`、`SaveImage`、`WanVideoSampler`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`LoadImage`、`FloatConstant`、`LoadAudio`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
