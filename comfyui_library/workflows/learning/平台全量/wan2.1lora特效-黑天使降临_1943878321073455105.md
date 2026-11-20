---
key: 平台全量/wan2.1lora特效-黑天使降临_1943878321073455105.json
name: wan2.1lora特效-黑天使降临_1943878321073455105
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.1lora特效-黑天使降临_1943878321073455105.json
hash: 16518095bee2fa1d
coverage: 0.947368
learned_at: 2026-11-14 01:19:11
nodes: [WanVideoClipVisionEncode, WanVideoImageToVideoEncode, WanVideoExperimentalArgs, CLIPVisionLoader, ImageResize+, WanVideoTeaCache, PreviewImage, WanVideoBlockSwap, WanVideoSLG, WanVideoEnhanceAVideo, WanVideoSampler, WanVideoModelLoader, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoVAELoader, WanVideoTextEncode, WanVideoLoraSelect, LoadImage]
patterns: []
missing: []
---

# 平台全量/wan2.1lora特效-黑天使降临_1943878321073455105.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.1lora特效-黑天使降临_1943878321073455105.json`

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
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `LoadImage`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`WanVideoExperimentalArgs`、`CLIPVisionLoader`、`ImageResize+`、`WanVideoTeaCache`、`WanVideoBlockSwap`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoSampler`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoLoraSelect`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoClipVisionEncode、WanVideoDecode、WanVideoImageToVideoEncode、WanVideoTextEncode、WanVideoVAELoader
