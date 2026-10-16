---
key: 视频生成/图生视频/wan2.2+4步最新lora 文生视频_1952555051271303170.json
name: wan2.2+4步最新lora 文生视频_1952555051271303170.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1952555051271303170.json
hash: 690d8bb54472809f
coverage: 0.948718
learned_at: 2026-10-15 22:31:02
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoModelLoader, CreateCFGScheduleFloatList, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoVAELoader, easy showAnything, RH_Prompter, CR Text Replace, TextBox, easy showAnything, SimpleMath+, easy imageSize, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, WanVideoEmptyEmbeds, DF_Integer, easy seed, easy cleanGpuUsed, VHS_VideoCombine, WanVideoDecode, easy cleanGpuUsed, easy cleanGpuUsed, LoadWanVideoT5TextEncoder, WanVideoTextEncode, CreateCFGScheduleFloatList, CogVideoEnhanceAVideo, WanVideoSampler, WanVideoSLG, WanVideoSampler, TextBox, WanVideoLoraSelect, WanVideoLoraSelect, EmptyImage, WanVideoBlockSwap]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2+4步最新lora 文生视频_1952555051271303170.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952555051271303170.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `CreateCFGScheduleFloatList`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
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
- `SimpleMath+`
- `WanVideoEmptyEmbeds`
- `DF_Integer`
- `easy seed`
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
- `TextBox`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `EmptyImage`
- `WanVideoBlockSwap`

## 知识

覆盖率 **95%**（37/39）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`CreateCFGScheduleFloatList`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`RH_Prompter`、`CR Text Replace`、`TextBox`、`SimpleMath+`、`easy imageSize`、`WanVideoEmptyEmbeds`、`DF_Integer`、`easy seed`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`CogVideoEnhanceAVideo`、`WanVideoSampler`、`WanVideoSLG`、`WanVideoLoraSelect`、`EmptyImage`、`WanVideoBlockSwap`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect
