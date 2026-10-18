---
key: 视频生成/文生视频/Wan2.2-动作迁移（VACE版）_1970083923097231361.json
name: Wan2.2-动作迁移（VACE版）_1970083923097231361.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2-动作迁移（VACE版）_1970083923097231361.json
hash: aa7e7d53bb6e33e6
coverage: 0.784314
learned_at: 2026-10-15 22:43:47
nodes: [Text Concatenate, WanVideoTeaCache, WanVideoSLG, WanVideoEnhanceAVideo, GetNode, LoadWanVideoT5TextEncoder, WanVideoTextEncode, GetNode, GetImageSizeAndCount, GetNode, WanVideoDecode, GetNode, SetNode, ImageResizeKJv2, AIO_Preprocessor, GetNode, VHS_VideoCombine, RH_Captioner, WanVideoVACEEncode, ColorMatch, Anything Everywhere, Text Multiline, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, SeedVR2BlockSwap, SetNode, WanVideoLoraSelect, WanVideoSampler, ImageBlend, Int, WanVideoSetBlockSwap, SetNode, WanVideoVAELoader, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoVACEModelSelect, WanVideoModelLoader, PreviewImage, ImageResizeKJ, DWPreprocessor, VHS_LoadVideo, Int, GetNode, SeedVR2, VHS_VideoCombine, GetImageSizeAndCount, MathExpression|pysssss, Int, LoadImage, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2-动作迁移（VACE版）_1970083923097231361.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1970083923097231361.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（51 个）：
- `Text Concatenate`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `SetNode`
- `ImageResizeKJv2`
- `AIO_Preprocessor`
- `GetNode`
- `VHS_VideoCombine`
- `RH_Captioner`
- `WanVideoVACEEncode`
- `ColorMatch`
- `Anything Everywhere`
- `Text Multiline`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `SeedVR2BlockSwap`
- `SetNode`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `ImageBlend`
- `Int`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoVAELoader`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `PreviewImage`
- `ImageResizeKJ`
- `DWPreprocessor`
- `VHS_LoadVideo`
- `Int`
- `GetNode`
- `SeedVR2`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `MathExpression|pysssss`
- `Int`
- `LoadImage`
- `VHS_VideoCombine`

## 知识

覆盖率 **78%**（40/51）

**有卡**：`Text Concatenate`、`WanVideoTeaCache`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`GetImageSizeAndCount`、`WanVideoDecode`、`ImageResizeKJv2`、`AIO_Preprocessor`、`VHS_VideoCombine`、`RH_Captioner`、`WanVideoVACEEncode`、`ColorMatch`、`Text Multiline`、`LayerUtility: PurgeVRAM V2`、`SeedVR2BlockSwap`、`WanVideoLoraSelect`、`WanVideoSampler`、`ImageBlend`、`Int`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoVACEModelSelect`、`WanVideoModelLoader`、`ImageResizeKJ`、`DWPreprocessor`、`VHS_LoadVideo`、`SeedVR2`、`MathExpression|pysssss`、`LoadImage`

**用到的条目**：LoadImage、SeedVR2、SeedVR2BlockSwap、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
