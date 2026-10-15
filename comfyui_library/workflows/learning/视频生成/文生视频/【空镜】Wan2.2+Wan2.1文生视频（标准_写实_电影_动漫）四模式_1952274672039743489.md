---
key: 视频生成/文生视频/【空镜】Wan2.2+Wan2.1文生视频（标准_写实_电影_动漫）四模式_1952274672039743489.json
name: 【空镜】Wan2.2+Wan2.1文生视频（标准_写实_电影_动漫）四模式_1952274672039743489
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【空镜】Wan2.2+Wan2.1文生视频（标准_写实_电影_动漫）四模式_1952274672039743489.json
hash: 6b3658228db6d1c1
coverage: 0.673077
learned_at: 2026-10-15 22:47:42
nodes: [Anything Everywhere, Note, Note, Note, Anything Everywhere, WanVideoBlockSwap, Anything Everywhere, CLIPVisionLoader, WanVideoSetBlockSwap, easy cleanGpuUsed, easy cleanGpuUsed, LayerUtility: PurgeVRAM V2, ImageCASharpening+, WanVideoDecode, WanVideoSLG, WanVideoExperimentalArgs, CogVideoEnhanceAVideo, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoVAELoader, CogVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, Note, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoLoraSelect, VHS_VideoCombine, WanVideoModelLoader, Int, SetNode, MathExpression|pysssss, Note, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, Int, MathExpression|pysssss, JWInteger, Int, Note, WanVideoSampler, GetNode, WanVideoSampler, GetNode, LoadImage, ShowText|pysssss, RHHiddenNodes, RH_Translator, SetNode, RH_Prompter, ShowText|pysssss, Seed, CR Text Concatenate, JjkText, ImpactStringSelector, RandomPrompt, LayerUtility: TextJoin, TextCombinerTwo, CR Text, RandomPrompt, RandomPrompt, Note, Note, ImpactStringSelector, FluxResolutionNode, ShowText|pysssss, WanVideoTextEncode, RHHiddenNodes, ImpactStringSelector, CreateCFGScheduleFloatList, Int, WanVideoEmptyEmbeds, ImpactStringSelector, Note, Int, ColorCorrectOfUtils, Note, Note, Int, Note, ImpactSwitch, Note, Note, Note, Note, Int, Note, Int, Note, Int, Int, Note, Int, WanVideoLoraSelect, WanVideoLoraSelect, JjkText, ShowText|pysssss, ImpactStringSelector, LayerUtility: TextJoin, ImpactStringSelector, Note]
patterns: []
missing: []
---

# 视频生成/文生视频/【空镜】Wan2.2+Wan2.1文生视频（标准_写实_电影_动漫）四模式_1952274672039743489.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/【空镜】Wan2.2+Wan2.1文生视频（标准_写实_电影_动漫）四模式_1952274672039743489.json`

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
- `RandomPrompt`
- `LayerUtility: TextJoin`
- `TextCombinerTwo`
- `CR Text`
- `RandomPrompt`
- `RandomPrompt`
- `Note`
- `Note`
- `ImpactStringSelector`
- `FluxResolutionNode`
- `ShowText|pysssss`
- `WanVideoTextEncode`
- `RHHiddenNodes`
- `ImpactStringSelector`
- `CreateCFGScheduleFloatList`
- `Int`
- `WanVideoEmptyEmbeds`
- `ImpactStringSelector`
- `Note`
- `Int`
- `ColorCorrectOfUtils`
- `Note`
- `Note`
- `Int`
- `Note`
- `ImpactSwitch`
- `Note`
- `Note`
- `Note`
- `Note`
- `Int`
- `Note`
- `Int`
- `Note`
- `Int`
- `Int`
- `Note`
- `Int`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `JjkText`
- `ShowText|pysssss`
- `ImpactStringSelector`
- `LayerUtility: TextJoin`
- `ImpactStringSelector`
- `Note`

## 知识

覆盖率 **67%**（70/104）

**有卡**：`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM V2`、`ImageCASharpening+`、`WanVideoDecode`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`CogVideoEnhanceAVideo`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`VHS_VideoCombine`、`Int`、`MathExpression|pysssss`、`JWInteger`、`WanVideoSampler`、`LoadImage`、`RHHiddenNodes`、`RH_Translator`、`RH_Prompter`、`Seed`、`CR Text Concatenate`、`ImpactStringSelector`、`RandomPrompt`、`LayerUtility: TextJoin`、`TextCombinerTwo`、`CR Text`、`FluxResolutionNode`、`WanVideoTextEncode`、`CreateCFGScheduleFloatList`、`WanVideoEmptyEmbeds`、`ColorCorrectOfUtils`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、Seed、Seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
