---
key: 视频生成/文生视频/KJ版-wan2.2-14B 文生视频_1950090977786683393.json
name: KJ版-wan2.2-14B 文生视频_1950090977786683393.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1950090977786683393.json
hash: 2f9a0297ec5ec74d
coverage: 0.948718
learned_at: 2026-10-15 22:43:34
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoModelLoader, CreateCFGScheduleFloatList, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoVAELoader, easy showAnything, RH_Prompter, CR Text Replace, TextBox, easy showAnything, SimpleMath+, easy imageSize, SimpleMath+, SimpleMath+, SimpleMath+, EmptyImage, SimpleMath+, WanVideoEmptyEmbeds, DF_Integer, easy seed, WanVideoBlockSwap, TextBox, easy cleanGpuUsed, VHS_VideoCombine, WanVideoDecode, easy cleanGpuUsed, easy cleanGpuUsed, LoadWanVideoT5TextEncoder, WanVideoTextEncode, CreateCFGScheduleFloatList, CogVideoEnhanceAVideo, WanVideoSampler, WanVideoSLG, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/文生视频/KJ版-wan2.2-14B 文生视频_1950090977786683393.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950090977786683393.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `CreateCFGScheduleFloatList`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `easy showAnything`
- `RH_Prompter`
- `CR Text Replace`
- `TextBox`
- `easy showAnything`
- `SimpleMath+`
- `easy imageSize`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `EmptyImage`
- `SimpleMath+`
- `WanVideoEmptyEmbeds`
- `DF_Integer`
- `easy seed`
- `WanVideoBlockSwap`
- `TextBox`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `CreateCFGScheduleFloatList`
- `CogVideoEnhanceAVideo`
- `WanVideoSampler` ★核心
- `WanVideoSLG`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **95%**（37/39）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`CreateCFGScheduleFloatList`、`WanVideoSetLoRAs`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`RH_Prompter`、`CR Text Replace`、`TextBox`、`SimpleMath+`、`easy imageSize`、`EmptyImage`、`WanVideoEmptyEmbeds`、`DF_Integer`、`easy seed`、`WanVideoBlockSwap`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`CogVideoEnhanceAVideo`、`WanVideoSampler`、`WanVideoSLG`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect
