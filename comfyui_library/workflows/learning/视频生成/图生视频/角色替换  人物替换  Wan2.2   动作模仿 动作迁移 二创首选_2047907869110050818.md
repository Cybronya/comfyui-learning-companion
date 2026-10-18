---
key: 视频生成/图生视频/角色替换  人物替换  Wan2.2   动作模仿 动作迁移 二创首选_2047907869110050818.json
name: 角色替换  人物替换  Wan2.2   动作模仿 动作迁移 二创首选_2047907869110050818.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/角色替换  人物替换  Wan2.2   动作模仿 动作迁移 二创首选_2047907869110050818.json
hash: 3674f3e0a556f9b0
coverage: 0.56962
learned_at: 2026-10-15 22:37:07
nodes: [OnnxDetectionModelLoader, GetNode, GetNode, VHS_VideoCombine, WanVideoSetLoRAs, GetNode, SetNode, GetNode, DrawMaskOnImage, easy cleanGpuUsed, SetNode, DrawViTPose, SetNode, easy cleanGpuUsed, SetNode, BlockifyMask, SeCModelLoader, SeCVideoSegmentation, GrowMask, InvertMask, MaskToImage, LayerUtility: ImageBlend, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoTextEncodeCached, CR Text, WanVideoClipVisionEncode, easy cleanGpuUsed, WanVideoAnimateEmbeds, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, ImageConcanate, easy cleanGpuUsed, GetNode, VHS_VideoCombine, Note, WanVideoLoraSelectMulti, WanVideoModelLoader, CLIPVisionLoader, SetNode, WanVideoVAELoader, WanVideoBlockSwap, WanVideoSetBlockSwap, GetNode, GetNode, PreviewImage, ImageResizeKJv2, LoadImage, JWInteger, ImageFromBatch+, PreviewImage, PointsEditor, SetNode, SetNode, GetImageSize, SetNode, SetNode, VHS_VideoInfo, INTConstant, VHS_LoadVideo, PoseAndFaceDetection, GetNode, GetImageSizeAndCount, VHS_VideoCombine, VHS_VideoCombine, SetNode, VHS_VideoCombine, SetNode]
patterns: []
missing: []
---

# 视频生成/图生视频/角色替换  人物替换  Wan2.2   动作模仿 动作迁移 二创首选_2047907869110050818.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2047907869110050818.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（79 个）：
- `OnnxDetectionModelLoader`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoSetLoRAs`
- `GetNode`
- `SetNode`
- `GetNode`
- `DrawMaskOnImage`
- `easy cleanGpuUsed`
- `SetNode`
- `DrawViTPose`
- `SetNode`
- `easy cleanGpuUsed`
- `SetNode`
- `BlockifyMask`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `GrowMask`
- `InvertMask`
- `MaskToImage`
- `LayerUtility: ImageBlend`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
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
- `VHS_VideoCombine`
- `Note`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `CLIPVisionLoader`
- `SetNode`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `ImageResizeKJv2`
- `LoadImage`
- `JWInteger`
- `ImageFromBatch+`
- `PreviewImage`
- `PointsEditor`
- `SetNode`
- `SetNode`
- `GetImageSize`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `INTConstant`
- `VHS_LoadVideo`
- `PoseAndFaceDetection`
- `GetNode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `VHS_VideoCombine`
- `SetNode`

## 知识

覆盖率 **57%**（45/79）

**有卡**：`OnnxDetectionModelLoader`、`VHS_VideoCombine`、`WanVideoSetLoRAs`、`DrawMaskOnImage`、`easy cleanGpuUsed`、`DrawViTPose`、`BlockifyMask`、`SeCModelLoader`、`SeCVideoSegmentation`、`GrowMask`、`InvertMask`、`MaskToImage`、`LayerUtility: ImageBlend`、`WanVideoTextEncodeCached`、`CR Text`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`ImageConcanate`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`ImageResizeKJv2`、`LoadImage`、`JWInteger`、`ImageFromBatch+`、`PointsEditor`、`GetImageSize`、`VHS_VideoInfo`、`INTConstant`、`VHS_LoadVideo`、`PoseAndFaceDetection`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
