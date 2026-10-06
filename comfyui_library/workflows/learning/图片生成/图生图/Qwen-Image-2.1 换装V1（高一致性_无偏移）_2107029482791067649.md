---
key: 图片生成/图生图/Qwen-Image-2.1 换装V1（高一致性_无偏移）_2107029482791067649.json
name: Qwen-Image-2.1 换装V1（高一致性_无偏移）_2107029482791067649
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 换装V1（高一致性_无偏移）_2107029482791067649.json
hash: 0c27fd156ce37fd5
coverage: 0.268293
learned_at: 2026-10-06 21:41:54
nodes: [Text, Text, CR Text, PrimitiveBoolean, Text, SeedNode, DF_Integer, CLIPLoader, VAELoader, UNETLoader, LoraLoaderModelOnly, LoadImage, JWImageResizeByLongerSide, JWImageResizeByLongerSide, ImageScaleToTotalPixels, ImageScaleToTotalPixels, JWImageResizeByLongerSide, JWImageResizeByLongerSide, ImageScaleToTotalPixels, ImageScaleToTotalPixels, TextGenerate, RegexMatch, TextGenerate, RegexMatch, ComfySwitchNode, CR Text, CR Text, ComfySwitchNode, TextGenerate, RegexReplace, ComfySwitchNode, StringFormat, TextEncodeQwenImage21, QwenImage21Cache, KSampler, VAEDecode, SplitImageWithAlpha, Image Compare (mtb), PreviewImage, SaveImage, LoadImage]
patterns: []
missing: [CR Text, CR Text, CR Text, DF_Integer, Image Compare (mtb), ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, PrimitiveBoolean, RegexMatch, RegexMatch, RegexReplace, SplitImageWithAlpha, StringFormat, Text, Text, Text, TextGenerate, TextGenerate, TextGenerate, JWImageResizeByLongerSide, JWImageResizeByLongerSide, JWImageResizeByLongerSide, JWImageResizeByLongerSide, SeedNode]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 20261001, "steps": 25}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `DF_Integer` 知识库中没有该节点类型的任何知识, 次要节点 `Image Compare (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识, 次要节点 `PrimitiveBoolean` 知识库中没有该节点类型的任何知识, 次要节点 `RegexMatch` 知识库中没有该节点类型的任何知识, 次要节点 `RegexMatch` 知识库中没有该节点类型的任何知识, 次要节点 `RegexReplace` 知识库中没有该节点类型的任何知识, 次要节点 `SplitImageWithAlpha` 知识库中没有该节点类型的任何知识, 次要节点 `StringFormat` 知识库中没有该节点类型的任何知识, 次要节点 `Text` 知识库中没有该节点类型的任何知识, 次要节点 `Text` 知识库中没有该节点类型的任何知识, 次要节点 `Text` 知识库中没有该节点类型的任何知识, 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识, 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识, 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识, 次要节点 `JWImageResizeByLongerSide` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `JWImageResizeByLongerSide` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `JWImageResizeByLongerSide` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `JWImageResizeByLongerSide` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `SeedNode` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/Qwen-Image-2.1 换装V1（高一致性_无偏移）_2107029482791067649.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 换装V1（高一致性_无偏移）_2107029482791067649.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（41 个）：
- `Text`
- `Text`
- `CR Text`
- `PrimitiveBoolean`
- `Text`
- `SeedNode`
- `DF_Integer`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `JWImageResizeByLongerSide`
- `JWImageResizeByLongerSide`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `JWImageResizeByLongerSide`
- `JWImageResizeByLongerSide`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `TextGenerate`
- `RegexMatch`
- `TextGenerate`
- `RegexMatch`
- `ComfySwitchNode`
- `CR Text`
- `CR Text`
- `ComfySwitchNode`
- `TextGenerate`
- `RegexReplace`
- `ComfySwitchNode`
- `StringFormat`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SplitImageWithAlpha`
- `Image Compare (mtb)`
- `PreviewImage`
- `SaveImage`
- `LoadImage`

## 关键参数

- `seed` = `20261001`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **27%**（11/41）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`SaveImage`

**缺卡**（26）：`CR Text`、`CR Text`、`CR Text`、`DF_Integer`、`Image Compare (mtb)`、`ImageScaleToTotalPixels`、`ImageScaleToTotalPixels`、`ImageScaleToTotalPixels`、`ImageScaleToTotalPixels`、`PrimitiveBoolean`、`RegexMatch`、`RegexMatch`、`RegexReplace`、`SplitImageWithAlpha`、`StringFormat`、`Text`、`Text`、`Text`、`TextGenerate`、`TextGenerate`、`TextGenerate`、`JWImageResizeByLongerSide`、`JWImageResizeByLongerSide`、`JWImageResizeByLongerSide`、`JWImageResizeByLongerSide`、`SeedNode`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `DF_Integer` 知识库中没有该节点类型的任何知识
- 次要节点 `Image Compare (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识
- 次要节点 `PrimitiveBoolean` 知识库中没有该节点类型的任何知识
- 次要节点 `RegexMatch` 知识库中没有该节点类型的任何知识
- 次要节点 `RegexMatch` 知识库中没有该节点类型的任何知识
- 次要节点 `RegexReplace` 知识库中没有该节点类型的任何知识
- 次要节点 `SplitImageWithAlpha` 知识库中没有该节点类型的任何知识
- 次要节点 `StringFormat` 知识库中没有该节点类型的任何知识
- 次要节点 `Text` 知识库中没有该节点类型的任何知识
- 次要节点 `Text` 知识库中没有该节点类型的任何知识
- 次要节点 `Text` 知识库中没有该节点类型的任何知识
- 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识
- 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识
- 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识
- 次要节点 `JWImageResizeByLongerSide` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `JWImageResizeByLongerSide` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `JWImageResizeByLongerSide` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `JWImageResizeByLongerSide` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `SeedNode` 仅有 KSampler 的通用知识，没有该节点自己的说明
