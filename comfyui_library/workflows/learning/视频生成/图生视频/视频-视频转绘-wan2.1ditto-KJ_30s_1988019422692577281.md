---
key: 视频生成/图生视频/视频-视频转绘-wan2.1ditto-KJ_30s_1988019422692577281.json
name: 视频-视频转绘-wan2.1ditto-KJ_30s_1988019422692577281.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/视频-视频转绘-wan2.1ditto-KJ_30s_1988019422692577281.json
hash: 45bfcb5dc74fccfb
coverage: 0.629032
learned_at: 2026-10-15 22:33:01
nodes: [SetNode, Reroute, VHS_VideoCombine, easy showAnything, GetImageSizeAndCount, Reroute, GetImageSizeAndCount, GetNode, easy showAnything, GetNode, SetNode, Reroute, PreviewImage, ImageFromBatch+, GetNode, ImageFromBatch, GetNode, WanVideoDecode, GetNode, PreviewImage, easy seed, GetImageSizeAndCount, SetNode, ImageFromBatch, GetImageSizeAndCount, VHS_VideoCombine, CM_IntToFloat, GetImageSizeAndCount, StringFunction|pysssss, INTConstant, VHS_VideoCombine, WanVideoBlockSwap, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoVAELoader, WanVideoTextEncodeCached, GetImageSizeAndCount, WanVideoVACEEncode, GetNode, GetImageSizeAndCount, WanVideoLoraSelect, easy positive, CR Prompt Text, PreviewImage, easy int, LayerUtility: ImageScaleByAspectRatio V2, ImageFromBatch, GetImageSizeAndCount, GetNode, SetNode, SetNode, VHS_VideoInfoLoaded, SetNode, GetNode, GetImageSizeAndCount, ImageConcanate, ImageFromBatch+, GetNode, GetImageSizeAndCount, VHS_LoadVideo, WanVideoSampler, easy int]
patterns: []
missing: []
---

# 视频生成/图生视频/视频-视频转绘-wan2.1ditto-KJ_30s_1988019422692577281.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1988019422692577281.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（62 个）：
- `SetNode`
- `Reroute`
- `VHS_VideoCombine`
- `easy showAnything`
- `GetImageSizeAndCount`
- `Reroute`
- `GetImageSizeAndCount`
- `GetNode`
- `easy showAnything`
- `GetNode`
- `SetNode`
- `Reroute`
- `PreviewImage`
- `ImageFromBatch+`
- `GetNode`
- `ImageFromBatch`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `PreviewImage`
- `easy seed`
- `GetImageSizeAndCount`
- `SetNode`
- `ImageFromBatch`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `CM_IntToFloat`
- `GetImageSizeAndCount`
- `StringFunction|pysssss`
- `INTConstant`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `GetImageSizeAndCount`
- `WanVideoVACEEncode`
- `GetNode`
- `GetImageSizeAndCount`
- `WanVideoLoraSelect`
- `easy positive`
- `CR Prompt Text`
- `PreviewImage`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `ImageConcanate`
- `ImageFromBatch+`
- `GetNode`
- `GetImageSizeAndCount`
- `VHS_LoadVideo`
- `WanVideoSampler` ★核心
- `easy int`

## 知识

覆盖率 **63%**（39/62）

**有卡**：`VHS_VideoCombine`、`GetImageSizeAndCount`、`ImageFromBatch+`、`ImageFromBatch`、`WanVideoDecode`、`easy seed`、`CM_IntToFloat`、`StringFunction|pysssss`、`INTConstant`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`WanVideoVACEEncode`、`WanVideoLoraSelect`、`easy positive`、`CR Prompt Text`、`easy int`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoInfoLoaded`、`ImageConcanate`、`VHS_LoadVideo`、`WanVideoSampler`

**用到的条目**：WanVideoSampler、easy seed、WanVideoDecode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、CR Prompt Text
