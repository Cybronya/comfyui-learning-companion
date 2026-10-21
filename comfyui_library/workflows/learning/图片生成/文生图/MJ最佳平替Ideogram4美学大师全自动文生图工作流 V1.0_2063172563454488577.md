---
key: 图片生成/文生图/MJ最佳平替Ideogram4美学大师全自动文生图工作流 V1.0_2063172563454488577.json
name: MJ最佳平替Ideogram4美学大师全自动文生图工作流 V1.0_2063172563454488577
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/MJ最佳平替Ideogram4美学大师全自动文生图工作流 V1.0_2063172563454488577.json
hash: 3b80dd78c3b11616
coverage: 0.76
learned_at: 2026-10-19 23:02:36
nodes: [VAELoader, ConditioningZeroOut, EmptyFlux2LatentImage, KSamplerSelect, Ideogram4Scheduler, RandomNoise, UNETLoader, CLIPTextEncode, CLIPLoader, PrimitiveInt, ComfyMathExpression, ComfyMathExpression, ComfyNumberConvert, JsonExtractString, ComfyNumberConvert, JsonExtractString, StringReplace, JsonExtractString, JsonExtractString, ComfyNumberConvert, UNETLoader, DualModelGuider, CustomCombo, CFGOverride, PreviewAny, PreviewAny, ComfyMathExpression, ComfyMathExpression, StringReplace, SamplerCustomAdvanced, PrimitiveInt, StringReplace, PreviewAny, RHLLMChatNode, MarkdownNote, SeedVR2VideoUpscaler, ImageScaleToTotalPixels, INTConstant, PreviewImage, SeedVR2LoadDiTModel, Image Comparer (rgthree), VAEDecode, SeedVR2LoadVAEModel, SaveImage, PreviewAny, MarkdownNote, PrimitiveStringMultiline, ResolutionSelector, SaveImage, Note]
patterns: []
missing: []
---

# 图片生成/文生图/MJ最佳平替Ideogram4美学大师全自动文生图工作流 V1.0_2063172563454488577.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/MJ最佳平替Ideogram4美学大师全自动文生图工作流 V1.0_2063172563454488577.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `VAELoader`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `KSamplerSelect` ★核心
- `Ideogram4Scheduler`
- `RandomNoise`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `PrimitiveInt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyNumberConvert`
- `JsonExtractString`
- `ComfyNumberConvert`
- `JsonExtractString`
- `StringReplace`
- `JsonExtractString`
- `JsonExtractString`
- `ComfyNumberConvert`
- `UNETLoader` ★核心
- `DualModelGuider`
- `CustomCombo`
- `CFGOverride`
- `PreviewAny`
- `PreviewAny`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `StringReplace`
- `SamplerCustomAdvanced` ★核心
- `PrimitiveInt`
- `StringReplace`
- `PreviewAny`
- `RHLLMChatNode`
- `MarkdownNote`
- `SeedVR2VideoUpscaler`
- `ImageScaleToTotalPixels`
- `INTConstant`
- `PreviewImage`
- `SeedVR2LoadDiTModel`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `SeedVR2LoadVAEModel`
- `SaveImage`
- `PreviewAny`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `Note`

## 知识

覆盖率 **76%**（38/50）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`EmptyFlux2LatentImage`、`KSamplerSelect`、`Ideogram4Scheduler`、`RandomNoise`、`UNETLoader`、`CLIPTextEncode`、`CLIPLoader`、`ComfyMathExpression`、`ComfyNumberConvert`、`JsonExtractString`、`StringReplace`、`DualModelGuider`、`CustomCombo`、`CFGOverride`、`SamplerCustomAdvanced`、`RHLLMChatNode`、`SeedVR2VideoUpscaler`、`ImageScaleToTotalPixels`、`INTConstant`、`SeedVR2LoadDiTModel`、`VAEDecode`、`SeedVR2LoadVAEModel`、`SaveImage`、`ResolutionSelector`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、ResolutionSelector、KSamplerSelect
