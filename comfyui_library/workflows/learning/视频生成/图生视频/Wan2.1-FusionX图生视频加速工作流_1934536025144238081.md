---
key: 视频生成/图生视频/Wan2.1-FusionX图生视频加速工作流_1934536025144238081.json
name: Wan2.1-FusionX图生视频加速工作流_1934536025144238081.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1-FusionX图生视频加速工作流_1934536025144238081.json
hash: 95ff9c0d1bcd84b1
coverage: 1
learned_at: 2026-10-15 22:30:17
nodes: [WanVideoBlockSwap, CLIPVisionLoader, LoadWanVideoT5TextEncoder, WanVideoClipVisionEncode, WanVideoSLG, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoExperimentalArgs, WanVideoTeaCache, WanVideoTextEncode, WanVideoSampler, WanVideoDecode, VHS_VideoCombine, Primitive integer [Crystools], Text Multiline, WanVideoModelLoader, LoadImage, WanVideoVAELoader, ImageResizeKJv2, Primitive integer [Crystools]]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1-FusionX图生视频加速工作流_1934536025144238081.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1934536025144238081.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（20 个）：
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoClipVisionEncode`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoExperimentalArgs`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `Primitive integer [Crystools]`
- `Text Multiline`
- `WanVideoModelLoader`
- `LoadImage`
- `WanVideoVAELoader`
- `ImageResizeKJv2`
- `Primitive integer [Crystools]`

## 知识

覆盖率 **100%**（20/20）

**有卡**：`WanVideoBlockSwap`、`CLIPVisionLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoClipVisionEncode`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoImageToVideoEncode`、`WanVideoExperimentalArgs`、`WanVideoTeaCache`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoDecode`、`VHS_VideoCombine`、`Primitive integer [Crystools]`、`Text Multiline`、`WanVideoModelLoader`、`LoadImage`、`WanVideoVAELoader`、`ImageResizeKJv2`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
