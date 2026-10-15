---
key: 图片生成/图生图/Qwen-Image-2.1 换装V1（高一致性_无偏移）_2107029482791067649.json
name: Qwen-Image-2.1 换装V1（高一致性_无偏移）_2107029482791067649
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 换装V1（高一致性_无偏移）_2107029482791067649.json
hash: 0c27fd156ce37fd5
coverage: 0.902439
learned_at: 2026-10-15 22:25:23
nodes: [Text, Text, CR Text, PrimitiveBoolean, Text, SeedNode, DF_Integer, CLIPLoader, VAELoader, UNETLoader, LoraLoaderModelOnly, LoadImage, JWImageResizeByLongerSide, JWImageResizeByLongerSide, ImageScaleToTotalPixels, ImageScaleToTotalPixels, JWImageResizeByLongerSide, JWImageResizeByLongerSide, ImageScaleToTotalPixels, ImageScaleToTotalPixels, TextGenerate, RegexMatch, TextGenerate, RegexMatch, ComfySwitchNode, CR Text, CR Text, ComfySwitchNode, TextGenerate, RegexReplace, ComfySwitchNode, StringFormat, TextEncodeQwenImage21, QwenImage21Cache, KSampler, VAEDecode, SplitImageWithAlpha, Image Compare (mtb), PreviewImage, SaveImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 20261001, "steps": 25}
---

# 图片生成/图生图/Qwen-Image-2.1 换装V1（高一致性_无偏移）_2107029482791067649.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 换装V1（高一致性_无偏移）_2107029482791067649.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

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

覆盖率 **90%**（37/41）

**有卡**：`Text`、`CR Text`、`PrimitiveBoolean`、`SeedNode`、`DF_Integer`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`、`JWImageResizeByLongerSide`、`ImageScaleToTotalPixels`、`TextGenerate`、`RegexMatch`、`RegexReplace`、`StringFormat`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`SplitImageWithAlpha`、`Image Compare (mtb)`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache
