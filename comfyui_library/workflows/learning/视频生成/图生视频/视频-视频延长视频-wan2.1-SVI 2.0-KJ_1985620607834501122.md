---
key: 视频生成/图生视频/视频-视频延长视频-wan2.1-SVI 2.0-KJ_1985620607834501122.json
name: 视频-视频延长视频-wan2.1-SVI 2.0-KJ_1985620607834501122.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/视频-视频延长视频-wan2.1-SVI 2.0-KJ_1985620607834501122.json
hash: d819920c1d1395ad
coverage: 0.652778
learned_at: 2026-10-15 22:32:52
nodes: [easy showAnything, easy imageSize, GetNode, SetNode, GetNode, GetImageSizeAndCount, SetNode, easy seed, SetNode, GetNode, ShowText|pysssss, GetNode, GetImageSizeAndCount, StringFunction|pysssss, StringFunction|pysssss, GetNode, easy showAnything, easy positive, ImpactFloat, PreviewImage, ImageFromBatch, SetNode, GetImageSizeAndCount, WanVideoLoraSelect, GetNode, WanVideoSetBlockSwap, GetNode, INTConstant, VHS_VideoCombine, GetImageSizeAndCount, WanVideoTextEncodeCached, GetImageSizeAndCount, VHS_VideoCombine, ImageFromBatch+, WanVideoDecode, SetNode, SetNode, GetNode, SetNode, ImageBatchMulti, VHS_VideoCombine, WanVideoVAELoader, WanVideoClipVisionEncode, CLIPVisionLoader, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetImageRangeFromBatch, GetImageRangeFromBatch, PreviewImage, PreviewImage, PreviewImage, WanVideoSampler, GetImageSizeAndCount, VHS_LoadVideo, GetImageSizeAndCount, WanVideoImageToVideoEncode, GetImageSizeAndCount, SetNode, SimpleMath+, GetImageRangeFromBatch, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoModelLoader, easy anythingIndexSwitch, Qwen3_VQA, WanVideoLoraSelect, easy int, easy int, MathExpression|pysssss, easy positive, PrimitiveFloat, easy int]
patterns: []
missing: []
---

# 视频生成/图生视频/视频-视频延长视频-wan2.1-SVI 2.0-KJ_1985620607834501122.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1985620607834501122.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（72 个）：
- `easy showAnything`
- `easy imageSize`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `SetNode`
- `easy seed`
- `SetNode`
- `GetNode`
- `ShowText|pysssss`
- `GetNode`
- `GetImageSizeAndCount`
- `StringFunction|pysssss`
- `StringFunction|pysssss`
- `GetNode`
- `easy showAnything`
- `easy positive`
- `ImpactFloat`
- `PreviewImage`
- `ImageFromBatch`
- `SetNode`
- `GetImageSizeAndCount`
- `WanVideoLoraSelect`
- `GetNode`
- `WanVideoSetBlockSwap`
- `GetNode`
- `INTConstant`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `WanVideoTextEncodeCached`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `ImageFromBatch+`
- `WanVideoDecode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `ImageBatchMulti`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `WanVideoSampler` ★核心
- `GetImageSizeAndCount`
- `VHS_LoadVideo`
- `GetImageSizeAndCount`
- `WanVideoImageToVideoEncode`
- `GetImageSizeAndCount`
- `SetNode`
- `SimpleMath+`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `easy anythingIndexSwitch`
- `Qwen3_VQA`
- `WanVideoLoraSelect`
- `easy int`
- `easy int`
- `MathExpression|pysssss`
- `easy positive`
- `PrimitiveFloat`
- `easy int`

## 知识

覆盖率 **65%**（47/72）

**有卡**：`easy imageSize`、`GetImageSizeAndCount`、`easy seed`、`StringFunction|pysssss`、`easy positive`、`ImpactFloat`、`ImageFromBatch`、`WanVideoLoraSelect`、`WanVideoSetBlockSwap`、`INTConstant`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`、`ImageFromBatch+`、`WanVideoDecode`、`ImageBatchMulti`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageRangeFromBatch`、`WanVideoSampler`、`VHS_LoadVideo`、`WanVideoImageToVideoEncode`、`SimpleMath+`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`easy anythingIndexSwitch`、`Qwen3_VQA`、`easy int`、`MathExpression|pysssss`

**用到的条目**：WanVideoSampler、easy seed、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、WanVideoLoraSelect
