---
key: 图片生成/文生图/树叶拼图风格 Leaf puzzle style For QwenImage_1974367997215289345.json
name: 树叶拼图风格 Leaf puzzle style For QwenImage_1974367997215289345
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/树叶拼图风格 Leaf puzzle style For QwenImage_1974367997215289345.json
hash: 125ed77b72d6915d
coverage: 0.842105
learned_at: 2026-10-10 20:59:51
nodes: [KSampler, CLIPTextEncode, ModelSamplingAuraFlow, PreviewImage, CLIPLoader, VAELoader, VAEDecode, SaveImage, ConcatText_Zho, CLIPTextEncode, UNETLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, Note, EmptyHunyuanLatentVideo, JjkText, Int, Int]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 392352416150076, "steps": 10}
---

# 图片生成/文生图/树叶拼图风格 Leaf puzzle style For QwenImage_1974367997215289345.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/树叶拼图风格 Leaf puzzle style For QwenImage_1974367997215289345.json`

## 结构

**节点**（19 个）：
- `KSampler`
- `CLIPTextEncode`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `CLIPLoader`
- `VAELoader`
- `VAEDecode`
- `SaveImage`
- `ConcatText_Zho`
- `CLIPTextEncode`
- `UNETLoader`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `Note`
- `EmptyHunyuanLatentVideo`
- `JjkText`
- `Int`
- `Int`

## 关键参数

- `cfg` = `1`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `392352416150076`
- `steps` = `10`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`KSampler`、`CLIPTextEncode`、`ModelSamplingAuraFlow`、`PreviewImage`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`SaveImage`、`ConcatText_Zho`、`UNETLoader`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`Note`、`EmptyHunyuanLatentVideo`
