---
key: 图片生成/图生图/Qwen-Image-2.1换装V2高一致性版｜服装替换无偏移不跑版型_2107300495013539841.json
name: Qwen-Image-2.1换装V2高一致性版｜服装替换无偏移不跑版型_2107300495013539841
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1换装V2高一致性版｜服装替换无偏移不跑版型_2107300495013539841.json
hash: 020344dc74f27330
coverage: 0.583333
learned_at: 2026-10-06 21:42:03
nodes: [Text, Text, CR Text, PrimitiveBoolean, Text, SeedNode, DF_Integer, CLIPLoader, VAELoader, UNETLoader, LoadImage, JWImageResizeByLongerSide, JWImageResizeByLongerSide, ImageScaleToTotalPixels, ImageScaleToTotalPixels, JWImageResizeByLongerSide, JWImageResizeByLongerSide, ImageScaleToTotalPixels, ImageScaleToTotalPixels, TextGenerate, RegexMatch, TextGenerate, RegexMatch, ComfySwitchNode, CR Text, CR Text, ComfySwitchNode, TextGenerate, RegexReplace, ComfySwitchNode, StringFormat, TextEncodeQwenImage21, QwenImage21Cache, KSampler, VAEDecode, SplitImageWithAlpha, Image Compare (mtb), PreviewImage, SaveImage, LoadImage, LoraLoaderModelOnly, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [CR Text, CR Text, CR Text, DF_Integer, Image Compare (mtb), ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, PrimitiveBoolean, RegexMatch, RegexMatch, RegexReplace, SplitImageWithAlpha, StringFormat, Text, Text, Text, TextGenerate, TextGenerate, TextGenerate, JWImageResizeByLongerSide, JWImageResizeByLongerSide, JWImageResizeByLongerSide, JWImageResizeByLongerSide, SeedNode, solarL_SaveImagesToZip]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `DF_Integer` 知识库中没有该节点类型的任何知识, 次要节点 `Image Compare (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识, 次要节点 `PrimitiveBoolean` 知识库中没有该节点类型的任何知识, 次要节点 `RegexMatch` 知识库中没有该节点类型的任何知识, 次要节点 `RegexMatch` 知识库中没有该节点类型的任何知识, 次要节点 `RegexReplace` 知识库中没有该节点类型的任何知识, 次要节点 `SplitImageWithAlpha` 知识库中没有该节点类型的任何知识, 次要节点 `StringFormat` 知识库中没有该节点类型的任何知识, 次要节点 `Text` 知识库中没有该节点类型的任何知识, 次要节点 `Text` 知识库中没有该节点类型的任何知识, 次要节点 `Text` 知识库中没有该节点类型的任何知识, 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识, 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识, 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识, 次要节点 `JWImageResizeByLongerSide` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `JWImageResizeByLongerSide` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `JWImageResizeByLongerSide` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `JWImageResizeByLongerSide` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `SeedNode` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Image-2.1换装V2高一致性版｜服装替换无偏移不跑版型_2107300495013539841.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1换装V2高一致性版｜服装替换无偏移不跑版型_2107300495013539841.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（84 个）：
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
- `LoraLoaderModelOnly` ★核心
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
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

覆盖率 **58%**（49/84）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoadImage`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`SaveImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`EmptyLatentImage`

**缺卡**（27）：`CR Text`、`CR Text`、`CR Text`、`DF_Integer`、`Image Compare (mtb)`、`ImageScaleToTotalPixels`、`ImageScaleToTotalPixels`、`ImageScaleToTotalPixels`、`ImageScaleToTotalPixels`、`PrimitiveBoolean`、`RegexMatch`、`RegexMatch`、`RegexReplace`、`SplitImageWithAlpha`、`StringFormat`、`Text`、`Text`、`Text`、`TextGenerate`、`TextGenerate`、`TextGenerate`、`JWImageResizeByLongerSide`、`JWImageResizeByLongerSide`、`JWImageResizeByLongerSide`、`JWImageResizeByLongerSide`、`SeedNode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

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
- 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
