---
key: 图片生成/文生图/Ideogram 4 KJ Prompt Builder 风格参考+自动文生图_2065368278498889730.json
name: Ideogram 4 KJ Prompt Builder 风格参考+自动文生图_2065368278498889730
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Ideogram 4 KJ Prompt Builder 风格参考+自动文生图_2065368278498889730.json
hash: 0a93b4be9e2f7c8a
coverage: 0.695652
learned_at: 2026-10-19 23:21:25
nodes: [UNETLoader, ConditioningZeroOut, CLIPTextEncode, ComfyMathExpression, EmptyFlux2LatentImage, ComfyMathExpression, VAELoader, CLIPLoader, UNETLoader, DualModelGuider, KSamplerSelect, Ideogram4Scheduler, CFGOverride, easy showAnything, StringReplace, JsonExtractString, JsonExtractString, JsonExtractString, ComfyNumberConvert, ComfyNumberConvert, ComfyNumberConvert, PrimitiveInt, PrimitiveInt, easy showAnything, easy showAnything, SamplerCustomAdvanced, VAEDecode, SaveImage, StringReplace, PreviewAny, ResolutionSelector, MarkdownNote, StringReplace, PreviewAny, ComfyMathExpression, ComfyMathExpression, PreviewAny, Ideogram4PromptBuilderKJ, PrimitiveStringMultiline, LoadImage, PreviewImage, PreviewAny, JsonExtractString, Note, Note, RandomNoise]
patterns: []
missing: []
---

# 图片生成/文生图/Ideogram 4 KJ Prompt Builder 风格参考+自动文生图_2065368278498889730.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Ideogram 4 KJ Prompt Builder 风格参考+自动文生图_2065368278498889730.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
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
- `ResolutionSelector`
- `MarkdownNote`
- `StringReplace`
- `PreviewAny`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `PreviewAny`
- `Ideogram4PromptBuilderKJ`
- `PrimitiveStringMultiline`
- `LoadImage`
- `PreviewImage`
- `PreviewAny`
- `JsonExtractString`
- `Note`
- `Note`
- `RandomNoise`

## 知识

覆盖率 **70%**（32/46）

**有卡**：`UNETLoader`、`ConditioningZeroOut`、`CLIPTextEncode`、`ComfyMathExpression`、`EmptyFlux2LatentImage`、`VAELoader`、`CLIPLoader`、`DualModelGuider`、`KSamplerSelect`、`Ideogram4Scheduler`、`CFGOverride`、`StringReplace`、`JsonExtractString`、`ComfyNumberConvert`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`ResolutionSelector`、`Ideogram4PromptBuilderKJ`、`LoadImage`、`RandomNoise`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage
