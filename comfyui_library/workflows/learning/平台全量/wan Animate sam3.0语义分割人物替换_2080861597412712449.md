---
key: 平台全量/wan Animate sam3.0语义分割人物替换_2080861597412712449.json
name: wan Animate sam3.0语义分割人物替换_2080861597412712449
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan Animate sam3.0语义分割人物替换_2080861597412712449.json
hash: 936f637f4fa974cb
coverage: 0.588235
learned_at: 2026-11-14 01:18:55
nodes: [GetNode, WanVideoClipVisionEncode, GetNode, CLIPVisionLoader, ImageCropByMaskAndResize, DWPreprocessor, WanVideoModelLoader, LayerUtility: PurgeVRAM, WanVideoSetLoRAs, LayerUtility: PurgeVRAM, FaceMaskFromPoseKeypoints, PixelPerfectResolution, Reroute, WanVideoVAELoader, SetNode, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, SetNode, SetNode, SetNode, SetNode, GetNode, WanVideoSampler, SetNode, MarkdownNote, easy sam3VideoModelExtraConfig, easy sam3ModelLoader, PreviewImage, WanVideoTextEncodeCached, GetNode, GetNode, JWInteger, JWInteger, SetNode, WanVideoDecode, GetNode, GetNode, GetNode, GetNode, GetNode, GrowMask, GetNode, easy sam3Visualization, BlockifyMask, CR Text, SetNode, DrawMaskOnImage, SetNode, GetNode, Int, easy sam3VideoSegmentation, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, DownloadAndLoadGIMMVFIModel, CR Text, easy showAnything, easy cleanGpuUsed, WanVideoBlockSwap, GIMMVFI_interpolate, SetNode, GetNode, GetNode, WanVideoAnimateEmbeds, LoadImage, VHS_VideoInfo, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/wan Animate sam3.0语义分割人物替换_2080861597412712449.json

> 来源文件 `comfyui_library/workflows/平台全量/wan Animate sam3.0语义分割人物替换_2080861597412712449.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（68 个）：
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `CLIPVisionLoader`
- `ImageCropByMaskAndResize`
- `DWPreprocessor`
- `WanVideoModelLoader`
- `LayerUtility: PurgeVRAM`
- `WanVideoSetLoRAs`
- `LayerUtility: PurgeVRAM`
- `FaceMaskFromPoseKeypoints`
- `PixelPerfectResolution`
- `Reroute`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `SetNode`
- `MarkdownNote`
- `easy sam3VideoModelExtraConfig`
- `easy sam3ModelLoader`
- `PreviewImage`
- `WanVideoTextEncodeCached`
- `GetNode`
- `GetNode`
- `JWInteger`
- `JWInteger`
- `SetNode`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GrowMask`
- `GetNode`
- `easy sam3Visualization`
- `BlockifyMask`
- `CR Text`
- `SetNode`
- `DrawMaskOnImage`
- `SetNode`
- `GetNode`
- `Int`
- `easy sam3VideoSegmentation`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `DownloadAndLoadGIMMVFIModel`
- `CR Text`
- `easy showAnything`
- `easy cleanGpuUsed`
- `WanVideoBlockSwap`
- `GIMMVFI_interpolate`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `LoadImage`
- `VHS_VideoInfo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`

## 知识

覆盖率 **59%**（40/68）

**有卡**：`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`ImageCropByMaskAndResize`、`DWPreprocessor`、`WanVideoModelLoader`、`LayerUtility: PurgeVRAM`、`WanVideoSetLoRAs`、`FaceMaskFromPoseKeypoints`、`PixelPerfectResolution`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoSampler`、`easy sam3VideoModelExtraConfig`、`easy sam3ModelLoader`、`WanVideoTextEncodeCached`、`JWInteger`、`WanVideoDecode`、`GrowMask`、`easy sam3Visualization`、`BlockifyMask`、`CR Text`、`DrawMaskOnImage`、`Int`、`easy sam3VideoSegmentation`、`LayerUtility: ImageScaleByAspectRatio V2`、`DownloadAndLoadGIMMVFIModel`、`easy cleanGpuUsed`、`WanVideoBlockSwap`、`GIMMVFI_interpolate`、`WanVideoAnimateEmbeds`、`LoadImage`、`VHS_VideoInfo`、`VHS_VideoCombine`、`VHS_LoadVideo`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti
