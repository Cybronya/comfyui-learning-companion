---
key: 视频生成/图生视频/Wan2.1 VACE 双图参考_1948576222688227330.json
name: Wan2.1 VACE 双图参考_1948576222688227330.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1948576222688227330.json
hash: aac27069a1b377f8
coverage: 0.578125
learned_at: 2026-10-15 22:30:47
nodes: [WanVideoTorchCompileSettings, SetNode, SetNode, EmptyImage, WanVideoBlockSwap, WanVideoVACEModelSelect, SetNode, WanVideoVAELoader, SetNode, WanVideoModelLoader, SetNode, LoadWanVideoT5TextEncoder, TransparentBGSession+, ImageRemoveBackground+, SetNode, SetNode, LoadImage, EmptyImage, SetNode, SetNode, JoinStrings, GetNode, String Literal, GetNode, GetNode, GetNode, easy imageScaleDownToSize, GetNode, GetNode, GetNode, GetNode, WanVideoTeaCache, GetNode, SetNode, WanVideoDecode, GetImageSizeAndCount, GetNode, SetNode, ImageConcatMulti, WanVideoVACEEncode, WanVideoExperimentalArgs, WanVideoTextEncode, PreviewImage, WanVideoSLG, SetNode, easy positive, LoadImage, GetNode, VHS_VideoCombine, GetNode, VHS_VideoCombine, Note Plus (mtb), LoadImageFromUrl, WanVideoSampler, easy int, easy int, easy int, GetNode, GetImageSizeAndCount, ImageCompositeMasked, ImageConcatMulti, easy imageScaleDownToSize, GetNode, ImageConcanate]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1 VACE 双图参考_1948576222688227330.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1948576222688227330.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（64 个）：
- `WanVideoTorchCompileSettings`
- `SetNode`
- `SetNode`
- `EmptyImage`
- `WanVideoBlockSwap`
- `WanVideoVACEModelSelect`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoModelLoader`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `TransparentBGSession+`
- `ImageRemoveBackground+`
- `SetNode`
- `SetNode`
- `LoadImage`
- `EmptyImage`
- `SetNode`
- `SetNode`
- `JoinStrings`
- `GetNode`
- `String Literal`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy imageScaleDownToSize`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoTeaCache`
- `GetNode`
- `SetNode`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `GetNode`
- `SetNode`
- `ImageConcatMulti`
- `WanVideoVACEEncode`
- `WanVideoExperimentalArgs`
- `WanVideoTextEncode`
- `PreviewImage`
- `WanVideoSLG`
- `SetNode`
- `easy positive`
- `LoadImage`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `VHS_VideoCombine`
- `Note Plus (mtb)`
- `LoadImageFromUrl`
- `WanVideoSampler` ★核心
- `easy int`
- `easy int`
- `easy int`
- `GetNode`
- `GetImageSizeAndCount`
- `ImageCompositeMasked`
- `ImageConcatMulti`
- `easy imageScaleDownToSize`
- `GetNode`
- `ImageConcanate`

## 知识

覆盖率 **58%**（37/64）

**有卡**：`WanVideoTorchCompileSettings`、`EmptyImage`、`WanVideoBlockSwap`、`WanVideoVACEModelSelect`、`WanVideoVAELoader`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`TransparentBGSession+`、`ImageRemoveBackground+`、`LoadImage`、`JoinStrings`、`String Literal`、`easy imageScaleDownToSize`、`WanVideoTeaCache`、`WanVideoDecode`、`GetImageSizeAndCount`、`ImageConcatMulti`、`WanVideoVACEEncode`、`WanVideoExperimentalArgs`、`WanVideoTextEncode`、`WanVideoSLG`、`easy positive`、`VHS_VideoCombine`、`Note Plus (mtb)`、`LoadImageFromUrl`、`WanVideoSampler`、`easy int`、`ImageCompositeMasked`、`ImageConcanate`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、GetImageSizeAndCount
