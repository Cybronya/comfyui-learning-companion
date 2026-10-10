---
key: Wan2.2真实系INS风组合调度非常规文生图工作流（海外版）_1955547695828144130.json
name: Wan2.2真实系INS风组合调度非常规文生图工作流（海外版）_1955547695828144130
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2真实系INS风组合调度非常规文生图工作流（海外版）_1955547695828144130.json
hash: e95c96106b9babf0
coverage: 1
learned_at: 2026-10-10 20:59:14
nodes: [PathchSageAttentionKJ, ModelSamplingSD3, CLIPTextEncode, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, UNETLoader, UNETLoader, VAELoader, CLIPLoader, JWInteger, JWInteger, LoraLoaderModelOnly, KSampler, KSampler, EmptyLatentImage, SaveImage, SaveImage, VAEDecode, SaveImage, KSampler, VAEDecode, SaveImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecode, SeedVR2, SeedVR2BlockSwap, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Bjornulf_TextToStringAndSeed]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 965369974524576, "steps": 10, "width": 512}
---

# Wan2.2真实系INS风组合调度非常规文生图工作流（海外版）_1955547695828144130.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2真实系INS风组合调度非常规文生图工作流（海外版）_1955547695828144130.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（34 个）：
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `JWInteger`
- `JWInteger`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `SaveImage`
- `SaveImage`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `SeedVR2`
- `SeedVR2BlockSwap`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Bjornulf_TextToStringAndSeed`

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

覆盖率 **100%**（34/34）

**有卡**：`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`JWInteger`、`KSampler`、`EmptyLatentImage`、`SaveImage`、`VAEDecode`、`SeedVR2`、`SeedVR2BlockSwap`、`Bjornulf_TextToStringAndSeed`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader
