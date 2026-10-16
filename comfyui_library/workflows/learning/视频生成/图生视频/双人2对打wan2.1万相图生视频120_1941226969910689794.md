---
key: 视频生成/图生视频/双人2对打wan2.1万相图生视频120_1941226969910689794.json
name: 双人2对打wan2.1万相图生视频120_1941226969910689794.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1941226969910689794.json
hash: a2e84f352c89e911
coverage: 0.916667
learned_at: 2026-10-15 22:30:35
nodes: [WanVideoExperimentalArgs, easy cleanGpuUsed, WanVideoModelLoader, WanVideoDecode, easy cleanGpuUsed, LayerUtility: PurgeVRAM, VHS_VideoCombine, LayerUtility: PurgeVRAM, Fast Groups Bypasser (rgthree), VHS_VideoCombine, LayerUtility: PurgeVRAM, WanVideoTorchCompileSettings, LoadImage, LoadWanVideoT5TextEncoder, LoadWanVideoClipTextEncoder, WanVideoVAELoader, WanVideoLoraSelect, Note, WanVideoTextEncode, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoBlockSwap, WanVideoSampler, WanVideoImageClipEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/双人2对打wan2.1万相图生视频120_1941226969910689794.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1941226969910689794.json`

## 结构

**生成流程**：Model → Condition → Sampling → Other

**节点**（24 个）：
- `WanVideoExperimentalArgs`
- `easy cleanGpuUsed`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM`
- `WanVideoTorchCompileSettings`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `Note`
- `WanVideoTextEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoImageClipEncode`

## 知识

覆盖率 **92%**（22/24）

**有卡**：`WanVideoExperimentalArgs`、`easy cleanGpuUsed`、`WanVideoModelLoader`、`WanVideoDecode`、`LayerUtility: PurgeVRAM`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`LoadImage`、`LoadWanVideoT5TextEncoder`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`WanVideoBlockSwap`、`WanVideoSampler`、`WanVideoImageClipEncode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
