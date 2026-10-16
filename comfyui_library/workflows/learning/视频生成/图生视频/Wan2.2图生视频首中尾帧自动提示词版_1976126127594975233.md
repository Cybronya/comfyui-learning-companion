---
key: 视频生成/图生视频/Wan2.2图生视频首中尾帧自动提示词版_1976126127594975233.json
name: Wan2.2图生视频首中尾帧自动提示词版_1976126127594975233.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1976126127594975233.json
hash: 7abc3feb21376324
coverage: 0.886364
learned_at: 2026-10-15 22:32:10
nodes: [WanVideoSetLoRAs, WanVideoVAELoader, easy cleanGpuUsed, easy cleanGpuUsed, LoadImage, WanVideoImageToVideoEncode, LoadWanVideoT5TextEncoder, easy cleanGpuUsed, WanVideoModelLoader, WanVideoTextEncode, LoadImage, PrimitiveInt, PrimitiveInt, LoadImage, easy cleanGpuUsed, WanVideoClipVisionEncode, ImageResizeKJv2, ImageResizeKJv2, WanVideoEncodeLatentBatch, WanVideoDecode, GetImageSizeAndCount, easy cleanGpuUsed, ImageBatchMultiple+, ShowText|pysssss, WanVideoContextOptions, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSampler, CLIPVisionLoader, VHS_VideoCombine, VHS_VideoCombine, PrimitiveInt, WanVideoSampler, AILab_MiniCPM_4_V_Advanced, ImageResizeKJv2, SimpleMath+, WanVideoTorchCompileSettings, LoadImage, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2图生视频首中尾帧自动提示词版_1976126127594975233.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1976126127594975233.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（44 个）：
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LoadImage`
- `WanVideoImageToVideoEncode`
- `LoadWanVideoT5TextEncoder`
- `easy cleanGpuUsed`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`
- `easy cleanGpuUsed`
- `WanVideoClipVisionEncode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `WanVideoEncodeLatentBatch`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `easy cleanGpuUsed`
- `ImageBatchMultiple+`
- `ShowText|pysssss`
- `WanVideoContextOptions`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `CLIPVisionLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `WanVideoSampler` ★核心
- `AILab_MiniCPM_4_V_Advanced`
- `ImageResizeKJv2`
- `SimpleMath+`
- `WanVideoTorchCompileSettings`
- `LoadImage`
- `MarkdownNote`

## 知识

覆盖率 **89%**（39/44）

**有卡**：`WanVideoSetLoRAs`、`WanVideoVAELoader`、`easy cleanGpuUsed`、`LoadImage`、`WanVideoImageToVideoEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoClipVisionEncode`、`ImageResizeKJv2`、`WanVideoEncodeLatentBatch`、`WanVideoDecode`、`GetImageSizeAndCount`、`ImageBatchMultiple+`、`WanVideoContextOptions`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoSampler`、`CLIPVisionLoader`、`VHS_VideoCombine`、`AILab_MiniCPM_4_V_Advanced`、`SimpleMath+`、`WanVideoTorchCompileSettings`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
