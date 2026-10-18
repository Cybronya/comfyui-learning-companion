---
key: 视频生成/图生视频/人物替换  角色替换  Wan2.2   动作模仿 动作迁移 二创首选_2061517996736208897.json
name: 人物替换  角色替换  Wan2.2   动作模仿 动作迁移 二创首选_2061517996736208897.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/人物替换  角色替换  Wan2.2   动作模仿 动作迁移 二创首选_2061517996736208897.json
hash: 309f28766a2bf04f
coverage: 0.560976
learned_at: 2026-10-15 22:38:55
nodes: [OnnxDetectionModelLoader, GetNode, GetNode, WanVideoSetLoRAs, JWInteger, ImageFromBatch+, PreviewImage, INTConstant, INTConstant, GetNode, GetNode, ImageResizeKJv2, SetNode, GetNode, DrawMaskOnImage, easy cleanGpuUsed, SetNode, PoseAndFaceDetection, DrawViTPose, SetNode, easy cleanGpuUsed, SetNode, BlockifyMask, VHS_VideoCombine, SeCModelLoader, SeCVideoSegmentation, GrowMask, InvertMask, MaskToImage, SetNode, GetImageSizeAndCount, VHS_VideoCombine, LayerUtility: ImageBlend, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, INTConstant, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoTextEncodeCached, CR Text, WanVideoClipVisionEncode, easy cleanGpuUsed, WanVideoAnimateEmbeds, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, ImageConcanate, easy cleanGpuUsed, GetNode, VHS_VideoInfo, PreviewImage, VHS_VideoCombine, VHS_VideoCombine, SetNode, Note, SetNode, WanVideoLoraSelectMulti, CLIPVisionLoader, SetNode, WanVideoVAELoader, WanVideoBlockSwap, WanVideoSetBlockSwap, VHS_LoadVideo, PointsEditor, LoadImage, WanVideoModelLoader, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/人物替换  角色替换  Wan2.2   动作模仿 动作迁移 二创首选_2061517996736208897.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2061517996736208897.json`

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
- `CLIPVisionLoader`
- `SetNode`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `VHS_LoadVideo`
- `PointsEditor`
- `LoadImage`
- `WanVideoModelLoader`
- `VHS_VideoCombine`

## 知识

覆盖率 **56%**（46/82）

**有卡**：`OnnxDetectionModelLoader`、`WanVideoSetLoRAs`、`JWInteger`、`ImageFromBatch+`、`INTConstant`、`ImageResizeKJv2`、`DrawMaskOnImage`、`easy cleanGpuUsed`、`PoseAndFaceDetection`、`DrawViTPose`、`BlockifyMask`、`VHS_VideoCombine`、`SeCModelLoader`、`SeCVideoSegmentation`、`GrowMask`、`InvertMask`、`MaskToImage`、`GetImageSizeAndCount`、`LayerUtility: ImageBlend`、`WanVideoTextEncodeCached`、`CR Text`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoDecode`、`ImageConcanate`、`VHS_VideoInfo`、`WanVideoLoraSelectMulti`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`VHS_LoadVideo`、`PointsEditor`、`LoadImage`、`WanVideoModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
