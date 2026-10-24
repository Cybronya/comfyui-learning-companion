---
key: 图片生成/图生图/Flex.2-preview-图生图_1917082177446809601.json
name: Flex.2-preview-图生图_1917082177446809601
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flex.2-preview-图生图_1917082177446809601.json
hash: 5cf11b3a494d81f6
coverage: 1
learned_at: 2026-10-23 10:56:02
nodes: [DualCLIPLoader, VAELoader, UNETLoader, LoraLoaderModelOnly, CLIPTextEncode, VAEDecode, ImageResizeKJ, VAEEncode, Flex2Conditioner, CLIPTextEncode, KSampler, LoadImage, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.7500000000000001, "sampler_name": "deis", "scheduler": "beta", "seed": 941764069771721, "steps": 25}
---

# 图片生成/图生图/Flex.2-preview-图生图_1917082177446809601.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flex.2-preview-图生图_1917082177446809601.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `DualCLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `ImageResizeKJ`
- `VAEEncode` ★核心
- `Flex2Conditioner`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `LoadImage`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `941764069771721`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `deis`
- `scheduler` = `beta`
- `denoise` = `0.7500000000000001`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`DualCLIPLoader`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`VAEDecode`、`ImageResizeKJ`、`VAEEncode`、`Flex2Conditioner`、`KSampler`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、VAEEncode
