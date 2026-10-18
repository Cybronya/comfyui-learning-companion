---
key: 视频生成/图生视频/Radial Attention提速20%-FusionX-舞蹈动作迁移v2_1943365680282693633.json
name: Radial Attention提速20%-FusionX-舞蹈动作迁移v2_1943365680282693633.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Radial Attention提速20%-FusionX-舞蹈动作迁移v2_1943365680282693633.json
hash: 0947ac2d24537f82
coverage: 0.69697
learned_at: 2026-10-15 22:30:38
nodes: [Reroute, GetNode, Reroute, ImpactSwitch, Primitive integer [Crystools], ImpactSwitch, SetNode, VHS_VideoCombine, PreviewImage, VHS_LoadVideo, AddLabel, AddLabel, ImageResizeKJ, ImageResizeKJ, Text Multiline, Text Multiline, AIO_Preprocessor, AIO_Preprocessor, GetImageSizeAndCount, ImageBlend, PreviewImage, ColorMatch, easy cleanGpuUsed, RH_Captioner, RH_Captioner, Primitive integer [Crystools], Primitive integer [Crystools], Text Concatenate, WanVideoTextEncode, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, ImageConcatMulti, ImageConcatMulti, EmptyImage, WanVideoVAELoader, SetNode, WanVideoVACEEncode, WanVideoEasyCache, WanVideoSLG, ShowText|pysssss, SetNode, LoadWanVideoT5TextEncoder, SetNode, SimpleMath+, SimpleMath+, Primitive integer [Crystools], GetImageSizeAndCount, GetNode, WanVideoDecode, WanVideoSampler, WanVideoModelLoader, GetNode, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoTorchCompileSettings, VHS_LoadVideo, LoadImage, Primitive integer [Crystools], Primitive integer [Crystools], WanVideoSetRadialAttention, SetNode, SetNode]
patterns: []
missing: []
---

# 视频生成/图生视频/Radial Attention提速20%-FusionX-舞蹈动作迁移v2_1943365680282693633.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1943365680282693633.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（66 个）：
- `Reroute`
- `GetNode`
- `Reroute`
- `ImpactSwitch`
- `Primitive integer [Crystools]`
- `ImpactSwitch`
- `SetNode`
- `VHS_VideoCombine`
- `PreviewImage`
- `VHS_LoadVideo`
- `AddLabel`
- `AddLabel`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `Text Multiline`
- `Text Multiline`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `GetImageSizeAndCount`
- `ImageBlend`
- `PreviewImage`
- `ColorMatch`
- `easy cleanGpuUsed`
- `RH_Captioner`
- `RH_Captioner`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Text Concatenate`
- `WanVideoTextEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `EmptyImage`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoVACEEncode`
- `WanVideoEasyCache`
- `WanVideoSLG`
- `ShowText|pysssss`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `SimpleMath+`
- `SimpleMath+`
- `Primitive integer [Crystools]`
- `GetImageSizeAndCount`
- `GetNode`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `GetNode`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `VHS_LoadVideo`
- `LoadImage`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `WanVideoSetRadialAttention`
- `SetNode`
- `SetNode`

## 知识

覆盖率 **70%**（46/66）

**有卡**：`Primitive integer [Crystools]`、`VHS_VideoCombine`、`VHS_LoadVideo`、`AddLabel`、`ImageResizeKJ`、`Text Multiline`、`AIO_Preprocessor`、`GetImageSizeAndCount`、`ImageBlend`、`ColorMatch`、`easy cleanGpuUsed`、`RH_Captioner`、`Text Concatenate`、`WanVideoTextEncode`、`ImageConcatMulti`、`EmptyImage`、`WanVideoVAELoader`、`WanVideoVACEEncode`、`WanVideoEasyCache`、`WanVideoSLG`、`LoadWanVideoT5TextEncoder`、`SimpleMath+`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`LoadImage`、`WanVideoSetRadialAttention`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect
