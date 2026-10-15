---
key: 图片生成/文生图/Qwen Image 2.1文生图原生FUN Viggle三图对比，图生图处理方案_2105795635810226177.json
name: Qwen Image 2.1文生图原生FUN Viggle三图对比，图生图处理方案_2105795635810226177
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图原生FUN Viggle三图对比，图生图处理方案_2105795635810226177.json
hash: e36a3400647aee54
coverage: 0.929825
learned_at: 2026-10-10 20:58:53
nodes: [StringConstantMultiline, INTConstant, INTConstant, INTConstant, UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, EmptyLatentImage, KSampler, LoraLoaderModelOnly, BasicGuider, RandomNoise, KSamplerSelect, CustomSigmas, SamplerCustomAdvanced, VAEDecode, VAEDecode, VAEDecode, SaveImage, T8QwenImage21FunAccPDD4Step, SaveImage, AddLabel, SaveImage, AddLabel, SaveImage, AddLabel, ImageConcatMulti, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1文生图原生FUN Viggle三图对比，图生图处理方案_2105795635810226177.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图原生FUN Viggle三图对比，图生图处理方案_2105795635810226177.json`

## 结构

**节点**（57 个）：
- `StringConstantMultiline`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `BasicGuider`
- `RandomNoise`
- `KSamplerSelect`
- `CustomSigmas`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `VAEDecode`
- `VAEDecode`
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
- `UNETLoader`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `KSampler`
- `EmptyLatentImage`
- `JjkText`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `solarL_SaveImagesToZip`
- `VAEDecode`
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `4.5`
- `denoise` = `1`
- `height` = `80`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `seed` = `598626327129635`
- `steps` = `4`
- `width` = `80`

## 知识

覆盖率 **93%**（53/57）

**有卡**：`StringConstantMultiline`、`INTConstant`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`KSampler`、`LoraLoaderModelOnly`、`BasicGuider`、`RandomNoise`、`KSamplerSelect`、`CustomSigmas`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`T8QwenImage21FunAccPDD4Step`、`AddLabel`、`ImageConcatMulti`、`孤海注释`、`JjkText`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
