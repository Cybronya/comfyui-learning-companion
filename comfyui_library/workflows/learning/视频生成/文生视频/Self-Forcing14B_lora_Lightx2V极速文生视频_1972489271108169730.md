---
key: 视频生成/文生视频/Self-Forcing14B_lora_Lightx2V极速文生视频_1972489271108169730.json
name: Self-Forcing14B_lora_Lightx2V极速文生视频_1972489271108169730
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Self-Forcing14B_lora_Lightx2V极速文生视频_1972489271108169730.json
hash: cafe0c76da3d6c8a
coverage: 0.68
learned_at: 2026-10-10 23:05:38
nodes: [WanVideoLoraSelect, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoModelLoader, WanVideoBlockSwap, WanVideoEnhanceAVideo, easy batchAnything, easy forLoopStart, WanVideoEmptyEmbeds, WanVideoTextEncode, Text Load Line From File, easy showAnything, easy forLoopEnd, easy cleanGpuUsed, VHS_VideoCombine, WanVideoDecode, GetImageRangeFromBatch, WanVideoLoraSelect, Int, Int, Text Multiline, Int, Int, Evaluate Integers]
patterns: []
missing: [Evaluate Integers, Text Load Line From File, Text Multiline, easy batchAnything, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart]
discoveries: [次要节点 `Evaluate Integers` 知识库中没有该节点类型的任何知识, 次要节点 `Text Load Line From File` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识]
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

覆盖率 **68%**（17/25）

**有卡**：`WanVideoLoraSelect`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoEnhanceAVideo`、`WanVideoEmptyEmbeds`、`WanVideoTextEncode`、`VHS_VideoCombine`、`WanVideoDecode`、`GetImageRangeFromBatch`、`Int`

**缺卡**（7）：`Evaluate Integers`、`Text Load Line From File`、`Text Multiline`、`easy batchAnything`、`easy cleanGpuUsed`、`easy forLoopEnd`、`easy forLoopStart`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、GetImageRangeFromBatch、Int

## 学习发现

- 次要节点 `Evaluate Integers` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Load Line From File` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
