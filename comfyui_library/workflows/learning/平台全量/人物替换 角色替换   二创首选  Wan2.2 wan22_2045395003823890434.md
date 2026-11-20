---
key: 平台全量/人物替换 角色替换   二创首选  Wan2.2 wan22_2045395003823890434.json
name: 人物替换 角色替换   二创首选  Wan2.2 wan22_2045395003823890434
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/人物替换 角色替换   二创首选  Wan2.2 wan22_2045395003823890434.json
hash: dfefe314235ecd5c
coverage: 0.560976
learned_at: 2026-11-14 01:37:36
nodes: [GetNode, WanVideoSetLoRAs, JWInteger, ImageFromBatch+, PreviewImage, INTConstant, INTConstant, InvertMask, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy cleanGpuUsed, GetNode, Note, WanVideoSetBlockSwap, VHS_LoadVideo, WanVideoVAELoader, SetNode, CLIPVisionLoader, GetNode, CR Text, WanVideoTextEncodeCached, WanVideoClipVisionEncode, WanVideoSampler, WanVideoAnimateEmbeds, easy cleanGpuUsed, WanVideoDecode, GetImageSizeAndCount, ImageConcanate, GetImageSizeAndCount, SetNode, OnnxDetectionModelLoader, SeCModelLoader, SeCVideoSegmentation, GrowMask, MaskToImage, BlockifyMask, SetNode, DrawMaskOnImage, GetNode, easy cleanGpuUsed, SetNode, SetNode, VHS_VideoCombine, PoseAndFaceDetection, DrawViTPose, easy cleanGpuUsed, SetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, LayerUtility: ImageBlend, GetNode, VHS_VideoInfo, SetNode, SetNode, WanVideoBlockSwap, WanVideoLoraSelectMulti, GetNode, WanVideoModelLoader, ImageResizeKJv2, PreviewImage, GetNode, SetNode, PointsEditor, INTConstant, LoadImage, GetNode, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/人物替换 角色替换   二创首选  Wan2.2 wan22_2045395003823890434.json

> 来源文件 `comfyui_library/workflows/平台全量/人物替换 角色替换   二创首选  Wan2.2 wan22_2045395003823890434.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（82 个）：
- `GetNode`
- `WanVideoSetLoRAs`
- `JWInteger`
- `ImageFromBatch+`
- `PreviewImage`
- `INTConstant`
- `INTConstant`
- `InvertMask`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `Note`
- `WanVideoSetBlockSwap`
- `VHS_LoadVideo`
- `WanVideoVAELoader`
- `SetNode`
- `CLIPVisionLoader`
- `GetNode`
- `CR Text`
- `WanVideoTextEncodeCached`
- `WanVideoClipVisionEncode`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `ImageConcanate`
- `GetImageSizeAndCount`
- `SetNode`
- `OnnxDetectionModelLoader`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `GrowMask`
- `MaskToImage`
- `BlockifyMask`
- `SetNode`
- `DrawMaskOnImage`
- `GetNode`
- `easy cleanGpuUsed`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `easy cleanGpuUsed`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LayerUtility: ImageBlend`
- `GetNode`
- `VHS_VideoInfo`
- `SetNode`
- `SetNode`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `WanVideoModelLoader`
- `ImageResizeKJv2`
- `PreviewImage`
- `GetNode`
- `SetNode`
- `PointsEditor`
- `INTConstant`
- `LoadImage`
- `GetNode`
- `VHS_VideoCombine`

## 知识

覆盖率 **56%**（46/82）

**有卡**：`WanVideoSetLoRAs`、`JWInteger`、`ImageFromBatch+`、`INTConstant`、`InvertMask`、`easy cleanGpuUsed`、`WanVideoSetBlockSwap`、`VHS_LoadVideo`、`WanVideoVAELoader`、`CLIPVisionLoader`、`CR Text`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`WanVideoDecode`、`GetImageSizeAndCount`、`ImageConcanate`、`OnnxDetectionModelLoader`、`SeCModelLoader`、`SeCVideoSegmentation`、`GrowMask`、`MaskToImage`、`BlockifyMask`、`DrawMaskOnImage`、`VHS_VideoCombine`、`PoseAndFaceDetection`、`DrawViTPose`、`LayerUtility: ImageBlend`、`VHS_VideoInfo`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`ImageResizeKJv2`、`PointsEditor`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
