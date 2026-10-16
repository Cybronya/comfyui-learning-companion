---
key: 视频生成/文生视频/wan2.1 水下潜水动画_1937316067234758658.json
name: wan2.1 水下潜水动画_1937316067234758658.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1937316067234758658.json
hash: 845843fe98d88393
coverage: 1
learned_at: 2026-10-15 22:43:29
nodes: [LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoBlockSwap, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoTorchCompileSettings, CLIPVisionLoader, WanVideoClipVisionEncode, ImageResizeKJ, WanVideoTextEncode, WanVideoTeaCache, WanVideoEnhanceAVideo, WanVideoSampler, WanVideoImageToVideoEncode, WanVideoDecode, VHS_VideoCombine, Primitive integer [Crystools], Primitive integer [Crystools], WanVideoLoraSelect, LoadImage, Text Multiline]
patterns: []
missing: []
---

# 视频生成/文生视频/wan2.1 水下潜水动画_1937316067234758658.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1937316067234758658.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（21 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `WanVideoTorchCompileSettings`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `ImageResizeKJ`
- `WanVideoTextEncode`
- `WanVideoTeaCache`
- `WanVideoEnhanceAVideo`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoEncode`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `WanVideoLoraSelect`
- `LoadImage`
- `Text Multiline`

## 知识

覆盖率 **100%**（21/21）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`WanVideoTorchCompileSettings`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`ImageResizeKJ`、`WanVideoTextEncode`、`WanVideoTeaCache`、`WanVideoEnhanceAVideo`、`WanVideoSampler`、`WanVideoImageToVideoEncode`、`WanVideoDecode`、`VHS_VideoCombine`、`Primitive integer [Crystools]`、`WanVideoLoraSelect`、`LoadImage`、`Text Multiline`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
