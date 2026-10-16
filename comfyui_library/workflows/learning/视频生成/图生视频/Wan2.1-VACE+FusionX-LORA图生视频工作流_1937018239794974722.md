---
key: 视频生成/图生视频/Wan2.1-VACE+FusionX-LORA图生视频工作流_1937018239794974722.json
name: Wan2.1-VACE+FusionX-LORA图生视频工作流_1937018239794974722.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1937018239794974722.json
hash: cde549b869551ed6
coverage: 1
learned_at: 2026-10-15 22:30:27
nodes: [LoadImage, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoSLG, WanVideoEnhanceAVideo, WanVideoVACEEncode, WanVideoTeaCache, VHS_VideoCombine, WanVideoVAELoader, Text Multiline, WanVideoTextEncode, WanVideoDecode, WanVideoSampler, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoVACEModelSelect, WanVideoVACEStartToEndFrame, Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], ImageResizeKJv2, WanVideoModelLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1-VACE+FusionX-LORA图生视频工作流_1937018239794974722.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1937018239794974722.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（23 个）：
- `LoadImage`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `WanVideoVACEEncode`
- `WanVideoTeaCache`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `Text Multiline`
- `WanVideoTextEncode`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelect`
- `WanVideoVACEModelSelect`
- `WanVideoVACEStartToEndFrame`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `ImageResizeKJv2`
- `WanVideoModelLoader`

## 知识

覆盖率 **100%**（23/23）

**有卡**：`LoadImage`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoVACEEncode`、`WanVideoTeaCache`、`VHS_VideoCombine`、`WanVideoVAELoader`、`Text Multiline`、`WanVideoTextEncode`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoExperimentalArgs`、`WanVideoLoraSelect`、`WanVideoVACEModelSelect`、`WanVideoVACEStartToEndFrame`、`Primitive integer [Crystools]`、`ImageResizeKJv2`、`WanVideoModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect
