---
key: 图片生成/文生图/Z-image图像反推提示词生图动作迁移Controlnet+lora(支持cn和lora)_1996932292809539585.json
name: Z-image图像反推提示词生图动作迁移Controlnet+lora(支持cn和lora)_1996932292809539585
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image图像反推提示词生图动作迁移Controlnet+lora(支持cn和lora)_1996932292809539585.json
hash: 599d703665fcaebf
coverage: 0.888889
learned_at: 2026-10-19 21:47:10
nodes: [Qwen3_VQA, ShellAgentPluginOutputText, GetImageSize, UNETLoader, AIO_Preprocessor, ImageScaleToTotalPixels, CLIPLoader, ModelPatchLoader, CLIPTextEncode, QwenImageDiffsynthControlnet, PreviewAny, PreviewImage, EmptyLatentImage, UpscaleModelLoader, VAEDecode, ConditioningZeroOut, KSampler, KSampler, ImageUpscaleWithModel, SaveImage, easy showAnything, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, CR Prompt Text, TT_img_enc]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.75, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 542444792868613, "steps": 10, "width": 1024}
---

# 图片生成/文生图/Z-image图像反推提示词生图动作迁移Controlnet+lora(支持cn和lora)_1996932292809539585.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image图像反推提示词生图动作迁移Controlnet+lora(支持cn和lora)_1996932292809539585.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `Qwen3_VQA`
- `ShellAgentPluginOutputText`
- `GetImageSize`
- `UNETLoader` ★核心
- `AIO_Preprocessor`
- `ImageScaleToTotalPixels`
- `CLIPLoader`
- `ModelPatchLoader`
- `CLIPTextEncode` ★核心
- `QwenImageDiffsynthControlnet`
- `PreviewAny`
- `PreviewImage`
- `EmptyLatentImage` ★核心
- `UpscaleModelLoader`
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `KSampler` ★核心
- `ImageUpscaleWithModel`
- `SaveImage`
- `easy showAnything`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `CR Prompt Text`
- `TT_img_enc`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `542444792868613`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.75`

## 知识

覆盖率 **89%**（24/27）

**有卡**：`Qwen3_VQA`、`ShellAgentPluginOutputText`、`GetImageSize`、`UNETLoader`、`AIO_Preprocessor`、`ImageScaleToTotalPixels`、`CLIPLoader`、`ModelPatchLoader`、`CLIPTextEncode`、`QwenImageDiffsynthControlnet`、`EmptyLatentImage`、`UpscaleModelLoader`、`VAEDecode`、`ConditioningZeroOut`、`KSampler`、`ImageUpscaleWithModel`、`SaveImage`、`VAELoader`、`LoraLoaderModelOnly`、`LoadImage`、`CR Prompt Text`、`TT_img_enc`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
