---
key: 数字人/数字人/人物替换   角色替换   二创首选  Wan2.2 wan22_2045772090871123969.json
name: 人物替换   角色替换   二创首选  Wan2.2 wan22_2045772090871123969
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/人物替换   角色替换   二创首选  Wan2.2 wan22_2045772090871123969.json
hash: 11b278ca34a3d665
coverage: 0.560976
learned_at: 2026-10-26 02:00:16
nodes: [WanVideoLoraSelectMulti, GetNode, GetNode, WanVideoSetLoRAs, WanVideoVAELoader, INTConstant, INTConstant, PoseAndFaceDetection, DrawViTPose, SetNode, easy cleanGpuUsed, SetNode, BlockifyMask, SeCModelLoader, GrowMask, InvertMask, MaskToImage, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, INTConstant, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoTextEncodeCached, WanVideoClipVisionEncode, easy cleanGpuUsed, WanVideoAnimateEmbeds, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, ImageConcanate, easy cleanGpuUsed, SetNode, CLIPVisionLoader, VHS_VideoCombine, VHS_VideoCombine, SetNode, SetNode, WanVideoSetBlockSwap, WanVideoBlockSwap, GetNode, GetNode, SetNode, PreviewImage, ImageFromBatch+, SeCVideoSegmentation, JWInteger, VHS_VideoInfo, CR Text, PreviewImage, Note, VHS_LoadVideo, PointsEditor, LoadImage, VHS_VideoCombine, GetNode, VHS_VideoCombine, SetNode, easy cleanGpuUsed, DrawMaskOnImage, GetNode, WanVideoModelLoader, ImageResizeKJv2, GetNode, LayerUtility: ImageBlend, SetNode, GetImageSizeAndCount, OnnxDetectionModelLoader, VHS_VideoCombine]
patterns: []
missing: []
---

# 数字人/数字人/人物替换   角色替换   二创首选  Wan2.2 wan22_2045772090871123969.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/人物替换   角色替换   二创首选  Wan2.2 wan22_2045772090871123969.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（82 个）：
- `WanVideoLoraSelectMulti`
- `GetNode`
- `GetNode`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `INTConstant`
- `INTConstant`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `SetNode`
- `easy cleanGpuUsed`
- `SetNode`
- `BlockifyMask`
- `SeCModelLoader`
- `GrowMask`
- `InvertMask`
- `MaskToImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `WanVideoClipVisionEncode`
- `easy cleanGpuUsed`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `ImageConcanate`
- `easy cleanGpuUsed`
- `SetNode`
- `CLIPVisionLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `GetNode`
- `GetNode`
- `SetNode`
- `PreviewImage`
- `ImageFromBatch+`
- `SeCVideoSegmentation`
- `JWInteger`
- `VHS_VideoInfo`
- `CR Text`
- `PreviewImage`
- `Note`
- `VHS_LoadVideo`
- `PointsEditor`
- `LoadImage`
- `VHS_VideoCombine`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `easy cleanGpuUsed`
- `DrawMaskOnImage`
- `GetNode`
- `WanVideoModelLoader`
- `ImageResizeKJv2`
- `GetNode`
- `LayerUtility: ImageBlend`
- `SetNode`
- `GetImageSizeAndCount`
- `OnnxDetectionModelLoader`
- `VHS_VideoCombine`

## 知识

覆盖率 **56%**（46/82）

**有卡**：`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`INTConstant`、`PoseAndFaceDetection`、`DrawViTPose`、`easy cleanGpuUsed`、`BlockifyMask`、`SeCModelLoader`、`GrowMask`、`InvertMask`、`MaskToImage`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`ImageConcanate`、`CLIPVisionLoader`、`VHS_VideoCombine`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`ImageFromBatch+`、`SeCVideoSegmentation`、`JWInteger`、`VHS_VideoInfo`、`CR Text`、`VHS_LoadVideo`、`PointsEditor`、`LoadImage`、`DrawMaskOnImage`、`WanVideoModelLoader`、`ImageResizeKJv2`、`LayerUtility: ImageBlend`、`OnnxDetectionModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
