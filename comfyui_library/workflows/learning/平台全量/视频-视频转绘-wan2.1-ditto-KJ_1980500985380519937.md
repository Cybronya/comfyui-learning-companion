---
key: 平台全量/视频-视频转绘-wan2.1-ditto-KJ_1980500985380519937.json
name: 视频-视频转绘-wan2.1-ditto-KJ_1980500985380519937
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频-视频转绘-wan2.1-ditto-KJ_1980500985380519937.json
hash: ad1870c72b441ce0
coverage: 0.629032
learned_at: 2026-11-14 02:34:41
nodes: [ImageFromBatch+, VHS_VideoInfoLoaded, SetNode, Reroute, VHS_VideoCombine, ImageConcanate, GetImageSizeAndCount, easy showAnything, GetImageSizeAndCount, SetNode, Reroute, GetImageSizeAndCount, GetNode, easy showAnything, GetNode, GetImageSizeAndCount, PreviewImage, GetNode, SetNode, SetNode, Reroute, PreviewImage, ImageFromBatch+, GetNode, ImageFromBatch, GetNode, WanVideoDecode, GetNode, PreviewImage, GetNode, easy seed, SetNode, GetImageSizeAndCount, LayerUtility: ImageScaleByAspectRatio V2, SetNode, GetNode, ImageFromBatch, GetImageSizeAndCount, VHS_VideoCombine, CM_IntToFloat, GetImageSizeAndCount, StringFunction|pysssss, easy int, INTConstant, VHS_VideoCombine, ImageFromBatch, WanVideoBlockSwap, WanVideoVACEModelSelect, WanVideoVAELoader, WanVideoTextEncodeCached, WanVideoSampler, GetImageSizeAndCount, WanVideoVACEEncode, GetNode, GetImageSizeAndCount, WanVideoLoraSelect, easy positive, CR Prompt Text, VHS_LoadVideo, GetImageSizeAndCount, easy int, WanVideoModelLoader]
patterns: []
missing: []
---

# 平台全量/视频-视频转绘-wan2.1-ditto-KJ_1980500985380519937.json

> 来源文件 `comfyui_library/workflows/平台全量/视频-视频转绘-wan2.1-ditto-KJ_1980500985380519937.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（62 个）：
- `ImageFromBatch+`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `Reroute`
- `VHS_VideoCombine`
- `ImageConcanate`
- `GetImageSizeAndCount`
- `easy showAnything`
- `GetImageSizeAndCount`
- `SetNode`
- `Reroute`
- `GetImageSizeAndCount`
- `GetNode`
- `easy showAnything`
- `GetNode`
- `GetImageSizeAndCount`
- `PreviewImage`
- `GetNode`
- `SetNode`
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
- `GetNode`
- `easy seed`
- `SetNode`
- `GetImageSizeAndCount`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `GetNode`
- `ImageFromBatch`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `CM_IntToFloat`
- `GetImageSizeAndCount`
- `StringFunction|pysssss`
- `easy int`
- `INTConstant`
- `VHS_VideoCombine`
- `ImageFromBatch`
- `WanVideoBlockSwap`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `WanVideoSampler` ★核心
- `GetImageSizeAndCount`
- `WanVideoVACEEncode`
- `GetNode`
- `GetImageSizeAndCount`
- `WanVideoLoraSelect`
- `easy positive`
- `CR Prompt Text`
- `VHS_LoadVideo`
- `GetImageSizeAndCount`
- `easy int`
- `WanVideoModelLoader`

## 知识

覆盖率 **63%**（39/62）

**有卡**：`ImageFromBatch+`、`VHS_VideoInfoLoaded`、`VHS_VideoCombine`、`ImageConcanate`、`GetImageSizeAndCount`、`ImageFromBatch`、`WanVideoDecode`、`easy seed`、`LayerUtility: ImageScaleByAspectRatio V2`、`CM_IntToFloat`、`StringFunction|pysssss`、`easy int`、`INTConstant`、`WanVideoBlockSwap`、`WanVideoVACEModelSelect`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`WanVideoVACEEncode`、`WanVideoLoraSelect`、`easy positive`、`CR Prompt Text`、`VHS_LoadVideo`、`WanVideoModelLoader`

**用到的条目**：easy seed、WanVideoSampler、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVACEEncode、WanVideoVAELoader、WanVideoLoraSelect、CR Prompt Text
