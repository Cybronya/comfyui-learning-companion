---
key: 视频生成/文生视频/【首创丝滑插帧法】Wan2.2-Smooth Mix文生视频（高质量分镜成片）_1980985544744255489.json
name: 【首创丝滑插帧法】Wan2.2-Smooth Mix文生视频（高质量分镜成片）_1980985544744255489
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【首创丝滑插帧法】Wan2.2-Smooth Mix文生视频（高质量分镜成片）_1980985544744255489.json
hash: 6abb20c8df035e89
coverage: 0.48913
learned_at: 2026-10-11 02:45:03
nodes: [LayerUtility: PurgeVRAM V2, ImageCASharpening+, MathExpression|pysssss, Note, MathExpression|pysssss, Note, RH_Prompter, CR Text Concatenate, JjkText, ImpactStringSelector, LayerUtility: TextJoin, LayerUtility: TextJoin, TextCombinerTwo, ImpactStringSelector, Note, RandomPrompt, Note, ImpactStringSelector, Note, ImpactStringSelector, Note, RHHiddenNodes, LayerUtility: TextJoin, ImpactStringSelector, Int, Int, Int, ImpactStringSelector, Note, Note, Int, Int, Int, Int, Note, Note, Note, Note, Note, JjkText, wanBlockSwap, ModelSamplingSD3, PathchSageAttentionKJ, ModelSamplingSD3, PathchSageAttentionKJ, wanBlockSwap, VAEDecode, easy cleanGpuUsed, easy cleanGpuUsed, CLIPLoader, KSamplerAdvanced, MathExpression|pysssss, MathExpression|pysssss, CLIPTextEncode, WanImageToVideo, UNETLoader, UNETLoader, CLIPTextEncode, VAELoader, LoraLoaderModelOnly, ShowText|pysssss, VHS_VideoCombine, ColorCorrectOfUtils, ShowText|pysssss, easy ifElse, Note, easy boolean, CR Text Concatenate, CR Text, KSamplerAdvanced, JWInteger, MathExpression|pysssss, MathExpression|pysssss, CR Integer To String, CR Integer To String, CR Text, CR Text Concatenate, CR Text, CR Text Concatenate, StringConcatenate, RIFE VFI, RHHiddenNodes, RHHiddenNodes, CR Text, Note, Make Interpolation State List, LoadImage, FluxResolutionNode, CR Text, Seed_, RandomPrompt, RandomPrompt]
patterns: []
missing: [CR Integer To String, CR Integer To String, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, ImageCASharpening+, LayerUtility: PurgeVRAM V2, LayerUtility: TextJoin, LayerUtility: TextJoin, LayerUtility: TextJoin, Make Interpolation State List, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, RIFE VFI, easy boolean, easy cleanGpuUsed, easy cleanGpuUsed]
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "randomize"}
discoveries: [次要节点 `CR Integer To String` 知识库中没有该节点类型的任何知识, 次要节点 `CR Integer To String` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `ImageCASharpening+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: TextJoin` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: TextJoin` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: TextJoin` 知识库中没有该节点类型的任何知识, 次要节点 `Make Interpolation State List` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/【首创丝滑插帧法】Wan2.2-Smooth Mix文生视频（高质量分镜成片）_1980985544744255489.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/【首创丝滑插帧法】Wan2.2-Smooth Mix文生视频（高质量分镜成片）_1980985544744255489.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（92 个）：
- `LayerUtility: PurgeVRAM V2`
- `ImageCASharpening+`
- `MathExpression|pysssss`
- `Note`
- `MathExpression|pysssss`
- `Note`
- `RH_Prompter`
- `CR Text Concatenate`
- `JjkText`
- `ImpactStringSelector`
- `LayerUtility: TextJoin`
- `LayerUtility: TextJoin`
- `TextCombinerTwo`
- `ImpactStringSelector`
- `Note`
- `RandomPrompt`
- `Note`
- `ImpactStringSelector`
- `Note`
- `ImpactStringSelector`
- `Note`
- `RHHiddenNodes`
- `LayerUtility: TextJoin`
- `ImpactStringSelector`
- `Int`
- `Int`
- `Int`
- `ImpactStringSelector`
- `Note`
- `Note`
- `Int`
- `Int`
- `Int`
- `Int`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `JjkText`
- `wanBlockSwap`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `ShowText|pysssss`
- `VHS_VideoCombine`
- `ColorCorrectOfUtils`
- `ShowText|pysssss`
- `easy ifElse`
- `Note`
- `easy boolean`
- `CR Text Concatenate`
- `CR Text`
- `KSamplerAdvanced` ★核心
- `JWInteger`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `CR Integer To String`
- `CR Integer To String`
- `CR Text`
- `CR Text Concatenate`
- `CR Text`
- `CR Text Concatenate`
- `StringConcatenate`
- `RIFE VFI`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `CR Text`
- `Note`
- `Make Interpolation State List`
- `LoadImage`
- `FluxResolutionNode`
- `CR Text`
- `Seed_`
- `RandomPrompt`
- `RandomPrompt`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **49%**（45/92）

**有卡**：`RH_Prompter`、`ImpactStringSelector`、`TextCombinerTwo`、`RandomPrompt`、`RHHiddenNodes`、`Int`、`wanBlockSwap`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`VAEDecode`、`CLIPLoader`、`KSamplerAdvanced`、`CLIPTextEncode`、`WanImageToVideo`、`UNETLoader`、`VAELoader`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`ColorCorrectOfUtils`、`JWInteger`、`StringConcatenate`、`LoadImage`、`FluxResolutionNode`、`Seed_`

**缺卡**（27）：`CR Integer To String`、`CR Integer To String`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text Concatenate`、`CR Text Concatenate`、`CR Text Concatenate`、`CR Text Concatenate`、`ImageCASharpening+`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: TextJoin`、`LayerUtility: TextJoin`、`LayerUtility: TextJoin`、`Make Interpolation State List`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`RIFE VFI`、`easy boolean`、`easy cleanGpuUsed`、`easy cleanGpuUsed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced

## 学习发现

- 次要节点 `CR Integer To String` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Integer To String` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageCASharpening+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: TextJoin` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: TextJoin` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: TextJoin` 知识库中没有该节点类型的任何知识
- 次要节点 `Make Interpolation State List` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
