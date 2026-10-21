---
key: 图片生成/文生图/Z-image-Turbo+Qwen3.5开源绝唱_2036091904038801410.json
name: Z-image-Turbo+Qwen3.5开源绝唱_2036091904038801410
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image-Turbo+Qwen3.5开源绝唱_2036091904038801410.json
hash: 8c28c05e05dce9c6
coverage: 0.9
learned_at: 2026-10-21 02:56:14
nodes: [llama_cpp_model_loader, llama_cpp_parameters, ModelSamplingAuraFlow, CLIPTextEncode, LoraLoaderModelOnly, VAELoader, UNETLoader, CLIPLoaderGGUF, easy showAnything, CLIPTextEncode, FastFilmGrain, Image Comparer (rgthree), SaveImage, VAEDecode, KSampler, EmptySD3LatentImage, LayerColor: BrightnessContrastV2, llama_cpp_instruct_adv, GetImageSize, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 105808833026464, "steps": 10}
---

# 图片生成/文生图/Z-image-Turbo+Qwen3.5开源绝唱_2036091904038801410.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image-Turbo+Qwen3.5开源绝唱_2036091904038801410.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoaderGGUF`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `FastFilmGrain`
- `Image Comparer (rgthree)`
- `SaveImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `EmptySD3LatentImage`
- `LayerColor: BrightnessContrastV2`
- `llama_cpp_instruct_adv`
- `GetImageSize`
- `LoadImage`

## 关键参数

- `seed` = `105808833026464`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`llama_cpp_model_loader`、`llama_cpp_parameters`、`ModelSamplingAuraFlow`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`VAELoader`、`UNETLoader`、`CLIPLoaderGGUF`、`FastFilmGrain`、`SaveImage`、`VAEDecode`、`KSampler`、`EmptySD3LatentImage`、`LayerColor: BrightnessContrastV2`、`llama_cpp_instruct_adv`、`GetImageSize`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CLIPLoaderGGUF
