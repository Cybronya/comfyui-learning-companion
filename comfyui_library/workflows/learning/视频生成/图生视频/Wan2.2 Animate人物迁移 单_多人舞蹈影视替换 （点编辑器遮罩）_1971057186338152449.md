---
key: 视频生成/图生视频/Wan2.2 Animate人物迁移 单_多人舞蹈影视替换 （点编辑器遮罩）_1971057186338152449.json
name: Wan2.2 Animate人物迁移 单_多人舞蹈影视替换 （点编辑器遮罩）_1971057186338152449.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1971057186338152449.json
hash: 7039c709a015d4ac
coverage: 0.457447
learned_at: 2026-10-15 22:31:55
nodes: [Fast Groups Bypasser (rgthree), WanVideoDecode, GetNode, GetNode, GetImageSizeAndCount, GetNode, GetNode, GetNode, GetNode, LayerUtility: PurgeVRAM, ImageConcatMulti, GetNode, PixelPerfectResolution, FaceMaskFromPoseKeypoints, GetNode, ImageResizeKJv2, CLIPVisionLoader, GetNode, WanVideoClipVisionEncode, LayerUtility: PurgeVRAM, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, WanVideoAnimateEmbeds, SetNode, GetNode, SetNode, WanVideoSampler, GetNode, WanVideoTorchCompileSettings, SetNode, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, SetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, Sam2Segmentation, DownloadAndLoadSAM2Model, BlockifyMask, Note, SetNode, DrawMaskOnImage, GetNode, GetNode, VHS_VideoCombine, VHS_VideoInfo, SetNode, GetNode, easy showAnything, easy showAnything, Int, Note, Note, Note, SetNode, VHS_LoadVideo, Note, DWPreprocessor, SetNode, LayerUtility: PurgeVRAM, GetNode, PointsEditor, GetNode, ImageConcatMulti, LayerUtility: PurgeVRAM, GetImageSizeAndCount, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, GetNode, VHS_VideoCombine, Int, Int, GrowMask, ImageCropByMaskAndResize, VHS_VideoCombine, LoadImage, WanVideoTextEncodeCached, WanVideoModelLoader, WanVideoVAELoader]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Animate人物迁移 单_多人舞蹈影视替换 （点编辑器遮罩）_1971057186338152449.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1971057186338152449.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（94 个）：
- `Fast Groups Bypasser (rgthree)`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `ImageConcatMulti`
- `GetNode`
- `PixelPerfectResolution`
- `FaceMaskFromPoseKeypoints`
- `GetNode`
- `ImageResizeKJv2`
- `CLIPVisionLoader`
- `GetNode`
- `WanVideoClipVisionEncode`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVideoAnimateEmbeds`
- `SetNode`
- `GetNode`
- `SetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Sam2Segmentation`
- `DownloadAndLoadSAM2Model`
- `BlockifyMask`
- `Note`
- `SetNode`
- `DrawMaskOnImage`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `SetNode`
- `GetNode`
- `easy showAnything`
- `easy showAnything`
- `Int`
- `Note`
- `Note`
- `Note`
- `SetNode`
- `VHS_LoadVideo`
- `Note`
- `DWPreprocessor`
- `SetNode`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `PointsEditor`
- `GetNode`
- `ImageConcatMulti`
- `LayerUtility: PurgeVRAM`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `VHS_VideoCombine`
- `Int`
- `Int`
- `GrowMask`
- `ImageCropByMaskAndResize`
- `VHS_VideoCombine`
- `LoadImage`
- `WanVideoTextEncodeCached`
- `WanVideoModelLoader`
- `WanVideoVAELoader`

## 知识

覆盖率 **46%**（43/94）

**有卡**：`WanVideoDecode`、`GetImageSizeAndCount`、`LayerUtility: PurgeVRAM`、`ImageConcatMulti`、`PixelPerfectResolution`、`FaceMaskFromPoseKeypoints`、`ImageResizeKJv2`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`Sam2Segmentation`、`DownloadAndLoadSAM2Model`、`BlockifyMask`、`DrawMaskOnImage`、`VHS_VideoCombine`、`VHS_VideoInfo`、`Int`、`VHS_LoadVideo`、`DWPreprocessor`、`PointsEditor`、`GrowMask`、`ImageCropByMaskAndResize`、`LoadImage`、`WanVideoTextEncodeCached`、`WanVideoModelLoader`、`WanVideoVAELoader`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
