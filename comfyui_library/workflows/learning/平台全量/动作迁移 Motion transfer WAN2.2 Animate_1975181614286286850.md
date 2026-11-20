---
key: 平台全量/动作迁移 Motion transfer WAN2.2 Animate_1975181614286286850.json
name: 动作迁移 Motion transfer WAN2.2 Animate_1975181614286286850
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/动作迁移 Motion transfer WAN2.2 Animate_1975181614286286850.json
hash: 52aa5150f68cb4bc
coverage: 0.647059
learned_at: 2026-11-14 01:44:44
nodes: [WanVideoBlockSwap, Anything Everywhere3, WanVideoVAELoader, Seed Everywhere, LayerUtility: PurgeVRAM V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, Text Multiline, GetNode, GetNode, MathExpression|pysssss, MathExpression|pysssss, Int, WanVideoTorchCompileSettings, WanVideoEncode, WanVideoUni3C_ControlnetLoader, PixelPerfectResolution, DWPreprocessor, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, SetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, WanVideoTextEncodeCached, GetNode, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, ImageResize+, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoCombine, GetNode, Anything Everywhere, WanVideoUni3C_embeds, GetNode, WanVideoModelLoader, WanVideoSampler, WanVideoDecode, VHS_VideoCombine, LayerUtility: PurgeVRAM V2, WanVideoLoraSelectMulti, LoadImage, VHS_LoadVideo, Int]
patterns: []
missing: []
---

# 平台全量/动作迁移 Motion transfer WAN2.2 Animate_1975181614286286850.json

> 来源文件 `comfyui_library/workflows/平台全量/动作迁移 Motion transfer WAN2.2 Animate_1975181614286286850.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（51 个）：
- `WanVideoBlockSwap`
- `Anything Everywhere3`
- `WanVideoVAELoader`
- `Seed Everywhere`
- `LayerUtility: PurgeVRAM V2`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `Text Multiline`
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `Int`
- `WanVideoTorchCompileSettings`
- `WanVideoEncode`
- `WanVideoUni3C_ControlnetLoader`
- `PixelPerfectResolution`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `GetNode`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoAnimateEmbeds`
- `ImageResize+`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `Anything Everywhere`
- `WanVideoUni3C_embeds`
- `GetNode`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoLoraSelectMulti`
- `LoadImage`
- `VHS_LoadVideo`
- `Int`

## 知识

覆盖率 **65%**（33/51）

**有卡**：`WanVideoBlockSwap`、`WanVideoVAELoader`、`Seed Everywhere`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`Text Multiline`、`MathExpression|pysssss`、`Int`、`WanVideoTorchCompileSettings`、`WanVideoEncode`、`WanVideoUni3C_ControlnetLoader`、`PixelPerfectResolution`、`DWPreprocessor`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`ImageResize+`、`WanVideoUni3C_embeds`、`WanVideoModelLoader`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoLoraSelectMulti`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoUni3C_ControlnetLoader、Seed Everywhere、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode
