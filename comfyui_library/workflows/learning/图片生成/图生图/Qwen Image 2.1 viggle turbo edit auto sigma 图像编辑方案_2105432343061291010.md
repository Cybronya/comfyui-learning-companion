---
key: 图片生成/图生图/Qwen Image 2.1 viggle turbo edit auto sigma 图像编辑方案_2105432343061291010.json
name: Qwen Image 2.1 viggle turbo edit auto sigma 图像编辑方案_2105432343061291010
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 viggle turbo edit auto sigma 图像编辑方案_2105432343061291010.json
hash: 2ba543ccd7f6ceae
coverage: 0.846154
learned_at: 2026-10-21 00:42:08
nodes: [UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, PrimitiveStringMultiline, PrimitiveBoolean, PrimitiveStringMultiline, StringFormat, TextGenerate, JsonExtractString, StringCompare, ComfySwitchNode, ComfySwitchNode, PreviewAny, TextEncodeQwenImage21, BasicGuider, RandomNoise, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, VAEDecode, SaveImage, BatchImagesNode, QwenImage21Cache, PrimitiveBoolean, ComfySwitchNode, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, StringFormat, LoadImage, ResolutionSelector, EmptyLatentImage, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1 viggle turbo edit auto sigma 图像编辑方案_2105432343061291010.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 viggle turbo edit auto sigma 图像编辑方案_2105432343061291010.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（65 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `PrimitiveStringMultiline`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `StringFormat`
- `TextGenerate`
- `JsonExtractString`
- `StringCompare`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `PreviewAny`
- `TextEncodeQwenImage21`
- `BasicGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `BatchImagesNode`
- `QwenImage21Cache`
- `PrimitiveBoolean`
- `ComfySwitchNode`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `StringFormat`
- `LoadImage`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `LoadImage`
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
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **85%**（55/65）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`PrimitiveBoolean`、`StringFormat`、`TextGenerate`、`JsonExtractString`、`StringCompare`、`TextEncodeQwenImage21`、`BasicGuider`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`BatchImagesNode`、`QwenImage21Cache`、`MathExpression|pysssss`、`LoadImage`、`ResolutionSelector`、`EmptyLatentImage`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
