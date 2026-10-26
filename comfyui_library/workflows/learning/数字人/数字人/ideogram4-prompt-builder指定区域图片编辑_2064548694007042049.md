---
key: 数字人/数字人/ideogram4-prompt-builder指定区域图片编辑_2064548694007042049.json
name: ideogram4-prompt-builder指定区域图片编辑_2064548694007042049
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/ideogram4-prompt-builder指定区域图片编辑_2064548694007042049.json
hash: 92e4d7772ec71b52
coverage: 0.842105
learned_at: 2026-10-26 01:58:36
nodes: [MarkdownNote, PrimitiveInt, PrimitiveInt, ComfyNumberConvert, JsonExtractString, ComfyNumberConvert, JsonExtractString, JsonExtractString, StringReplace, JsonExtractString, ComfyNumberConvert, PreviewAny, MarkdownNote, UNETLoader, VAELoader, ComfyMathExpression, ComfyMathExpression, CLIPLoader, EmptyFlux2LatentImage, CFGOverride, CLIPTextEncode, VAEDecode, RandomNoise, UNETLoader, Ideogram4OptimizationsKJ, CLIPTextEncode, ResolutionSelector, Ideogram4Scheduler, SamplerCustomAdvanced, KSamplerSelect, DualModelGuider, CustomCombo, RH_LLMAPI_NODE, RH_LLMAPI_NODE, Ideogram4DirectJSONBuilderModified, PreviewAny, SaveImage, LoadImage]
patterns: []
missing: []
---

# 数字人/数字人/ideogram4-prompt-builder指定区域图片编辑_2064548694007042049.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/ideogram4-prompt-builder指定区域图片编辑_2064548694007042049.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `MarkdownNote`
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfyNumberConvert`
- `JsonExtractString`
- `ComfyNumberConvert`
- `JsonExtractString`
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
- `Ideogram4Scheduler`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `DualModelGuider`
- `CustomCombo`
- `RH_LLMAPI_NODE`
- `RH_LLMAPI_NODE`
- `Ideogram4DirectJSONBuilderModified`
- `PreviewAny`
- `SaveImage`
- `LoadImage`

## 知识

覆盖率 **84%**（32/38）

**有卡**：`ComfyNumberConvert`、`JsonExtractString`、`StringReplace`、`UNETLoader`、`VAELoader`、`ComfyMathExpression`、`CLIPLoader`、`EmptyFlux2LatentImage`、`CFGOverride`、`CLIPTextEncode`、`VAEDecode`、`RandomNoise`、`Ideogram4OptimizationsKJ`、`ResolutionSelector`、`Ideogram4Scheduler`、`SamplerCustomAdvanced`、`KSamplerSelect`、`DualModelGuider`、`CustomCombo`、`RH_LLMAPI_NODE`、`Ideogram4DirectJSONBuilderModified`、`SaveImage`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、KSamplerSelect
