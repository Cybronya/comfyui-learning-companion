---
key: 视频生成/图生视频/人物替换     角色替换    二创首选  Wan2.2 wan22_2061909733405188097.json
name: 人物替换     角色替换    二创首选  Wan2.2 wan22_2061909733405188097.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/人物替换     角色替换    二创首选  Wan2.2 wan22_2061909733405188097.json
hash: 992e26838f9617bf
coverage: 0.560976
learned_at: 2026-10-15 22:38:58
nodes: [WanVideoLoraSelectMulti, GetNode, GetNode, WanVideoSetLoRAs, WanVideoVAELoader, INTConstant, INTConstant, GetNode, easy cleanGpuUsed, SetNode, PoseAndFaceDetection, DrawViTPose, SetNode, easy cleanGpuUsed, SetNode, BlockifyMask, SeCModelLoader, GrowMask, InvertMask, MaskToImage, SetNode, GetImageSizeAndCount, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, INTConstant, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoTextEncodeCached, WanVideoClipVisionEncode, easy cleanGpuUsed, WanVideoAnimateEmbeds, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, ImageConcanate, SetNode, CLIPVisionLoader, VHS_VideoCombine, SetNode, SetNode, WanVideoSetBlockSwap, WanVideoBlockSwap, ImageResizeKJv2, GetNode, GetNode, SetNode, ImageFromBatch+, SeCVideoSegmentation, LayerUtility: ImageBlend, JWInteger, GetNode, VHS_VideoInfo, CR Text, VHS_VideoCombine, PreviewImage, Note, DrawMaskOnImage, PreviewImage, OnnxDetectionModelLoader, GetNode, WanVideoModelLoader, easy cleanGpuUsed, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo, PointsEditor, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/人物替换     角色替换    二创首选  Wan2.2 wan22_2061909733405188097.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2061909733405188097.json`

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
- `GetNode`
- `easy cleanGpuUsed`
- `SetNode`
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
- `SetNode`
- `GetImageSizeAndCount`
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
- `SetNode`
- `CLIPVisionLoader`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `SetNode`
- `ImageFromBatch+`
- `SeCVideoSegmentation`
- `LayerUtility: ImageBlend`
- `JWInteger`
- `GetNode`
- `VHS_VideoInfo`
- `CR Text`
- `VHS_VideoCombine`
- `PreviewImage`
- `Note`
- `DrawMaskOnImage`
- `PreviewImage`
- `OnnxDetectionModelLoader`
- `GetNode`
- `WanVideoModelLoader`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `PointsEditor`
- `LoadImage`

## 知识

覆盖率 **56%**（46/82）

**有卡**：`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`INTConstant`、`easy cleanGpuUsed`、`PoseAndFaceDetection`、`DrawViTPose`、`BlockifyMask`、`SeCModelLoader`、`GrowMask`、`InvertMask`、`MaskToImage`、`GetImageSizeAndCount`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoDecode`、`ImageConcanate`、`CLIPVisionLoader`、`VHS_VideoCombine`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`ImageResizeKJv2`、`ImageFromBatch+`、`SeCVideoSegmentation`、`LayerUtility: ImageBlend`、`JWInteger`、`VHS_VideoInfo`、`CR Text`、`DrawMaskOnImage`、`OnnxDetectionModelLoader`、`WanVideoModelLoader`、`VHS_LoadVideo`、`PointsEditor`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
