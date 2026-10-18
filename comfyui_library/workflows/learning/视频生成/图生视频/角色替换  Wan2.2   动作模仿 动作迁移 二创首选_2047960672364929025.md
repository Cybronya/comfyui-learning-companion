---
key: 视频生成/图生视频/角色替换  Wan2.2   动作模仿 动作迁移 二创首选_2047960672364929025.json
name: 角色替换  Wan2.2   动作模仿 动作迁移 二创首选_2047960672364929025.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/角色替换  Wan2.2   动作模仿 动作迁移 二创首选_2047960672364929025.json
hash: 4381d16508a8e2d7
coverage: 0.560976
learned_at: 2026-10-15 22:37:07
nodes: [OnnxDetectionModelLoader, GetNode, GetNode, WanVideoSetLoRAs, JWInteger, ImageFromBatch+, PreviewImage, INTConstant, INTConstant, GetNode, GetNode, ImageResizeKJv2, SetNode, GetNode, DrawMaskOnImage, easy cleanGpuUsed, SetNode, PoseAndFaceDetection, DrawViTPose, SetNode, easy cleanGpuUsed, SetNode, BlockifyMask, VHS_VideoCombine, SeCModelLoader, SeCVideoSegmentation, GrowMask, InvertMask, MaskToImage, SetNode, GetImageSizeAndCount, VHS_VideoCombine, LayerUtility: ImageBlend, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, INTConstant, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoTextEncodeCached, CR Text, WanVideoClipVisionEncode, easy cleanGpuUsed, WanVideoAnimateEmbeds, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, ImageConcanate, easy cleanGpuUsed, GetNode, VHS_VideoInfo, PreviewImage, VHS_VideoCombine, VHS_VideoCombine, SetNode, Note, SetNode, WanVideoLoraSelectMulti, WanVideoModelLoader, CLIPVisionLoader, SetNode, WanVideoVAELoader, WanVideoBlockSwap, WanVideoSetBlockSwap, LoadImage, VHS_LoadVideo, PointsEditor, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/角色替换  Wan2.2   动作模仿 动作迁移 二创首选_2047960672364929025.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2047960672364929025.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（82 个）：
- `OnnxDetectionModelLoader`
- `GetNode`
- `GetNode`
- `WanVideoSetLoRAs`
- `JWInteger`
- `ImageFromBatch+`
- `PreviewImage`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `DrawMaskOnImage`
- `easy cleanGpuUsed`
- `SetNode`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `SetNode`
- `easy cleanGpuUsed`
- `SetNode`
- `BlockifyMask`
- `VHS_VideoCombine`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `GrowMask`
- `InvertMask`
- `MaskToImage`
- `SetNode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `LayerUtility: ImageBlend`
- `GetNode`
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
- `CR Text`
- `WanVideoClipVisionEncode`
- `easy cleanGpuUsed`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `ImageConcanate`
- `easy cleanGpuUsed`
- `GetNode`
- `VHS_VideoInfo`
- `PreviewImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `Note`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `CLIPVisionLoader`
- `SetNode`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `LoadImage`
- `VHS_LoadVideo`
- `PointsEditor`
- `VHS_VideoCombine`

## 知识

覆盖率 **56%**（46/82）

**有卡**：`OnnxDetectionModelLoader`、`WanVideoSetLoRAs`、`JWInteger`、`ImageFromBatch+`、`INTConstant`、`ImageResizeKJv2`、`DrawMaskOnImage`、`easy cleanGpuUsed`、`PoseAndFaceDetection`、`DrawViTPose`、`BlockifyMask`、`VHS_VideoCombine`、`SeCModelLoader`、`SeCVideoSegmentation`、`GrowMask`、`InvertMask`、`MaskToImage`、`GetImageSizeAndCount`、`LayerUtility: ImageBlend`、`WanVideoTextEncodeCached`、`CR Text`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoDecode`、`ImageConcanate`、`VHS_VideoInfo`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`LoadImage`、`VHS_LoadVideo`、`PointsEditor`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
