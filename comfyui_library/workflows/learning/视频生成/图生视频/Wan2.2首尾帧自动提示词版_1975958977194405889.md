---
key: 视频生成/图生视频/Wan2.2首尾帧自动提示词版_1975958977194405889.json
name: Wan2.2首尾帧自动提示词版_1975958977194405889.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2首尾帧自动提示词版_1975958977194405889.json
hash: 0d9524a59c33dde0
coverage: 0.875
learned_at: 2026-10-15 22:32:10
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, LoadImage, WanVideoModelLoader, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, WanVideoTorchCompileSettings, WanVideoLoraSelect, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, easy cleanGpuUsed, WanVideoTextEncode, WanVideoSetLoRAs, WanVideoSetBlockSwap, GetImageSizeAndCount, PrimitiveInt, PrimitiveInt, PrimitiveInt, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSampler, ImageResizeKJv2, ImageResizeKJv2, VHS_VideoCombine, WanVideoSampler, VHS_VideoCombine, ImageBatchMultiple+, SimpleMath+, AILab_MiniCPM_4_V_Advanced, ShowText|pysssss, LoadImage, LoadImage, CLIPVisionLoader, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2首尾帧自动提示词版_1975958977194405889.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1975958977194405889.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（40 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoClipVisionEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `easy cleanGpuUsed`
- `WanVideoTextEncode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `GetImageSizeAndCount`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `ImageBatchMultiple+`
- `SimpleMath+`
- `AILab_MiniCPM_4_V_Advanced`
- `ShowText|pysssss`
- `LoadImage`
- `LoadImage`
- `CLIPVisionLoader`
- `MarkdownNote`

## 知识

覆盖率 **88%**（35/40）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`easy cleanGpuUsed`、`LoadImage`、`WanVideoModelLoader`、`WanVideoDecode`、`WanVideoImageToVideoEncode`、`WanVideoClipVisionEncode`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoSampler`、`ImageResizeKJv2`、`VHS_VideoCombine`、`ImageBatchMultiple+`、`SimpleMath+`、`AILab_MiniCPM_4_V_Advanced`、`CLIPVisionLoader`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
