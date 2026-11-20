---
key: 平台全量/Wan2.2 Animate人物替换 二创视频恶搞视频二创动漫视频形象替换 角色替换 人物更换_2079906862341906434.json
name: Wan2.2 Animate人物替换 二创视频恶搞视频二创动漫视频形象替换 角色替换 人物更换_2079906862341906434
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Animate人物替换 二创视频恶搞视频二创动漫视频形象替换 角色替换 人物更换_2079906862341906434.json
hash: b72f5eafb986f6fa
coverage: 0.518072
learned_at: 2026-11-14 01:05:08
nodes: [GetNode, WanVideoDecode, GetNode, VHS_VideoCombine, DrawViTPose, OnnxDetectionModelLoader, CLIPVisionLoader, PoseAndFaceDetection, LayerUtility: ImageBlend, SetNode, DrawMaskOnImage, GetNode, SetNode, Reroute, MaskToImage, SeCModelLoader, InvertMask, Reroute, GetImageSizeAndCount, GetNode, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoClipVisionEncode, WanVideoSampler, SetNode, GetNode, VHS_VideoCombine, SetNode, ImageFromBatch+, PreviewImage, PreviewImage, Reroute, Reroute, ImageConcanate, VHS_VideoCombine, ImageResizeKJv2, PreviewImage, Reroute, WanVideoTextEncodeCached, SeCVideoSegmentation, INTConstant, INTConstant, SetNode, SetNode, WanVideoVAELoader, SetNode, WanVideoSetLoRAs, GetNode, GetNode, GetNode, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, Note, VHS_VideoCombine, CR Text, JWInteger, BlockifyMask, GrowMask, Note, Note, WanVideoAnimateEmbeds, INTConstant, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetImageSizeAndCount, VHS_VideoInfo, PreviewImage, VHS_LoadVideo, PointsEditor, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
---

# 平台全量/Wan2.2 Animate人物替换 二创视频恶搞视频二创动漫视频形象替换 角色替换 人物更换_2079906862341906434.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Animate人物替换 二创视频恶搞视频二创动漫视频形象替换 角色替换 人物更换_2079906862341906434.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（83 个）：
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `VHS_VideoCombine`
- `DrawViTPose`
- `OnnxDetectionModelLoader`
- `CLIPVisionLoader`
- `PoseAndFaceDetection`
- `LayerUtility: ImageBlend`
- `SetNode`
- `DrawMaskOnImage`
- `GetNode`
- `SetNode`
- `Reroute`
- `MaskToImage`
- `SeCModelLoader`
- `InvertMask`
- `Reroute`
- `GetImageSizeAndCount`
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoClipVisionEncode`
- `WanVideoSampler` ★核心
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `ImageFromBatch+`
- `PreviewImage`
- `PreviewImage`
- `Reroute`
- `Reroute`
- `ImageConcanate`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `PreviewImage`
- `Reroute`
- `WanVideoTextEncodeCached`
- `SeCVideoSegmentation`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoSetLoRAs`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `Note`
- `VHS_VideoCombine`
- `CR Text`
- `JWInteger`
- `BlockifyMask`
- `GrowMask`
- `Note`
- `Note`
- `WanVideoAnimateEmbeds`
- `INTConstant`
- `GetNode`
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
- `SetNode`
- `GetImageSizeAndCount`
- `VHS_VideoInfo`
- `PreviewImage`
- `VHS_LoadVideo`
- `PointsEditor`
- `VHS_VideoCombine`
- `LoadImage`

## 知识

覆盖率 **52%**（43/83）

**有卡**：`WanVideoDecode`、`VHS_VideoCombine`、`DrawViTPose`、`OnnxDetectionModelLoader`、`CLIPVisionLoader`、`PoseAndFaceDetection`、`LayerUtility: ImageBlend`、`DrawMaskOnImage`、`MaskToImage`、`SeCModelLoader`、`InvertMask`、`GetImageSizeAndCount`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoClipVisionEncode`、`WanVideoSampler`、`ImageFromBatch+`、`ImageConcanate`、`ImageResizeKJv2`、`WanVideoTextEncodeCached`、`SeCVideoSegmentation`、`INTConstant`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`、`CR Text`、`JWInteger`、`BlockifyMask`、`GrowMask`、`WanVideoAnimateEmbeds`、`VHS_VideoInfo`、`VHS_LoadVideo`、`PointsEditor`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
