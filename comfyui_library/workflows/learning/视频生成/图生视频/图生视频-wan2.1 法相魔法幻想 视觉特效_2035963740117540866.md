---
key: 视频生成/图生视频/图生视频-wan2.1 法相魔法幻想 视觉特效_2035963740117540866.json
name: 图生视频-wan2.1 法相魔法幻想 视觉特效_2035963740117540866.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2035963740117540866.json
hash: b9233e0fa12ae77a
coverage: 1
learned_at: 2026-10-15 22:35:50
nodes: [LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoBlockSwap, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoTorchCompileSettings, Primitive integer [Crystools], Primitive integer [Crystools], CLIPVisionLoader, WanVideoClipVisionEncode, ImageResizeKJ, WanVideoTextEncode, WanVideoTeaCache, WanVideoEnhanceAVideo, WanVideoSampler, WanVideoImageToVideoEncode, WanVideoDecode, VHS_VideoCombine, WanVideoLoraSelect, Text Multiline, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/图生视频-wan2.1 法相魔法幻想 视觉特效_2035963740117540866.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2035963740117540866.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（21 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `WanVideoTorchCompileSettings`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
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
- `WanVideoLoraSelect`
- `Text Multiline`
- `LoadImage`

## 知识

覆盖率 **100%**（21/21）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`WanVideoTorchCompileSettings`、`Primitive integer [Crystools]`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`ImageResizeKJ`、`WanVideoTextEncode`、`WanVideoTeaCache`、`WanVideoEnhanceAVideo`、`WanVideoSampler`、`WanVideoImageToVideoEncode`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`Text Multiline`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
