---
key: 图片生成/文生图/Anima V1.0-超强动漫生成（提示词扩写）_2057810746918133762.json
name: Anima V1.0-超强动漫生成（提示词扩写）_2057810746918133762
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima V1.0-超强动漫生成（提示词扩写）_2057810746918133762.json
hash: 8637ba606a3c251a
coverage: 0.923077
learned_at: 2026-10-19 22:45:21
nodes: [CLIPLoader, UNETLoader, CLIPTextEncode, EmptyLatentImage, CLIPTextEncode, VAELoader, KSampler, llama_cpp_model_loader, ShowText|pysssss, llama_cpp_instruct_adv, CR Prompt Text, SaveImage, VAEDecode]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 1280, "sampler_name": "er_sde", "scheduler": "beta", "seed": 1008573121003048, "steps": 40, "width": 720}
---

# 图片生成/文生图/Anima V1.0-超强动漫生成（提示词扩写）_2057810746918133762.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima V1.0-超强动漫生成（提示词扩写）_2057810746918133762.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `KSampler` ★核心
- `llama_cpp_model_loader`
- `ShowText|pysssss`
- `llama_cpp_instruct_adv`
- `CR Prompt Text`
- `SaveImage`
- `VAEDecode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `720`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `1008573121003048`
- `steps` = `40`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`CLIPLoader`、`UNETLoader`、`CLIPTextEncode`、`EmptyLatentImage`、`VAELoader`、`KSampler`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`CR Prompt Text`、`SaveImage`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、CR Prompt Text
