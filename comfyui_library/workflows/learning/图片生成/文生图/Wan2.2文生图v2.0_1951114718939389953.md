---
key: 图片生成/文生图/Wan2.2文生图v2.0_1951114718939389953.json
name: Wan2.2文生图v2.0_1951114718939389953
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2文生图v2.0_1951114718939389953.json
hash: 5906d99ff9b0f801
coverage: 0.896552
learned_at: 2026-10-10 20:59:14
nodes: [ModelSamplingSD3, LoraLoaderModelOnly, KSampler, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, JWInteger, PrimitiveInt, SaveImage, VAEDecode, JWInteger, JjkText, PMRF, VAELoader, CLIPLoader, CLIPTextEncode, EmptyLatentImage, LoadImage, PreviewImage, VAEDecode, KSampler, SaveImage, CLIPTextEncode, UNETLoader, Seed_, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "heun", "scheduler": "beta", "seed": 497163970725457, "steps": 10, "width": 512}
---

# 图片生成/文生图/Wan2.2文生图v2.0_1951114718939389953.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2文生图v2.0_1951114718939389953.json`

## 结构

**节点**（29 个）：
- `ModelSamplingSD3`
- `LoraLoaderModelOnly`
- `KSampler`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `JWInteger`
- `PrimitiveInt`
- `SaveImage`
- `VAEDecode`
- `JWInteger`
- `JjkText`
- `PMRF`
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `LoadImage`
- `PreviewImage`
- `VAEDecode`
- `KSampler`
- `SaveImage`
- `CLIPTextEncode`
- `UNETLoader`
- `Seed_`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `512`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `seed` = `497163970725457`
- `steps` = `10`
- `width` = `512`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`ModelSamplingSD3`、`LoraLoaderModelOnly`、`KSampler`、`PathchSageAttentionKJ`、`JWInteger`、`PrimitiveInt`、`SaveImage`、`VAEDecode`、`JjkText`、`PMRF`、`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`EmptyLatentImage`、`LoadImage`、`PreviewImage`、`UNETLoader`、`Seed_`
