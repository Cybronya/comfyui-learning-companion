---
key: 图片生成/文生图/wan2.2高低频超真实+超级快文生图（自动提示词）V2_1950700991370973185.json
name: wan2.2高低频超真实+超级快文生图（自动提示词）V2_1950700991370973185.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2高低频超真实+超级快文生图（自动提示词）V2_1950700991370973185.json
hash: 85f9b9376bcb0065
coverage: 0.83871
learned_at: 2026-10-07 22:58:36
nodes: [LoraLoaderModelOnly, CLIPLoader, UNETLoader, LoraLoaderModelOnly, UNETLoader, PathchSageAttentionKJ, ModelSamplingSD3, CLIPTextEncode, VAELoader, ShowText|pysssss, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, JWInteger, EmptyLatentImage, Wan_video_prompt_generator, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, RH_LLMAPI_NODE, ShowText|pysssss, Text Multiline, ModelSamplingSD3, Bjornulf_TextToStringAndSeed, VAEDecode, KSampler, JWInteger, Text Multiline, CR Text Concatenate, SaveImage]
patterns: [text_to_image]
missing: [CR Text Concatenate, Text Multiline, Text Multiline]
parameters: {"batch_size": 4, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 965369974524576, "steps": 10, "width": 512}
discoveries: [次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/wan2.2高低频超真实+超级快文生图（自动提示词）V2_1950700991370973185.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1950700991370973185.json`

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
- `JWInteger`
- `EmptyLatentImage` ★核心
- `Wan_video_prompt_generator`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `Text Multiline`
- `ModelSamplingSD3`
- `Bjornulf_TextToStringAndSeed`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `JWInteger`
- `Text Multiline`
- `CR Text Concatenate`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `4`
- `seed` = `965369974524576`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **84%**（26/31）

**有卡**：`LoraLoaderModelOnly`、`CLIPLoader`、`UNETLoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPTextEncode`、`VAELoader`、`JWInteger`、`EmptyLatentImage`、`Wan_video_prompt_generator`、`RH_LLMAPI_NODE`、`Bjornulf_TextToStringAndSeed`、`VAEDecode`、`KSampler`、`SaveImage`

**缺卡**（3）：`CR Text Concatenate`、`Text Multiline`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 学习发现

- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
