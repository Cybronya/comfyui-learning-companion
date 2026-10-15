---
key: 图片生成/文生图/Qwen Image2.1文生图三件套｜原生FUN Viggle三图对比全都有_2105538670647406594.json
name: Qwen Image2.1文生图三件套｜原生FUN Viggle三图对比全都有_2105538670647406594
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image2.1文生图三件套｜原生FUN Viggle三图对比全都有_2105538670647406594.json
hash: d17e7ceba2e899b0
coverage: 0.943662
learned_at: 2026-10-10 20:58:56
nodes: [StringConstantMultiline, INTConstant, INTConstant, INTConstant, UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, EmptyLatentImage, KSampler, LoraLoaderModelOnly, BasicGuider, RandomNoise, KSamplerSelect, CustomSigmas, SamplerCustomAdvanced, VAEDecode, VAEDecode, VAEDecode, SaveImage, T8QwenImage21FunAccPDD4Step, SaveImage, AddLabel, SaveImage, AddLabel, SaveImage, AddLabel, ImageConcatMulti, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image2.1文生图三件套｜原生FUN Viggle三图对比全都有_2105538670647406594.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image2.1文生图三件套｜原生FUN Viggle三图对比全都有_2105538670647406594.json`

## 结构

**节点**（71 个）：
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
- `CLIPLoader`
- `CLIPTextEncode`
- `VAELoader`
- `EmptyLatentImage`
- `KSampler`
- `VAEDecode`
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode`
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

覆盖率 **94%**（67/71）

**有卡**：`StringConstantMultiline`、`INTConstant`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`KSampler`、`LoraLoaderModelOnly`、`BasicGuider`、`RandomNoise`、`KSamplerSelect`、`CustomSigmas`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`T8QwenImage21FunAccPDD4Step`、`AddLabel`、`ImageConcatMulti`、`孤海注释`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`JjkText`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
