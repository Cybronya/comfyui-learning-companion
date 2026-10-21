---
key: 图片生成/图生图/Qwen-Image 2.1角色三视图｜5倍加速出图 人物角色设计必备_2105549633886973953.json
name: Qwen-Image 2.1角色三视图｜5倍加速出图 人物角色设计必备_2105549633886973953
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image 2.1角色三视图｜5倍加速出图 人物角色设计必备_2105549633886973953.json
hash: 45dc629b342af5b9
coverage: 0.865854
learned_at: 2026-10-21 00:43:11
nodes: [LoraLoaderModelOnly, RandomNoise, KSamplerSelect, ManualSigmas, LoraLoaderModelOnly, SamplerCustomAdvanced, Reroute, Reroute, MathExpression|pysssss, BasicGuider, StringFormat, CLIPLoader, ResolutionSelector, UNETLoader, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, VAEDecode, easy imageConcat, PreviewImage, CLIPLoader, QwenImage21Cache, TextEncodeQwenImage21, EmptyLatentImage, UNETLoader, QwenImage21Cache, KSampler, PrimitiveStringMultiline, TextGenerateLTX2Prompt, easy showAnything, JsonExtractString, VAELoader, VAEDecode, PreviewImage, SaveImage, SeedNode, LoadImage, PrimitiveStringMultiline, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Image 2.1角色三视图｜5倍加速出图 人物角色设计必备_2105549633886973953.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image 2.1角色三视图｜5倍加速出图 人物角色设计必备_2105549633886973953.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（82 个）：
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LoraLoaderModelOnly` ★核心
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `Reroute`
- `MathExpression|pysssss`
- `BasicGuider`
- `StringFormat`
- `CLIPLoader`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `VAEDecode` ★核心
- `easy imageConcat`
- `PreviewImage`
- `CLIPLoader`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `KSampler` ★核心
- `PrimitiveStringMultiline`
- `TextGenerateLTX2Prompt`
- `easy showAnything`
- `JsonExtractString`
- `VAELoader`
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImage`
- `SeedNode`
- `LoadImage`
- `PrimitiveStringMultiline`
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

覆盖率 **87%**（71/82）

**有卡**：`LoraLoaderModelOnly`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`MathExpression|pysssss`、`BasicGuider`、`StringFormat`、`CLIPLoader`、`ResolutionSelector`、`UNETLoader`、`VAEDecode`、`easy imageConcat`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`KSampler`、`TextGenerateLTX2Prompt`、`JsonExtractString`、`VAELoader`、`SaveImage`、`SeedNode`、`LoadImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
