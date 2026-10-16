---
key: 视频生成/图生视频/wan2.1 法相魔法幻想 视觉特效_2062016628551933953.json
name: wan2.1 法相魔法幻想 视觉特效_2062016628551933953.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2062016628551933953.json
hash: 4d312e6c841edf2b
coverage: 0.956522
learned_at: 2026-10-15 22:38:59
nodes: [LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoBlockSwap, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoTorchCompileSettings, Primitive integer [Crystools], Primitive integer [Crystools], CLIPVisionLoader, WanVideoClipVisionEncode, ImageResizeKJ, WanVideoTextEncode, WanVideoTeaCache, WanVideoEnhanceAVideo, WanVideoSampler, WanVideoImageToVideoEncode, WanVideoDecode, VHS_VideoCombine, WanVideoLoraSelect, Text Multiline, LoadImage, MarkdownNote, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1 法相魔法幻想 视觉特效_2062016628551933953.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2062016628551933953.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（23 个）：
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
- `MarkdownNote`
- `LoadImage`

## 知识

覆盖率 **96%**（22/23）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`WanVideoTorchCompileSettings`、`Primitive integer [Crystools]`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`ImageResizeKJ`、`WanVideoTextEncode`、`WanVideoTeaCache`、`WanVideoEnhanceAVideo`、`WanVideoSampler`、`WanVideoImageToVideoEncode`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`Text Multiline`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
