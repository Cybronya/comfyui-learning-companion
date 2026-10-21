---
key: 图片生成/文生图/PromptLine+Anima Preview2艺术家批量风格测试_2033542990416846849.json
name: PromptLine+Anima Preview2艺术家批量风格测试_2033542990416846849
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/PromptLine+Anima Preview2艺术家批量风格测试_2033542990416846849.json
hash: 681a5984614f3c0a
coverage: 0.9375
learned_at: 2026-10-21 02:53:59
nodes: [SaveImage, CLIPTextEncode, EmptyLatentImage, CLIPLoader, CLIPTextEncode, KSampler, KSampler, LatentUpscaleBy, VAEDecode, VAEDecode, VAELoader, UNETLoader, easy promptLine, JWStringConcat, String Literal, PreviewImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 2.5, "denoise": 0.6500000000000001, "height": 1024, "sampler_name": "dpmpp_2m_sde_gpu", "scheduler": "sgm_uniform", "seed": 1124984513537044, "steps": 20, "width": 1024}
---

# 图片生成/文生图/PromptLine+Anima Preview2艺术家批量风格测试_2033542990416846849.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/PromptLine+Anima Preview2艺术家批量风格测试_2033542990416846849.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `SaveImage`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `LatentUpscaleBy`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `easy promptLine`
- `JWStringConcat`
- `String Literal`
- `PreviewImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1124984513537044`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `dpmpp_2m_sde_gpu`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.6500000000000001`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`SaveImage`、`CLIPTextEncode`、`EmptyLatentImage`、`CLIPLoader`、`KSampler`、`LatentUpscaleBy`、`VAEDecode`、`VAELoader`、`UNETLoader`、`easy promptLine`、`JWStringConcat`、`String Literal`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、LatentUpscaleBy
