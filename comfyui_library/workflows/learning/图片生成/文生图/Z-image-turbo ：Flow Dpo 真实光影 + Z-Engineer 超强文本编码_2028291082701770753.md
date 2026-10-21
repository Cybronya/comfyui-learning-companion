---
key: 图片生成/文生图/Z-image-turbo ：Flow Dpo 真实光影 + Z-Engineer 超强文本编码_2028291082701770753.json
name: Z-image-turbo ：Flow Dpo 真实光影 + Z-Engineer 超强文本编码_2028291082701770753
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image-turbo ：Flow Dpo 真实光影 + Z-Engineer 超强文本编码_2028291082701770753.json
hash: f1d1181582d21558
coverage: 0.851852
learned_at: 2026-10-20 23:21:53
nodes: [UNETLoader, VAELoader, VAEDecode, CLIPLoaderGGUF, easy seed, EmptyLatentImage, LoraLoaderModelOnly, CLIPTextEncode, SaveImage, ConditioningZeroOut, KSampler, Note, MuyeSizeSelector, Int, Int, llama_cpp_parameters, ShowText|pysssss, llama_cpp_model_loader, llama_cpp_instruct_adv, ShowText|pysssss, CR Prompt Text, ZML_AnyTypeSwitch, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_instruct_adv, LoadImage, ShowText|pysssss]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 605878670720361, "steps": 10, "width": 1920}
---

# 图片生成/文生图/Z-image-turbo ：Flow Dpo 真实光影 + Z-Engineer 超强文本编码_2028291082701770753.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image-turbo ：Flow Dpo 真实光影 + Z-Engineer 超强文本编码_2028291082701770753.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（27 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `CLIPLoaderGGUF`
- `easy seed`
- `EmptyLatentImage` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `Note`
- `MuyeSizeSelector`
- `Int`
- `Int`
- `llama_cpp_parameters`
- `ShowText|pysssss`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `ShowText|pysssss`
- `CR Prompt Text`
- `ZML_AnyTypeSwitch`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `LoadImage`
- `ShowText|pysssss`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`
- `seed` = `605878670720361`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（23/27）

**有卡**：`UNETLoader`、`VAELoader`、`VAEDecode`、`CLIPLoaderGGUF`、`easy seed`、`EmptyLatentImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`SaveImage`、`ConditioningZeroOut`、`KSampler`、`MuyeSizeSelector`、`Int`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`CR Prompt Text`、`ZML_AnyTypeSwitch`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage
