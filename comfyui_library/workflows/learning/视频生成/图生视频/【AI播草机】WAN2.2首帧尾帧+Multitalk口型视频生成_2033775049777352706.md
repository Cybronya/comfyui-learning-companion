---
key: 视频生成/图生视频/【AI播草机】WAN2.2首帧尾帧+Multitalk口型视频生成_2033775049777352706.json
name: 【AI播草机】WAN2.2首帧尾帧+Multitalk口型视频生成_2033775049777352706.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2033775049777352706.json
hash: 94c9ecc56fa8f9eb
coverage: 0.970588
learned_at: 2026-10-15 22:35:41
nodes: [DownloadAndLoadWav2VecModel, WanVideoModelLoader, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoDecode, easy cleanGpuUsed, WanVideoVAELoader, MultiTalkWav2VecEmbeds, easy cleanGpuUsed, easy cleanGpuUsed, BasicMath, WanVideoTextEncode, MultiTalkModelLoader, BasicMath, INTConstant, INTConstant, easy showAnything, ToFloat, ToInt, VHS_VideoCombine, INTConstant, INTConstant, WanVideoSampler, WanVideoSampler, LoadWanVideoT5TextEncoder, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, StringConcatenate, LoadImage, LoadImage, LoadAudio, FloatConstant, StringConcatenate]
patterns: []
missing: []
---

# 视频生成/图生视频/【AI播草机】WAN2.2首帧尾帧+Multitalk口型视频生成_2033775049777352706.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2033775049777352706.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（34 个）：
- `DownloadAndLoadWav2VecModel`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `WanVideoVAELoader`
- `MultiTalkWav2VecEmbeds`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `BasicMath`
- `WanVideoTextEncode`
- `MultiTalkModelLoader`
- `BasicMath`
- `INTConstant`
- `INTConstant`
- `easy showAnything`
- `ToFloat`
- `ToInt`
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `LoadWanVideoT5TextEncoder`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `StringConcatenate`
- `LoadImage`
- `LoadImage`
- `LoadAudio`
- `FloatConstant`
- `StringConcatenate`

## 知识

覆盖率 **97%**（33/34）

**有卡**：`DownloadAndLoadWav2VecModel`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`easy cleanGpuUsed`、`WanVideoVAELoader`、`MultiTalkWav2VecEmbeds`、`BasicMath`、`WanVideoTextEncode`、`MultiTalkModelLoader`、`INTConstant`、`ToFloat`、`ToInt`、`VHS_VideoCombine`、`WanVideoSampler`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`StringConcatenate`、`LoadImage`、`LoadAudio`、`FloatConstant`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
