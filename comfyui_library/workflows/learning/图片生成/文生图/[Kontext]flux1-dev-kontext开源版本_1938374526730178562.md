---
key: 图片生成/文生图/[Kontext]flux1-dev-kontext开源版本_1938374526730178562.json
name: [Kontext]flux1-dev-kontext开源版本_1938374526730178562
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/[Kontext]flux1-dev-kontext开源版本_1938374526730178562.json
hash: 6fd620d4ec1328cf
coverage: 0.810811
learned_at: 2026-10-15 22:27:42
nodes: [BasicScheduler, KSamplerSelect, ModelSamplingFlux, SamplerCustomAdvanced, CLIPTextEncode, RandomNoise, VAELoader, FluxGuidance, easy showAnything, CR Integer To String, PrimitiveStringMultiline, easy ifElse, easy showAnything, CR Split String, StringToInt, StringToInt, Text Concatenate, CR Integer To String, GetImageSize, INTConstant, DualCLIPLoader, easy compare, JWStringGetLine, UNETLoader, BasicGuider, ETN_ReferenceImage, VAEDecode, EmptySD3LatentImage, VAEEncode, ReferenceLatent, Int, LoadImage, DeepTranslatorTextNode, SaveImage, PrimitiveStringMultiline, Note, Note]
patterns: []
missing: []
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

覆盖率 **81%**（30/37）

**有卡**：`BasicScheduler`、`KSamplerSelect`、`ModelSamplingFlux`、`SamplerCustomAdvanced`、`CLIPTextEncode`、`RandomNoise`、`VAELoader`、`FluxGuidance`、`CR Integer To String`、`CR Split String`、`StringToInt`、`Text Concatenate`、`GetImageSize`、`INTConstant`、`DualCLIPLoader`、`easy compare`、`JWStringGetLine`、`UNETLoader`、`BasicGuider`、`ETN_ReferenceImage`、`VAEDecode`、`EmptySD3LatentImage`、`VAEEncode`、`ReferenceLatent`、`Int`、`LoadImage`、`DeepTranslatorTextNode`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
