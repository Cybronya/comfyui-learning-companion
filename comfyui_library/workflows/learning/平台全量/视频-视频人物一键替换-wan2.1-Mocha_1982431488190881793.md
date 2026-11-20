---
key: 平台全量/视频-视频人物一键替换-wan2.1-Mocha_1982431488190881793.json
name: 视频-视频人物一键替换-wan2.1-Mocha_1982431488190881793
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频-视频人物一键替换-wan2.1-Mocha_1982431488190881793.json
hash: 46f06de95ef1be34
coverage: 0.671875
learned_at: 2026-11-14 02:34:28
nodes: [WanVideoLoraSelectMulti, VHS_VideoInfoLoaded, SetNode, SetNode, GetImageSizeAndCount, SetNode, CM_IntToFloat, easy int, INTConstant, VHS_LoadVideo, easy int, PreviewImage, ImageFromBatch+, VHS_VideoCombine, ImageConcanate, GetNode, GetImageSizeAndCount, Reroute, easy showAnything, VHS_VideoCombine, GetNode, Reroute, GetImageSizeAndCount, GetImageSizeAndCount, WanVideoDecode, WanVideoSampler, GetNode, GetNode, GetNode, WanVideoVAELoader, MochaEmbeds, PreviewImage, PreviewImage, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, GetImageRangeFromBatch, easy cleanGpuUsed, BlockifyMask, MaskPreview+, GrowMask, LayerMask: SegmentAnythingUltra V2, LoadImage, WanVideoTextEncodeCached, SetNode, easy positive, easy showAnything, GetImageSizeAndCount, StringFunction|pysssss, GetNode, FaceBoundingBox, FaceAnalysisModels, easy seed, GetNode, GetNode, GetImageSizeAndCount, PreviewImage, SetNode, ImageFromBatch, GetImageSizeAndCount, GetImageSizeAndCount, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, ImageResizeKJv2]
patterns: []
missing: []
---

# 平台全量/视频-视频人物一键替换-wan2.1-Mocha_1982431488190881793.json

> 来源文件 `comfyui_library/workflows/平台全量/视频-视频人物一键替换-wan2.1-Mocha_1982431488190881793.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（64 个）：
- `WanVideoLoraSelectMulti`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `SetNode`
- `GetImageSizeAndCount`
- `SetNode`
- `CM_IntToFloat`
- `easy int`
- `INTConstant`
- `VHS_LoadVideo`
- `easy int`
- `PreviewImage`
- `ImageFromBatch+`
- `VHS_VideoCombine`
- `ImageConcanate`
- `GetNode`
- `GetImageSizeAndCount`
- `Reroute`
- `easy showAnything`
- `VHS_VideoCombine`
- `GetNode`
- `Reroute`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoVAELoader`
- `MochaEmbeds`
- `PreviewImage`
- `PreviewImage`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `GetImageRangeFromBatch`
- `easy cleanGpuUsed`
- `BlockifyMask`
- `MaskPreview+`
- `GrowMask`
- `LayerMask: SegmentAnythingUltra V2`
- `LoadImage`
- `WanVideoTextEncodeCached`
- `SetNode`
- `easy positive`
- `easy showAnything`
- `GetImageSizeAndCount`
- `StringFunction|pysssss`
- `GetNode`
- `FaceBoundingBox`
- `FaceAnalysisModels`
- `easy seed`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `PreviewImage`
- `SetNode`
- `ImageFromBatch`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`

## 知识

覆盖率 **67%**（43/64）

**有卡**：`WanVideoLoraSelectMulti`、`VHS_VideoInfoLoaded`、`GetImageSizeAndCount`、`CM_IntToFloat`、`easy int`、`INTConstant`、`VHS_LoadVideo`、`ImageFromBatch+`、`VHS_VideoCombine`、`ImageConcanate`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoVAELoader`、`MochaEmbeds`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`GetImageRangeFromBatch`、`easy cleanGpuUsed`、`BlockifyMask`、`MaskPreview+`、`GrowMask`、`LayerMask: SegmentAnythingUltra V2`、`LoadImage`、`WanVideoTextEncodeCached`、`easy positive`、`StringFunction|pysssss`、`FaceBoundingBox`、`FaceAnalysisModels`、`easy seed`、`ImageFromBatch`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、easy seed、WanVideoSampler、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti
