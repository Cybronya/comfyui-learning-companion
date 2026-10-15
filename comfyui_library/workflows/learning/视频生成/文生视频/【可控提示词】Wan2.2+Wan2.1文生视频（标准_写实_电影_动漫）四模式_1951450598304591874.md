---
key: 视频生成/文生视频/【可控提示词】Wan2.2+Wan2.1文生视频（标准_写实_电影_动漫）四模式_1951450598304591874.json
name: 【可控提示词】Wan2.2+Wan2.1文生视频（标准_写实_电影_动漫）四模式_1951450598304591874
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【可控提示词】Wan2.2+Wan2.1文生视频（标准_写实_电影_动漫）四模式_1951450598304591874.json
hash: bfb0ef5fb539f866
coverage: 0.673077
learned_at: 2026-10-15 22:47:41
nodes: [Anything Everywhere, Note, Note, Note, Anything Everywhere, WanVideoBlockSwap, Anything Everywhere, CLIPVisionLoader, WanVideoSetBlockSwap, easy cleanGpuUsed, easy cleanGpuUsed, LayerUtility: PurgeVRAM V2, ImageCASharpening+, WanVideoDecode, WanVideoSLG, WanVideoExperimentalArgs, CogVideoEnhanceAVideo, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoVAELoader, CogVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, Note, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoLoraSelect, VHS_VideoCombine, WanVideoModelLoader, Int, SetNode, MathExpression|pysssss, Note, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, Int, MathExpression|pysssss, JWInteger, Int, Note, WanVideoSampler, GetNode, WanVideoSampler, GetNode, LoadImage, ShowText|pysssss, RHHiddenNodes, RH_Translator, SetNode, RH_Prompter, ShowText|pysssss, Seed, CR Text Concatenate, JjkText, ImpactStringSelector, LayerUtility: TextJoin, RandomPrompt, LayerUtility: TextJoin, TextCombinerTwo, CR Text, ImpactStringSelector, Note, RandomPrompt, RandomPrompt, Note, ImpactStringSelector, Note, ImpactStringSelector, Note, FluxResolutionNode, ShowText|pysssss, WanVideoTextEncode, RHHiddenNodes, LayerUtility: TextJoin, ShowText|pysssss, ImpactStringSelector, CreateCFGScheduleFloatList, Int, Int, WanVideoEmptyEmbeds, Int, ImpactStringSelector, Note, Note, Int, Int, Int, Int, ColorCorrectOfUtils, JjkText, Note, Note, Int, Note, ImpactSwitch, Note, Note, Note, Note, Note]
patterns: []
missing: []
---

# 视频生成/文生视频/【可控提示词】Wan2.2+Wan2.1文生视频（标准_写实_电影_动漫）四模式_1951450598304591874.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/【可控提示词】Wan2.2+Wan2.1文生视频（标准_写实_电影_动漫）四模式_1951450598304591874.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（104 个）：
- `Anything Everywhere`
- `Note`
- `Note`
- `Note`
- `Anything Everywhere`
- `WanVideoBlockSwap`
- `Anything Everywhere`
- `CLIPVisionLoader`
- `WanVideoSetBlockSwap`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM V2`
- `ImageCASharpening+`
- `WanVideoDecode`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `CogVideoEnhanceAVideo`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoVAELoader`
- `CogVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `Note`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `Int`
- `SetNode`
- `MathExpression|pysssss`
- `Note`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `Int`
- `MathExpression|pysssss`
- `JWInteger`
- `Int`
- `Note`
- `WanVideoSampler` ★核心
- `GetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `LoadImage`
- `ShowText|pysssss`
- `RHHiddenNodes`
- `RH_Translator`
- `SetNode`
- `RH_Prompter`
- `ShowText|pysssss`
- `Seed`
- `CR Text Concatenate`
- `JjkText`
- `ImpactStringSelector`
- `LayerUtility: TextJoin`
- `RandomPrompt`
- `LayerUtility: TextJoin`
- `TextCombinerTwo`
- `CR Text`
- `ImpactStringSelector`
- `Note`
- `RandomPrompt`
- `RandomPrompt`
- `Note`
- `ImpactStringSelector`
- `Note`
- `ImpactStringSelector`
- `Note`
- `FluxResolutionNode`
- `ShowText|pysssss`
- `WanVideoTextEncode`
- `RHHiddenNodes`
- `LayerUtility: TextJoin`
- `ShowText|pysssss`
- `ImpactStringSelector`
- `CreateCFGScheduleFloatList`
- `Int`
- `Int`
- `WanVideoEmptyEmbeds`
- `Int`
- `ImpactStringSelector`
- `Note`
- `Note`
- `Int`
- `Int`
- `Int`
- `Int`
- `ColorCorrectOfUtils`
- `JjkText`
- `Note`
- `Note`
- `Int`
- `Note`
- `ImpactSwitch`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`

## 知识

覆盖率 **67%**（70/104）

**有卡**：`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM V2`、`ImageCASharpening+`、`WanVideoDecode`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`CogVideoEnhanceAVideo`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`VHS_VideoCombine`、`Int`、`MathExpression|pysssss`、`JWInteger`、`WanVideoSampler`、`LoadImage`、`RHHiddenNodes`、`RH_Translator`、`RH_Prompter`、`Seed`、`CR Text Concatenate`、`ImpactStringSelector`、`LayerUtility: TextJoin`、`RandomPrompt`、`TextCombinerTwo`、`CR Text`、`FluxResolutionNode`、`WanVideoTextEncode`、`CreateCFGScheduleFloatList`、`WanVideoEmptyEmbeds`、`ColorCorrectOfUtils`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、Seed、Seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
