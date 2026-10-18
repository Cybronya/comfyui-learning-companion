---
key: 视频生成/图生视频/KJ版-wan2.2-14B 图生视频_1950075530189127682.json
name: KJ版-wan2.2-14B 图生视频_1950075530189127682.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/KJ版-wan2.2-14B 图生视频_1950075530189127682.json
hash: 011baf61992efc19
coverage: 0.9
learned_at: 2026-10-15 22:30:52
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, CreateCFGScheduleFloatList, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, easy ifElse, TextBox, easy showAnything, CR Text Replace, Note, easy int, LayerUtility: ImageScaleByAspectRatio V2, WanVideoVAELoader, TextBox, RH_Captioner, easy showAnything, WanVideoModelLoader, WanVideoModelLoader, easy seed, DF_Integer, WanVideoImageToVideoEncode, SimpleMath+, WanVideoBlockSwap, LoadImage, TextBox, PrimitiveBoolean, easy cleanGpuUsed, WanVideoSampler, VHS_VideoCombine, easy cleanGpuUsed, WanVideoDecode, easy cleanGpuUsed, CreateCFGScheduleFloatList, CogVideoEnhanceAVideo, WanVideoSLG, WanVideoTextEncode, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/图生视频/KJ版-wan2.2-14B 图生视频_1950075530189127682.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950075530189127682.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（40 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `CreateCFGScheduleFloatList`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `easy ifElse`
- `TextBox`
- `easy showAnything`
- `CR Text Replace`
- `Note`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoVAELoader`
- `TextBox`
- `RH_Captioner`
- `easy showAnything`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `easy seed`
- `DF_Integer`
- `WanVideoImageToVideoEncode`
- `SimpleMath+`
- `WanVideoBlockSwap`
- `LoadImage`
- `TextBox`
- `PrimitiveBoolean`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `CreateCFGScheduleFloatList`
- `CogVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **90%**（36/40）

**有卡**：`WanVideoSetBlockSwap`、`CreateCFGScheduleFloatList`、`WanVideoSetLoRAs`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`TextBox`、`CR Text Replace`、`easy int`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoVAELoader`、`RH_Captioner`、`WanVideoModelLoader`、`easy seed`、`DF_Integer`、`WanVideoImageToVideoEncode`、`SimpleMath+`、`WanVideoBlockSwap`、`LoadImage`、`PrimitiveBoolean`、`easy cleanGpuUsed`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoDecode`、`CogVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
