---
key: 图片生成/图生图/Z-image Controlnet+lora起效工作流_1996843101358628866.json
name: Z-image Controlnet+lora起效工作流_1996843101358628866
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-image Controlnet+lora起效工作流_1996843101358628866.json
hash: a3075765ad21e4df
coverage: 0.954545
learned_at: 2026-10-23 11:30:19
nodes: [ConditioningZeroOut, VAEDecode, QwenImageDiffsynthControlnet, KSampler, KSampler, UNETLoader, CLIPLoader, VAELoader, UpscaleModelLoader, AIO_Preprocessor, EmptyLatentImage, GetImageSize, LoadImage, LoraLoaderModelOnly, CLIPTextEncode, ImageScaleToTotalPixels, ModelPatchLoader, PreviewImage, ImageUpscaleWithModel, SaveImage, SaveImage, ImageConcanate]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.75, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 275286575498364, "steps": 10, "width": 1024}
---

# 图片生成/图生图/Z-image Controlnet+lora起效工作流_1996843101358628866.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-image Controlnet+lora起效工作流_1996843101358628866.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `QwenImageDiffsynthControlnet`
- `KSampler` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `UpscaleModelLoader`
- `AIO_Preprocessor`
- `EmptyLatentImage` ★核心
- `GetImageSize`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `ImageScaleToTotalPixels`
- `ModelPatchLoader`
- `PreviewImage`
- `ImageUpscaleWithModel`
- `SaveImage`
- `SaveImage`
- `ImageConcanate`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `275286575498364`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.75`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（21/22）

**有卡**：`ConditioningZeroOut`、`VAEDecode`、`QwenImageDiffsynthControlnet`、`KSampler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`UpscaleModelLoader`、`AIO_Preprocessor`、`EmptyLatentImage`、`GetImageSize`、`LoadImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`ImageScaleToTotalPixels`、`ModelPatchLoader`、`ImageUpscaleWithModel`、`SaveImage`、`ImageConcanate`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
