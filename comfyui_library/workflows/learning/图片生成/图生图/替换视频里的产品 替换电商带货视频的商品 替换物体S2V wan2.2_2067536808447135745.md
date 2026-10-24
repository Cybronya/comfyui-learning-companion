---
key: 图片生成/图生图/替换视频里的产品 替换电商带货视频的商品 替换物体S2V wan2.2_2067536808447135745.json
name: 替换视频里的产品 替换电商带货视频的商品 替换物体S2V wan2.2_2067536808447135745
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/替换视频里的产品 替换电商带货视频的商品 替换物体S2V wan2.2_2067536808447135745.json
hash: 723e67cf74bcd62c
coverage: 0.66
learned_at: 2026-10-23 13:05:23
nodes: [WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, INTConstant, INTConstant, GetNode, GetNode, WanVideoVAELoader, Reroute, VHS_VideoCombine, WanVideoDecode, GetNode, ImageResizeKJv2, SetNode, WanVideoSampler, WanVideoTorchCompileSettings, AudioEncoderEncode, WanVideoAddS2VEmbeds, PreviewAny, GetImageSizeAndCount, ColorMatch, WanVideoTextEncodeCached, RHHiddenNodes, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoBlockSwap, RHHiddenNodes, RH_Nano_Banana_Image2Image, SetNode, ImageResizeKJv2, LayerMask: RemBgUltra, PreviewImage, PreviewImage, GetImageRangeFromBatch, VHS_LoadVideo, LoadImage, RH_Translator, VHS_LoadVideo, WanVideoEncode, VHS_LoadVideo, GetNode, RHHiddenNodes, VHS_VideoCombine, DWPreprocessor, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 图片生成/图生图/替换视频里的产品 替换电商带货视频的商品 替换物体S2V wan2.2_2067536808447135745.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/替换视频里的产品 替换电商带货视频的商品 替换物体S2V wan2.2_2067536808447135745.json`

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
- `WanVideoVAELoader`
- `Reroute`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `GetNode`
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
- `WanVideoBlockSwap`
- `RHHiddenNodes`
- `RH_Nano_Banana_Image2Image`
- `SetNode`
- `ImageResizeKJv2`
- `LayerMask: RemBgUltra`
- `PreviewImage`
- `PreviewImage`
- `GetImageRangeFromBatch`
- `VHS_LoadVideo`
- `LoadImage`
- `RH_Translator`
- `VHS_LoadVideo`
- `WanVideoEncode`
- `VHS_LoadVideo`
- `GetNode`
- `RHHiddenNodes`
- `VHS_VideoCombine`
- `DWPreprocessor`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **66%**（33/50）

**有卡**：`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`INTConstant`、`WanVideoVAELoader`、`VHS_VideoCombine`、`WanVideoDecode`、`ImageResizeKJv2`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`AudioEncoderEncode`、`WanVideoAddS2VEmbeds`、`GetImageSizeAndCount`、`ColorMatch`、`WanVideoTextEncodeCached`、`RHHiddenNodes`、`WanVideoEmptyEmbeds`、`WanVideoEncode`、`WanVideoBlockSwap`、`RH_Nano_Banana_Image2Image`、`LayerMask: RemBgUltra`、`GetImageRangeFromBatch`、`VHS_LoadVideo`、`LoadImage`、`RH_Translator`、`DWPreprocessor`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、AudioEncoderEncode、WanVideoTextEncodeCached、WanVideoEncode、WanVideoSetLoRAs
