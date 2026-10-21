---
key: 图片生成/文生图/ZIMAGE-Turbo & （百度）Ernie-image-Turbo 生成对比  _   洗图_2026868093791768578.json
name: ZIMAGE-Turbo & （百度）Ernie-image-Turbo 生成对比  _   洗图_2026868093791768578
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/ZIMAGE-Turbo & （百度）Ernie-image-Turbo 生成对比  _   洗图_2026868093791768578.json
hash: 4ddc2b4ca65de82d
coverage: 0.936508
learned_at: 2026-10-19 22:30:09
nodes: [VAELoader, Note, VAELoader, CLIPTextEncode, KSampler, KSampler, ModelSamplingAuraFlow, ModelSamplingAuraFlow, EmptyLatentImage, ConditioningZeroOut, ModelSamplingAuraFlow, KSamplerAdvanced, CLIPLoader, VAEDecode, Int, KSamplerAdvanced, Int, CLIPTextEncode, easy cleanGpuUsed, llama_cpp_parameters, llama_cpp_instruct_adv, CR Latent Batch Size, VAELoader, CLIPTextEncode, KSamplerAdvanced, ConditioningZeroOut, CLIPLoader, VAELoader, UNETLoader, VAEDecode, easy cleanGpuUsed, easy seed, LoraLoaderModelOnly, ModelSamplingAuraFlow, CLIPTextEncode, CLIPTextEncode, SaveImage, Anything Everywhere3, CLIPLoaderGGUF, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, SaveImage, UNETLoader, UNETLoader, QWEN_TextDisplay, SaveImage, easy cleanGpuUsed, SaveImage, EmptySD3LatentImage, LoadImage, VAEDecode, ImageConcatMulti, ImageConcatMulti, PreviewImage, ImageConcatMulti, llama_cpp_model_loader, llama_cpp_model_loader, VAEDecode, CR Prompt Text, CR Prompt Text, MuyeSizeSelector, PreviewAny]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 8, "denoise": "simple", "height": 1536, "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize", "width": 1024}
---

# 图片生成/文生图/ZIMAGE-Turbo & （百度）Ernie-image-Turbo 生成对比  _   洗图_2026868093791768578.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/ZIMAGE-Turbo & （百度）Ernie-image-Turbo 生成对比  _   洗图_2026868093791768578.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（63 个）：
- `VAELoader`
- `Note`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `ModelSamplingAuraFlow`
- `EmptyLatentImage` ★核心
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `Int`
- `KSamplerAdvanced` ★核心
- `Int`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `CR Latent Batch Size`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `ConditioningZeroOut`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `easy seed`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `Anything Everywhere3`
- `CLIPLoaderGGUF`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `QWEN_TextDisplay`
- `SaveImage`
- `easy cleanGpuUsed`
- `SaveImage`
- `EmptySD3LatentImage`
- `LoadImage`
- `VAEDecode` ★核心
- `ImageConcatMulti`
- `ImageConcatMulti`
- `PreviewImage`
- `ImageConcatMulti`
- `llama_cpp_model_loader`
- `llama_cpp_model_loader`
- `VAEDecode` ★核心
- `CR Prompt Text`
- `CR Prompt Text`
- `MuyeSizeSelector`
- `PreviewAny`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（59/63）

**有卡**：`VAELoader`、`CLIPTextEncode`、`KSampler`、`ModelSamplingAuraFlow`、`EmptyLatentImage`、`ConditioningZeroOut`、`KSamplerAdvanced`、`CLIPLoader`、`VAEDecode`、`Int`、`easy cleanGpuUsed`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`CR Latent Batch Size`、`UNETLoader`、`easy seed`、`LoraLoaderModelOnly`、`SaveImage`、`CLIPLoaderGGUF`、`QWEN_TextDisplay`、`EmptySD3LatentImage`、`LoadImage`、`ImageConcatMulti`、`llama_cpp_model_loader`、`CR Prompt Text`、`MuyeSizeSelector`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
