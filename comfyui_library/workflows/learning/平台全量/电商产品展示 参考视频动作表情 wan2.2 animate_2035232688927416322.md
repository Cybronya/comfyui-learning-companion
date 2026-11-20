---
key: 平台全量/电商产品展示 参考视频动作表情 wan2.2 animate_2035232688927416322.json
name: 电商产品展示 参考视频动作表情 wan2.2 animate_2035232688927416322
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/电商产品展示 参考视频动作表情 wan2.2 animate_2035232688927416322.json
hash: 5e7e82104fa08120
coverage: 0.54902
learned_at: 2026-11-14 02:23:01
nodes: [Anything Everywhere3, WanVideoVAELoader, GetNode, Seed Everywhere, SetNode, WanVideoClipVisionEncode, CLIPVisionLoader, WanVideoDecode, WanVideoLoraSelectMulti, GetNode, GetNode, PixelPerfectResolution, ImageCropByMaskAndResize, DWPreprocessor, WanVideoSampler, FaceMaskFromPoseKeypoints, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, LayerUtility: PurgeVRAM V2, WanVideoModelLoader, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, MathExpression|pysssss, WanVideoTorchCompileSettings, WanVideoBlockSwap, MathExpression|pysssss, Int, LayerUtility: PurgeVRAM V2, Int, VHS_LoadVideo, VHS_VideoCombine, LoadImage, WanVideoAnimateEmbeds, GetNode, WanVideoTextEncodeCached, ImageResizeKJv2, SetNode, SetNode, ImageResizeKJv2, Text Multiline, Note, Note, Note]
patterns: []
missing: []
---

# 平台全量/电商产品展示 参考视频动作表情 wan2.2 animate_2035232688927416322.json

> 来源文件 `comfyui_library/workflows/平台全量/电商产品展示 参考视频动作表情 wan2.2 animate_2035232688927416322.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（51 个）：
- `Anything Everywhere3`
- `WanVideoVAELoader`
- `GetNode`
- `Seed Everywhere`
- `SetNode`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `GetNode`
- `PixelPerfectResolution`
- `ImageCropByMaskAndResize`
- `DWPreprocessor`
- `WanVideoSampler` ★核心
- `FaceMaskFromPoseKeypoints`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoModelLoader`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `MathExpression|pysssss`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `MathExpression|pysssss`
- `Int`
- `LayerUtility: PurgeVRAM V2`
- `Int`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `LoadImage`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `WanVideoTextEncodeCached`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `Text Multiline`
- `Note`
- `Note`
- `Note`

## 知识

覆盖率 **55%**（28/51）

**有卡**：`WanVideoVAELoader`、`Seed Everywhere`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoDecode`、`WanVideoLoraSelectMulti`、`PixelPerfectResolution`、`ImageCropByMaskAndResize`、`DWPreprocessor`、`WanVideoSampler`、`FaceMaskFromPoseKeypoints`、`LayerUtility: PurgeVRAM V2`、`WanVideoModelLoader`、`MathExpression|pysssss`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`Int`、`VHS_LoadVideo`、`VHS_VideoCombine`、`LoadImage`、`WanVideoAnimateEmbeds`、`WanVideoTextEncodeCached`、`ImageResizeKJv2`、`Text Multiline`

**用到的条目**：LoadImage、Seed Everywhere、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti
