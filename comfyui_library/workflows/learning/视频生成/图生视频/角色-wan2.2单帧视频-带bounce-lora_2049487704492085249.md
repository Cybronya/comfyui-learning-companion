---
key: 视频生成/图生视频/角色-wan2.2单帧视频-带bounce-lora_2049487704492085249.json
name: 角色-wan2.2单帧视频-带bounce-lora_2049487704492085249.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/角色-wan2.2单帧视频-带bounce-lora_2049487704492085249.json
hash: 0490dd31f7f4095b
coverage: 0.966667
learned_at: 2026-10-15 22:37:15
nodes: [WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, LoadWanVideoClipTextEncoder, WanVideoDecode, WanVideoModelLoader, WanVideoClipVisionEncode, WanVideoLoraSelect, ImageResize+, WanVideoSetBlockSwap, WanVideoSetLoRAs, SimpleMath+, WanVideoImageToVideoEncode, PrimitiveNode, JWInteger, CreateCFGScheduleFloatList, WanVideoSampler, WanVideoSampler, VHS_VideoCombine, WanVideoLoraSelect, LoadImage, JWInteger, JWInteger, WanVideoTextEncode, JWInteger, INTConstant, WanVideoLoraSelect]
patterns: []
missing: []
---

# 视频生成/图生视频/角色-wan2.2单帧视频-带bounce-lora_2049487704492085249.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2049487704492085249.json`

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
- `WanVideoLoraSelect`
- `ImageResize+`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SimpleMath+`
- `WanVideoImageToVideoEncode`
- `PrimitiveNode`
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
- `JWInteger`
- `INTConstant`
- `WanVideoLoraSelect`

## 知识

覆盖率 **97%**（29/30）

**有卡**：`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`LoadWanVideoClipTextEncoder`、`WanVideoDecode`、`WanVideoClipVisionEncode`、`WanVideoLoraSelect`、`ImageResize+`、`SimpleMath+`、`WanVideoImageToVideoEncode`、`JWInteger`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`VHS_VideoCombine`、`LoadImage`、`WanVideoTextEncode`、`INTConstant`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
