---
key: 视频生成/图生视频/Wan2.1-VACE+FusionX-LORA图生视频_1935624058308317186.json
name: Wan2.1-VACE+FusionX-LORA图生视频_1935624058308317186.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1935624058308317186.json
hash: 9ee2b058b0c8601a
coverage: 1
learned_at: 2026-10-15 22:30:23
nodes: [WanVideoSLG, WanVideoEnhanceAVideo, Text Multiline, WanVideoTextEncode, WanVideoExperimentalArgs, WanVideoSampler, WanVideoVACEEncode, WanVideoTeaCache, WanVideoDecode, VHS_VideoCombine, ImageResizeKJv2, Primitive integer [Crystools], WanVideoBlockSwap, LoadImage, WanVideoModelLoader, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoVACEModelSelect, WanVideoLoraSelect, WanVideoVACEStartToEndFrame, Primitive integer [Crystools]]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1-VACE+FusionX-LORA图生视频_1935624058308317186.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1935624058308317186.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（21 个）：
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `Text Multiline`
- `WanVideoTextEncode`
- `WanVideoExperimentalArgs`
- `WanVideoSampler` ★核心
- `WanVideoVACEEncode`
- `WanVideoTeaCache`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `Primitive integer [Crystools]`
- `WanVideoBlockSwap`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVACEModelSelect`
- `WanVideoLoraSelect`
- `WanVideoVACEStartToEndFrame`
- `Primitive integer [Crystools]`

## 知识

覆盖率 **100%**（21/21）

**有卡**：`WanVideoSLG`、`WanVideoEnhanceAVideo`、`Text Multiline`、`WanVideoTextEncode`、`WanVideoExperimentalArgs`、`WanVideoSampler`、`WanVideoVACEEncode`、`WanVideoTeaCache`、`WanVideoDecode`、`VHS_VideoCombine`、`ImageResizeKJv2`、`Primitive integer [Crystools]`、`WanVideoBlockSwap`、`LoadImage`、`WanVideoModelLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVACEModelSelect`、`WanVideoLoraSelect`、`WanVideoVACEStartToEndFrame`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect
