---
key: 图片生成/文生图/qwen image 2.1文生图游戏角色设计 游戏人物批量生成_2105403211334115329.json
name: qwen image 2.1文生图游戏角色设计 游戏人物批量生成_2105403211334115329
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen image 2.1文生图游戏角色设计 游戏人物批量生成_2105403211334115329.json
hash: 82828e5f9bbb1d38
coverage: 0.876404
learned_at: 2026-10-10 20:59:23
nodes: [QwenImage21Cache, CLIPLoader, SamplerCustomAdvanced, KSamplerSelect, BasicGuider, VAELoader, ReferenceLatent, CLIPLoader, VAEDecode, VAEEncode, UNETLoader, TextGenerateLTX2Prompt, KSampler, RandomNoise, SaveImage, VAEDecode, PreviewImage, PreviewImage, CLIPTextEncode, VAELoader, BasicScheduler, ResolutionSelector, easy positive, Seed (rgthree), easy showAnything, CLIPLoader, TextEncodeQwenImage21, EmptyLatentImage, ImageScaleToTotalPixelsX, UNETLoader, ColorMatchV2, VOSR2ModelLoader, VOSR2Upscale, PreviewImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [easy positive, Seed (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/qwen image 2.1文生图游戏角色设计 游戏人物批量生成_2105403211334115329.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen image 2.1文生图游戏角色设计 游戏人物批量生成_2105403211334115329.json`

## 结构

**节点**（89 个）：
- `QwenImage21Cache`
- `CLIPLoader`
- `SamplerCustomAdvanced`
- `KSamplerSelect`
- `BasicGuider`
- `VAELoader`
- `ReferenceLatent`
- `CLIPLoader`
- `VAEDecode`
- `VAEEncode`
- `UNETLoader`
- `TextGenerateLTX2Prompt`
- `KSampler`
- `RandomNoise`
- `SaveImage`
- `VAEDecode`
- `PreviewImage`
- `PreviewImage`
- `CLIPTextEncode`
- `VAELoader`
- `BasicScheduler`
- `ResolutionSelector`
- `easy positive`
- `Seed (rgthree)`
- `easy showAnything`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `EmptyLatentImage`
- `ImageScaleToTotalPixelsX`
- `UNETLoader`
- `ColorMatchV2`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `PreviewImage`
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

覆盖率 **88%**（78/89）

**有卡**：`QwenImage21Cache`、`CLIPLoader`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicGuider`、`VAELoader`、`ReferenceLatent`、`VAEDecode`、`VAEEncode`、`UNETLoader`、`TextGenerateLTX2Prompt`、`KSampler`、`RandomNoise`、`SaveImage`、`PreviewImage`、`CLIPTextEncode`、`BasicScheduler`、`ResolutionSelector`、`easy positive`、`Seed (rgthree)`、`easy showAnything`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`ImageScaleToTotalPixelsX`、`ColorMatchV2`、`VOSR2ModelLoader`、`VOSR2Upscale`、`LoraLoaderModelOnly`、`JjkText`、`solarL_SaveImagesToZip`、`孤海注释`

**缺卡**（2）：`easy positive`、`Seed (rgthree)`

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
