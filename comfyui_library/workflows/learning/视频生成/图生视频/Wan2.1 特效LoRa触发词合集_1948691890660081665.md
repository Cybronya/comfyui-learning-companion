---
key: 视频生成/图生视频/Wan2.1 特效LoRa触发词合集_1948691890660081665.json
name: Wan2.1 特效LoRa触发词合集_1948691890660081665.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1948691890660081665.json
hash: 564ddc145ba8b292
coverage: 0.952381
learned_at: 2026-10-15 22:30:48
nodes: [WanVideoVRAMManagement, WanVideoTorchCompileSettings, LoadWanVideoT5TextEncoder, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoVAELoader, WanVideoModelLoader, WanVideoTextEncode, WanVideoDecode, WanVideoImageToVideoEncode, ImageResizeKJ, Note Plus (mtb), LoadImageFromUrl, LoadImage, WanVideoSampler, VHS_VideoCombine, WanVideoTeaCache, WanVideoEnhanceAVideo, WanVideoBlockSwap, WanVideoLoraSelect, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1 特效LoRa触发词合集_1948691890660081665.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1948691890660081665.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（21 个）：
- `WanVideoVRAMManagement`
- `WanVideoTorchCompileSettings`
- `LoadWanVideoT5TextEncoder`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `ImageResizeKJ`
- `Note Plus (mtb)`
- `LoadImageFromUrl`
- `LoadImage`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `WanVideoTeaCache`
- `WanVideoEnhanceAVideo`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `Note`

## 知识

覆盖率 **95%**（20/21）

**有卡**：`WanVideoVRAMManagement`、`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoDecode`、`WanVideoImageToVideoEncode`、`ImageResizeKJ`、`Note Plus (mtb)`、`LoadImageFromUrl`、`LoadImage`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoTeaCache`、`WanVideoEnhanceAVideo`、`WanVideoBlockSwap`、`WanVideoLoraSelect`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
