---
key: 图片生成/文生图/[Kontext]flux1-dev-kontext开源版本_1938374526730178562.json
name: [Kontext]flux1-dev-kontext开源版本_1938374526730178562
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/[Kontext]flux1-dev-kontext开源版本_1938374526730178562.json
hash: 6fd620d4ec1328cf
coverage: 0.675676
learned_at: 2026-10-10 23:16:13
nodes: [BasicScheduler, KSamplerSelect, ModelSamplingFlux, SamplerCustomAdvanced, CLIPTextEncode, RandomNoise, VAELoader, FluxGuidance, easy showAnything, CR Integer To String, PrimitiveStringMultiline, easy ifElse, easy showAnything, CR Split String, StringToInt, StringToInt, Text Concatenate, CR Integer To String, GetImageSize, INTConstant, DualCLIPLoader, easy compare, JWStringGetLine, UNETLoader, BasicGuider, ETN_ReferenceImage, VAEDecode, EmptySD3LatentImage, VAEEncode, ReferenceLatent, Int, LoadImage, DeepTranslatorTextNode, SaveImage, PrimitiveStringMultiline, Note, Note]
patterns: []
missing: [CR Integer To String, CR Integer To String, CR Split String, Text Concatenate, easy compare]
discoveries: [次要节点 `CR Integer To String` 知识库中没有该节点类型的任何知识, 次要节点 `CR Integer To String` 知识库中没有该节点类型的任何知识, 次要节点 `CR Split String` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `easy compare` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/[Kontext]flux1-dev-kontext开源版本_1938374526730178562.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/[Kontext]flux1-dev-kontext开源版本_1938374526730178562.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `ModelSamplingFlux`
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `VAELoader`
- `FluxGuidance`
- `easy showAnything`
- `CR Integer To String`
- `PrimitiveStringMultiline`
- `easy ifElse`
- `easy showAnything`
- `CR Split String`
- `StringToInt`
- `StringToInt`
- `Text Concatenate`
- `CR Integer To String`
- `GetImageSize`
- `INTConstant`
- `DualCLIPLoader`
- `easy compare`
- `JWStringGetLine`
- `UNETLoader` ★核心
- `BasicGuider`
- `ETN_ReferenceImage`
- `VAEDecode` ★核心
- `EmptySD3LatentImage`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `Int`
- `LoadImage`
- `DeepTranslatorTextNode`
- `SaveImage`
- `PrimitiveStringMultiline`
- `Note`
- `Note`

## 知识

覆盖率 **68%**（25/37）

**有卡**：`BasicScheduler`、`KSamplerSelect`、`ModelSamplingFlux`、`SamplerCustomAdvanced`、`CLIPTextEncode`、`RandomNoise`、`VAELoader`、`FluxGuidance`、`StringToInt`、`GetImageSize`、`INTConstant`、`DualCLIPLoader`、`JWStringGetLine`、`UNETLoader`、`BasicGuider`、`ETN_ReferenceImage`、`VAEDecode`、`EmptySD3LatentImage`、`VAEEncode`、`ReferenceLatent`、`Int`、`LoadImage`、`DeepTranslatorTextNode`、`SaveImage`

**缺卡**（5）：`CR Integer To String`、`CR Integer To String`、`CR Split String`、`Text Concatenate`、`easy compare`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced

## 学习发现

- 次要节点 `CR Integer To String` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Integer To String` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Split String` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `easy compare` 知识库中没有该节点类型的任何知识
