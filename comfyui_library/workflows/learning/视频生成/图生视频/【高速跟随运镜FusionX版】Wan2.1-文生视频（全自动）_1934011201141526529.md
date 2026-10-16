---
key: 视频生成/图生视频/【高速跟随运镜FusionX版】Wan2.1-文生视频（全自动）_1934011201141526529.json
name: 【高速跟随运镜FusionX版】Wan2.1-文生视频（全自动）_1934011201141526529.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1934011201141526529.json
hash: 884159ab23dff26e
coverage: 0.681818
learned_at: 2026-10-15 22:30:15
nodes: [Anything Everywhere, Anything Everywhere, WanVideoDecode, WanVideoSetBlockSwap, WanVideoBlockSwap, Anything Everywhere, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoTextEncodeSingle, WanVideoModelLoader, WanVideoLoraSelect, CogVideoEnhanceAVideo, Note, WanVideoSLG, WanVideoExperimentalArgs, Note, WanVideoTextEncodeSingle, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, LayerColor: Brightness & Contrast, GetNode, ImageCASharpening+, VHS_VideoCombine, easy anythingIndexSwitch, easy showAnything, RHHiddenNodes, JjkText, Note, WanVideoSampler, PreviewBridge, ShowText|pysssss, RHHiddenNodes, VHS_VideoCombine, RHHiddenNodes, easy showAnything, easy showAnything, Int, MMAudioFeatureUtilsLoader, Anything Everywhere, Anything Everywhere, MMAudioModelLoader, MMAudioSampler, MMAudioSampler, Evaluate Integers, WanVideoApplyNAG, Note, AudioCombine, Int, SetNode, Note, Note, MathExpression|pysssss, FluxResolutionNode, Note, WanVideoEmptyEmbeds, MathExpression|pysssss, JWInteger, Note, CR Text, LoadImage, PreviewAudio, PreviewAudio, RHHiddenNodes, easy showAnything, Int]
patterns: []
missing: []
---

# 视频生成/图生视频/【高速跟随运镜FusionX版】Wan2.1-文生视频（全自动）_1934011201141526529.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1934011201141526529.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（66 个）：
- `Anything Everywhere`
- `Anything Everywhere`
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `Anything Everywhere`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncodeSingle`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `CogVideoEnhanceAVideo`
- `Note`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `Note`
- `WanVideoTextEncodeSingle`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `LayerColor: Brightness & Contrast`
- `GetNode`
- `ImageCASharpening+`
- `VHS_VideoCombine`
- `easy anythingIndexSwitch`
- `easy showAnything`
- `RHHiddenNodes`
- `JjkText`
- `Note`
- `WanVideoSampler` ★核心
- `PreviewBridge`
- `ShowText|pysssss`
- `RHHiddenNodes`
- `VHS_VideoCombine`
- `RHHiddenNodes`
- `easy showAnything`
- `easy showAnything`
- `Int`
- `MMAudioFeatureUtilsLoader`
- `Anything Everywhere`
- `Anything Everywhere`
- `MMAudioModelLoader`
- `MMAudioSampler` ★核心
- `MMAudioSampler` ★核心
- `Evaluate Integers`
- `WanVideoApplyNAG`
- `Note`
- `AudioCombine`
- `Int`
- `SetNode`
- `Note`
- `Note`
- `MathExpression|pysssss`
- `FluxResolutionNode`
- `Note`
- `WanVideoEmptyEmbeds`
- `MathExpression|pysssss`
- `JWInteger`
- `Note`
- `CR Text`
- `LoadImage`
- `PreviewAudio`
- `PreviewAudio`
- `RHHiddenNodes`
- `easy showAnything`
- `Int`

## 知识

覆盖率 **68%**（45/66）

**有卡**：`WanVideoDecode`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncodeSingle`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`CogVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`MathExpression|pysssss`、`LayerColor: Brightness & Contrast`、`ImageCASharpening+`、`VHS_VideoCombine`、`easy anythingIndexSwitch`、`RHHiddenNodes`、`WanVideoSampler`、`PreviewBridge`、`Int`、`MMAudioFeatureUtilsLoader`、`MMAudioModelLoader`、`MMAudioSampler`、`Evaluate Integers`、`WanVideoApplyNAG`、`AudioCombine`、`FluxResolutionNode`、`WanVideoEmptyEmbeds`、`JWInteger`、`CR Text`、`LoadImage`、`PreviewAudio`

**用到的条目**：LoadImage、WanVideoSampler、MMAudioSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeSingle、WanVideoLoraSelect
