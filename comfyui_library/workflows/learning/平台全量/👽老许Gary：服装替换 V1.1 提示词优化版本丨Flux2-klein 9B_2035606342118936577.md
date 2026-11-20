---
key: 平台全量/👽老许Gary：服装替换 V1.1 提示词优化版本丨Flux2-klein 9B_2035606342118936577.json
name: 👽老许Gary：服装替换 V1.1 提示词优化版本丨Flux2-klein 9B_2035606342118936577
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/👽老许Gary：服装替换 V1.1 提示词优化版本丨Flux2-klein 9B_2035606342118936577.json
hash: 0f17d1f1ef797148
coverage: 0.757576
learned_at: 2026-11-14 02:54:54
nodes: [Label (rgthree), KSamplerSelect, ConditioningZeroOut, CFGGuider, ReferenceLatent, ReferenceLatent, VAELoader, Anything Everywhere3, Label (rgthree), MarkdownNote, MarkdownNote, CLIPLoader, Flux2Scheduler, UNETLoader, PrimitiveString, easy showAnything, VAEDecode, easy imageConcat, PreviewImage, CLIPTextEncode, ReferenceLatent, ReferenceLatent, VAEEncode, SaveImage, Reroute, AILab_ImageCompare, easy imageConcat, PreviewImage, easy imageConcat, easy imageConcat, SaveImage, Fast Groups Bypasser (rgthree), CLIPTextEncode, ConditioningZeroOut, KSamplerSelect, CFGGuider, Flux2Scheduler, EmptyFlux2LatentImage, LoraLoaderModelOnly, SamplerCustomAdvanced, VAEEncode, ReferenceLatent, ReferenceLatent, GetImageSize, SaveImage, PrimitiveStringMultiline, RandomNoise, PrimitiveStringMultiline, AILab_ImageResize, RandomNoise, VAEDecode, SaveImage, LoadImage, LoadImage, MarkdownNote, VAEEncode, AILab_ImageResize, AILab_ImageResize, SamplerCustomAdvanced, LoraLoaderModelOnly, Qwen3VL_Chat, PrimitiveStringMultiline, PreviewImage, PrimitiveStringMultiline, PreviewImage, EmptyFlux2LatentImage]
patterns: []
missing: []
---

# 平台全量/👽老许Gary：服装替换 V1.1 提示词优化版本丨Flux2-klein 9B_2035606342118936577.json

> 来源文件 `comfyui_library/workflows/平台全量/👽老许Gary：服装替换 V1.1 提示词优化版本丨Flux2-klein 9B_2035606342118936577.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（66 个）：
- `Label (rgthree)`
- `KSamplerSelect` ★核心
- `ConditioningZeroOut`
- `CFGGuider`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAELoader`
- `Anything Everywhere3`
- `Label (rgthree)`
- `MarkdownNote`
- `MarkdownNote`
- `CLIPLoader`
- `Flux2Scheduler`
- `UNETLoader` ★核心
- `PrimitiveString`
- `easy showAnything`
- `VAEDecode` ★核心
- `easy imageConcat`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `SaveImage`
- `Reroute`
- `AILab_ImageCompare`
- `easy imageConcat`
- `PreviewImage`
- `easy imageConcat`
- `easy imageConcat`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `LoraLoaderModelOnly` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `GetImageSize`
- `SaveImage`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `PrimitiveStringMultiline`
- `AILab_ImageResize`
- `RandomNoise`
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `VAEEncode` ★核心
- `AILab_ImageResize`
- `AILab_ImageResize`
- `SamplerCustomAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `Qwen3VL_Chat`
- `PrimitiveStringMultiline`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `PreviewImage`
- `EmptyFlux2LatentImage`

## 知识

覆盖率 **76%**（50/66）

**有卡**：`Label (rgthree)`、`KSamplerSelect`、`ConditioningZeroOut`、`CFGGuider`、`ReferenceLatent`、`VAELoader`、`CLIPLoader`、`Flux2Scheduler`、`UNETLoader`、`VAEDecode`、`easy imageConcat`、`CLIPTextEncode`、`VAEEncode`、`SaveImage`、`AILab_ImageCompare`、`EmptyFlux2LatentImage`、`LoraLoaderModelOnly`、`SamplerCustomAdvanced`、`GetImageSize`、`RandomNoise`、`AILab_ImageResize`、`LoadImage`、`Qwen3VL_Chat`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
