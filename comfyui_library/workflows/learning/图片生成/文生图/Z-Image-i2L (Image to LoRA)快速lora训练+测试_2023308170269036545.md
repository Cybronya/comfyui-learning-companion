---
key: Z-Image-i2L (Image to LoRA)快速lora训练+测试_2023308170269036545.json
name: Z-Image-i2L (Image to LoRA)快速lora训练+测试_2023308170269036545
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image-i2L (Image to LoRA)快速lora训练+测试_2023308170269036545.json
hash: ea4bc1c1e2feaa86
coverage: 0.913043
learned_at: 2026-10-10 20:59:17
nodes: [RunningHub_ZImageI2L_Saver, easy cleanGpuUsed, RunningHub_ZImageI2L_Loader, KSampler, VAEDecode, PreviewAny, EmptySD3LatentImage, RunningHub_ZImageI2L_LoraGenerator, CLIPLoader, UNETLoader, VAELoader, ModelSamplingAuraFlow, CLIPTextEncode, LoraLoader, ImageBatchMulti, CLIPTextEncode, SaveImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage]
patterns: [lora]
missing: [easy cleanGpuUsed]
parameters: {"cfg": 4, "denoise": 1, "lora_name": null, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 23228479659329, "steps": 50, "strength_clip": 1.0000000000000002, "strength_model": 1.1000000000000003}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# Z-Image-i2L (Image to LoRA)快速lora训练+测试_2023308170269036545.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image-i2L (Image to LoRA)快速lora训练+测试_2023308170269036545.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `RunningHub_ZImageI2L_Saver`
- `easy cleanGpuUsed`
- `RunningHub_ZImageI2L_Loader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PreviewAny`
- `EmptySD3LatentImage`
- `RunningHub_ZImageI2L_LoraGenerator`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `ImageBatchMulti`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`

**识别到的模式**：lora

## 关键参数

- `seed` = `23228479659329`
- `steps` = `50`
- `cfg` = `4`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `None`
- `strength_model` = `1.1000000000000003`
- `strength_clip` = `1.0000000000000002`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`RunningHub_ZImageI2L_Saver`、`RunningHub_ZImageI2L_Loader`、`KSampler`、`VAEDecode`、`EmptySD3LatentImage`、`RunningHub_ZImageI2L_LoraGenerator`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`CLIPTextEncode`、`LoraLoader`、`ImageBatchMulti`、`SaveImage`、`LoadImage`

**缺卡**（1）：`easy cleanGpuUsed`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LoraLoader

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
