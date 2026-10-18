---
key: 视频生成/文生视频/Wan2.2 文生视频加速KJ版_1950100642577694721.json
name: Wan2.2 文生视频加速KJ版_1950100642577694721.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 文生视频加速KJ版_1950100642577694721.json
hash: 6d8c21f38f8f874a
coverage: 0.952381
learned_at: 2026-10-15 22:43:34
nodes: [WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoTextEncode, WanVideoEmptyEmbeds, LoadWanVideoT5TextEncoder, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, PrimitiveNode, WanVideoVAELoader, WanVideoDecode, GetImageSizeAndCount, VHS_VideoCombine, CreateCFGScheduleFloatList, WanVideoSampler, WanVideoSampler, CR Prompt Text]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2 文生视频加速KJ版_1950100642577694721.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950100642577694721.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（21 个）：
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `WanVideoEmptyEmbeds`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `PrimitiveNode`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `CR Prompt Text`

## 知识

覆盖率 **95%**（20/21）

**有卡**：`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`WanVideoEmptyEmbeds`、`LoadWanVideoT5TextEncoder`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoDecode`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`CR Prompt Text`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
