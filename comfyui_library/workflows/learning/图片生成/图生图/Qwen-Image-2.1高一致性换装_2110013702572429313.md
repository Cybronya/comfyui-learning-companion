---
key: 图片生成/图生图/Qwen-Image-2.1高一致性换装_2110013702572429313.json
name: Qwen-Image-2.1高一致性换装_2110013702572429313
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1高一致性换装_2110013702572429313.json
hash: 6a8d22150bf056c1
coverage: 0.860465
learned_at: 2026-10-23 11:16:32
nodes: [Text, Text, SeedNode, DF_Integer, CLIPLoader, VAELoader, UNETLoader, JWImageResizeByLongerSide, JWImageResizeByLongerSide, JWImageResizeByLongerSide, ImageScaleToTotalPixels, TextGenerate, RegexMatch, RegexReplace, StringFormat, QwenImage21Cache, VAEDecode, SplitImageWithAlpha, LoraLoaderModelOnly, TextEncodeQwenImage21, ImageScaleToTotalPixels, KSampler, TextGenerate, CR Text, CR Text, CR Text, RegexMatch, ComfySwitchNode, ComfySwitchNode, TextGenerate, ImageScaleToTotalPixels, ComfySwitchNode, ImageScaleToTotalPixels, JWImageResizeByLongerSide, PrimitiveBoolean, Text, 孤海注释, 孤海注释, LoadImage, LoadImage, PreviewImage, SaveImage, Image Compare (mtb)]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 20261001, "steps": 25}
---

# 图片生成/图生图/Qwen-Image-2.1高一致性换装_2110013702572429313.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1高一致性换装_2110013702572429313.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `Text`
- `Text`
- `SeedNode`
- `DF_Integer`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `JWImageResizeByLongerSide`
- `JWImageResizeByLongerSide`
- `JWImageResizeByLongerSide`
- `ImageScaleToTotalPixels`
- `TextGenerate`
- `RegexMatch`
- `RegexReplace`
- `StringFormat`
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `SplitImageWithAlpha`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImage21`
- `ImageScaleToTotalPixels`
- `KSampler` ★核心
- `TextGenerate`
- `CR Text`
- `CR Text`
- `CR Text`
- `RegexMatch`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `TextGenerate`
- `ImageScaleToTotalPixels`
- `ComfySwitchNode`
- `ImageScaleToTotalPixels`
- `JWImageResizeByLongerSide`
- `PrimitiveBoolean`
- `Text`
- `孤海注释`
- `孤海注释`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `Image Compare (mtb)`

## 关键参数

- `seed` = `20261001`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（37/43）

**有卡**：`Text`、`SeedNode`、`DF_Integer`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`JWImageResizeByLongerSide`、`ImageScaleToTotalPixels`、`TextGenerate`、`RegexMatch`、`RegexReplace`、`StringFormat`、`QwenImage21Cache`、`VAEDecode`、`SplitImageWithAlpha`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`、`KSampler`、`CR Text`、`PrimitiveBoolean`、`LoadImage`、`SaveImage`、`Image Compare (mtb)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache
