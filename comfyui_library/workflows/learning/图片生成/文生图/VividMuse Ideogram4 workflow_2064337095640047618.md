---
key: 图片生成/文生图/VividMuse Ideogram4 workflow_2064337095640047618.json
name: VividMuse Ideogram4 workflow_2064337095640047618
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/VividMuse Ideogram4 workflow_2064337095640047618.json
hash: 41c1823ce49cf6f7
coverage: 0.787879
learned_at: 2026-10-19 23:21:46
nodes: [UNETLoader, StringReplace, JsonExtractString, JsonExtractString, JsonExtractString, ComfyNumberConvert, ComfyNumberConvert, ComfyNumberConvert, PreviewAny, PreviewAny, ComfyMathExpression, RandomNoise, ImpactSwitch, UNETLoader, CFGOverride, Ideogram4Scheduler, KSamplerSelect, EmptyFlux2LatentImage, SamplerCustomAdvanced, VAEDecode, VAELoader, JsonExtractString, CLIPLoader, CLIPTextEncode, CLIPTextEncode, PrimitiveStringMultiline, ShowText|pysssss, SaveImage, ResolutionSelector, ShowText|pysssss, TextGenerate, CLIPLoader, StringReplace, StringReplace, PrimitiveStringMultiline, StringReplace, easy promptList, easy promptList, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, DualModelGuider, ComfyMathExpression, Seed (rgthree), PrimitiveStringMultiline, LoadImage, easy promptList, PrimitiveStringMultiline, ImpactSwitch, Fast Groups Bypasser (rgthree), Ideogram4PromptBuilderKJ, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 图片生成/文生图/VividMuse Ideogram4 workflow_2064337095640047618.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/VividMuse Ideogram4 workflow_2064337095640047618.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（66 个）：
- `UNETLoader` ★核心
- `StringReplace`
- `JsonExtractString`
- `JsonExtractString`
- `JsonExtractString`
- `ComfyNumberConvert`
- `ComfyNumberConvert`
- `ComfyNumberConvert`
- `PreviewAny`
- `PreviewAny`
- `ComfyMathExpression`
- `RandomNoise`
- `ImpactSwitch`
- `UNETLoader` ★核心
- `CFGOverride`
- `Ideogram4Scheduler`
- `KSamplerSelect` ★核心
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `JsonExtractString`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `ShowText|pysssss`
- `SaveImage`
- `ResolutionSelector`
- `ShowText|pysssss`
- `TextGenerate`
- `CLIPLoader`
- `StringReplace`
- `StringReplace`
- `PrimitiveStringMultiline`
- `StringReplace`
- `easy promptList`
- `easy promptList`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `DualModelGuider`
- `ComfyMathExpression`
- `Seed (rgthree)`
- `PrimitiveStringMultiline`
- `LoadImage`
- `easy promptList`
- `PrimitiveStringMultiline`
- `ImpactSwitch`
- `Fast Groups Bypasser (rgthree)`
- `Ideogram4PromptBuilderKJ`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **79%**（52/66）

**有卡**：`UNETLoader`、`StringReplace`、`JsonExtractString`、`ComfyNumberConvert`、`ComfyMathExpression`、`RandomNoise`、`CFGOverride`、`Ideogram4Scheduler`、`KSamplerSelect`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`VAEDecode`、`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`SaveImage`、`ResolutionSelector`、`TextGenerate`、`easy promptList`、`LoadImage`、`DualModelGuider`、`Seed (rgthree)`、`Ideogram4PromptBuilderKJ`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、KSamplerSelect
