---
key: 图片生成/图生图/视频-图生视频长视频-wan2.1-SVI 2.0-KJ_1985612085986045953.json
name: 视频-图生视频长视频-wan2.1-SVI 2.0-KJ_1985612085986045953
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/视频-图生视频长视频-wan2.1-SVI 2.0-KJ_1985612085986045953.json
hash: 373af4b9cc4e2c4a
coverage: 0.616667
learned_at: 2026-10-23 13:25:57
nodes: [easy showAnything, easy imageSize, GetNode, SetNode, GetNode, SetNode, GetImageSizeAndCount, PreviewImage, SetNode, easy seed, SetNode, GetNode, ShowText|pysssss, GetNode, GetImageSizeAndCount, ImageFromBatch+, StringFunction|pysssss, StringFunction|pysssss, GetNode, PreviewImage, ImageFromBatch, SetNode, GetImageSizeAndCount, WanVideoLoraSelect, WanVideoVAELoader, WanVideoDecode, WanVideoSetBlockSwap, GetNode, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, CLIPVisionLoader, GetImageSizeAndCount, GetImageSizeAndCount, VHS_VideoCombine, WanVideoSampler, WanVideoTextEncodeCached, easy showAnything, LayerUtility: ImageScaleByAspectRatio V2, easy positive, VHS_VideoCombine, LoadImage, WanVideoModelLoader, easy int, GetImageSizeAndCount, SetNode, ImpactFloat, PrimitiveFloat, SetNode, easy int, easy positive, MathExpression|pysssss, easy anythingIndexSwitch, SetNode, GetNode, GetImageSizeAndCount, GetNode, GetNode, WanVideoBlockSwap, WanVideoLoraSelect, Qwen3_VQA]
patterns: []
missing: []
---

# 图片生成/图生图/视频-图生视频长视频-wan2.1-SVI 2.0-KJ_1985612085986045953.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/视频-图生视频长视频-wan2.1-SVI 2.0-KJ_1985612085986045953.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（60 个）：
- `easy showAnything`
- `easy imageSize`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetImageSizeAndCount`
- `PreviewImage`
- `SetNode`
- `easy seed`
- `SetNode`
- `GetNode`
- `ShowText|pysssss`
- `GetNode`
- `GetImageSizeAndCount`
- `ImageFromBatch+`
- `StringFunction|pysssss`
- `StringFunction|pysssss`
- `GetNode`
- `PreviewImage`
- `ImageFromBatch`
- `SetNode`
- `GetImageSizeAndCount`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoTextEncodeCached`
- `easy showAnything`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy positive`
- `VHS_VideoCombine`
- `LoadImage`
- `WanVideoModelLoader`
- `easy int`
- `GetImageSizeAndCount`
- `SetNode`
- `ImpactFloat`
- `PrimitiveFloat`
- `SetNode`
- `easy int`
- `easy positive`
- `MathExpression|pysssss`
- `easy anythingIndexSwitch`
- `SetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `Qwen3_VQA`

## 知识

覆盖率 **62%**（37/60）

**有卡**：`easy imageSize`、`GetImageSizeAndCount`、`easy seed`、`ImageFromBatch+`、`StringFunction|pysssss`、`ImageFromBatch`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`WanVideoDecode`、`WanVideoSetBlockSwap`、`WanVideoImageToVideoEncode`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy positive`、`LoadImage`、`WanVideoModelLoader`、`easy int`、`ImpactFloat`、`MathExpression|pysssss`、`easy anythingIndexSwitch`、`WanVideoBlockSwap`、`Qwen3_VQA`

**用到的条目**：LoadImage、WanVideoSampler、easy seed、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached
