---
key: 图片生成/文生图/Qwen Image 2.1文生图原生FUN Viggle三图对比，图生图处理方案_2105795635810226177.json
name: Qwen Image 2.1文生图原生FUN Viggle三图对比，图生图处理方案_2105795635810226177
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图原生FUN Viggle三图对比，图生图处理方案_2105795635810226177.json
hash: e36a3400647aee54
coverage: 0.894737
learned_at: 2026-10-06 22:37:49
nodes: [StringConstantMultiline, INTConstant, INTConstant, INTConstant, UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, EmptyLatentImage, KSampler, LoraLoaderModelOnly, BasicGuider, RandomNoise, KSamplerSelect, CustomSigmas, SamplerCustomAdvanced, VAEDecode, VAEDecode, VAEDecode, SaveImage, T8QwenImage21FunAccPDD4Step, SaveImage, AddLabel, SaveImage, AddLabel, SaveImage, AddLabel, ImageConcatMulti, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [CustomSigmas, T8QwenImage21FunAccPDD4Step]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CustomSigmas` 知识库中没有该节点类型的任何知识, 次要节点 `T8QwenImage21FunAccPDD4Step` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1文生图原生FUN Viggle三图对比，图生图处理方案_2105795635810226177.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图原生FUN Viggle三图对比，图生图处理方案_2105795635810226177.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
- `StringConstantMultiline`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `BasicGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CustomSigmas`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `T8QwenImage21FunAccPDD4Step`
- `SaveImage`
- `AddLabel`
- `SaveImage`
- `AddLabel`
- `SaveImage`
- `AddLabel`
- `ImageConcatMulti`
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

覆盖率 **89%**（51/57）

**有卡**：`StringConstantMultiline`、`INTConstant`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`KSampler`、`LoraLoaderModelOnly`、`BasicGuider`、`RandomNoise`、`KSamplerSelect`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`AddLabel`、`ImageConcatMulti`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（2）：`CustomSigmas`、`T8QwenImage21FunAccPDD4Step`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CustomSigmas` 知识库中没有该节点类型的任何知识
- 次要节点 `T8QwenImage21FunAccPDD4Step` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
