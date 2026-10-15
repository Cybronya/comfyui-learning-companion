---
key: 图片生成/文生图/Wan2.2 超真实文生图+放大_1950719208512491521.json
name: Wan2.2 超真实文生图+放大_1950719208512491521
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2 超真实文生图+放大_1950719208512491521.json
hash: d2d90f3825a6d33b
coverage: 1
learned_at: 2026-10-10 20:59:14
nodes: [KSampler, ModelSamplingSD3, CLIPTextEncode, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, VAELoader, CLIPLoader, CLIPTextEncode, EmptyLatentImage, VAEDecode, PMRF, Bjornulf_TextToStringAndSeed, SaveImage, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 965369974524576, "steps": 10, "width": 720}
---

# 图片生成/文生图/Wan2.2 超真实文生图+放大_1950719208512491521.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2 超真实文生图+放大_1950719208512491521.json`

## 结构

**节点**（16 个）：
- `KSampler`
- `ModelSamplingSD3`
- `CLIPTextEncode`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `VAEDecode`
- `PMRF`
- `Bjornulf_TextToStringAndSeed`
- `SaveImage`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1280`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `965369974524576`
- `steps` = `10`
- `width` = `720`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`KSampler`、`ModelSamplingSD3`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`EmptyLatentImage`、`VAEDecode`、`PMRF`、`Bjornulf_TextToStringAndSeed`、`SaveImage`
