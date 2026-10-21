---
key: 图片生成/文生图/ideogram4-prompt-builder-fixed_2063828351755833345.json
name: ideogram4-prompt-builder-fixed_2063828351755833345
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/ideogram4-prompt-builder-fixed_2063828351755833345.json
hash: 3325b40e73249061
coverage: 0.833333
learned_at: 2026-10-19 23:22:23
nodes: [MarkdownNote, PrimitiveInt, PrimitiveInt, ComfyNumberConvert, JsonExtractString, ComfyNumberConvert, JsonExtractString, CustomCombo, JsonExtractString, StringReplace, JsonExtractString, ComfyNumberConvert, PreviewAny, MarkdownNote, UNETLoader, VAELoader, ComfyMathExpression, ComfyMathExpression, CLIPLoader, EmptyFlux2LatentImage, CFGOverride, CLIPTextEncode, VAEDecode, RandomNoise, UNETLoader, Ideogram4OptimizationsKJ, CLIPTextEncode, ResolutionSelector, PreviewAny, Ideogram4Scheduler, SamplerCustomAdvanced, KSamplerSelect, DualModelGuider, SaveImage, LoadImage, Ideogram4PromptBuilderKJ]
patterns: []
missing: []
---

# 图片生成/文生图/ideogram4-prompt-builder-fixed_2063828351755833345.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/ideogram4-prompt-builder-fixed_2063828351755833345.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `MarkdownNote`
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfyNumberConvert`
- `JsonExtractString`
- `ComfyNumberConvert`
- `JsonExtractString`
- `CustomCombo`
- `JsonExtractString`
- `StringReplace`
- `JsonExtractString`
- `ComfyNumberConvert`
- `PreviewAny`
- `MarkdownNote`
- `UNETLoader` ★核心
- `VAELoader`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `CLIPLoader`
- `EmptyFlux2LatentImage`
- `CFGOverride`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `RandomNoise`
- `UNETLoader` ★核心
- `Ideogram4OptimizationsKJ`
- `CLIPTextEncode` ★核心
- `ResolutionSelector`
- `PreviewAny`
- `Ideogram4Scheduler`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `DualModelGuider`
- `SaveImage`
- `LoadImage`
- `Ideogram4PromptBuilderKJ`

## 知识

覆盖率 **83%**（30/36）

**有卡**：`ComfyNumberConvert`、`JsonExtractString`、`CustomCombo`、`StringReplace`、`UNETLoader`、`VAELoader`、`ComfyMathExpression`、`CLIPLoader`、`EmptyFlux2LatentImage`、`CFGOverride`、`CLIPTextEncode`、`VAEDecode`、`RandomNoise`、`Ideogram4OptimizationsKJ`、`ResolutionSelector`、`Ideogram4Scheduler`、`SamplerCustomAdvanced`、`KSamplerSelect`、`DualModelGuider`、`SaveImage`、`LoadImage`、`Ideogram4PromptBuilderKJ`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、KSamplerSelect
