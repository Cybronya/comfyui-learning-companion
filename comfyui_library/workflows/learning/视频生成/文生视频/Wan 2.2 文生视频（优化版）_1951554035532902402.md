---
key: 视频生成/文生视频/Wan 2.2 文生视频（优化版）_1951554035532902402.json
name: Wan 2.2 文生视频（优化版）_1951554035532902402.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1951554035532902402.json
hash: fb0280539962775b
coverage: 0.966667
learned_at: 2026-10-15 22:43:38
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, GetImageSizeAndCount, easy cleanGpuUsed, WanVideoDecode, WanVideoSampler, WanVideoSampler, RH_LLMAPI_NODE, ShowText, WanVideoEmptyEmbeds, CreateCFGScheduleFloatList, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoVAELoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoTorchCompileSettings, SeargePromptText, SeargePromptText, SeargePromptText, SeargePromptText, VHS_VideoCombine, ImpactSwitch, SeargePromptText, SeargePromptText]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan 2.2 文生视频（优化版）_1951554035532902402.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1951554035532902402.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（30 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `RH_LLMAPI_NODE`
- `ShowText`
- `WanVideoEmptyEmbeds`
- `CreateCFGScheduleFloatList`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `SeargePromptText`
- `SeargePromptText`
- `SeargePromptText`
- `SeargePromptText`
- `VHS_VideoCombine`
- `ImpactSwitch`
- `SeargePromptText`
- `SeargePromptText`

## 知识

覆盖率 **97%**（29/30）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`easy cleanGpuUsed`、`WanVideoDecode`、`WanVideoSampler`、`RH_LLMAPI_NODE`、`ShowText`、`WanVideoEmptyEmbeds`、`CreateCFGScheduleFloatList`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`SeargePromptText`、`VHS_VideoCombine`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
