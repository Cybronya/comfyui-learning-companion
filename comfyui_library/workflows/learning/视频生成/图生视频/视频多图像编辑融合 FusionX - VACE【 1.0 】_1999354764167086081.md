---
key: 视频生成/图生视频/视频多图像编辑融合 FusionX - VACE【 1.0 】_1999354764167086081.json
name: 视频多图像编辑融合 FusionX - VACE【 1.0 】_1999354764167086081.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1999354764167086081.json
hash: 5e680f02b5c1d6fd
coverage: 0.805556
learned_at: 2026-10-15 22:33:36
nodes: [WanVideoTorchCompileSettings, SetNode, SetNode, SetNode, LoadImage, LoadImage, ImageConcanate, Primitive integer [Crystools], Primitive integer [Crystools], WanVideoBlockSwap, SimpleMath+, SimpleMath+, WanVideoTextEncodeSingle, WanVideoTextEncodeSingle, WanVideoVACEEncode, WanVideoApplyNAG, WanVideoSampler, WanVideoDecode, VHS_VideoCombine, PreviewImage, LayerUtility: ImageRemoveAlpha, ImageResizeKJ, WanVideoModelLoader, WanVideoVAELoader, LoadWanVideoT5TextEncoder, GetNode, GetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, Primitive integer [Crystools], Primitive integer [Crystools], InspyrenetRembg, LoadImage, InspyrenetRembg, LayerUtility: ImageRemoveAlpha, CR Text]
patterns: []
missing: []
---

# 视频生成/图生视频/视频多图像编辑融合 FusionX - VACE【 1.0 】_1999354764167086081.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1999354764167086081.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（36 个）：
- `WanVideoTorchCompileSettings`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `ImageConcanate`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `WanVideoBlockSwap`
- `SimpleMath+`
- `SimpleMath+`
- `WanVideoTextEncodeSingle`
- `WanVideoTextEncodeSingle`
- `WanVideoVACEEncode`
- `WanVideoApplyNAG`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `PreviewImage`
- `LayerUtility: ImageRemoveAlpha`
- `ImageResizeKJ`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `InspyrenetRembg`
- `LoadImage`
- `InspyrenetRembg`
- `LayerUtility: ImageRemoveAlpha`
- `CR Text`

## 知识

覆盖率 **81%**（29/36）

**有卡**：`WanVideoTorchCompileSettings`、`LoadImage`、`ImageConcanate`、`Primitive integer [Crystools]`、`WanVideoBlockSwap`、`SimpleMath+`、`WanVideoTextEncodeSingle`、`WanVideoVACEEncode`、`WanVideoApplyNAG`、`WanVideoSampler`、`WanVideoDecode`、`VHS_VideoCombine`、`LayerUtility: ImageRemoveAlpha`、`ImageResizeKJ`、`WanVideoModelLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`LayerUtility: ImageScaleByAspectRatio V2`、`InspyrenetRembg`、`CR Text`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeSingle、WanVideoVACEEncode
