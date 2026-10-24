---
key: 图片生成/图生图/Qwen-Image-2.1高一致性换装，服装展示商品替换自如_2110506858170642433.json
name: Qwen-Image-2.1高一致性换装，服装展示商品替换自如_2110506858170642433
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1高一致性换装，服装展示商品替换自如_2110506858170642433.json
hash: b5f751403e63d364
coverage: 0.885714
learned_at: 2026-10-23 11:16:32
nodes: [Text, Text, SeedNode, DF_Integer, CLIPLoader, VAELoader, UNETLoader, JWImageResizeByLongerSide, JWImageResizeByLongerSide, JWImageResizeByLongerSide, ImageScaleToTotalPixels, TextGenerate, RegexMatch, RegexReplace, StringFormat, QwenImage21Cache, VAEDecode, SplitImageWithAlpha, LoraLoaderModelOnly, TextEncodeQwenImage21, ImageScaleToTotalPixels, KSampler, TextGenerate, CR Text, CR Text, CR Text, RegexMatch, ComfySwitchNode, ComfySwitchNode, TextGenerate, ImageScaleToTotalPixels, ComfySwitchNode, ImageScaleToTotalPixels, JWImageResizeByLongerSide, PrimitiveBoolean, Text, LoadImage, LoadImage, PreviewImage, SaveImage, Image Compare (mtb), 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Image-2.1高一致性换装，服装展示商品替换自如_2110506858170642433.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1高一致性换装，服装展示商品替换自如_2110506858170642433.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（70 个）：
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
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `Image Compare (mtb)`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（62/70）

**有卡**：`Text`、`SeedNode`、`DF_Integer`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`JWImageResizeByLongerSide`、`ImageScaleToTotalPixels`、`TextGenerate`、`RegexMatch`、`RegexReplace`、`StringFormat`、`QwenImage21Cache`、`VAEDecode`、`SplitImageWithAlpha`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`、`KSampler`、`CR Text`、`PrimitiveBoolean`、`LoadImage`、`SaveImage`、`Image Compare (mtb)`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
