---
key: 视频生成/图生视频/wan2.2首尾帧视频工作流_2013162152139431937.json
name: wan2.2首尾帧视频工作流_2013162152139431937.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2013162152139431937.json
hash: 4199adacf943a742
coverage: 0.967742
learned_at: 2026-10-15 22:34:30
nodes: [WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSampler, WanVideoClipVisionEncode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, LoadWanVideoClipTextEncoder, WanVideoDecode, ImageResize+, ImageResize+, WanVideoImageToVideoEncode, PrimitiveNode, INTConstant, JWInteger, CreateCFGScheduleFloatList, WanVideoSampler, VHS_VideoCombine, SimpleMath+, WanVideoBlockSwap, WanVideoModelLoader, WanVideoModelLoader, LoadImage, WanVideoLoraSelect, WanVideoLoraSelect, LoadImage, JWInteger, JWInteger, JWInteger, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2首尾帧视频工作流_2013162152139431937.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2013162152139431937.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（31 个）：
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoClipVisionEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoDecode`
- `ImageResize+`
- `ImageResize+`
- `WanVideoImageToVideoEncode`
- `PrimitiveNode`
- `INTConstant`
- `JWInteger`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `SimpleMath+`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `LoadImage`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadImage`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `WanVideoTextEncode`

## 知识

覆盖率 **97%**（30/31）

**有卡**：`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoSampler`、`WanVideoClipVisionEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`LoadWanVideoClipTextEncoder`、`WanVideoDecode`、`ImageResize+`、`WanVideoImageToVideoEncode`、`INTConstant`、`JWInteger`、`CreateCFGScheduleFloatList`、`VHS_VideoCombine`、`SimpleMath+`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`LoadImage`、`WanVideoLoraSelect`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
