---
key: 平台全量/视频-动作迁移Lynx一致性-wan2.1vace-KJ_1977379034298503169.json
name: 视频-动作迁移Lynx一致性-wan2.1vace-KJ_1977379034298503169
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频-动作迁移Lynx一致性-wan2.1vace-KJ_1977379034298503169.json
hash: 7af11791094fcd9d
coverage: 0.648148
learned_at: 2026-11-14 02:34:10
nodes: [PreviewImage, PreviewImage, ImageFromBatch+, VHS_VideoInfoLoaded, SetNode, Reroute, VHS_VideoCombine, ImageConcanate, GetImageSizeAndCount, easy showAnything, GetImageSizeAndCount, SetNode, Reroute, GetImageSizeAndCount, SetNode, Florence2Run, GetNode, easy showAnything, GetNode, GetImageSizeAndCount, PreviewImage, GetNode, ShowText|pysssss, PreviewImage, SetNode, GetImageSizeAndCount, SetNode, GetNode, GetImageSizeAndCount, Reroute, PreviewImage, VHS_VideoCombine, WanVideoSetBlockSwap, ImageFromBatch+, WanVideoSetLoRAs, GetNode, GetNode, GetNode, GetImageSizeAndCount, ImageFromBatch, GetNode, WanVideoDecode, GetNode, GetImageSizeAndCount, ImageConcatMulti, PreviewImage, GetNode, GetNode, GetImageSizeAndCount, easy seed, SetNode, GetImageSizeAndCount, StringFunction|pysssss, ImageFromBatch+, GetImageSizeAndCount, LayerUtility: ImageScaleByAspectRatio V2, easy anythingIndexSwitch, PreviewImage, SetNode, ImageResizeKJ, GetNode, ImageFromBatch, GetImageSizeAndCount, ImageResizeKJ, SetNode, GetNode, ImageFromBatch, Florence2ModelLoader, SetNode, ImageResizeKJ, GetImageSizeAndCount, VHS_VideoCombine, CR Upscale Image, GetImageSizeAndCount, SetNode, easy positive, CM_IntToFloat, LoadImage, ImageFromBatch, GetImageSizeAndCount, GetImageSizeAndCount, StringFunction|pysssss, easy int, easy int, easy int, AIO_Preprocessor, VHS_LoadVideo, INTConstant, WanVideoBlockSwap, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoExtraModelSelect, WanVideoSampler, LoadLynxResampler, GetImageSizeAndCount, WanVideoExtraModelSelect, WanVideoVAELoader, LynxInsightFaceCrop, WanVideoVACEStartToEndFrame, GetImageSizeAndCount, WanVideoVACEEncode, WanVideoAddLynxEmbeds, PreviewImage, PreviewImage, LynxEncodeFaceIP, WanVideoTextEncodeCached, WanVideoTextEncodeCached, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/视频-动作迁移Lynx一致性-wan2.1vace-KJ_1977379034298503169.json

> 来源文件 `comfyui_library/workflows/平台全量/视频-动作迁移Lynx一致性-wan2.1vace-KJ_1977379034298503169.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（108 个）：
- `PreviewImage`
- `PreviewImage`
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
- `SetNode`
- `Florence2Run`
- `GetNode`
- `easy showAnything`
- `GetNode`
- `GetImageSizeAndCount`
- `PreviewImage`
- `GetNode`
- `ShowText|pysssss`
- `PreviewImage`
- `SetNode`
- `GetImageSizeAndCount`
- `SetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `Reroute`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoSetBlockSwap`
- `ImageFromBatch+`
- `WanVideoSetLoRAs`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `ImageFromBatch`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `easy seed`
- `SetNode`
- `GetImageSizeAndCount`
- `StringFunction|pysssss`
- `ImageFromBatch+`
- `GetImageSizeAndCount`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy anythingIndexSwitch`
- `PreviewImage`
- `SetNode`
- `ImageResizeKJ`
- `GetNode`
- `ImageFromBatch`
- `GetImageSizeAndCount`
- `ImageResizeKJ`
- `SetNode`
- `GetNode`
- `ImageFromBatch`
- `Florence2ModelLoader`
- `SetNode`
- `ImageResizeKJ`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `CR Upscale Image`
- `GetImageSizeAndCount`
- `SetNode`
- `easy positive`
- `CM_IntToFloat`
- `LoadImage`
- `ImageFromBatch`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `StringFunction|pysssss`
- `easy int`
- `easy int`
- `easy int`
- `AIO_Preprocessor`
- `VHS_LoadVideo`
- `INTConstant`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoExtraModelSelect`
- `WanVideoSampler` ★核心
- `LoadLynxResampler` ★核心
- `GetImageSizeAndCount`
- `WanVideoExtraModelSelect`
- `WanVideoVAELoader`
- `LynxInsightFaceCrop`
- `WanVideoVACEStartToEndFrame`
- `GetImageSizeAndCount`
- `WanVideoVACEEncode`
- `WanVideoAddLynxEmbeds`
- `PreviewImage`
- `PreviewImage`
- `LynxEncodeFaceIP`
- `WanVideoTextEncodeCached`
- `WanVideoTextEncodeCached`
- `VHS_VideoCombine`

## 知识

覆盖率 **65%**（70/108）

**有卡**：`ImageFromBatch+`、`VHS_VideoInfoLoaded`、`VHS_VideoCombine`、`ImageConcanate`、`GetImageSizeAndCount`、`Florence2Run`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageFromBatch`、`WanVideoDecode`、`ImageConcatMulti`、`easy seed`、`StringFunction|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy anythingIndexSwitch`、`ImageResizeKJ`、`Florence2ModelLoader`、`CR Upscale Image`、`easy positive`、`CM_IntToFloat`、`LoadImage`、`easy int`、`AIO_Preprocessor`、`VHS_LoadVideo`、`INTConstant`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoExtraModelSelect`、`WanVideoSampler`、`LoadLynxResampler`、`WanVideoVAELoader`、`LynxInsightFaceCrop`、`WanVideoVACEStartToEndFrame`、`WanVideoVACEEncode`、`WanVideoAddLynxEmbeds`、`LynxEncodeFaceIP`、`WanVideoTextEncodeCached`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、easy seed、LoadLynxResampler、WanVideoSampler、LynxEncodeFaceIP、WanVideoDecode、WanVideoTextEncodeCached
