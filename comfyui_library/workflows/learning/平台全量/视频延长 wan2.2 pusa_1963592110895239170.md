---
key: 平台全量/视频延长 wan2.2 pusa_1963592110895239170.json
name: 视频延长 wan2.2 pusa_1963592110895239170
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频延长 wan2.2 pusa_1963592110895239170.json
hash: 9e0414b76b049cb9
coverage: 0.902439
learned_at: 2026-11-14 02:37:50
nodes: [VHS_VideoInfo, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoModelLoader, MathExpression|pysssss, MathExpression|pysssss, WanVideoModelLoader, ImageResizeKJv2, WanVideoEncode, WanVideoEmptyEmbeds, GetLatentSizeAndCount, CreateScheduleFloatList, WanVideoAddExtraLatent, easy showAnything, WanVideoSetBlockSwap, WanVideoAddPusaNoise, easy float, WanVideoScheduler, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoAddPusaNoise, easy int, WanVideoSigmaToStep, WanVideoScheduler, ImageFromBatch+, ImageFromBatch+, WanVideoDecode, ImageBatchMulti, easy int, VHS_VideoCombine, VHS_LoadVideo, MathExpression|pysssss, JjkText, WanVideoSampler, TrimVideoLatent, WanVideoVAELoader, Note, Note]
patterns: []
missing: []
---

# 平台全量/视频延长 wan2.2 pusa_1963592110895239170.json

> 来源文件 `comfyui_library/workflows/平台全量/视频延长 wan2.2 pusa_1963592110895239170.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（41 个）：
- `VHS_VideoInfo`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `WanVideoModelLoader`
- `ImageResizeKJv2`
- `WanVideoEncode`
- `WanVideoEmptyEmbeds`
- `GetLatentSizeAndCount`
- `CreateScheduleFloatList`
- `WanVideoAddExtraLatent`
- `easy showAnything`
- `WanVideoSetBlockSwap`
- `WanVideoAddPusaNoise`
- `easy float`
- `WanVideoScheduler`
- `WanVideoSampler` ★核心
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoAddPusaNoise`
- `easy int`
- `WanVideoSigmaToStep`
- `WanVideoScheduler`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `WanVideoDecode`
- `ImageBatchMulti`
- `easy int`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `MathExpression|pysssss`
- `JjkText`
- `WanVideoSampler` ★核心
- `TrimVideoLatent`
- `WanVideoVAELoader`
- `Note`
- `Note`

## 知识

覆盖率 **90%**（37/41）

**有卡**：`VHS_VideoInfo`、`WanVideoLoraSelectMulti`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`MathExpression|pysssss`、`ImageResizeKJv2`、`WanVideoEncode`、`WanVideoEmptyEmbeds`、`GetLatentSizeAndCount`、`CreateScheduleFloatList`、`WanVideoAddExtraLatent`、`WanVideoSetBlockSwap`、`WanVideoAddPusaNoise`、`easy float`、`WanVideoScheduler`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`easy int`、`WanVideoSigmaToStep`、`ImageFromBatch+`、`WanVideoDecode`、`ImageBatchMulti`、`VHS_VideoCombine`、`VHS_LoadVideo`、`TrimVideoLatent`、`WanVideoVAELoader`

**用到的条目**：WanVideoSampler、GetLatentSizeAndCount、TrimVideoLatent、WanVideoAddExtraLatent、WanVideoDecode、WanVideoEncode、WanVideoTextEncodeCached、WanVideoVAELoader
