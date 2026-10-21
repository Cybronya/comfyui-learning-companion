---
key: 图片生成/文生图/wan2.2高低频超真实+超级快文生图_2028351546110517249.json
name: wan2.2高低频超真实+超级快文生图_2028351546110517249
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2高低频超真实+超级快文生图_2028351546110517249.json
hash: e33d376ca94f3a8f
coverage: 0.935484
learned_at: 2026-10-20 23:22:01
nodes: [LoraLoaderModelOnly, CLIPLoader, UNETLoader, LoraLoaderModelOnly, UNETLoader, PathchSageAttentionKJ, ModelSamplingSD3, CLIPTextEncode, VAELoader, ShowText|pysssss, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ShowText|pysssss, ModelSamplingSD3, Bjornulf_TextToStringAndSeed, VAEDecode, KSampler, Text Multiline, CR Text Concatenate, RH_LLMAPI_NODE, SaveImage, Wan_video_prompt_generator, Text Multiline, EmptyLatentImage, JWInteger, JWInteger]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 965369974524576, "steps": 10, "width": 512}
---

# 图片生成/文生图/wan2.2高低频超真实+超级快文生图_2028351546110517249.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2高低频超真实+超级快文生图_2028351546110517249.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（31 个）：
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ShowText|pysssss`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ShowText|pysssss`
- `ModelSamplingSD3`
- `Bjornulf_TextToStringAndSeed`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `Text Multiline`
- `CR Text Concatenate`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `Wan_video_prompt_generator`
- `Text Multiline`
- `EmptyLatentImage` ★核心
- `JWInteger`
- `JWInteger`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `965369974524576`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（29/31）

**有卡**：`LoraLoaderModelOnly`、`CLIPLoader`、`UNETLoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPTextEncode`、`VAELoader`、`Bjornulf_TextToStringAndSeed`、`VAEDecode`、`KSampler`、`Text Multiline`、`CR Text Concatenate`、`RH_LLMAPI_NODE`、`SaveImage`、`Wan_video_prompt_generator`、`EmptyLatentImage`、`JWInteger`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader
