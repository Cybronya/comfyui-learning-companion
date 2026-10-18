---
key: 视频生成/文生视频/wan2.2 文生视频_1956285811346079746.json
name: wan2.2 文生视频_1956285811346079746.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2 文生视频_1956285811346079746.json
hash: 1cfdad22ddf9d4b2
coverage: 1
learned_at: 2026-10-15 22:43:41
nodes: [WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoEmptyEmbeds, WanVideoSetLoRAs, INTConstant, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, easy int, easy int, LayerUtility: PurgeVRAM V2, INTConstant, WanVideoSampler, WanVideoTextEncode, LoadWanVideoT5TextEncoder, WanVideoLoraSelect, CreateCFGScheduleFloatList, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoVAELoader, SimpleMath+, WanVideoLoraSelect, WanVideoModelLoader, WanVideoDecode, LayerColor: Brightness & Contrast, ImageFromBatch+, VHS_VideoCombine, easy int, WanVideoModelLoader, Text Multiline, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/文生视频/wan2.2 文生视频_1956285811346079746.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1956285811346079746.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（31 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoEmptyEmbeds`
- `WanVideoSetLoRAs`
- `INTConstant`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `easy int`
- `easy int`
- `LayerUtility: PurgeVRAM V2`
- `INTConstant`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoLoraSelect`
- `CreateCFGScheduleFloatList`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `SimpleMath+`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `LayerColor: Brightness & Contrast`
- `ImageFromBatch+`
- `VHS_VideoCombine`
- `easy int`
- `WanVideoModelLoader`
- `Text Multiline`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **100%**（31/31）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoEmptyEmbeds`、`WanVideoSetLoRAs`、`INTConstant`、`WanVideoBlockSwap`、`easy int`、`LayerUtility: PurgeVRAM V2`、`WanVideoSampler`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoLoraSelect`、`CreateCFGScheduleFloatList`、`WanVideoVAELoader`、`SimpleMath+`、`WanVideoModelLoader`、`WanVideoDecode`、`LayerColor: Brightness & Contrast`、`ImageFromBatch+`、`VHS_VideoCombine`、`Text Multiline`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
