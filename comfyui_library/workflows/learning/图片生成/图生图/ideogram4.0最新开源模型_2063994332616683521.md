---
key: 图片生成/图生图/ideogram4.0最新开源模型_2063994332616683521.json
name: ideogram4.0最新开源模型_2063994332616683521
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/ideogram4.0最新开源模型_2063994332616683521.json
hash: 9549d9c3f2e63e08
coverage: 0.857143
learned_at: 2026-10-23 11:37:40
nodes: [ComfyNumberConvert, JsonExtractString, ComfyNumberConvert, JsonExtractString, CustomCombo, JsonExtractString, StringReplace, JsonExtractString, ComfyNumberConvert, UNETLoader, VAELoader, ComfyMathExpression, ComfyMathExpression, CLIPLoader, CFGOverride, CLIPTextEncode, UNETLoader, SamplerCustomAdvanced, KSamplerSelect, Ideogram4Scheduler, EmptyFlux2LatentImage, DualModelGuider, Ideogram4OptimizationsKJ, MarkdownNote, MarkdownNote, VAEDecode, PrimitiveInt, PrimitiveInt, ResolutionSelector, PreviewAny, RandomNoise, SaveImage, CLIPTextEncode, LoadImage, CR Text]
patterns: []
missing: []
---

# 图片生成/图生图/ideogram4.0最新开源模型_2063994332616683521.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/ideogram4.0最新开源模型_2063994332616683521.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `ComfyNumberConvert`
- `JsonExtractString`
- `ComfyNumberConvert`
- `JsonExtractString`
- `CustomCombo`
- `JsonExtractString`
- `StringReplace`
- `JsonExtractString`
- `ComfyNumberConvert`
- `UNETLoader` ★核心
- `VAELoader`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `CLIPLoader`
- `CFGOverride`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `Ideogram4Scheduler`
- `EmptyFlux2LatentImage`
- `DualModelGuider`
- `Ideogram4OptimizationsKJ`
- `MarkdownNote`
- `MarkdownNote`
- `VAEDecode` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `ResolutionSelector`
- `PreviewAny`
- `RandomNoise`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CR Text`

## 知识

覆盖率 **86%**（30/35）

**有卡**：`ComfyNumberConvert`、`JsonExtractString`、`CustomCombo`、`StringReplace`、`UNETLoader`、`VAELoader`、`ComfyMathExpression`、`CLIPLoader`、`CFGOverride`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`KSamplerSelect`、`Ideogram4Scheduler`、`EmptyFlux2LatentImage`、`DualModelGuider`、`Ideogram4OptimizationsKJ`、`VAEDecode`、`ResolutionSelector`、`RandomNoise`、`SaveImage`、`LoadImage`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、KSamplerSelect
