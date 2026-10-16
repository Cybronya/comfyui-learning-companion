---
key: 视频生成/图生视频/极速图生视频工作流(self-forcing-cfg-step-distill)_1935517569509937153.json
name: 极速图生视频工作流(self-forcing-cfg-step-distill)_1935517569509937153.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1935517569509937153.json
hash: 3d211efb30f867f2
coverage: 0.709677
learned_at: 2026-10-15 22:30:22
nodes: [WanVideoTextEmbedBridge, CLIPTextEncode, CLIPLoader, CLIPTextEncode, Note, Note, Note, Note, Note, Note, WanVideoEnhanceAVideo, VHS_VideoCombine, WanVideoDecode, WanVideoClipVisionEncode, WanVideoBlockSwap, Note, LoadImage, WanVideoTorchCompileSettings, WanVideoTeaCache, WanVideoVRAMManagement, Note, ImageResizeKJ, WanVideoLoraSelect, LoadWanVideoClipTextEncoder, WanVideoModelLoader, MarkdownNote, WanVideoSampler, WanVideoTextEncode, WanVideoImageToVideoEncode, WanVideoVAELoader, LoadWanVideoT5TextEncoder]
patterns: []
missing: []
---

# 视频生成/图生视频/极速图生视频工作流(self-forcing-cfg-step-distill)_1935517569509937153.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1935517569509937153.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（31 个）：
- `WanVideoTextEmbedBridge`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `WanVideoEnhanceAVideo`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoClipVisionEncode`
- `WanVideoBlockSwap`
- `Note`
- `LoadImage`
- `WanVideoTorchCompileSettings`
- `WanVideoTeaCache`
- `WanVideoVRAMManagement`
- `Note`
- `ImageResizeKJ`
- `WanVideoLoraSelect`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoModelLoader`
- `MarkdownNote`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`

## 知识

覆盖率 **71%**（22/31）

**有卡**：`WanVideoTextEmbedBridge`、`CLIPTextEncode`、`CLIPLoader`、`WanVideoEnhanceAVideo`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoClipVisionEncode`、`WanVideoBlockSwap`、`LoadImage`、`WanVideoTorchCompileSettings`、`WanVideoTeaCache`、`WanVideoVRAMManagement`、`ImageResizeKJ`、`WanVideoLoraSelect`、`LoadWanVideoClipTextEncoder`、`WanVideoModelLoader`、`WanVideoSampler`、`WanVideoTextEncode`、`WanVideoImageToVideoEncode`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`

**用到的条目**：CLIPTextEncode、CLIPLoader、LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
