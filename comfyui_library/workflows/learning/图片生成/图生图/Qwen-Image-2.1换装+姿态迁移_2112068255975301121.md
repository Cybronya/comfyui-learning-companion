---
key: 图片生成/图生图/Qwen-Image-2.1换装+姿态迁移_2112068255975301121.json
name: Qwen-Image-2.1换装+姿态迁移_2112068255975301121
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1换装+姿态迁移_2112068255975301121.json
hash: b2fc2b14e14e2950
coverage: 0.789474
learned_at: 2026-10-23 11:16:28
nodes: [SeedNode, DF_Integer, VAELoader, JWImageResizeByLongerSide, JWImageResizeByLongerSide, TextGenerate, VAEDecode, SplitImageWithAlpha, KSampler, CR Text, CR Text, ImageScaleToTotalPixels, 孤海注释, LoadImage, QwenImage21Cache, SaveImage, RegexMatch, CR Text, Text, TextGenerate, ImageScaleToTotalPixels, JWImageResizeByLongerSide, JWImageResizeByLongerSide, ImageScaleToTotalPixels, ImageScaleToTotalPixels, RegexMatch, GoohaiDisplayAny, ComfySwitchNode, ComfySwitchNode, TextEncodeQwenImage21, RegexReplace, TextGenerate, CLIPLoader, SDPoseOODLoader, SDPoseOODProcessor, LoadImage, ComfySwitchNode, GoohaiDisplayAny, GoohaiDisplayAny, PrimitiveBoolean, Text, Text, UNETLoader, LoraLoaderModelOnly, LoadImage, LoadImage, PreviewImage, GoohaiDisplayAny, StringFormat, GoohaiDisplayAny, Image Comparer (rgthree), 孤海注释, 孤海注释, 孤海注释, 孤海注释, 孤海注释, 孤海注释]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 20261001, "steps": 25}
---

# 图片生成/图生图/Qwen-Image-2.1换装+姿态迁移_2112068255975301121.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1换装+姿态迁移_2112068255975301121.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
- `SeedNode`
- `DF_Integer`
- `VAELoader`
- `JWImageResizeByLongerSide`
- `JWImageResizeByLongerSide`
- `TextGenerate`
- `VAEDecode` ★核心
- `SplitImageWithAlpha`
- `KSampler` ★核心
- `CR Text`
- `CR Text`
- `ImageScaleToTotalPixels`
- `孤海注释`
- `LoadImage`
- `QwenImage21Cache`
- `SaveImage`
- `RegexMatch`
- `CR Text`
- `Text`
- `TextGenerate`
- `ImageScaleToTotalPixels`
- `JWImageResizeByLongerSide`
- `JWImageResizeByLongerSide`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `RegexMatch`
- `GoohaiDisplayAny`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `RegexReplace`
- `TextGenerate`
- `CLIPLoader`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `LoadImage`
- `ComfySwitchNode`
- `GoohaiDisplayAny`
- `GoohaiDisplayAny`
- `PrimitiveBoolean`
- `Text`
- `Text`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `GoohaiDisplayAny`
- `StringFormat`
- `GoohaiDisplayAny`
- `Image Comparer (rgthree)`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`

## 关键参数

- `seed` = `20261001`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（45/57）

**有卡**：`SeedNode`、`DF_Integer`、`VAELoader`、`JWImageResizeByLongerSide`、`TextGenerate`、`VAEDecode`、`SplitImageWithAlpha`、`KSampler`、`CR Text`、`ImageScaleToTotalPixels`、`LoadImage`、`QwenImage21Cache`、`SaveImage`、`RegexMatch`、`Text`、`GoohaiDisplayAny`、`TextEncodeQwenImage21`、`RegexReplace`、`CLIPLoader`、`SDPoseOODLoader`、`SDPoseOODProcessor`、`PrimitiveBoolean`、`UNETLoader`、`LoraLoaderModelOnly`、`StringFormat`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache
