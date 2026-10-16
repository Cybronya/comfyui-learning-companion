---
key: 视频生成/图生视频/Wan2.1_FusionX+lightx2v极速高质量首尾帧_1935617476765863938.json
name: Wan2.1_FusionX+lightx2v极速高质量首尾帧_1935617476765863938.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1935617476765863938.json
hash: e3fc018ad2b21098
coverage: 0.88
learned_at: 2026-10-15 22:30:23
nodes: [LoadImage, LoadImage, ImageResizeKJv2, ImageResizeKJv2, SetNode, WanVideoSampler, WanVideoImageToVideoEncode, easy int, easy int, easy int, WanVideoModelLoader, WanVideoClipVisionEncode, SetNode, VHS_VideoCombine, LoadWanVideoT5TextEncoder, WanVideoVAELoader, LoadWanVideoClipTextEncoder, Fast Groups Bypasser (rgthree), WanVideoSLG, WanVideoExperimentalArgs, WanVideoDecode, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1_FusionX+lightx2v极速高质量首尾帧_1935617476765863938.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1935617476765863938.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（25 个）：
- `LoadImage`
- `LoadImage`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `SetNode`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoEncode`
- `easy int`
- `easy int`
- `easy int`
- `WanVideoModelLoader`
- `WanVideoClipVisionEncode`
- `SetNode`
- `VHS_VideoCombine`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `Fast Groups Bypasser (rgthree)`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`

## 知识

覆盖率 **88%**（22/25）

**有卡**：`LoadImage`、`ImageResizeKJv2`、`WanVideoSampler`、`WanVideoImageToVideoEncode`、`easy int`、`WanVideoModelLoader`、`WanVideoClipVisionEncode`、`VHS_VideoCombine`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`LoadWanVideoClipTextEncoder`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoDecode`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
