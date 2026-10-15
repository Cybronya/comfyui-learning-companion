---
key: 视频生成/文生视频/Self-Forcing14B_lora_Lightx2V极速文生视频_1972489271108169730.json
name: Self-Forcing14B_lora_Lightx2V极速文生视频_1972489271108169730
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Self-Forcing14B_lora_Lightx2V极速文生视频_1972489271108169730.json
hash: cafe0c76da3d6c8a
coverage: 0.96
learned_at: 2026-10-15 22:47:00
nodes: [WanVideoLoraSelect, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoModelLoader, WanVideoBlockSwap, WanVideoEnhanceAVideo, easy batchAnything, easy forLoopStart, WanVideoEmptyEmbeds, WanVideoTextEncode, Text Load Line From File, easy showAnything, easy forLoopEnd, easy cleanGpuUsed, VHS_VideoCombine, WanVideoDecode, GetImageRangeFromBatch, WanVideoLoraSelect, Int, Int, Text Multiline, Int, Int, Evaluate Integers]
patterns: []
missing: []
---

# 视频生成/文生视频/Self-Forcing14B_lora_Lightx2V极速文生视频_1972489271108169730.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Self-Forcing14B_lora_Lightx2V极速文生视频_1972489271108169730.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（25 个）：
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoEnhanceAVideo`
- `easy batchAnything`
- `easy forLoopStart`
- `WanVideoEmptyEmbeds`
- `WanVideoTextEncode`
- `Text Load Line From File`
- `easy showAnything`
- `easy forLoopEnd`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `GetImageRangeFromBatch`
- `WanVideoLoraSelect`
- `Int`
- `Int`
- `Text Multiline`
- `Int`
- `Int`
- `Evaluate Integers`

## 知识

覆盖率 **96%**（24/25）

**有卡**：`WanVideoLoraSelect`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoEnhanceAVideo`、`easy batchAnything`、`easy forLoopStart`、`WanVideoEmptyEmbeds`、`WanVideoTextEncode`、`Text Load Line From File`、`easy forLoopEnd`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`WanVideoDecode`、`GetImageRangeFromBatch`、`Int`、`Text Multiline`、`Evaluate Integers`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、GetImageRangeFromBatch、Int
