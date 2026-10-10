---
key: 视频生成/文生视频/LongCat_T2V_full_automatic_1985535936635224065.json
name: LongCat_T2V_full_automatic_1985535936635224065
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LongCat_T2V_full_automatic_1985535936635224065.json
hash: 9b5411f1db583d9a
coverage: 0.402439
learned_at: 2026-10-11 02:45:00
nodes: [WanVideoLoraSelect, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, MarkdownNote, WanVideoVAELoader, SetNode, INTConstant, SetNode, INTConstant, SetNode, INTConstant, SetNode, FloatConstant, SetNode, FloatConstant, SetNode, GetNode, GetNode, WanVideoScheduler, SetNode, INTConstant, SetNode, INTConstant, SetNode, GetNode, WanVideoTextEncodeCached, GetNode, PrimitiveNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoSamplerFromSettings, WanVideoSamplerSettings, VHS_VideoCombine, GetNode, WanVideoEmptyEmbeds, GetNode, WanVideoDecode, GetNode, WanVideoEncode, WanVideoTextEncodeCached, WanVideoEmptyEmbeds, GetNode, GetNode, GetNode, GetNode, GetNode, PrimitiveNode, VHS_VideoCombine, easy promptLine, MathExpression|pysssss, GetNode, easy promptLine, Reroute, GetNode, ImageBatchExtendWithOverlap, GetImageSizeAndCount, GetImageSizeAndCount, MarkdownNote, SetNode, easy forLoopEnd, WanVideoSamplerSettings, ImageBatchExtendWithOverlap, WanVideoDecode, GetNode, GetNode, WanVideoSamplerFromSettings, easy forLoopStart, easy showAnything, easy showAnything, SetNode, easy showAnything, Note, Note, VHS_VideoCombine, AILab_QwenVL]
patterns: []
missing: [MathExpression|pysssss, easy forLoopEnd, easy forLoopStart, easy promptLine, easy promptLine]
discoveries: [次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/LongCat_T2V_full_automatic_1985535936635224065.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LongCat_T2V_full_automatic_1985535936635224065.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（82 个）：
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `SetNode`
- `MarkdownNote`
- `WanVideoVAELoader`
- `SetNode`
- `INTConstant`
- `SetNode`
- `INTConstant`
- `SetNode`
- `INTConstant`
- `SetNode`
- `FloatConstant`
- `SetNode`
- `FloatConstant`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoScheduler`
- `SetNode`
- `INTConstant`
- `SetNode`
- `INTConstant`
- `SetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `GetNode`
- `PrimitiveNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSamplerFromSettings` ★核心
- `WanVideoSamplerSettings` ★核心
- `VHS_VideoCombine`
- `GetNode`
- `WanVideoEmptyEmbeds`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `WanVideoEncode`
- `WanVideoTextEncodeCached`
- `WanVideoEmptyEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveNode`
- `VHS_VideoCombine`
- `easy promptLine`
- `MathExpression|pysssss`
- `GetNode`
- `easy promptLine`
- `Reroute`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `MarkdownNote`
- `SetNode`
- `easy forLoopEnd`
- `WanVideoSamplerSettings` ★核心
- `ImageBatchExtendWithOverlap`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `WanVideoSamplerFromSettings` ★核心
- `easy forLoopStart`
- `easy showAnything`
- `easy showAnything`
- `SetNode`
- `easy showAnything`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `AILab_QwenVL`

## 知识

覆盖率 **40%**（33/82）

**有卡**：`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`INTConstant`、`FloatConstant`、`WanVideoScheduler`、`WanVideoTextEncodeCached`、`WanVideoSamplerFromSettings`、`WanVideoSamplerSettings`、`VHS_VideoCombine`、`WanVideoEmptyEmbeds`、`WanVideoDecode`、`WanVideoEncode`、`ImageBatchExtendWithOverlap`、`GetImageSizeAndCount`、`AILab_QwenVL`

**缺卡**（5）：`MathExpression|pysssss`、`easy forLoopEnd`、`easy forLoopStart`、`easy promptLine`、`easy promptLine`

**用到的条目**：WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoEncode、WanVideoLoraSelect、WanVideoSetLoRAs

## 学习发现

- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
- 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
