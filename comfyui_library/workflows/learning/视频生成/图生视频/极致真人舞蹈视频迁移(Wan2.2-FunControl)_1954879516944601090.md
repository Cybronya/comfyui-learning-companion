---
key: 视频生成/图生视频/极致真人舞蹈视频迁移(Wan2.2-FunControl)_1954879516944601090.json
name: 极致真人舞蹈视频迁移(Wan2.2-FunControl)_1954879516944601090.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1954879516944601090.json
hash: 311485b4e5edcce0
coverage: 0.62963
learned_at: 2026-10-15 22:31:07
nodes: [LoadWanVideoT5TextEncoder, WanVideoSampler, GetNode, WanVideoSampler, WanVideoImageToVideoEncode, Reroute, Reroute, SetNode, GetNode, Reroute, Note, WanVideoSetBlockSwap, Note, GetNode, LoadImage, WanVideoModelLoader, WanVideoVAELoader, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoLoraSelectMulti, WanVideoSetLoRAs, PrimitiveNode, PrimitiveNode, Note, PrimitiveNode, PrimitiveNode, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, WanVideoSetLoRAs, MarkdownNote, WanVideoEmptyEmbeds, WanVideoControlEmbeds, WanVideoEncode, GetImageSizeAndCount, PrimitiveInt, PrimitiveInt, ImageResizeKJv2, Note, SetNode, VHS_VideoCombine, Zoe-DepthMapPreprocessor, DownloadAndLoadDepthAnythingV2Model, DepthAnything_V2, VHS_LoadVideo, ImageResizeKJv2, GetNode, VHS_VideoCombine, WanVideoDecode, VHS_VideoCombine, ImageBlend, ImageConcatMulti, DWPreprocessor]
patterns: []
missing: []
---

# 视频生成/图生视频/极致真人舞蹈视频迁移(Wan2.2-FunControl)_1954879516944601090.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1954879516944601090.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（54 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoEncode`
- `Reroute`
- `Reroute`
- `SetNode`
- `GetNode`
- `Reroute`
- `Note`
- `WanVideoSetBlockSwap`
- `Note`
- `GetNode`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `PrimitiveNode`
- `PrimitiveNode`
- `Note`
- `PrimitiveNode`
- `PrimitiveNode`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `MarkdownNote`
- `WanVideoEmptyEmbeds`
- `WanVideoControlEmbeds`
- `WanVideoEncode`
- `GetImageSizeAndCount`
- `PrimitiveInt`
- `PrimitiveInt`
- `ImageResizeKJv2`
- `Note`
- `SetNode`
- `VHS_VideoCombine`
- `Zoe-DepthMapPreprocessor`
- `DownloadAndLoadDepthAnythingV2Model`
- `DepthAnything_V2`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `ImageBlend`
- `ImageConcatMulti`
- `DWPreprocessor`

## 知识

覆盖率 **63%**（34/54）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoImageToVideoEncode`、`WanVideoSetBlockSwap`、`LoadImage`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoEmptyEmbeds`、`WanVideoControlEmbeds`、`WanVideoEncode`、`GetImageSizeAndCount`、`ImageResizeKJv2`、`VHS_VideoCombine`、`Zoe-DepthMapPreprocessor`、`DownloadAndLoadDepthAnythingV2Model`、`DepthAnything_V2`、`VHS_LoadVideo`、`WanVideoDecode`、`ImageBlend`、`ImageConcatMulti`、`DWPreprocessor`

**用到的条目**：LoadImage、DepthAnything_V2、DownloadAndLoadDepthAnythingV2Model、Zoe-DepthMapPreprocessor、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
