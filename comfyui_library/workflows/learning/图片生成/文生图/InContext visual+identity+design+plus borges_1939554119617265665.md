---
key: 图片生成/文生图/InContext visual+identity+design+plus borges_1939554119617265665.json
name: InContext visual+identity+design+plus borges_1939554119617265665
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/InContext visual+identity+design+plus borges_1939554119617265665.json
hash: d1ec1fcd2554e4b3
coverage: 0.659574
learned_at: 2026-10-10 20:58:40
nodes: [Seed Everywhere, EmptyLatentImage, CR Draw Shape, CR Draw Shape, ImageConcanate, ImageConcanate, UNETLoader, DualCLIPLoader, JoyCaption2_simple, Note, VAELoader, TTP_text_mix, GetImageSizeAndCount, LoraLoaderModelOnly, MathExpression|pysssss, MathExpression|pysssss, SaveImage, PreviewImage, TextInput_, TextInput_, Note, Note, VAEDecode, CLIPTextEncode, BasicGuider, KSamplerSelect, VAEEncode, SetLatentNoiseMask, ImageCrop, ImageToMask, RandomNoise, SamplerCustomAdvanced, PreviewImage, ImageScale, Note, ShowText|pysssss, ModelSamplingFlux, PreviewImage, BasicScheduler, FileNamePrefix, ExtraOptionsNode, Note, PreviewImage, LoadImage, RMBG, Note Plus (mtb), LoadImageFromUrl]
patterns: []
missing: [CR Draw Shape, CR Draw Shape, MathExpression|pysssss, MathExpression|pysssss, Note Plus (mtb), Seed Everywhere]
parameters: {"batch_size": 1, "height": 1344, "width": 768}
discoveries: [次要节点 `CR Draw Shape` 知识库中没有该节点类型的任何知识, 次要节点 `CR Draw Shape` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/InContext visual+identity+design+plus borges_1939554119617265665.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/InContext visual+identity+design+plus borges_1939554119617265665.json`

## 结构

**节点**（47 个）：
- `Seed Everywhere`
- `EmptyLatentImage`
- `CR Draw Shape`
- `CR Draw Shape`
- `ImageConcanate`
- `ImageConcanate`
- `UNETLoader`
- `DualCLIPLoader`
- `JoyCaption2_simple`
- `Note`
- `VAELoader`
- `TTP_text_mix`
- `GetImageSizeAndCount`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `SaveImage`
- `PreviewImage`
- `TextInput_`
- `TextInput_`
- `Note`
- `Note`
- `VAEDecode`
- `CLIPTextEncode`
- `BasicGuider`
- `KSamplerSelect`
- `VAEEncode`
- `SetLatentNoiseMask`
- `ImageCrop`
- `ImageToMask`
- `RandomNoise`
- `SamplerCustomAdvanced`
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

- `batch_size` = `1`
- `height` = `1344`
- `width` = `768`

## 知识

覆盖率 **66%**（31/47）

**有卡**：`Seed Everywhere`、`EmptyLatentImage`、`CR Draw Shape`、`ImageConcanate`、`UNETLoader`、`DualCLIPLoader`、`JoyCaption2_simple`、`Note`、`VAELoader`、`TTP_text_mix`、`GetImageSizeAndCount`、`LoraLoaderModelOnly`、`MathExpression|pysssss`、`SaveImage`、`PreviewImage`、`TextInput_`、`VAEDecode`、`CLIPTextEncode`、`BasicGuider`、`KSamplerSelect`、`VAEEncode`、`SetLatentNoiseMask`、`ImageCrop`、`ImageToMask`、`RandomNoise`

**缺卡**（6）：`CR Draw Shape`、`CR Draw Shape`、`MathExpression|pysssss`、`MathExpression|pysssss`、`Note Plus (mtb)`、`Seed Everywhere`

## 学习发现

- 次要节点 `CR Draw Shape` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Draw Shape` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明
