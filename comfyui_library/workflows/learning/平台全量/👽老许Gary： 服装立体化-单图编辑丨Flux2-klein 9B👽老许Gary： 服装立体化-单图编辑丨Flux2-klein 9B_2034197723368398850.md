---
key: 平台全量/👽老许Gary： 服装立体化-单图编辑丨Flux2-klein 9B👽老许Gary： 服装立体化-单图编辑丨Flux2-klein 9B_2034197723368398850.json
name: 👽老许Gary： 服装立体化-单图编辑丨Flux2-klein 9B👽老许Gary： 服装立体化-单图编辑丨Flux2-klein 9B_2034197723368398850
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/👽老许Gary： 服装立体化-单图编辑丨Flux2-klein 9B👽老许Gary： 服装立体化-单图编辑丨Flux2-klein 9B_2034197723368398850.json
hash: 23a7bc64aa294de7
coverage: 0.590164
learned_at: 2026-11-14 02:54:52
nodes: [Note, Note, Note, Note, Note, Note, Note, ReferenceLatent, GetImageSize+, SamplerCustomAdvanced, VAEEncode, EmptyFlux2LatentImage, SetNode, SetNode, SetNode, Fast Groups Bypasser (rgthree), VAELoader, Flux2Scheduler, CFGGuider, KSamplerSelect, CLIPTextEncode, Int, Int, SaveImage, GetNode, GetNode, RandomNoise, MarkdownNote, VAEDecode, ImageStitch, MarkdownNote, AILab_ImageResize, Note, UNETLoader, CLIPLoader, Anything Everywhere3, ReferenceLatent, LayerUtility: PurgeVRAM V2, MarkdownNote, Seed (rgthree), LoadImage, CR Text, Qwen3VL_Chat, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, LoadImage, LoadImage, LoadImage, SaveImage, PreviewImage, CLIPTextEncode, PreviewAny, CR Text, LoraLoaderModelOnly, LoadImage, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), TextInputNode, CR Text]
patterns: []
missing: []
---

# 平台全量/👽老许Gary： 服装立体化-单图编辑丨Flux2-klein 9B👽老许Gary： 服装立体化-单图编辑丨Flux2-klein 9B_2034197723368398850.json

> 来源文件 `comfyui_library/workflows/平台全量/👽老许Gary： 服装立体化-单图编辑丨Flux2-klein 9B👽老许Gary： 服装立体化-单图编辑丨Flux2-klein 9B_2034197723368398850.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（61 个）：
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `ReferenceLatent`
- `GetImageSize+`
- `SamplerCustomAdvanced` ★核心
- `VAEEncode` ★核心
- `EmptyFlux2LatentImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `VAELoader`
- `Flux2Scheduler`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `Int`
- `Int`
- `SaveImage`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `MarkdownNote`
- `VAEDecode` ★核心
- `ImageStitch`
- `MarkdownNote`
- `AILab_ImageResize`
- `Note`
- `UNETLoader` ★核心
- `CLIPLoader`
- `Anything Everywhere3`
- `ReferenceLatent`
- `LayerUtility: PurgeVRAM V2`
- `MarkdownNote`
- `Seed (rgthree)`
- `LoadImage`
- `CR Text`
- `Qwen3VL_Chat`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `TextInputNode`
- `CR Text`

## 知识

覆盖率 **59%**（36/61）

**有卡**：`ReferenceLatent`、`GetImageSize+`、`SamplerCustomAdvanced`、`VAEEncode`、`EmptyFlux2LatentImage`、`VAELoader`、`Flux2Scheduler`、`CFGGuider`、`KSamplerSelect`、`CLIPTextEncode`、`Int`、`SaveImage`、`RandomNoise`、`VAEDecode`、`ImageStitch`、`AILab_ImageResize`、`UNETLoader`、`CLIPLoader`、`LayerUtility: PurgeVRAM V2`、`Seed (rgthree)`、`LoadImage`、`CR Text`、`Qwen3VL_Chat`、`LoraLoaderModelOnly`、`TextInputNode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、LoadImage、CFGGuider
