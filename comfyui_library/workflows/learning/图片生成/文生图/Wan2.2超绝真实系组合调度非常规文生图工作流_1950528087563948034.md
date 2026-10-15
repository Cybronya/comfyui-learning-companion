---
key: 图片生成/文生图/Wan2.2超绝真实系组合调度非常规文生图工作流_1950528087563948034.json
name: Wan2.2超绝真实系组合调度非常规文生图工作流_1950528087563948034
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2超绝真实系组合调度非常规文生图工作流_1950528087563948034.json
hash: 3e009821569a4c96
coverage: 1
learned_at: 2026-10-10 20:59:15
nodes: [PathchSageAttentionKJ, ModelSamplingSD3, CLIPTextEncode, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, UNETLoader, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, Bjornulf_TextToStringAndSeed, VAELoader, CLIPLoader, JWInteger, JWInteger, CLIPTextEncode, LoraLoaderModelOnly, KSampler, KSampler, EmptyLatentImage, VAEDecode, PMRF, SaveImage, SaveImage, VAEDecode, SaveImage, KSampler, VAEDecode, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 965369974524576, "steps": 10, "width": 512}
---

# 图片生成/文生图/Wan2.2超绝真实系组合调度非常规文生图工作流_1950528087563948034.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2超绝真实系组合调度非常规文生图工作流_1950528087563948034.json`

## 结构

**节点**（29 个）：
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPTextEncode`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `Bjornulf_TextToStringAndSeed`
- `VAELoader`
- `CLIPLoader`
- `JWInteger`
- `JWInteger`
- `CLIPTextEncode`
- `LoraLoaderModelOnly`
- `KSampler`
- `KSampler`
- `EmptyLatentImage`
- `VAEDecode`
- `PMRF`
- `SaveImage`
- `SaveImage`
- `VAEDecode`
- `SaveImage`
- `KSampler`
- `VAEDecode`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `512`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `965369974524576`
- `steps` = `10`
- `width` = `512`

## 知识

覆盖率 **100%**（29/29）

**有卡**：`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`UNETLoader`、`Bjornulf_TextToStringAndSeed`、`VAELoader`、`CLIPLoader`、`JWInteger`、`KSampler`、`EmptyLatentImage`、`VAEDecode`、`PMRF`、`SaveImage`
