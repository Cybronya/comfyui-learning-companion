---
key: 视频生成/图生视频/wan2.1万相图生视拔刀特效lora_1920904820126060546.json
name: wan2.1万相图生视拔刀特效lora_1920904820126060546.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1920904820126060546.json
hash: a90b321473d332e7
coverage: 0.894737
learned_at: 2026-10-15 22:29:43
nodes: [WanVideoDecode, LayerUtility: PurgeVRAM, WanVideoTeaCache, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoBlockSwap, WanVideoEnhanceAVideo, VHS_VideoCombine, VHS_VideoCombine, Note, WanVideoSampler, WanVideoModelLoader, LoadWanVideoClipTextEncoder, Note, LoadImage, ImageResizeKJ, WanVideoImageClipEncode, WanVideoTextEncode, WanVideoLoraSelect]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1万相图生视拔刀特效lora_1920904820126060546.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1920904820126060546.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（19 个）：
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM`
- `WanVideoTeaCache`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoEnhanceAVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Note`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `Note`
- `LoadImage`
- `ImageResizeKJ`
- `WanVideoImageClipEncode`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`WanVideoDecode`、`LayerUtility: PurgeVRAM`、`WanVideoTeaCache`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoEnhanceAVideo`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoModelLoader`、`LoadWanVideoClipTextEncoder`、`LoadImage`、`ImageResizeKJ`、`WanVideoImageClipEncode`、`WanVideoTextEncode`、`WanVideoLoraSelect`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
