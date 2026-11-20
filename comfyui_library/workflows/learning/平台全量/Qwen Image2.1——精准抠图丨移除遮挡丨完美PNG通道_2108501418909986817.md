---
key: 平台全量/Qwen Image2.1——精准抠图丨移除遮挡丨完美PNG通道_2108501418909986817.json
name: Qwen Image2.1——精准抠图丨移除遮挡丨完美PNG通道_2108501418909986817
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen Image2.1——精准抠图丨移除遮挡丨完美PNG通道_2108501418909986817.json
hash: 14784e46e6e33fee
coverage: 0.75
learned_at: 2026-11-14 00:50:19
nodes: [UNETLoader, JjkText, JjkText, easy ifElse, easy boolean, StringToAnyNode, StringToAnyNode, TextEncodeQwenImage21, ShowText|pysssss, KSampler, VAEDecode, SaveImage, Image Comparer (rgthree), LoadImage, LoraLoaderModelOnly, CLIPLoader, XinbaoImageStandardizer, VAELoader, CR Text Replace, QwenImage21Cache]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 918424043973166, "steps": 40}
---

# 平台全量/Qwen Image2.1——精准抠图丨移除遮挡丨完美PNG通道_2108501418909986817.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen Image2.1——精准抠图丨移除遮挡丨完美PNG通道_2108501418909986817.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `UNETLoader` ★核心
- `JjkText`
- `JjkText`
- `easy ifElse`
- `easy boolean`
- `StringToAnyNode`
- `StringToAnyNode`
- `TextEncodeQwenImage21`
- `ShowText|pysssss`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `XinbaoImageStandardizer`
- `VAELoader`
- `CR Text Replace`
- `QwenImage21Cache`

## 关键参数

- `seed` = `918424043973166`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **75%**（15/20）

**有卡**：`UNETLoader`、`easy boolean`、`StringToAnyNode`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`SaveImage`、`LoadImage`、`LoraLoaderModelOnly`、`CLIPLoader`、`XinbaoImageStandardizer`、`VAELoader`、`CR Text Replace`、`QwenImage21Cache`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache
