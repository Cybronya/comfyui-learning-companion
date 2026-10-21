---
key: 图片生成/文生图/Anima V1.1 文生图_2078367758005399554.json
name: Anima V1.1 文生图_2078367758005399554
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima V1.1 文生图_2078367758005399554.json
hash: 038486af8e5d0646
coverage: 0.956522
learned_at: 2026-10-20 00:18:45
nodes: [UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, CLIPTextEncode, llama_cpp_parameters, CR Prompt Text, llama_cpp_model_loader, llama_cpp_parameters, CR Prompt Text, ConcatTextOfUtils, PreviewAny, easy cleanGpuUsed, CLIPTextEncode, llama_cpp_instruct_adv, llama_cpp_model_loader, Random Line, llama_cpp_instruct_adv, KSampler, VAEDecode, easy cleanGpuUsed, SaveImage, CR Prompt Text]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 1920, "sampler_name": "er_sde", "scheduler": "beta", "seed": 823871822363841, "steps": 40, "width": 1080}
---

# 图片生成/文生图/Anima V1.1 文生图_2078367758005399554.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima V1.1 文生图_2078367758005399554.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（23 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `llama_cpp_parameters`
- `CR Prompt Text`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `CR Prompt Text`
- `ConcatTextOfUtils`
- `PreviewAny`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `Random Line`
- `llama_cpp_instruct_adv`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `SaveImage`
- `CR Prompt Text`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `823871822363841`
- `steps` = `40`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **96%**（22/23）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`CLIPTextEncode`、`llama_cpp_parameters`、`CR Prompt Text`、`llama_cpp_model_loader`、`ConcatTextOfUtils`、`easy cleanGpuUsed`、`llama_cpp_instruct_adv`、`Random Line`、`KSampler`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、CR Prompt Text
