---
key: 视频生成/文生视频/Wan2.2 T2V 原生文生视频+智能优化+加速版 Borges_1951967061645971457.json
name: Wan2.2 T2V 原生文生视频+智能优化+加速版 Borges_1951967061645971457.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 T2V 原生文生视频+智能优化+加速版 Borges_1951967061645971457.json
hash: e418266091928cab
coverage: 0.245614
learned_at: 2026-10-15 22:43:38
nodes: [PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, PathchSageAttentionKJ, Primitive integer [Crystools], PrimitiveFloat, MathExpression|pysssss, Any Switch (rgthree), MathExpression|pysssss, Any Switch (rgthree), VAEDecode, CLIPTextEncode, CLIPTextEncode, CreateVideo, easy showAnything, EmptyHunyuanLatentVideo, Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], CLIPLoader, VAELoader, UNETLoader, KSamplerAdvanced, Primitive integer [Crystools], PrimitiveFloat, UNETLoader, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, Any Switch (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), SetNode, SetNode, SetNode, easy showAnything, Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), JjkText, SetNode, Any Switch (rgthree), SetNode, Any Switch (rgthree), SetNode, Any Switch (rgthree), SetNode, Any Switch (rgthree), SetNode, Any Switch (rgthree), SetNode, Any Switch (rgthree), SetNode, Any Switch (rgthree), SetNode, Any Switch (rgthree), SetNode, Any Switch (rgthree), SetNode, Text _O, Text _O, LTXVPromptEnhancer, LTXVPromptEnhancerLoader, Text _O, Any Switch (rgthree), SetNode, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), SetNode, Note, Note, TTP_text_mix, GetNode, GetNode, GetNode, GetNode, GetNode, TTP_text_mix, TTP_text_mix, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy showAnything, TTP_text_mix, easy showAnything, TTP_text_mix, Any Switch (rgthree), TTP_text_mix, TTP_text_mix, JjkConcat, GetNode, TTP_text_mix, Fast Groups Muter (rgthree), Fast Groups Bypasser (rgthree), Note, easy showAnything, SaveVideo, iToolsPromptStyler, Bjornulf_ShowStringText, KSamplerAdvanced, Note Plus (mtb)]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "normal", "sampler_name": 6, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/Wan2.2 T2V 原生文生视频+智能优化+加速版 Borges_1951967061645971457.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1951967061645971457.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（171 个）：
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `Primitive integer [Crystools]`
- `PrimitiveFloat`
- `MathExpression|pysssss`
- `Any Switch (rgthree)`
- `MathExpression|pysssss`
- `Any Switch (rgthree)`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `easy showAnything`
- `EmptyHunyuanLatentVideo`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `Primitive integer [Crystools]`
- `PrimitiveFloat`
- `UNETLoader` ★核心
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `Any Switch (rgthree)`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Muter (rgthree)`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy showAnything`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Muter (rgthree)`
- `JjkText`
- `SetNode`
- `Any Switch (rgthree)`
- `SetNode`
- `Any Switch (rgthree)`
- `SetNode`
- `Any Switch (rgthree)`
- `SetNode`
- `Any Switch (rgthree)`
- `SetNode`
- `Any Switch (rgthree)`
- `SetNode`
- `Any Switch (rgthree)`
- `SetNode`
- `Any Switch (rgthree)`
- `SetNode`
- `Any Switch (rgthree)`
- `SetNode`
- `Any Switch (rgthree)`
- `SetNode`
- `Text _O`
- `Text _O`
- `LTXVPromptEnhancer`
- `LTXVPromptEnhancerLoader`
- `Text _O`
- `Any Switch (rgthree)`
- `SetNode`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Muter (rgthree)`
- `SetNode`
- `Note`
- `Note`
- `TTP_text_mix`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `TTP_text_mix`
- `TTP_text_mix`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `TTP_text_mix`
- `easy showAnything`
- `TTP_text_mix`
- `Any Switch (rgthree)`
- `TTP_text_mix`
- `TTP_text_mix`
- `JjkConcat`
- `GetNode`
- `TTP_text_mix`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `easy showAnything`
- `SaveVideo`
- `iToolsPromptStyler`
- `Bjornulf_ShowStringText`
- `KSamplerAdvanced` ★核心
- `Note Plus (mtb)`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `6`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **25%**（42/171）

**有卡**：`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`Primitive integer [Crystools]`、`MathExpression|pysssss`、`VAEDecode`、`CLIPTextEncode`、`CreateVideo`、`EmptyHunyuanLatentVideo`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`KSamplerAdvanced`、`Text _O`、`LTXVPromptEnhancer`、`LTXVPromptEnhancerLoader`、`TTP_text_mix`、`JjkConcat`、`SaveVideo`、`iToolsPromptStyler`、`Bjornulf_ShowStringText`、`Note Plus (mtb)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
