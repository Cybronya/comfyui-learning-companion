---
key: 视频生成/文生视频/KJ版 WAN2.1自动扩写文生视频加速高清放大补帧工作流-Starai_1894643330280763394.json
name: KJ版 WAN2.1自动扩写文生视频加速高清放大补帧工作流-Starai_1894643330280763394.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1894643330280763394.json
hash: 6b27ba7ad553c4f1
coverage: 0.885714
learned_at: 2026-10-15 22:43:20
nodes: [WanVideoSLG, WanVideoTeaCache, ImageUpscaleWithModel, easy cleanGpuUsed, FILM VFI, VHS_VideoCombine, WanVideoExperimentalArgs, LayerUtility: PurgeVRAM, Note Plus (mtb), Note, Int, Int, VHS_VideoCombine, ImageResizeKJ, WanVideoEmptyEmbeds, Note, WanVideoEnhanceAVideo, WanVideoTorchCompileSettings, easy cleanGpuUsed, UpscaleModelLoader, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoModelLoader, WanVideoBlockSwap, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoDecode, easy cleanGpuUsed, WanVideoSampler, Int, JjkText, WanVideoTextEncode, ShowText|pysssss, RHHiddenNodes, Int]
patterns: []
missing: []
---

# 视频生成/文生视频/KJ版 WAN2.1自动扩写文生视频加速高清放大补帧工作流-Starai_1894643330280763394.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1894643330280763394.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（35 个）：
- `WanVideoSLG`
- `WanVideoTeaCache`
- `ImageUpscaleWithModel`
- `easy cleanGpuUsed`
- `FILM VFI`
- `VHS_VideoCombine`
- `WanVideoExperimentalArgs`
- `LayerUtility: PurgeVRAM`
- `Note Plus (mtb)`
- `Note`
- `Int`
- `Int`
- `VHS_VideoCombine`
- `ImageResizeKJ`
- `WanVideoEmptyEmbeds`
- `Note`
- `WanVideoEnhanceAVideo`
- `WanVideoTorchCompileSettings`
- `easy cleanGpuUsed`
- `UpscaleModelLoader`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `Int`
- `JjkText`
- `WanVideoTextEncode`
- `ShowText|pysssss`
- `RHHiddenNodes`
- `Int`

## 知识

覆盖率 **89%**（31/35）

**有卡**：`WanVideoSLG`、`WanVideoTeaCache`、`ImageUpscaleWithModel`、`easy cleanGpuUsed`、`FILM VFI`、`VHS_VideoCombine`、`WanVideoExperimentalArgs`、`LayerUtility: PurgeVRAM`、`Note Plus (mtb)`、`Int`、`ImageResizeKJ`、`WanVideoEmptyEmbeds`、`WanVideoEnhanceAVideo`、`WanVideoTorchCompileSettings`、`UpscaleModelLoader`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoTextEncode`、`RHHiddenNodes`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、ImageUpscaleWithModel、UpscaleModelLoader、UpscaleModelLoader
