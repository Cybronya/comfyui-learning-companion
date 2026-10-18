---
key: 视频生成/图生视频/Wan2.1 VACE双图参考改进版_1948588073054535682.json
name: Wan2.1 VACE双图参考改进版_1948588073054535682.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1 VACE双图参考改进版_1948588073054535682.json
hash: 452d29a119655c1e
coverage: 0.962963
learned_at: 2026-10-15 22:30:47
nodes: [WanVideoTorchCompileSettings, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoVAELoader, Primitive integer [Crystools], Primitive integer [Crystools], WanVideoModelLoader, Primitive integer [Crystools], WanVideoDecode, ColorMatch, WanVideoSampler, WanVideoVACEEncode, Primitive integer [Crystools], WanVideoTextEncode, ImageConcanate, ImageResizeKJ, WanVideoVACEModelSelect, WanVideoLoraSelect, LoadImage, LoadImage, PreviewImage, easy imageRemBg, ImageConcanate, VHS_VideoCombine, Note Plus (mtb), LoadImageFromUrl, Text Multiline]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1 VACE双图参考改进版_1948588073054535682.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1948588073054535682.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（27 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `WanVideoModelLoader`
- `Primitive integer [Crystools]`
- `WanVideoDecode`
- `ColorMatch`
- `WanVideoSampler` ★核心
- `WanVideoVACEEncode`
- `Primitive integer [Crystools]`
- `WanVideoTextEncode`
- `ImageConcanate`
- `ImageResizeKJ`
- `WanVideoVACEModelSelect`
- `WanVideoLoraSelect`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `easy imageRemBg`
- `ImageConcanate`
- `VHS_VideoCombine`
- `Note Plus (mtb)`
- `LoadImageFromUrl`
- `Text Multiline`

## 知识

覆盖率 **96%**（26/27）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`Primitive integer [Crystools]`、`WanVideoModelLoader`、`WanVideoDecode`、`ColorMatch`、`WanVideoSampler`、`WanVideoVACEEncode`、`WanVideoTextEncode`、`ImageConcanate`、`ImageResizeKJ`、`WanVideoVACEModelSelect`、`WanVideoLoraSelect`、`LoadImage`、`easy imageRemBg`、`VHS_VideoCombine`、`Note Plus (mtb)`、`LoadImageFromUrl`、`Text Multiline`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect
