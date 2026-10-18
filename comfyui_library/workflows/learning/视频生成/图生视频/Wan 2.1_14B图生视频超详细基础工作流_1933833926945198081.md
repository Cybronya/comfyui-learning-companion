---
key: 视频生成/图生视频/Wan 2.1_14B图生视频超详细基础工作流_1933833926945198081.json
name: Wan 2.1_14B图生视频超详细基础工作流_1933833926945198081.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan 2.1_14B图生视频超详细基础工作流_1933833926945198081.json
hash: 644d08b77834d0a9
coverage: 0.54
learned_at: 2026-10-15 22:30:15
nodes: [SetNode, WanVideoTextEncode, Note, Note, LoadWanVideoT5TextEncoder, GetNode, SetNode, SetNode, WanVideoVAELoader, Note, Note, Note, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoSLG, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, Note, GetNode, WanVideoDecode, ImageUpscaleWithModel, VHS_VideoCombine, Note, WanVideoTeaCache, Note, Int, Note, Int, Fast Groups Bypasser (rgthree), VHS_VideoCombine, GetNode, GetNode, MathExpression|pysssss, WanVideoSampler, GetNode, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, CLIPVisionLoader, Note, WanVideoModelLoader, Note, UpscaleModelLoader, WanVideoVACEModelSelect, Note, RH_Captioner, SetNode, RH_OneShot_Prompter, easy showAnything, LoadImage, ImageResizeKJv2]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan 2.1_14B图生视频超详细基础工作流_1933833926945198081.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1933833926945198081.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（50 个）：
- `SetNode`
- `WanVideoTextEncode`
- `Note`
- `Note`
- `LoadWanVideoT5TextEncoder`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVideoVAELoader`
- `Note`
- `Note`
- `Note`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `Note`
- `GetNode`
- `WanVideoDecode`
- `ImageUpscaleWithModel`
- `VHS_VideoCombine`
- `Note`
- `WanVideoTeaCache`
- `Note`
- `Int`
- `Note`
- `Int`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `WanVideoSampler` ★核心
- `GetNode`
- `WanVideoImageToVideoEncode`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `Note`
- `WanVideoModelLoader`
- `Note`
- `UpscaleModelLoader`
- `WanVideoVACEModelSelect`
- `Note`
- `RH_Captioner`
- `SetNode`
- `RH_OneShot_Prompter`
- `easy showAnything`
- `LoadImage`
- `ImageResizeKJv2`

## 知识

覆盖率 **54%**（27/50）

**有卡**：`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoExperimentalArgs`、`WanVideoDecode`、`ImageUpscaleWithModel`、`VHS_VideoCombine`、`WanVideoTeaCache`、`Int`、`MathExpression|pysssss`、`WanVideoSampler`、`WanVideoImageToVideoEncode`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoModelLoader`、`UpscaleModelLoader`、`WanVideoVACEModelSelect`、`RH_Captioner`、`RH_OneShot_Prompter`、`LoadImage`、`ImageResizeKJv2`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
