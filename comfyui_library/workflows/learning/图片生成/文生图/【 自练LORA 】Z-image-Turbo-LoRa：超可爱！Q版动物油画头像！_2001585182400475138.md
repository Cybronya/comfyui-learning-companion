---
key: 图片生成/文生图/【 自练LORA 】Z-image-Turbo-LoRa：超可爱！Q版动物油画头像！_2001585182400475138.json
name: 【 自练LORA 】Z-image-Turbo-LoRa：超可爱！Q版动物油画头像！_2001585182400475138
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【 自练LORA 】Z-image-Turbo-LoRa：超可爱！Q版动物油画头像！_2001585182400475138.json
hash: bd5194b630cec78a
coverage: 0.875
learned_at: 2026-10-19 21:47:25
nodes: [VAEDecode, ConditioningZeroOut, CLIPLoader, CLIPTextEncode, Note, SaveImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, MuyeTextEditOutput, LoadImage, PreviewImage, VAELoader, LoraLoaderModelOnly, KSampler, MuyeTextEditOutput, UNETLoader, EmptyLatentImage, Note, MultiTextConcatenate]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "dpmpp_2m_sde", "scheduler": "sgm_uniform", "seed": 323408323033328, "steps": 10, "width": 1280}
---

# 图片生成/文生图/【 自练LORA 】Z-image-Turbo-LoRa：超可爱！Q版动物油画头像！_2001585182400475138.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【 自练LORA 】Z-image-Turbo-LoRa：超可爱！Q版动物油画头像！_2001585182400475138.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（24 个）：
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `Note`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `MuyeTextEditOutput`
- `LoadImage`
- `PreviewImage`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `MuyeTextEditOutput`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `Note`
- `MultiTextConcatenate`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `323408323033328`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2m_sde`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `width` = `1280`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`VAEDecode`、`ConditioningZeroOut`、`CLIPLoader`、`CLIPTextEncode`、`SaveImage`、`LoadImage`、`MuyeTextEditOutput`、`VAELoader`、`LoraLoaderModelOnly`、`KSampler`、`UNETLoader`、`EmptyLatentImage`、`MultiTextConcatenate`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、SaveImage
