---
key: 图片生成/文生图/Ideogram 4+Prompt Builder 中文提示词自动文生图_2085249483184627714.json
name: Ideogram 4+Prompt Builder 中文提示词自动文生图_2085249483184627714
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Ideogram 4+Prompt Builder 中文提示词自动文生图_2085249483184627714.json
hash: 9516b3b19a979fb9
coverage: 0.744681
learned_at: 2026-10-20 00:38:52
nodes: [UNETLoader, ConditioningZeroOut, CLIPTextEncode, ComfyMathExpression, EmptyFlux2LatentImage, ComfyMathExpression, VAELoader, CLIPLoader, UNETLoader, DualModelGuider, KSamplerSelect, Ideogram4Scheduler, CFGOverride, easy showAnything, StringReplace, JsonExtractString, JsonExtractString, JsonExtractString, ComfyNumberConvert, ComfyNumberConvert, ComfyNumberConvert, PrimitiveInt, PrimitiveInt, easy showAnything, easy showAnything, SamplerCustomAdvanced, VAEDecode, SaveImage, StringReplace, PreviewAny, MarkdownNote, StringReplace, PreviewAny, ComfyMathExpression, ComfyMathExpression, PreviewAny, JsonExtractString, PrimitiveStringMultiline, llama_cpp_model_loader, llama_cpp_parameters, easy cleanGpuUsed, easy saveText, llama_cpp_instruct_adv, PreviewAny, ResolutionSelector, RandomNoise, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 图片生成/文生图/Ideogram 4+Prompt Builder 中文提示词自动文生图_2085249483184627714.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Ideogram 4+Prompt Builder 中文提示词自动文生图_2085249483184627714.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `EmptyFlux2LatentImage`
- `ComfyMathExpression`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `DualModelGuider`
- `KSamplerSelect` ★核心
- `Ideogram4Scheduler`
- `CFGOverride`
- `easy showAnything`
- `StringReplace`
- `JsonExtractString`
- `JsonExtractString`
- `JsonExtractString`
- `ComfyNumberConvert`
- `ComfyNumberConvert`
- `ComfyNumberConvert`
- `PrimitiveInt`
- `PrimitiveInt`
- `easy showAnything`
- `easy showAnything`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `StringReplace`
- `PreviewAny`
- `MarkdownNote`
- `StringReplace`
- `PreviewAny`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `PreviewAny`
- `JsonExtractString`
- `PrimitiveStringMultiline`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `easy cleanGpuUsed`
- `easy saveText`
- `llama_cpp_instruct_adv`
- `PreviewAny`
- `ResolutionSelector`
- `RandomNoise`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **74%**（35/47）

**有卡**：`UNETLoader`、`ConditioningZeroOut`、`CLIPTextEncode`、`ComfyMathExpression`、`EmptyFlux2LatentImage`、`VAELoader`、`CLIPLoader`、`DualModelGuider`、`KSamplerSelect`、`Ideogram4Scheduler`、`CFGOverride`、`StringReplace`、`JsonExtractString`、`ComfyNumberConvert`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`easy cleanGpuUsed`、`easy saveText`、`llama_cpp_instruct_adv`、`ResolutionSelector`、`RandomNoise`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、ResolutionSelector、KSamplerSelect
