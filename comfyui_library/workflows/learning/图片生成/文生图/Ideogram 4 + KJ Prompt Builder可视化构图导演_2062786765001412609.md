---
key: 图片生成/文生图/Ideogram 4 + KJ Prompt Builder可视化构图导演_2062786765001412609.json
name: Ideogram 4 + KJ Prompt Builder可视化构图导演_2062786765001412609
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Ideogram 4 + KJ Prompt Builder可视化构图导演_2062786765001412609.json
hash: 4093b4c73269f7b0
coverage: 0.674419
learned_at: 2026-10-19 23:02:26
nodes: [VAELoader, ConditioningZeroOut, EmptyFlux2LatentImage, SamplerCustomAdvanced, VAEDecode, KSamplerSelect, Ideogram4Scheduler, RandomNoise, UNETLoader, CLIPTextEncode, CLIPLoader, PrimitiveInt, PrimitiveInt, ComfyMathExpression, ComfyMathExpression, ComfyNumberConvert, JsonExtractString, ComfyNumberConvert, StringReplace, JsonExtractString, JsonExtractString, ComfyNumberConvert, UNETLoader, DualModelGuider, CFGOverride, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, JsonExtractString, ResolutionSelector, MarkdownNote, ComfyNumberConvert, JsonExtractString, SaveImage, Ideogram4PromptBuilderKJ]
patterns: []
missing: []
---

# 图片生成/文生图/Ideogram 4 + KJ Prompt Builder可视化构图导演_2062786765001412609.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Ideogram 4 + KJ Prompt Builder可视化构图导演_2062786765001412609.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `VAELoader`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `Ideogram4Scheduler`
- `RandomNoise`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyNumberConvert`
- `JsonExtractString`
- `ComfyNumberConvert`
- `StringReplace`
- `JsonExtractString`
- `JsonExtractString`
- `ComfyNumberConvert`
- `UNETLoader` ★核心
- `DualModelGuider`
- `CFGOverride`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `JsonExtractString`
- `ResolutionSelector`
- `MarkdownNote`
- `ComfyNumberConvert`
- `JsonExtractString`
- `SaveImage`
- `Ideogram4PromptBuilderKJ`

## 知识

覆盖率 **67%**（29/43）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`VAEDecode`、`KSamplerSelect`、`Ideogram4Scheduler`、`RandomNoise`、`UNETLoader`、`CLIPTextEncode`、`CLIPLoader`、`ComfyMathExpression`、`ComfyNumberConvert`、`JsonExtractString`、`StringReplace`、`DualModelGuider`、`CFGOverride`、`ResolutionSelector`、`SaveImage`、`Ideogram4PromptBuilderKJ`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、ResolutionSelector、KSamplerSelect
