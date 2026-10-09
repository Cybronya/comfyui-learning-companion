---
key: 图片生成/文生图/Living Comic Style-wan2.2 T2V (speed)+auto prompt_1957131741351829505.json
name: Living Comic Style-wan2.2 T2V (speed)+auto prompt_1957131741351829505.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Living Comic Style-wan2.2 T2V (speed)+auto prompt_1957131741351829505.json
hash: e071ed7891dd6dae
coverage: 0.690476
learned_at: 2026-10-07 23:30:52
nodes: [VAEDecode, VAELoader, PathchSageAttentionKJ, ModelSamplingSD3, PathchSageAttentionKJ, ModelSamplingSD3, Note, Note, CLIPLoader, KSamplerAdvanced, KSamplerAdvanced, SimpleMath+, EmptyHunyuanLatentVideo, MathExpression|pysssss, MathExpression|pysssss, ShowText|pysssss, DF_Integer, MathExpression|pysssss, MathExpression|pysssss, CR Text Concatenate, RH_Prompter, ShowText|pysssss, INTConstant, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, easy ifElse, CLIPTextEncode, INTConstant, DF_Integer, DF_Integer, PrimitiveBoolean, RH_Translator, CR Text, ShellAgentPluginInputText, VHS_VideoCombine, ShellAgentPluginSaveVideoVHS, Text Multiline]
patterns: []
missing: [CR Text, CR Text Concatenate, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, SimpleMath+, Text Multiline]
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Living Comic Style-wan2.2 T2V (speed)+auto prompt_1957131741351829505.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1957131741351829505.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（42 个）：
- `VAEDecode` ★核心
- `VAELoader`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `Note`
- `Note`
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `SimpleMath+`
- `EmptyHunyuanLatentVideo`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `ShowText|pysssss`
- `DF_Integer`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `CR Text Concatenate`
- `RH_Prompter`
- `ShowText|pysssss`
- `INTConstant`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `easy ifElse`
- `CLIPTextEncode` ★核心
- `INTConstant`
- `DF_Integer`
- `DF_Integer`
- `PrimitiveBoolean`
- `RH_Translator`
- `CR Text`
- `ShellAgentPluginInputText`
- `VHS_VideoCombine`
- `ShellAgentPluginSaveVideoVHS`
- `Text Multiline`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **69%**（29/42）

**有卡**：`VAEDecode`、`VAELoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPLoader`、`KSamplerAdvanced`、`EmptyHunyuanLatentVideo`、`DF_Integer`、`RH_Prompter`、`INTConstant`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`PrimitiveBoolean`、`RH_Translator`、`ShellAgentPluginInputText`、`VHS_VideoCombine`、`ShellAgentPluginSaveVideoVHS`

**缺卡**（8）：`CR Text`、`CR Text Concatenate`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`SimpleMath+`、`Text Multiline`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
