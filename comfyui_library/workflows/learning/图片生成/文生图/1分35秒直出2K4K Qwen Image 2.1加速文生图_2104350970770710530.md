---
key: 图片生成/文生图/1分35秒直出2K4K Qwen Image 2.1加速文生图_2104350970770710530.json
name: 1分35秒直出2K4K Qwen Image 2.1加速文生图_2104350970770710530
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/1分35秒直出2K4K Qwen Image 2.1加速文生图_2104350970770710530.json
hash: e7929de85b0857b0
coverage: 0.844828
learned_at: 2026-10-15 22:26:09
nodes: [VAELoader, ComfySwitchNode, UNETLoader, CLIPLoader, EmptyLatentImage, PlaySound|pysssss, VAEDecode, easy cleanGpuUsed, PreviewImage, Image Remove Alpha JK, VOSR2ModelLoader, SaveImage, CLIPLoader, TextEncodeQwenImage21, UNETLoader, QwenImage21SageAttentionT8, QwenImage21BlockCacheT8, QwenImage21Cache, Lora Loader Stack (rgthree), QwenImage21SpectrumT8, ResolutionSelector, PrimitiveStringMultiline, SaveImage, KSampler, easy imageChooser, ImageApplyLUT+, PreviewImage, VOSR2Upscale, PreviewImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/1分35秒直出2K4K Qwen Image 2.1加速文生图_2104350970770710530.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1分35秒直出2K4K Qwen Image 2.1加速文生图_2104350970770710530.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `VAELoader`
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `PlaySound|pysssss`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `PreviewImage`
- `Image Remove Alpha JK`
- `VOSR2ModelLoader`
- `SaveImage`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `QwenImage21SageAttentionT8`
- `QwenImage21BlockCacheT8`
- `QwenImage21Cache`
- `Lora Loader Stack (rgthree)`
- `QwenImage21SpectrumT8`
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `SaveImage`
- `KSampler` ★核心
- `easy imageChooser`
- `ImageApplyLUT+`
- `PreviewImage`
- `VOSR2Upscale`
- `PreviewImage`
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

覆盖率 **84%**（49/58）

**有卡**：`VAELoader`、`UNETLoader`、`CLIPLoader`、`EmptyLatentImage`、`PlaySound|pysssss`、`VAEDecode`、`easy cleanGpuUsed`、`Image Remove Alpha JK`、`VOSR2ModelLoader`、`SaveImage`、`TextEncodeQwenImage21`、`QwenImage21SageAttentionT8`、`QwenImage21BlockCacheT8`、`QwenImage21Cache`、`Lora Loader Stack (rgthree)`、`QwenImage21SpectrumT8`、`ResolutionSelector`、`KSampler`、`easy imageChooser`、`ImageApplyLUT+`、`VOSR2Upscale`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
