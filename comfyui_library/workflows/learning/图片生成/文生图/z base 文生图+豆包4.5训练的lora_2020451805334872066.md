---
key: 图片生成/文生图/z base 文生图+豆包4.5训练的lora_2020451805334872066.json
name: z base 文生图+豆包4.5训练的lora_2020451805334872066
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/z base 文生图+豆包4.5训练的lora_2020451805334872066.json
hash: 1b5e5de61b1491a9
coverage: 0.866667
learned_at: 2026-10-19 22:30:14
nodes: [MarkdownNote, VAEDecode, ModelSamplingAuraFlow, CLIPTextEncode, MarkdownNote, Text Multiline, CR Prompt List, LoraLoaderModelOnly, EmptySD3LatentImage, UNETLoader, KSampler, VAELoader, CLIPLoader, SaveImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 87870690685363, "steps": 30}
---

# 图片生成/文生图/z base 文生图+豆包4.5训练的lora_2020451805334872066.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/z base 文生图+豆包4.5训练的lora_2020451805334872066.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `MarkdownNote`
- `VAEDecode` ★核心
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `Text Multiline`
- `CR Prompt List`
- `LoraLoaderModelOnly` ★核心
- `EmptySD3LatentImage`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAELoader`
- `CLIPLoader`
- `SaveImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `87870690685363`
- `steps` = `30`
- `cfg` = `4`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`VAEDecode`、`ModelSamplingAuraFlow`、`CLIPTextEncode`、`Text Multiline`、`CR Prompt List`、`LoraLoaderModelOnly`、`EmptySD3LatentImage`、`UNETLoader`、`KSampler`、`VAELoader`、`CLIPLoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、CR Prompt List
