---
key: 视频生成/图生视频/【Wan2.1系列】AI视频lora特效之《360度旋转》_1917932584058425345.json
name: 【Wan2.1系列】AI视频lora特效之《360度旋转》_1917932584058425345.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1917932584058425345.json
hash: d519927f5fd3d81b
coverage: 0.894737
learned_at: 2026-10-15 22:29:40
nodes: [LoadWanVideoT5TextEncoder, WanVideoTeaCache, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoEnhanceAVideo, WanVideoDecode, WanVideoClipVisionEncode, WanVideoTorchCompileSettings, ImageResizeKJ, WanVideoModelLoader, WanVideoVAELoader, PreviewImage, CLIPVisionLoader, WanVideoTextEncode, LoadImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoLoraSelect, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/【Wan2.1系列】AI视频lora特效之《360度旋转》_1917932584058425345.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1917932584058425345.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（19 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoTeaCache`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoEnhanceAVideo`
- `WanVideoDecode`
- `WanVideoClipVisionEncode`
- `WanVideoTorchCompileSettings`
- `ImageResizeKJ`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `PreviewImage`
- `CLIPVisionLoader`
- `WanVideoTextEncode`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `MarkdownNote`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoTeaCache`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`WanVideoEnhanceAVideo`、`WanVideoDecode`、`WanVideoClipVisionEncode`、`WanVideoTorchCompileSettings`、`ImageResizeKJ`、`WanVideoModelLoader`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoTextEncode`、`LoadImage`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`WanVideoLoraSelect`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
