---
key: 平台全量/Wan2.2-VACE视频物品重绘_1981639602450644994.json
name: Wan2.2-VACE视频物品重绘_1981639602450644994
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2-VACE视频物品重绘_1981639602450644994.json
hash: 7d5831b9895292e9
coverage: 0.972973
learned_at: 2026-11-14 01:06:05
nodes: [WanVideoBlockSwap, WanVideoVACEModelSelect, INTConstant, WanVideoVACEModelSelect, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, INTConstant, VHS_LoadVideo, WanVideoVAELoader, INTConstant, WanVideoSampler, WanVideoSampler, SeCModelLoader, PreviewImage, WanVideoModelLoader, ImageResizeKJv2, WanVideoSetBlockSwap, WanVideoSetBlockSwap, CreateCFGScheduleFloatList, WanVideoTextEncodeCached, WanVideoDecode, VHS_VideoCombine, MaskToImage, SolidMask, VHS_VideoCombine, SeCVideoSegmentation, GrowMask, WanVideoModelLoader, INTConstant, INTConstant, LoadImage, SimpleMath+, ImageCompositeMasked, PointsEditor, ImageResizeKJv2, WanVideoVACEEncode]
patterns: []
missing: []
---

# 平台全量/Wan2.2-VACE视频物品重绘_1981639602450644994.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2-VACE视频物品重绘_1981639602450644994.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（37 个）：
- `WanVideoBlockSwap`
- `WanVideoVACEModelSelect`
- `INTConstant`
- `WanVideoVACEModelSelect`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `INTConstant`
- `VHS_LoadVideo`
- `WanVideoVAELoader`
- `INTConstant`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `SeCModelLoader`
- `PreviewImage`
- `WanVideoModelLoader`
- `ImageResizeKJv2`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `CreateCFGScheduleFloatList`
- `WanVideoTextEncodeCached`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `MaskToImage`
- `SolidMask`
- `VHS_VideoCombine`
- `SeCVideoSegmentation`
- `GrowMask`
- `WanVideoModelLoader`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `SimpleMath+`
- `ImageCompositeMasked`
- `PointsEditor`
- `ImageResizeKJv2`
- `WanVideoVACEEncode`

## 知识

覆盖率 **97%**（36/37）

**有卡**：`WanVideoBlockSwap`、`WanVideoVACEModelSelect`、`INTConstant`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`VHS_LoadVideo`、`WanVideoVAELoader`、`WanVideoSampler`、`SeCModelLoader`、`WanVideoModelLoader`、`ImageResizeKJv2`、`WanVideoSetBlockSwap`、`CreateCFGScheduleFloatList`、`WanVideoTextEncodeCached`、`WanVideoDecode`、`VHS_VideoCombine`、`MaskToImage`、`SolidMask`、`SeCVideoSegmentation`、`GrowMask`、`LoadImage`、`SimpleMath+`、`ImageCompositeMasked`、`PointsEditor`、`WanVideoVACEEncode`

**用到的条目**：LoadImage、CreateCFGScheduleFloatList、WanVideoSampler、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVACEEncode、WanVideoVAELoader、WanVideoLoraSelectMulti
