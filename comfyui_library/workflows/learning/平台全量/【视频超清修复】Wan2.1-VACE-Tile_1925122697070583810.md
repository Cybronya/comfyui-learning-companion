---
key: 平台全量/【视频超清修复】Wan2.1-VACE-Tile_1925122697070583810.json
name: 【视频超清修复】Wan2.1-VACE-Tile_1925122697070583810
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【视频超清修复】Wan2.1-VACE-Tile_1925122697070583810.json
hash: fc42c6cf015493d7
coverage: 0.74359
learned_at: 2026-11-14 01:25:12
nodes: [LoadWanVideoT5TextEncoder, WanVideoSetBlockSwap, WanVideoBlockSwap, Note, WanVideoSampler, Note, Note, Note, WanVideoTeaCache, WanVideoLoraSelect, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoVACEStartToEndFrame, ImageCASharpening+, WanVideoVACEEncode, Int, LayerUtility: ImageScaleByAspectRatio V2, WanVideoVAELoader, Anything Everywhere, Anything Everywhere, Anything Everywhere, WanVideoDecode, RIFE VFI, WanVideoTextEncode, ShowText|pysssss, RH_Translator, LTXVPromptEnhancer, LTXVPromptEnhancerLoader, Anything Everywhere, ImageUpscaleWithModel, Anything Everywhere, UpscaleModelLoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoInfoSource, CogVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs]
patterns: []
missing: []
---

# 平台全量/【视频超清修复】Wan2.1-VACE-Tile_1925122697070583810.json

> 来源文件 `comfyui_library/workflows/平台全量/【视频超清修复】Wan2.1-VACE-Tile_1925122697070583810.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `Note`
- `WanVideoSampler` ★核心
- `Note`
- `Note`
- `Note`
- `WanVideoTeaCache`
- `WanVideoLoraSelect`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `WanVideoVACEStartToEndFrame`
- `ImageCASharpening+`
- `WanVideoVACEEncode`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoVAELoader`
- `Anything Everywhere`
- `Anything Everywhere`
- `Anything Everywhere`
- `WanVideoDecode`
- `RIFE VFI`
- `WanVideoTextEncode`
- `ShowText|pysssss`
- `RH_Translator`
- `LTXVPromptEnhancer`
- `LTXVPromptEnhancerLoader`
- `Anything Everywhere`
- `ImageUpscaleWithModel`
- `Anything Everywhere`
- `UpscaleModelLoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoInfoSource`
- `CogVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`

## 知识

覆盖率 **74%**（29/39）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoSampler`、`WanVideoTeaCache`、`WanVideoLoraSelect`、`WanVideoVACEModelSelect`、`WanVideoModelLoader`、`WanVideoVACEStartToEndFrame`、`ImageCASharpening+`、`WanVideoVACEEncode`、`Int`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoVAELoader`、`WanVideoDecode`、`RIFE VFI`、`WanVideoTextEncode`、`RH_Translator`、`LTXVPromptEnhancer`、`LTXVPromptEnhancerLoader`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`VHS_LoadVideo`、`VHS_VideoCombine`、`VHS_VideoInfoSource`、`CogVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader、WanVideoLoraSelect、ImageUpscaleWithModel
