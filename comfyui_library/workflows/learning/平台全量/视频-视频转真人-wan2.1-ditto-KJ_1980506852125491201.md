---
key: 平台全量/视频-视频转真人-wan2.1-ditto-KJ_1980506852125491201.json
name: 视频-视频转真人-wan2.1-ditto-KJ_1980506852125491201
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频-视频转真人-wan2.1-ditto-KJ_1980506852125491201.json
hash: df60bc7b554c6c6e
coverage: 0.634921
learned_at: 2026-11-14 02:34:41
nodes: [ImageFromBatch+, VHS_VideoInfoLoaded, SetNode, Reroute, VHS_VideoCombine, ImageConcanate, GetImageSizeAndCount, easy showAnything, GetImageSizeAndCount, SetNode, Reroute, GetImageSizeAndCount, GetNode, easy showAnything, GetNode, GetImageSizeAndCount, PreviewImage, GetNode, SetNode, SetNode, Reroute, PreviewImage, ImageFromBatch+, ImageFromBatch, GetNode, WanVideoDecode, GetNode, PreviewImage, GetNode, easy seed, SetNode, GetImageSizeAndCount, LayerUtility: ImageScaleByAspectRatio V2, SetNode, GetNode, ImageFromBatch, GetImageSizeAndCount, VHS_VideoCombine, CM_IntToFloat, GetImageSizeAndCount, INTConstant, VHS_VideoCombine, ImageFromBatch, WanVideoVAELoader, WanVideoTextEncodeCached, GetImageSizeAndCount, WanVideoVACEEncode, GetNode, GetImageSizeAndCount, WanVideoLoraSelect, CR Prompt Text, WanVideoVACEModelSelect, GetNode, ShowText, GetImageSizeAndCount, VHS_LoadVideo, WanVideoSampler, StringFunction|pysssss, easy positive, WanVideoBlockSwap, easy int, easy int, WanVideoModelLoader]
patterns: []
missing: []
---

# 平台全量/视频-视频转真人-wan2.1-ditto-KJ_1980506852125491201.json

> 来源文件 `comfyui_library/workflows/平台全量/视频-视频转真人-wan2.1-ditto-KJ_1980506852125491201.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（63 个）：
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
- `INTConstant`
- `VHS_VideoCombine`
- `ImageFromBatch`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `GetImageSizeAndCount`
- `WanVideoVACEEncode`
- `GetNode`
- `GetImageSizeAndCount`
- `WanVideoLoraSelect`
- `CR Prompt Text`
- `WanVideoVACEModelSelect`
- `GetNode`
- `ShowText`
- `GetImageSizeAndCount`
- `VHS_LoadVideo`
- `WanVideoSampler` ★核心
- `StringFunction|pysssss`
- `easy positive`
- `WanVideoBlockSwap`
- `easy int`
- `easy int`
- `WanVideoModelLoader`

## 知识

覆盖率 **63%**（40/63）

**有卡**：`ImageFromBatch+`、`VHS_VideoInfoLoaded`、`VHS_VideoCombine`、`ImageConcanate`、`GetImageSizeAndCount`、`ImageFromBatch`、`WanVideoDecode`、`easy seed`、`LayerUtility: ImageScaleByAspectRatio V2`、`CM_IntToFloat`、`INTConstant`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`WanVideoVACEEncode`、`WanVideoLoraSelect`、`CR Prompt Text`、`WanVideoVACEModelSelect`、`ShowText`、`VHS_LoadVideo`、`WanVideoSampler`、`StringFunction|pysssss`、`easy positive`、`WanVideoBlockSwap`、`easy int`、`WanVideoModelLoader`

**用到的条目**：easy seed、WanVideoSampler、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVACEEncode、WanVideoVAELoader、WanVideoLoraSelect、CR Prompt Text
