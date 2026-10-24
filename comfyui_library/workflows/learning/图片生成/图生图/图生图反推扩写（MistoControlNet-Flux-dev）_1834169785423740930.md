---
key: 图片生成/图生图/图生图反推扩写（MistoControlNet-Flux-dev）_1834169785423740930.json
name: 图生图反推扩写（MistoControlNet-Flux-dev）_1834169785423740930
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图生图反推扩写（MistoControlNet-Flux-dev）_1834169785423740930.json
hash: 24a7e03a1e3a9af2
coverage: 0.652174
learned_at: 2026-10-23 12:43:36
nodes: [CLIPTextEncodeFlux, VAELoader, CheckpointLoaderSimple, Reroute, SaveImage, LoadTheMistoFluxControlNet, DualCLIPLoader, CLIPTextEncodeFlux, PreviewImage, AnyLineArtPreprocessor_aux, Note, KSamplerTheMisto, DeepTranslatorTextNode, RH_Prompter, WD14Tagger|pysssss, ShowText|pysssss, Note, ShowText|pysssss, Note, LoadImage, ApplyTheMistoFluxControlNet, LoraLoaderModelOnly, PreviewImage]
patterns: []
missing: []
parameters: {"checkpoint": "flux1-dev-fp8-Comfy-Org.safetensors"}
---

# 图片生成/图生图/图生图反推扩写（MistoControlNet-Flux-dev）_1834169785423740930.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图生图反推扩写（MistoControlNet-Flux-dev）_1834169785423740930.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Output → Other

**节点**（23 个）：
- `CLIPTextEncodeFlux` ★核心
- `VAELoader`
- `CheckpointLoaderSimple` ★核心
- `Reroute`
- `SaveImage`
- `LoadTheMistoFluxControlNet`
- `DualCLIPLoader`
- `CLIPTextEncodeFlux` ★核心
- `PreviewImage`
- `AnyLineArtPreprocessor_aux`
- `Note`
- `KSamplerTheMisto` ★核心
- `DeepTranslatorTextNode`
- `RH_Prompter`
- `WD14Tagger|pysssss`
- `ShowText|pysssss`
- `Note`
- `ShowText|pysssss`
- `Note`
- `LoadImage`
- `ApplyTheMistoFluxControlNet`
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`

## 关键参数

- `checkpoint` = `flux1-dev-fp8-Comfy-Org.safetensors`

## 知识

覆盖率 **65%**（15/23）

**有卡**：`CLIPTextEncodeFlux`、`VAELoader`、`CheckpointLoaderSimple`、`SaveImage`、`LoadTheMistoFluxControlNet`、`DualCLIPLoader`、`AnyLineArtPreprocessor_aux`、`KSamplerTheMisto`、`DeepTranslatorTextNode`、`RH_Prompter`、`WD14Tagger|pysssss`、`LoadImage`、`ApplyTheMistoFluxControlNet`、`LoraLoaderModelOnly`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、LoadImage、ApplyTheMistoFluxControlNet、LoadTheMistoFluxControlNet、KSamplerTheMisto、CLIPTextEncodeFlux
