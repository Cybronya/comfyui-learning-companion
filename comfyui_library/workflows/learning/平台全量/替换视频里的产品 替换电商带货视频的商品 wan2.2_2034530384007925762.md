---
key: 平台全量/替换视频里的产品 替换电商带货视频的商品 wan2.2_2034530384007925762.json
name: 替换视频里的产品 替换电商带货视频的商品 wan2.2_2034530384007925762
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/替换视频里的产品 替换电商带货视频的商品 wan2.2_2034530384007925762.json
hash: a4fe5deaaf0c17b0
coverage: 0.66
learned_at: 2026-11-14 02:13:58
nodes: [WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, INTConstant, INTConstant, GetNode, GetNode, GetNode, WanVideoVAELoader, Reroute, VHS_VideoCombine, VHS_VideoCombine, WanVideoDecode, GetNode, WanVideoEncode, ImageResizeKJv2, SetNode, WanVideoSampler, WanVideoTorchCompileSettings, AudioEncoderEncode, WanVideoAddS2VEmbeds, PreviewAny, GetImageSizeAndCount, ColorMatch, WanVideoTextEncodeCached, RHHiddenNodes, WanVideoEmptyEmbeds, WanVideoEncode, DWPreprocessor, RHHiddenNodes, WanVideoBlockSwap, RHHiddenNodes, RH_Nano_Banana_Image2Image, SetNode, ImageResizeKJv2, LayerMask: RemBgUltra, PreviewImage, PreviewImage, GetImageRangeFromBatch, LoadImage, VHS_LoadVideo, RH_Translator, PrimitiveStringMultiline, VHS_LoadVideo, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/替换视频里的产品 替换电商带货视频的商品 wan2.2_2034530384007925762.json

> 来源文件 `comfyui_library/workflows/平台全量/替换视频里的产品 替换电商带货视频的商品 wan2.2_2034530384007925762.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（50 个）：
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoVAELoader`
- `Reroute`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `GetNode`
- `WanVideoEncode`
- `ImageResizeKJv2`
- `SetNode`
- `WanVideoSampler` ★核心
- `WanVideoTorchCompileSettings`
- `AudioEncoderEncode`
- `WanVideoAddS2VEmbeds`
- `PreviewAny`
- `GetImageSizeAndCount`
- `ColorMatch`
- `WanVideoTextEncodeCached`
- `RHHiddenNodes`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `DWPreprocessor`
- `RHHiddenNodes`
- `WanVideoBlockSwap`
- `RHHiddenNodes`
- `RH_Nano_Banana_Image2Image`
- `SetNode`
- `ImageResizeKJv2`
- `LayerMask: RemBgUltra`
- `PreviewImage`
- `PreviewImage`
- `GetImageRangeFromBatch`
- `LoadImage`
- `VHS_LoadVideo`
- `RH_Translator`
- `PrimitiveStringMultiline`
- `VHS_LoadVideo`
- `VHS_LoadVideo`

## 知识

覆盖率 **66%**（33/50）

**有卡**：`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`INTConstant`、`WanVideoVAELoader`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoEncode`、`ImageResizeKJv2`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`AudioEncoderEncode`、`WanVideoAddS2VEmbeds`、`GetImageSizeAndCount`、`ColorMatch`、`WanVideoTextEncodeCached`、`RHHiddenNodes`、`WanVideoEmptyEmbeds`、`DWPreprocessor`、`WanVideoBlockSwap`、`RH_Nano_Banana_Image2Image`、`LayerMask: RemBgUltra`、`GetImageRangeFromBatch`、`LoadImage`、`VHS_LoadVideo`、`RH_Translator`

**用到的条目**：LoadImage、WanVideoSampler、AudioEncoderEncode、WanVideoDecode、WanVideoEncode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoSetLoRAs
