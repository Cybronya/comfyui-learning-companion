---
key: 视频生成/文生视频/wan2.2官方优化版250928（dyno底模+加速lora+提示词工程工具）_1973571337966981122.json
name: wan2.2官方优化版250928（dyno底模+加速lora+提示词工程工具）_1973571337966981122
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2官方优化版250928（dyno底模+加速lora+提示词工程工具）_1973571337966981122.json
hash: b97158c8ec561b4d
coverage: 0.685714
learned_at: 2026-10-10 23:09:46
nodes: [VAEDecode, EmptyHunyuanLatentVideo, VAELoader, Note, CLIPTextEncode, UNETLoader, UNETLoader, CLIPLoader, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, Note, LoraLoaderModelOnly, ModelSamplingSD3, CreateVideo, CLIPTextEncode, CR Prompt Text, JWStringConcat, easy showAnything, Int, Int, Int, Int, easy showAnything, Note, CR Prompt Text, CR Prompt Text, Wan22PromptSelector, ShowText|pysssss, TextConcat, easy showAnything, RH_LLMAPI_NODE, MathExpression|pysssss, DF_Int_to_Float, SaveVideo]
patterns: []
missing: [MathExpression|pysssss, CR Prompt Text, CR Prompt Text, CR Prompt Text]
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/wan2.2官方优化版250928（dyno底模+加速lora+提示词工程工具）_1973571337966981122.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2官方优化版250928（dyno底模+加速lora+提示词工程工具）_1973571337966981122.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（35 个）：
- `VAEDecode` ★核心
- `EmptyHunyuanLatentVideo`
- `VAELoader`
- `Note`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Note`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `CreateVideo`
- `CLIPTextEncode` ★核心
- `CR Prompt Text`
- `JWStringConcat`
- `easy showAnything`
- `Int`
- `Int`
- `Int`
- `Int`
- `easy showAnything`
- `Note`
- `CR Prompt Text`
- `CR Prompt Text`
- `Wan22PromptSelector`
- `ShowText|pysssss`
- `TextConcat`
- `easy showAnything`
- `RH_LLMAPI_NODE`
- `MathExpression|pysssss`
- `DF_Int_to_Float`
- `SaveVideo`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **69%**（24/35）

**有卡**：`VAEDecode`、`EmptyHunyuanLatentVideo`、`VAELoader`、`CLIPTextEncode`、`UNETLoader`、`CLIPLoader`、`ModelSamplingSD3`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`CreateVideo`、`JWStringConcat`、`Int`、`Wan22PromptSelector`、`TextConcat`、`RH_LLMAPI_NODE`、`DF_Int_to_Float`、`SaveVideo`

**缺卡**（4）：`MathExpression|pysssss`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

## 学习发现

- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
