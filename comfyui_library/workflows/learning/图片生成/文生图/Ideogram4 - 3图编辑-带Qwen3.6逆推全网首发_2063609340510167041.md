---
key: 图片生成/文生图/Ideogram4 - 3图编辑-带Qwen3.6逆推全网首发_2063609340510167041.json
name: Ideogram4 - 3图编辑-带Qwen3.6逆推全网首发_2063609340510167041
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Ideogram4 - 3图编辑-带Qwen3.6逆推全网首发_2063609340510167041.json
hash: 6dc5d26e93cfa78f
coverage: 0.480392
learned_at: 2026-10-19 23:21:30
nodes: [SetNode, PrimitiveInt, SetNode, SetNode, UNETLoader, CLIPLoader, VAELoader, Reroute, PrimitiveInt, GetNode, SetNode, SetNode, SetNode, PrimitiveInt, TextEncodeQwenImageEditPlus, Reroute, SetNode, CR Prompt Text, CR Prompt Text, CR Prompt Text, ComfyMathExpression, PrimitiveInt, ComfyMathExpression, EmptyFlux2LatentImage, JsonExtractString, JsonExtractString, ComfyNumberConvert, ComfyNumberConvert, KSamplerSelect, ConditioningZeroOut, GetNode, GetNode, GetNode, RandomNoise, GetNode, GetNode, DualModelGuider, GetNode, VAEDecode, ComfyNumberConvert, StringReplace, JsonExtractString, JsonExtractString, Ideogram4Scheduler, easy anythingIndexSwitch, GetNode, CFGOverride, SamplerCustomAdvanced, SaveImage, SetNode, Reroute, SetNode, Reroute, PrimitiveStringMultiline, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, easy showAnything, SetNode, GetNode, ImageStitch, SetNode, ImageStitch, easy joinImageBatch, LoadImage, LoadImage, LoadImage, llama_cpp_instruct_adv, easy cleanGpuUsed, GetNode, llama_cpp_model_loader, SetNode, llama_cpp_parameters, PrimitiveStringMultiline, GetNode, GetNode, GetNode, UNETLoader, PrimitiveInt, easy cleanGpuUsed, GetNode, SetNode, SetNode, TextConcatenator, TextConcatenator, CR Text, CR Text, GetNode, Switch any [Crystools], SetNode, SetNode, EmptySD3LatentImage, Switch any [Crystools], SetNode, PrimitiveBoolean, GetNode, PrimitiveInt, PrimitiveInt, CR Text]
patterns: []
missing: []
---

# 图片生成/文生图/Ideogram4 - 3图编辑-带Qwen3.6逆推全网首发_2063609340510167041.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Ideogram4 - 3图编辑-带Qwen3.6逆推全网首发_2063609340510167041.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（102 个）：
- `SetNode`
- `PrimitiveInt`
- `SetNode`
- `SetNode`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Reroute`
- `PrimitiveInt`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveInt`
- `TextEncodeQwenImageEditPlus`
- `Reroute`
- `SetNode`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `ComfyMathExpression`
- `PrimitiveInt`
- `ComfyMathExpression`
- `EmptyFlux2LatentImage`
- `JsonExtractString`
- `JsonExtractString`
- `ComfyNumberConvert`
- `ComfyNumberConvert`
- `KSamplerSelect` ★核心
- `ConditioningZeroOut`
- `GetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `DualModelGuider`
- `GetNode`
- `VAEDecode` ★核心
- `ComfyNumberConvert`
- `StringReplace`
- `JsonExtractString`
- `JsonExtractString`
- `Ideogram4Scheduler`
- `easy anythingIndexSwitch`
- `GetNode`
- `CFGOverride`
- `SamplerCustomAdvanced` ★核心
- `SaveImage`
- `SetNode`
- `Reroute`
- `SetNode`
- `Reroute`
- `PrimitiveStringMultiline`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `easy showAnything`
- `SetNode`
- `GetNode`
- `ImageStitch`
- `SetNode`
- `ImageStitch`
- `easy joinImageBatch`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `llama_cpp_instruct_adv`
- `easy cleanGpuUsed`
- `GetNode`
- `llama_cpp_model_loader`
- `SetNode`
- `llama_cpp_parameters`
- `PrimitiveStringMultiline`
- `GetNode`
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `PrimitiveInt`
- `easy cleanGpuUsed`
- `GetNode`
- `SetNode`
- `SetNode`
- `TextConcatenator`
- `TextConcatenator`
- `CR Text`
- `CR Text`
- `GetNode`
- `Switch any [Crystools]`
- `SetNode`
- `SetNode`
- `EmptySD3LatentImage`
- `Switch any [Crystools]`
- `SetNode`
- `PrimitiveBoolean`
- `GetNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `CR Text`

## 知识

覆盖率 **48%**（49/102）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImageEditPlus`、`CR Prompt Text`、`ComfyMathExpression`、`EmptyFlux2LatentImage`、`JsonExtractString`、`ComfyNumberConvert`、`KSamplerSelect`、`ConditioningZeroOut`、`RandomNoise`、`DualModelGuider`、`VAEDecode`、`StringReplace`、`Ideogram4Scheduler`、`easy anythingIndexSwitch`、`CFGOverride`、`SamplerCustomAdvanced`、`SaveImage`、`ImageStitch`、`easy joinImageBatch`、`LoadImage`、`llama_cpp_instruct_adv`、`easy cleanGpuUsed`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`TextConcatenator`、`CR Text`、`Switch any [Crystools]`、`EmptySD3LatentImage`、`PrimitiveBoolean`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPLoader、ConditioningZeroOut、LoadImage、KSamplerSelect、SamplerCustomAdvanced
