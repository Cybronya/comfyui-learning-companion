---
key: 图片生成/文生图/ideogram4_t2i文生图+Ideogram 4 Prompt Builder KJ_2064175389697724418.json
name: ideogram4_t2i文生图+Ideogram 4 Prompt Builder KJ_2064175389697724418
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/ideogram4_t2i文生图+Ideogram 4 Prompt Builder KJ_2064175389697724418.json
hash: 2d23b168d5a83d44
coverage: 0.723404
learned_at: 2026-10-19 23:22:23
nodes: [MarkdownNote, MarkdownNote, VAELoader, ConditioningZeroOut, EmptyFlux2LatentImage, SamplerCustomAdvanced, KSamplerSelect, Ideogram4Scheduler, RandomNoise, UNETLoader, CLIPTextEncode, CLIPLoader, ComfyMathExpression, ComfyMathExpression, ComfyNumberConvert, JsonExtractString, ComfyNumberConvert, JsonExtractString, StringReplace, JsonExtractString, ComfyNumberConvert, UNETLoader, CFGOverride, DualModelGuider, ComfyMathExpression, PrimitiveStringMultiline, ComfyMathExpression, PreviewAny, PreviewAny, StringReplace, StringReplace, StringReplace, ShowText|pysssss, VAEDecode, PrimitiveInt, PrimitiveInt, PrimitiveNode, JsonExtractString, CustomCombo, easy ifElse, PrimitiveStringMultiline, ShowText|pysssss, AILab_QwenVL, SaveImage, PrimitiveNode, ResolutionSelector, Ideogram4PromptBuilderKJ]
patterns: []
missing: []
---

# 图片生成/文生图/ideogram4_t2i文生图+Ideogram 4 Prompt Builder KJ_2064175389697724418.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/ideogram4_t2i文生图+Ideogram 4 Prompt Builder KJ_2064175389697724418.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `MarkdownNote`
- `MarkdownNote`
- `VAELoader`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `Ideogram4Scheduler`
- `RandomNoise`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyNumberConvert`
- `JsonExtractString`
- `ComfyNumberConvert`
- `JsonExtractString`
- `StringReplace`
- `JsonExtractString`
- `ComfyNumberConvert`
- `UNETLoader` ★核心
- `CFGOverride`
- `DualModelGuider`
- `ComfyMathExpression`
- `PrimitiveStringMultiline`
- `ComfyMathExpression`
- `PreviewAny`
- `PreviewAny`
- `StringReplace`
- `StringReplace`
- `StringReplace`
- `ShowText|pysssss`
- `VAEDecode` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveNode`
- `JsonExtractString`
- `CustomCombo`
- `easy ifElse`
- `PrimitiveStringMultiline`
- `ShowText|pysssss`
- `AILab_QwenVL`
- `SaveImage`
- `PrimitiveNode`
- `ResolutionSelector`
- `Ideogram4PromptBuilderKJ`

## 知识

覆盖率 **72%**（34/47）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`KSamplerSelect`、`Ideogram4Scheduler`、`RandomNoise`、`UNETLoader`、`CLIPTextEncode`、`CLIPLoader`、`ComfyMathExpression`、`ComfyNumberConvert`、`JsonExtractString`、`StringReplace`、`CFGOverride`、`DualModelGuider`、`VAEDecode`、`CustomCombo`、`AILab_QwenVL`、`SaveImage`、`ResolutionSelector`、`Ideogram4PromptBuilderKJ`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、ResolutionSelector、KSamplerSelect
