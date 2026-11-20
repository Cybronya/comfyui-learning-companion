---
key: 平台全量/F.2 klein 9b一键多角度漫剧分镜流免费版_2058435700449701890.json
name: F.2 klein 9b一键多角度漫剧分镜流免费版_2058435700449701890
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/F.2 klein 9b一键多角度漫剧分镜流免费版_2058435700449701890.json
hash: 50bdcfe84dc037f9
coverage: 0.574627
learned_at: 2026-11-14 00:24:07
nodes: [CR Text Concatenate, GetNode, CR Text Concatenate, GetNode, GetNode, GetNode, CR Text Concatenate, Split String, CR Text Concatenate, CR Text Concatenate, GetNode, KSamplerSelect, RandomNoise, CFGGuider, Flux2Scheduler, SamplerCustomAdvanced, VAEDecode, Reroute, VAELoader, Reroute, Reroute, CLIPLoader, Reroute, Reroute, UNETLoader, Reroute, CLIPTextEncode, VAEEncode, Reroute, Reroute, VAEEncode, Reroute, Reroute, ReferenceLatent, ReferenceLatent, GetImageSize, ReferenceLatent, ReferenceLatent, Reroute, Reroute, ShowText|pysssss, ShowText|pysssss, ShowText|pysssss, CLIPTextEncode, ShowText|pysssss, ShowText|pysssss, List of strings [Crystools], EmptyFlux2LatentImage, SomethingToString, PromptBatchQueue, SetNode, Note, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, ShowText|pysssss, INTConstant, LoadImage, ShowText|pysssss, CR Text Concatenate, CR Text Concatenate, Split String, CR Text Concatenate, CR Text Concatenate, KSamplerSelect, RandomNoise, CFGGuider, Flux2Scheduler, SamplerCustomAdvanced, VAEDecode, Reroute, Reroute, Reroute, CLIPLoader, Reroute, Reroute, UNETLoader, Reroute, CLIPTextEncode, Reroute, Reroute, VAEEncode, Reroute, Reroute, Reroute, ReferenceLatent, ReferenceLatent, GetImageSize, ReferenceLatent, ReferenceLatent, Reroute, ShowText|pysssss, ShowText|pysssss, ShowText|pysssss, CLIPTextEncode, ShowText|pysssss, ShowText|pysssss, List of strings [Crystools], EmptyFlux2LatentImage, Reroute, SomethingToString, PromptBatchQueue, Reroute, MarkdownNote, Note, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, ShowText|pysssss, INTConstant, LoadImage, MarkdownNote, SaveImage, INTConstant, ShowText|pysssss, VAEEncode, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, VAELoader, Reroute, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, CR Text Concatenate, CR Prompt Text, CR Prompt Text, LoadImage, LoadImage, INTConstant, LoadImage, CR Prompt Text, SaveImage, CR Prompt Text]
patterns: []
missing: []
---

# 平台全量/F.2 klein 9b一键多角度漫剧分镜流免费版_2058435700449701890.json

> 来源文件 `comfyui_library/workflows/平台全量/F.2 klein 9b一键多角度漫剧分镜流免费版_2058435700449701890.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（134 个）：
- `CR Text Concatenate`
- `GetNode`
- `CR Text Concatenate`
- `GetNode`
- `GetNode`
- `GetNode`
- `CR Text Concatenate`
- `Split String`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `GetNode`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CFGGuider`
- `Flux2Scheduler`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `Reroute`
- `VAELoader`
- `Reroute`
- `Reroute`
- `CLIPLoader`
- `Reroute`
- `Reroute`
- `UNETLoader` ★核心
- `Reroute`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `Reroute`
- `Reroute`
- `VAEEncode` ★核心
- `Reroute`
- `Reroute`
- `ReferenceLatent`
- `ReferenceLatent`
- `GetImageSize`
- `ReferenceLatent`
- `ReferenceLatent`
- `Reroute`
- `Reroute`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `ShowText|pysssss`
- `ShowText|pysssss`
- `List of strings [Crystools]`
- `EmptyFlux2LatentImage`
- `SomethingToString`
- `PromptBatchQueue`
- `SetNode`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ShowText|pysssss`
- `INTConstant`
- `LoadImage`
- `ShowText|pysssss`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `Split String`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CFGGuider`
- `Flux2Scheduler`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `CLIPLoader`
- `Reroute`
- `Reroute`
- `UNETLoader` ★核心
- `Reroute`
- `CLIPTextEncode` ★核心
- `Reroute`
- `Reroute`
- `VAEEncode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `ReferenceLatent`
- `ReferenceLatent`
- `GetImageSize`
- `ReferenceLatent`
- `ReferenceLatent`
- `Reroute`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `ShowText|pysssss`
- `ShowText|pysssss`
- `List of strings [Crystools]`
- `EmptyFlux2LatentImage`
- `Reroute`
- `SomethingToString`
- `PromptBatchQueue`
- `Reroute`
- `MarkdownNote`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ShowText|pysssss`
- `INTConstant`
- `LoadImage`
- `MarkdownNote`
- `SaveImage`
- `INTConstant`
- `ShowText|pysssss`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAELoader`
- `Reroute`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CR Text Concatenate`
- `CR Prompt Text`
- `CR Prompt Text`
- `LoadImage`
- `LoadImage`
- `INTConstant`
- `LoadImage`
- `CR Prompt Text`
- `SaveImage`
- `CR Prompt Text`

## 知识

覆盖率 **57%**（77/134）

**有卡**：`CR Text Concatenate`、`Split String`、`KSamplerSelect`、`RandomNoise`、`CFGGuider`、`Flux2Scheduler`、`SamplerCustomAdvanced`、`VAEDecode`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`CLIPTextEncode`、`VAEEncode`、`ReferenceLatent`、`GetImageSize`、`List of strings [Crystools]`、`EmptyFlux2LatentImage`、`SomethingToString`、`PromptBatchQueue`、`LayerUtility: ImageScaleByAspectRatio V2`、`INTConstant`、`LoadImage`、`SaveImage`、`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPLoader、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect
