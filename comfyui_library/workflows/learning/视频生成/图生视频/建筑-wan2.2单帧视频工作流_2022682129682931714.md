---
key: 视频生成/图生视频/建筑-wan2.2单帧视频工作流_2022682129682931714.json
name: 建筑-wan2.2单帧视频工作流_2022682129682931714.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2022682129682931714.json
hash: a8932dd6ca5f108c
coverage: 0.966667
learned_at: 2026-10-15 22:35:10
nodes: [WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, LoadWanVideoClipTextEncoder, WanVideoDecode, WanVideoModelLoader, WanVideoClipVisionEncode, JWInteger, WanVideoLoraSelect, ImageResize+, WanVideoSetBlockSwap, WanVideoSetLoRAs, SimpleMath+, WanVideoImageToVideoEncode, PrimitiveNode, INTConstant, JWInteger, CreateCFGScheduleFloatList, WanVideoSampler, WanVideoSampler, VHS_VideoCombine, WanVideoLoraSelect, LoadImage, JWInteger, JWInteger, WanVideoTextEncode, WanVideoLoraSelect]
patterns: []
missing: []
---

# 视频生成/图生视频/建筑-wan2.2单帧视频工作流_2022682129682931714.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2022682129682931714.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（30 个）：
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoClipVisionEncode`
- `JWInteger`
- `WanVideoLoraSelect`
- `ImageResize+`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SimpleMath+`
- `WanVideoImageToVideoEncode`
- `PrimitiveNode`
- `INTConstant`
- `JWInteger`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `LoadImage`
- `JWInteger`
- `JWInteger`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`

## 知识

覆盖率 **97%**（29/30）

**有卡**：`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`LoadWanVideoClipTextEncoder`、`WanVideoDecode`、`WanVideoClipVisionEncode`、`JWInteger`、`WanVideoLoraSelect`、`ImageResize+`、`SimpleMath+`、`WanVideoImageToVideoEncode`、`INTConstant`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`VHS_VideoCombine`、`LoadImage`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
