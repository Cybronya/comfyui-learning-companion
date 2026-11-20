---
key: 平台全量/Qwen-Image 2.1｜5倍加速 _ 角色三视图工作流批处理_2117240144154677250.json
name: Qwen-Image 2.1｜5倍加速 _ 角色三视图工作流批处理_2117240144154677250
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-Image 2.1｜5倍加速 _ 角色三视图工作流批处理_2117240144154677250.json
hash: bccac5e03c822cc9
coverage: 0.711111
learned_at: 2026-11-14 00:51:30
nodes: [LoraLoaderModelOnly, RandomNoise, KSamplerSelect, ManualSigmas, LoraLoaderModelOnly, SamplerCustomAdvanced, Reroute, Reroute, MathExpression|pysssss, BasicGuider, StringFormat, CLIPLoader, ResolutionSelector, UNETLoader, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, VAEDecode, CLIPLoader, QwenImage21Cache, TextEncodeQwenImage21, EmptyLatentImage, UNETLoader, PrimitiveStringMultiline, TextGenerateLTX2Prompt, easy showAnything, JsonExtractString, VAELoader, SeedNode, LoadImage, MarkdownNote, PrimitiveStringMultiline, HAIGC_LoadImagesFromZip, MarkdownNote, ImageListToBatch+, ImageFromBatch+, PreviewImage, HAIGC_SaveImagesToZip, Reroute, Reroute, easy showAnything, PreviewImage, PreviewImage, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 平台全量/Qwen-Image 2.1｜5倍加速 _ 角色三视图工作流批处理_2117240144154677250.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-Image 2.1｜5倍加速 _ 角色三视图工作流批处理_2117240144154677250.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LoraLoaderModelOnly` ★核心
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `Reroute`
- `MathExpression|pysssss`
- `BasicGuider`
- `StringFormat`
- `CLIPLoader`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `VAEDecode` ★核心
- `CLIPLoader`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`
- `TextGenerateLTX2Prompt`
- `easy showAnything`
- `JsonExtractString`
- `VAELoader`
- `SeedNode`
- `LoadImage`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `HAIGC_LoadImagesFromZip`
- `MarkdownNote`
- `ImageListToBatch+`
- `ImageFromBatch+`
- `PreviewImage`
- `HAIGC_SaveImagesToZip`
- `Reroute`
- `Reroute`
- `easy showAnything`
- `PreviewImage`
- `PreviewImage`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **71%**（32/45）

**有卡**：`LoraLoaderModelOnly`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`MathExpression|pysssss`、`BasicGuider`、`StringFormat`、`CLIPLoader`、`ResolutionSelector`、`UNETLoader`、`VAEDecode`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`TextGenerateLTX2Prompt`、`JsonExtractString`、`VAELoader`、`SeedNode`、`LoadImage`、`HAIGC_LoadImagesFromZip`、`ImageListToBatch+`、`ImageFromBatch+`、`HAIGC_SaveImagesToZip`、`SaveImage`

**用到的条目**：TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
