---
key: 图片生成/文生图/InContext visual+identity+design+plus borges_1939554119617265665.json
name: InContext visual+identity+design+plus borges_1939554119617265665
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/InContext visual+identity+design+plus borges_1939554119617265665.json
hash: d1ec1fcd2554e4b3
coverage: 0.787234
learned_at: 2026-10-15 22:26:34
nodes: [Seed Everywhere, EmptyLatentImage, CR Draw Shape, CR Draw Shape, ImageConcanate, ImageConcanate, UNETLoader, DualCLIPLoader, JoyCaption2_simple, Note, VAELoader, TTP_text_mix, GetImageSizeAndCount, LoraLoaderModelOnly, MathExpression|pysssss, MathExpression|pysssss, SaveImage, PreviewImage, TextInput_, TextInput_, Note, Note, VAEDecode, CLIPTextEncode, BasicGuider, KSamplerSelect, VAEEncode, SetLatentNoiseMask, ImageCrop, ImageToMask, RandomNoise, SamplerCustomAdvanced, PreviewImage, ImageScale, Note, ShowText|pysssss, ModelSamplingFlux, PreviewImage, BasicScheduler, FileNamePrefix, ExtraOptionsNode, Note, PreviewImage, LoadImage, RMBG, Note Plus (mtb), LoadImageFromUrl]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1344, "width": 768}
---

# 图片生成/文生图/InContext visual+identity+design+plus borges_1939554119617265665.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/InContext visual+identity+design+plus borges_1939554119617265665.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `Seed Everywhere`
- `EmptyLatentImage` ★核心
- `CR Draw Shape`
- `CR Draw Shape`
- `ImageConcanate`
- `ImageConcanate`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `JoyCaption2_simple`
- `Note`
- `VAELoader`
- `TTP_text_mix`
- `GetImageSizeAndCount`
- `LoraLoaderModelOnly` ★核心
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `SaveImage`
- `PreviewImage`
- `TextInput_`
- `TextInput_`
- `Note`
- `Note`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `BasicGuider`
- `KSamplerSelect` ★核心
- `VAEEncode` ★核心
- `SetLatentNoiseMask`
- `ImageCrop`
- `ImageToMask`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `PreviewImage`
- `ImageScale`
- `Note`
- `ShowText|pysssss`
- `ModelSamplingFlux`
- `PreviewImage`
- `BasicScheduler`
- `FileNamePrefix`
- `ExtraOptionsNode`
- `Note`
- `PreviewImage`
- `LoadImage`
- `RMBG`
- `Note Plus (mtb)`
- `LoadImageFromUrl`

## 关键参数

- `width` = `768`
- `height` = `1344`
- `batch_size` = `1`

## 知识

覆盖率 **79%**（37/47）

**有卡**：`Seed Everywhere`、`EmptyLatentImage`、`CR Draw Shape`、`ImageConcanate`、`UNETLoader`、`DualCLIPLoader`、`JoyCaption2_simple`、`VAELoader`、`TTP_text_mix`、`GetImageSizeAndCount`、`LoraLoaderModelOnly`、`MathExpression|pysssss`、`SaveImage`、`TextInput_`、`VAEDecode`、`CLIPTextEncode`、`BasicGuider`、`KSamplerSelect`、`VAEEncode`、`SetLatentNoiseMask`、`ImageCrop`、`ImageToMask`、`RandomNoise`、`SamplerCustomAdvanced`、`ImageScale`、`ModelSamplingFlux`、`BasicScheduler`、`FileNamePrefix`、`ExtraOptionsNode`、`LoadImage`、`RMBG`、`Note Plus (mtb)`、`LoadImageFromUrl`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、KSamplerSelect
