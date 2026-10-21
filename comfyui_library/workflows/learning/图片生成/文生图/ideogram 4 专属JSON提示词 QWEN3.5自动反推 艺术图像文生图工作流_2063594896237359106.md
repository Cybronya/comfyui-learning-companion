---
key: 图片生成/文生图/ideogram 4 专属JSON提示词 QWEN3.5自动反推 艺术图像文生图工作流_2063594896237359106.json
name: ideogram 4 专属JSON提示词 QWEN3.5自动反推 艺术图像文生图工作流_2063594896237359106
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/ideogram 4 专属JSON提示词 QWEN3.5自动反推 艺术图像文生图工作流_2063594896237359106.json
hash: 046e80f297bdde17
coverage: 0.860465
learned_at: 2026-10-19 23:22:20
nodes: [MarkdownNote, ResolutionSelector, Text Multiline, easy seed, MarkdownNote, Label (rgthree), LoadImage, llama_cpp_parameters, Text Multiline, easy showAnything, easy cleanGpuUsed, llama_cpp_instruct_adv, PrimitiveInt, PrimitiveInt, ComfyMathExpression, ComfyMathExpression, ComfyNumberConvert, JsonExtractString, CustomCombo, ComfyNumberConvert, JsonExtractString, ConditioningZeroOut, UNETLoader, JsonExtractString, ComfyNumberConvert, JsonExtractString, StringReplace, CLIPTextEncode, CLIPLoader, UNETLoader, RandomNoise, CFGOverride, DualModelGuider, KSamplerSelect, Ideogram4Scheduler, EmptyFlux2LatentImage, VAELoader, MarkdownNote, Label (rgthree), VAEDecode, SamplerCustomAdvanced, SaveImage, llama_cpp_model_loader]
patterns: []
missing: []
---

# 图片生成/文生图/ideogram 4 专属JSON提示词 QWEN3.5自动反推 艺术图像文生图工作流_2063594896237359106.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/ideogram 4 专属JSON提示词 QWEN3.5自动反推 艺术图像文生图工作流_2063594896237359106.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `MarkdownNote`
- `ResolutionSelector`
- `Text Multiline`
- `easy seed`
- `MarkdownNote`
- `Label (rgthree)`
- `LoadImage`
- `llama_cpp_parameters`
- `Text Multiline`
- `easy showAnything`
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyNumberConvert`
- `JsonExtractString`
- `CustomCombo`
- `ComfyNumberConvert`
- `JsonExtractString`
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `JsonExtractString`
- `ComfyNumberConvert`
- `JsonExtractString`
- `StringReplace`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `RandomNoise`
- `CFGOverride`
- `DualModelGuider`
- `KSamplerSelect` ★核心
- `Ideogram4Scheduler`
- `EmptyFlux2LatentImage`
- `VAELoader`
- `MarkdownNote`
- `Label (rgthree)`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `SaveImage`
- `llama_cpp_model_loader`

## 知识

覆盖率 **86%**（37/43）

**有卡**：`ResolutionSelector`、`Text Multiline`、`easy seed`、`Label (rgthree)`、`LoadImage`、`llama_cpp_parameters`、`easy cleanGpuUsed`、`llama_cpp_instruct_adv`、`ComfyMathExpression`、`ComfyNumberConvert`、`JsonExtractString`、`CustomCombo`、`ConditioningZeroOut`、`UNETLoader`、`StringReplace`、`CLIPTextEncode`、`CLIPLoader`、`RandomNoise`、`CFGOverride`、`DualModelGuider`、`KSamplerSelect`、`Ideogram4Scheduler`、`EmptyFlux2LatentImage`、`VAELoader`、`VAEDecode`、`SamplerCustomAdvanced`、`SaveImage`、`llama_cpp_model_loader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage
