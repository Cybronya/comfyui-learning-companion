---
key: 视频生成/图生视频/Wan2.2图生视频自动添加音效_1974129823239024642.json
name: Wan2.2图生视频自动添加音效_1974129823239024642.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2图生视频自动添加音效_1974129823239024642.json
hash: 9aedb8511b0e8007
coverage: 0.875
learned_at: 2026-10-15 22:32:04
nodes: [WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader, WanVideoTorchCompileSettings, WanVideoTextEncode, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoSetLoRAs, WanVideoSetBlockSwap, ImageResizeKJv2, WanVideoBlockSwap, CLIPVisionLoader, easy cleanGpuUsed, WanVideoSampler, WanVideoSampler, LoadImage, CR Text, WanVideoClipVisionEncode, PrimitiveInt, GetImageSizeAndCount, HunyuanVideoFoley, AILab_MiniCPM_4_V_Advanced, ShowText|pysssss, SimpleMath+, VHS_VideoCombine, VHS_VideoCombine, LoadImage, PrimitiveInt, PrimitiveInt, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2图生视频自动添加音效_1974129823239024642.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1974129823239024642.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（40 个）：
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `WanVideoTorchCompileSettings`
- `WanVideoTextEncode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `ImageResizeKJv2`
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `LoadImage`
- `CR Text`
- `WanVideoClipVisionEncode`
- `PrimitiveInt`
- `GetImageSizeAndCount`
- `HunyuanVideoFoley`
- `AILab_MiniCPM_4_V_Advanced`
- `ShowText|pysssss`
- `SimpleMath+`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `MarkdownNote`

## 知识

覆盖率 **88%**（35/40）

**有卡**：`WanVideoLoraSelect`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoTextEncode`、`easy cleanGpuUsed`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`WanVideoImageToVideoEncode`、`ImageResizeKJv2`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoSampler`、`LoadImage`、`CR Text`、`WanVideoClipVisionEncode`、`GetImageSizeAndCount`、`HunyuanVideoFoley`、`AILab_MiniCPM_4_V_Advanced`、`SimpleMath+`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
