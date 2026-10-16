---
key: 视频生成/图生视频/wan2.2+FusxionX_14B_自动提示词优化_图生视频-加速版-KJ模型_1951465254188429313.json
name: wan2.2+FusxionX_14B_自动提示词优化_图生视频-加速版-KJ模型_1951465254188429313.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1951465254188429313.json
hash: 015fbbbc7bd7143f
coverage: 0.90566
learned_at: 2026-10-15 22:30:58
nodes: [WanVideoTorchCompileSettings, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSetBlockSwap, LayerUtility: PurgeVRAM, WanVideoBlockSwap, LayerUtility: PurgeVRAM, TextBox, TextBox, WanVideoBlockSwap, WanVideoSetBlockSwap, Note, easy showAnything, WanVideoTextEncode, RH_Captioner, LayerUtility: PurgeVRAM, easy showAnything, CR Text Replace, MarkdownNote, PrimitiveBoolean, easy ifElse, CLIPVisionLoader, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoSLG, CogVideoEnhanceAVideo, Int, CreateCFGScheduleFloatList, WanVideoSLG, WanVideoExperimentalArgs, WanVideoSampler, CogVideoEnhanceAVideo, WanVideoSampler, WanVideoExperimentalArgs, Int, WanVideoDecode, CreateVideo, ColorCorrectOfUtils, SaveVideo, ImageCASharpening+, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, LayerUtility: ImageScaleByAspectRatio V2, SimpleMath+, easy cleanGpuUsed, TextBox, DF_Integer, DF_Integer, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2+FusxionX_14B_自动提示词优化_图生视频-加速版-KJ模型_1951465254188429313.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1951465254188429313.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（53 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `LayerUtility: PurgeVRAM`
- `WanVideoBlockSwap`
- `LayerUtility: PurgeVRAM`
- `TextBox`
- `TextBox`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `Note`
- `easy showAnything`
- `WanVideoTextEncode`
- `RH_Captioner`
- `LayerUtility: PurgeVRAM`
- `easy showAnything`
- `CR Text Replace`
- `MarkdownNote`
- `PrimitiveBoolean`
- `easy ifElse`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSLG`
- `CogVideoEnhanceAVideo`
- `Int`
- `CreateCFGScheduleFloatList`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoSampler` ★核心
- `CogVideoEnhanceAVideo`
- `WanVideoSampler` ★核心
- `WanVideoExperimentalArgs`
- `Int`
- `WanVideoDecode`
- `CreateVideo`
- `ColorCorrectOfUtils`
- `SaveVideo`
- `ImageCASharpening+`
- `WanVideoImageToVideoEncode`
- `WanVideoClipVisionEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SimpleMath+`
- `easy cleanGpuUsed`
- `TextBox`
- `DF_Integer`
- `DF_Integer`
- `LoadImage`

## 知识

覆盖率 **91%**（48/53）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`LayerUtility: PurgeVRAM`、`WanVideoBlockSwap`、`TextBox`、`WanVideoTextEncode`、`RH_Captioner`、`CR Text Replace`、`PrimitiveBoolean`、`CLIPVisionLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoSLG`、`CogVideoEnhanceAVideo`、`Int`、`CreateCFGScheduleFloatList`、`WanVideoExperimentalArgs`、`WanVideoSampler`、`WanVideoDecode`、`CreateVideo`、`ColorCorrectOfUtils`、`SaveVideo`、`ImageCASharpening+`、`WanVideoImageToVideoEncode`、`WanVideoClipVisionEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`SimpleMath+`、`easy cleanGpuUsed`、`DF_Integer`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
