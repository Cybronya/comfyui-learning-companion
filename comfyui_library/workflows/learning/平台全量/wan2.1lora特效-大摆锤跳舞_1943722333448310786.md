---
key: 平台全量/wan2.1lora特效-大摆锤跳舞_1943722333448310786.json
name: wan2.1lora特效-大摆锤跳舞_1943722333448310786
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.1lora特效-大摆锤跳舞_1943722333448310786.json
hash: a470c6645e06faf2
coverage: 0.947368
learned_at: 2026-11-14 01:19:11
nodes: [WanVideoClipVisionEncode, WanVideoImageToVideoEncode, WanVideoExperimentalArgs, CLIPVisionLoader, ImageResize+, WanVideoTeaCache, LoadImage, PreviewImage, WanVideoBlockSwap, WanVideoSLG, WanVideoEnhanceAVideo, WanVideoSampler, WanVideoModelLoader, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoTextEncode, VHS_VideoCombine, WanVideoDecode, WanVideoVAELoader]
patterns: []
missing: []
---

# 平台全量/wan2.1lora特效-大摆锤跳舞_1943722333448310786.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.1lora特效-大摆锤跳舞_1943722333448310786.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（19 个）：
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoExperimentalArgs`
- `CLIPVisionLoader`
- `ImageResize+`
- `WanVideoTeaCache`
- `LoadImage`
- `PreviewImage`
- `WanVideoBlockSwap`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoVAELoader`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`WanVideoExperimentalArgs`、`CLIPVisionLoader`、`ImageResize+`、`WanVideoTeaCache`、`LoadImage`、`WanVideoBlockSwap`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoVAELoader`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoClipVisionEncode、WanVideoDecode、WanVideoImageToVideoEncode、WanVideoTextEncode、WanVideoVAELoader
