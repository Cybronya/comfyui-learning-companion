---
key: 视频生成/图生视频/wan2.2 KJ版图生视频-低显存工作流_1950109940024262657.json
name: wan2.2 KJ版图生视频-低显存工作流_1950109940024262657.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950109940024262657.json
hash: 78341c36a97c9f2e
coverage: 0.909091
learned_at: 2026-10-15 22:30:53
nodes: [Note, WanVideoVAELoader, LoadWanVideoT5TextEncoder, ImageResizeKJv2, PreviewImage, WanVideoDecode, easy globalSeed, WanVideoTextEncode, Display Any (rgthree), WanVideoLoraSelect, WanVideoLoraSelect, WanVideoImageToVideoEncode, INTConstant, CreateCFGScheduleFloatList, WanVideoSampler, WanVideoSampler, LoadImage, WanVideoModelLoader, WanVideoModelLoader, VHS_VideoCombine, LoadImage, WanVideoBlockSwap]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2 KJ版图生视频-低显存工作流_1950109940024262657.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950109940024262657.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（22 个）：
- `Note`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `ImageResizeKJv2`
- `PreviewImage`
- `WanVideoDecode`
- `easy globalSeed`
- `WanVideoTextEncode`
- `Display Any (rgthree)`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoImageToVideoEncode`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `LoadImage`
- `WanVideoBlockSwap`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`ImageResizeKJv2`、`WanVideoDecode`、`easy globalSeed`、`WanVideoTextEncode`、`Display Any (rgthree)`、`WanVideoLoraSelect`、`WanVideoImageToVideoEncode`、`INTConstant`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`LoadImage`、`WanVideoModelLoader`、`VHS_VideoCombine`、`WanVideoBlockSwap`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、easy globalSeed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
