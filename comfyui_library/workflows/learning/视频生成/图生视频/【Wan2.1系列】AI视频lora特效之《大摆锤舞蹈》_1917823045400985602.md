---
key: 视频生成/图生视频/【Wan2.1系列】AI视频lora特效之《大摆锤舞蹈》_1917823045400985602.json
name: 【Wan2.1系列】AI视频lora特效之《大摆锤舞蹈》_1917823045400985602.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1917823045400985602.json
hash: 4492a6e9077ac084
coverage: 0.894737
learned_at: 2026-10-15 22:29:40
nodes: [LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoImageToVideoEncode, WanVideoEnhanceAVideo, VHS_VideoCombine, WanVideoDecode, WanVideoClipVisionEncode, WanVideoTorchCompileSettings, ImageResizeKJ, WanVideoModelLoader, WanVideoVAELoader, PreviewImage, CLIPVisionLoader, WanVideoTeaCache, WanVideoSampler, LoadImage, WanVideoLoraSelect, WanVideoTextEncode, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/【Wan2.1系列】AI视频lora特效之《大摆锤舞蹈》_1917823045400985602.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1917823045400985602.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（19 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `WanVideoImageToVideoEncode`
- `WanVideoEnhanceAVideo`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoClipVisionEncode`
- `WanVideoTorchCompileSettings`
- `ImageResizeKJ`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `PreviewImage`
- `CLIPVisionLoader`
- `WanVideoTeaCache`
- `WanVideoSampler` ★核心
- `LoadImage`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `MarkdownNote`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`WanVideoImageToVideoEncode`、`WanVideoEnhanceAVideo`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoClipVisionEncode`、`WanVideoTorchCompileSettings`、`ImageResizeKJ`、`WanVideoModelLoader`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoTeaCache`、`WanVideoSampler`、`LoadImage`、`WanVideoLoraSelect`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
