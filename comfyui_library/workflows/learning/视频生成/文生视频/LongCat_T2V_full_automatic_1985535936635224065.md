---
key: 视频生成/文生视频/LongCat_T2V_full_automatic_1985535936635224065.json
name: LongCat_T2V_full_automatic_1985535936635224065
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LongCat_T2V_full_automatic_1985535936635224065.json
hash: 9b5411f1db583d9a
coverage: 0.463415
learned_at: 2026-10-15 22:45:20
nodes: [WanVideoLoraSelect, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, MarkdownNote, WanVideoVAELoader, SetNode, INTConstant, SetNode, INTConstant, SetNode, INTConstant, SetNode, FloatConstant, SetNode, FloatConstant, SetNode, GetNode, GetNode, WanVideoScheduler, SetNode, INTConstant, SetNode, INTConstant, SetNode, GetNode, WanVideoTextEncodeCached, GetNode, PrimitiveNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoSamplerFromSettings, WanVideoSamplerSettings, VHS_VideoCombine, GetNode, WanVideoEmptyEmbeds, GetNode, WanVideoDecode, GetNode, WanVideoEncode, WanVideoTextEncodeCached, WanVideoEmptyEmbeds, GetNode, GetNode, GetNode, GetNode, GetNode, PrimitiveNode, VHS_VideoCombine, easy promptLine, MathExpression|pysssss, GetNode, easy promptLine, Reroute, GetNode, ImageBatchExtendWithOverlap, GetImageSizeAndCount, GetImageSizeAndCount, MarkdownNote, SetNode, easy forLoopEnd, WanVideoSamplerSettings, ImageBatchExtendWithOverlap, WanVideoDecode, GetNode, GetNode, WanVideoSamplerFromSettings, easy forLoopStart, easy showAnything, easy showAnything, SetNode, easy showAnything, Note, Note, VHS_VideoCombine, AILab_QwenVL]
patterns: []
missing: []
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

覆盖率 **46%**（38/82）

**有卡**：`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`INTConstant`、`FloatConstant`、`WanVideoScheduler`、`WanVideoTextEncodeCached`、`WanVideoSamplerFromSettings`、`WanVideoSamplerSettings`、`VHS_VideoCombine`、`WanVideoEmptyEmbeds`、`WanVideoDecode`、`WanVideoEncode`、`easy promptLine`、`MathExpression|pysssss`、`ImageBatchExtendWithOverlap`、`GetImageSizeAndCount`、`easy forLoopEnd`、`easy forLoopStart`、`AILab_QwenVL`

**用到的条目**：WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoEncode、WanVideoLoraSelect、WanVideoSetLoRAs
