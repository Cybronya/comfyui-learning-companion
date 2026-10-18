---
key: 视频生成/图生视频/人物替换   角色替换   二创首选  Wan2.2 wan22_2047879824609386498.json
name: 人物替换   角色替换   二创首选  Wan2.2 wan22_2047879824609386498.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/人物替换   角色替换   二创首选  Wan2.2 wan22_2047879824609386498.json
hash: d7cf9e4af7806c56
coverage: 0.560976
learned_at: 2026-10-15 22:37:07
nodes: [WanVideoModelLoader, WanVideoLoraSelectMulti, GetNode, GetNode, WanVideoSetLoRAs, WanVideoVAELoader, INTConstant, INTConstant, GetNode, easy cleanGpuUsed, SetNode, PoseAndFaceDetection, DrawViTPose, SetNode, easy cleanGpuUsed, SetNode, BlockifyMask, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, INTConstant, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoTextEncodeCached, WanVideoClipVisionEncode, easy cleanGpuUsed, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, ImageConcanate, easy cleanGpuUsed, SetNode, CLIPVisionLoader, VHS_VideoCombine, VHS_VideoCombine, SetNode, SetNode, WanVideoSetBlockSwap, WanVideoBlockSwap, VHS_VideoCombine, VHS_VideoInfo, CR Text, DrawMaskOnImage, ImageResizeKJv2, GetNode, GetNode, SetNode, PreviewImage, GetNode, WanVideoAnimateEmbeds, GetImageSizeAndCount, PreviewImage, Note, PointsEditor, LoadImage, VHS_LoadVideo, JWInteger, SeCModelLoader, SeCVideoSegmentation, InvertMask, MaskToImage, LayerUtility: ImageBlend, SetNode, ImageFromBatch+, GetNode, GrowMask, OnnxDetectionModelLoader, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/人物替换   角色替换   二创首选  Wan2.2 wan22_2047879824609386498.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2047879824609386498.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（82 个）：
- `WanVideoModelLoader`
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
- `VHS_VideoCombine`
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
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `CR Text`
- `DrawMaskOnImage`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `GetImageSizeAndCount`
- `PreviewImage`
- `Note`
- `PointsEditor`
- `LoadImage`
- `VHS_LoadVideo`
- `JWInteger`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `InvertMask`
- `MaskToImage`
- `LayerUtility: ImageBlend`
- `SetNode`
- `ImageFromBatch+`
- `GetNode`
- `GrowMask`
- `OnnxDetectionModelLoader`
- `VHS_VideoCombine`

## 知识

覆盖率 **56%**（46/82）

**有卡**：`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`INTConstant`、`easy cleanGpuUsed`、`PoseAndFaceDetection`、`DrawViTPose`、`BlockifyMask`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`ImageConcanate`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`VHS_VideoInfo`、`CR Text`、`DrawMaskOnImage`、`ImageResizeKJv2`、`WanVideoAnimateEmbeds`、`PointsEditor`、`LoadImage`、`VHS_LoadVideo`、`JWInteger`、`SeCModelLoader`、`SeCVideoSegmentation`、`InvertMask`、`MaskToImage`、`LayerUtility: ImageBlend`、`ImageFromBatch+`、`GrowMask`、`OnnxDetectionModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
