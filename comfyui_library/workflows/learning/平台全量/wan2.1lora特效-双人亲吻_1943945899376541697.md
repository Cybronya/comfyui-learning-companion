---
key: 平台全量/wan2.1lora特效-双人亲吻_1943945899376541697.json
name: wan2.1lora特效-双人亲吻_1943945899376541697
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.1lora特效-双人亲吻_1943945899376541697.json
hash: 1b05c2b179b2674b
coverage: 0.947368
learned_at: 2026-11-14 01:19:09
nodes: [WanVideoClipVisionEncode, WanVideoImageToVideoEncode, WanVideoExperimentalArgs, CLIPVisionLoader, ImageResize+, WanVideoTeaCache, PreviewImage, WanVideoBlockSwap, WanVideoSLG, WanVideoEnhanceAVideo, WanVideoSampler, WanVideoModelLoader, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoVAELoader, WanVideoLoraSelect, WanVideoTextEncode, LoadImage]
patterns: []
missing: []
---

# 平台全量/wan2.1lora特效-双人亲吻_1943945899376541697.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.1lora特效-双人亲吻_1943945899376541697.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（19 个）：
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoExperimentalArgs`
- `CLIPVisionLoader`
- `ImageResize+`
- `WanVideoTeaCache`
- `PreviewImage`
- `WanVideoBlockSwap`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `LoadImage`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`WanVideoExperimentalArgs`、`CLIPVisionLoader`、`ImageResize+`、`WanVideoTeaCache`、`WanVideoBlockSwap`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoSampler`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoClipVisionEncode、WanVideoDecode、WanVideoImageToVideoEncode、WanVideoTextEncode、WanVideoVAELoader
