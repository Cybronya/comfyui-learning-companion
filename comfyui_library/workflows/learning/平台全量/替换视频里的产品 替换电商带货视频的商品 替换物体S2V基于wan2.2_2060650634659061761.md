---
key: 平台全量/替换视频里的产品 替换电商带货视频的商品 替换物体S2V基于wan2.2_2060650634659061761.json
name: 替换视频里的产品 替换电商带货视频的商品 替换物体S2V基于wan2.2_2060650634659061761
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/替换视频里的产品 替换电商带货视频的商品 替换物体S2V基于wan2.2_2060650634659061761.json
hash: 3177a4c3833cd417
coverage: 0.66
learned_at: 2026-11-14 02:14:00
nodes: [WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, INTConstant, INTConstant, GetNode, GetNode, GetNode, WanVideoVAELoader, Reroute, VHS_VideoCombine, VHS_VideoCombine, WanVideoDecode, GetNode, WanVideoEncode, ImageResizeKJv2, SetNode, WanVideoSampler, VHS_LoadVideo, RH_Translator, PrimitiveStringMultiline, WanVideoTorchCompileSettings, AudioEncoderEncode, WanVideoAddS2VEmbeds, PreviewAny, GetImageSizeAndCount, ColorMatch, WanVideoTextEncodeCached, RHHiddenNodes, WanVideoEmptyEmbeds, WanVideoEncode, DWPreprocessor, RHHiddenNodes, WanVideoBlockSwap, RHHiddenNodes, RH_Nano_Banana_Image2Image, SetNode, ImageResizeKJv2, LayerMask: RemBgUltra, PreviewImage, PreviewImage, VHS_LoadVideo, VHS_LoadVideo, GetImageRangeFromBatch, LoadImage]
patterns: []
missing: []
---

# 平台全量/替换视频里的产品 替换电商带货视频的商品 替换物体S2V基于wan2.2_2060650634659061761.json

> 来源文件 `comfyui_library/workflows/平台全量/替换视频里的产品 替换电商带货视频的商品 替换物体S2V基于wan2.2_2060650634659061761.json`

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
- `VHS_LoadVideo`
- `RH_Translator`
- `PrimitiveStringMultiline`
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
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `GetImageRangeFromBatch`
- `LoadImage`

## 知识

覆盖率 **66%**（33/50）

**有卡**：`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`INTConstant`、`WanVideoVAELoader`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoEncode`、`ImageResizeKJv2`、`WanVideoSampler`、`VHS_LoadVideo`、`RH_Translator`、`WanVideoTorchCompileSettings`、`AudioEncoderEncode`、`WanVideoAddS2VEmbeds`、`GetImageSizeAndCount`、`ColorMatch`、`WanVideoTextEncodeCached`、`RHHiddenNodes`、`WanVideoEmptyEmbeds`、`DWPreprocessor`、`WanVideoBlockSwap`、`RH_Nano_Banana_Image2Image`、`LayerMask: RemBgUltra`、`GetImageRangeFromBatch`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、AudioEncoderEncode、WanVideoDecode、WanVideoEncode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoSetLoRAs
