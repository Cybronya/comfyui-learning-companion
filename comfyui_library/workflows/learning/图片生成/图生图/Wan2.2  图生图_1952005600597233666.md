---
key: 图片生成/图生图/Wan2.2  图生图_1952005600597233666.json
name: Wan2.2  图生图_1952005600597233666
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2  图生图_1952005600597233666.json
hash: 9dbfa6a20f042814
coverage: 1
learned_at: 2026-10-23 11:27:55
nodes: [UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, KSampler, Seed_, CLIPTextEncode, CLIPLoader, CLIPTextEncode, VAEDecode, ModelSamplingSD3, SaveImage, VAEEncode, VAELoader, LoadImage, ConstrainImage|pysssss, RH_Captioner, KSampler]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.5000000000000001, "sampler_name": "heun", "scheduler": "beta", "seed": 497163970725457, "steps": 10}
---

# 图片生成/图生图/Wan2.2  图生图_1952005600597233666.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2  图生图_1952005600597233666.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `KSampler` ★核心
- `Seed_`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `SaveImage`
- `VAEEncode` ★核心
- `VAELoader`
- `LoadImage`
- `ConstrainImage|pysssss`
- `RH_Captioner`
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `497163970725457`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.5000000000000001`

## 知识

覆盖率 **100%**（23/23）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`KSampler`、`Seed_`、`CLIPTextEncode`、`CLIPLoader`、`VAEDecode`、`SaveImage`、`VAEEncode`、`VAELoader`、`LoadImage`、`ConstrainImage|pysssss`、`RH_Captioner`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
