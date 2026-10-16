---
key: 视频生成/图生视频/Wan2.1-FusionX-VACE图生视频加速工作流_1935618594950807553.json
name: Wan2.1-FusionX-VACE图生视频加速工作流_1935618594950807553.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1935618594950807553.json
hash: 98e8985d90d94133
coverage: 1
learned_at: 2026-10-15 22:30:23
nodes: [WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoModelLoader, WanVideoSLG, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoDecode, WanVideoSampler, VHS_VideoCombine, WanVideoVACEStartToEndFrame, WanVideoTextEncode, WanVideoVACEEncode, WanVideoTeaCache, Primitive integer [Crystools], Primitive integer [Crystools], ImageResizeKJv2, LoadImage, Text Multiline]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1-FusionX-VACE图生视频加速工作流_1935618594950807553.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1935618594950807553.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（19 个）：
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `WanVideoVACEStartToEndFrame`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoTeaCache`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `ImageResizeKJv2`
- `LoadImage`
- `Text Multiline`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoExperimentalArgs`、`WanVideoDecode`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoVACEStartToEndFrame`、`WanVideoTextEncode`、`WanVideoVACEEncode`、`WanVideoTeaCache`、`Primitive integer [Crystools]`、`ImageResizeKJv2`、`LoadImage`、`Text Multiline`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、ImageResizeKJv2
