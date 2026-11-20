---
key: 平台全量/Wan2.1 吉卜力风格视频转绘_2030899997117521922.json
name: Wan2.1 吉卜力风格视频转绘_2030899997117521922
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.1 吉卜力风格视频转绘_2030899997117521922.json
hash: 4723d0532f297320
coverage: 0.544118
learned_at: 2026-11-14 01:04:29
nodes: [SetNode, WanVideoTorchCompileSettings, WanVideoTextEncode, WanVideoTeaCache, WanVideoEnhanceAVideo, WanVideoSLG, GetNode, WanVideoBlockSwap, GetNode, GetImageSize+, GoogleTranslateTextNode, SetNode, AddLabel, SetNode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, SetNode, JoinStrings, JoinStrings, GetNode, GetNode, PreviewImage, ImageConcatMulti, GetNode, SetNode, WanVideoVACEEncode, GetNode, WanVideoExperimentalArgs, ImageFromBatch, WanVideoDecode, GetNode, WanVideoSampler, easy showAnything, SetNode, GetNode, VHS_VideoCombine, PrimitiveString, PrimitiveString, SetNode, VHS_VideoInfo, easy showAnything, easy positive, GetNode, GetImageSizeAndCount, PrimitiveString, DepthAnythingV2Preprocessor, WanVideoLoraSelect, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, GetNode, WanVideoVACEModelSelect, GoogleTranslateTextNode, MiniCPM_VQA_Polished, easy anythingIndexSwitch, easy int, easy seed, easy int, VHS_LoadVideo, GetNode, ImageResizeKJv2, VHS_VideoCombine, WanVideoContextOptions, MarkdownNote]
patterns: []
missing: []
---

# 平台全量/Wan2.1 吉卜力风格视频转绘_2030899997117521922.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.1 吉卜力风格视频转绘_2030899997117521922.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（68 个）：
- `SetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoTextEncode`
- `WanVideoTeaCache`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `GetNode`
- `WanVideoBlockSwap`
- `GetNode`
- `GetImageSize+`
- `GoogleTranslateTextNode`
- `SetNode`
- `AddLabel`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `JoinStrings`
- `JoinStrings`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `ImageConcatMulti`
- `GetNode`
- `SetNode`
- `WanVideoVACEEncode`
- `GetNode`
- `WanVideoExperimentalArgs`
- `ImageFromBatch`
- `WanVideoDecode`
- `GetNode`
- `WanVideoSampler` ★核心
- `easy showAnything`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `PrimitiveString`
- `PrimitiveString`
- `SetNode`
- `VHS_VideoInfo`
- `easy showAnything`
- `easy positive`
- `GetNode`
- `GetImageSizeAndCount`
- `PrimitiveString`
- `DepthAnythingV2Preprocessor`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `GetNode`
- `WanVideoVACEModelSelect`
- `GoogleTranslateTextNode`
- `MiniCPM_VQA_Polished`
- `easy anythingIndexSwitch`
- `easy int`
- `easy seed`
- `easy int`
- `VHS_LoadVideo`
- `GetNode`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `WanVideoContextOptions`
- `MarkdownNote`

## 知识

覆盖率 **54%**（37/68）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoTextEncode`、`WanVideoTeaCache`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoBlockSwap`、`GetImageSize+`、`GoogleTranslateTextNode`、`AddLabel`、`JoinStrings`、`ImageConcatMulti`、`WanVideoVACEEncode`、`WanVideoExperimentalArgs`、`ImageFromBatch`、`WanVideoDecode`、`WanVideoSampler`、`VHS_VideoCombine`、`VHS_VideoInfo`、`easy positive`、`GetImageSizeAndCount`、`DepthAnythingV2Preprocessor`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoVACEModelSelect`、`MiniCPM_VQA_Polished`、`easy anythingIndexSwitch`、`easy int`、`easy seed`、`VHS_LoadVideo`、`ImageResizeKJv2`、`WanVideoContextOptions`

**用到的条目**：DepthAnythingV2Preprocessor、easy seed、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader
