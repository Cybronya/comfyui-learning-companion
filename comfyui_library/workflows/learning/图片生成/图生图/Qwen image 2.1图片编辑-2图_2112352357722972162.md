---
key: 图片生成/图生图/Qwen image 2.1图片编辑-2图_2112352357722972162.json
name: Qwen image 2.1图片编辑-2图_2112352357722972162
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1图片编辑-2图_2112352357722972162.json
hash: aff0477ca020b64f
coverage: 0.703704
learned_at: 2026-10-23 11:14:02
nodes: [VAEDecode, ComfySwitchNode, QwenImage21Cache, CLIPLoader, CLIPLoader, KSampler, SaveImage, EmptyLatentImage, TextEncodeQwenImage21, SaveImageAdvanced, VAELoader, Int, Int, UNETLoader, SDVN Load Image Url, PrimitiveStringMultiline, SDVN Load Image Url, PrimitiveStringMultiline, SDVN Load Image Url, PrimitiveStringMultiline, SDVN Load Image Url, PrimitiveStringMultiline, SDVN Load Image Url, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, SDVN Load Image Url]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 50, "width": 16}
---

# 图片生成/图生图/Qwen image 2.1图片编辑-2图_2112352357722972162.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1图片编辑-2图_2112352357722972162.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（27 个）：
- `VAEDecode` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `CLIPLoader`
- `CLIPLoader`
- `KSampler` ★核心
- `SaveImage`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `SaveImageAdvanced`
- `VAELoader`
- `Int`
- `Int`
- `UNETLoader` ★核心
- `SDVN Load Image Url`
- `PrimitiveStringMultiline`
- `SDVN Load Image Url`
- `PrimitiveStringMultiline`
- `SDVN Load Image Url`
- `PrimitiveStringMultiline`
- `SDVN Load Image Url`
- `PrimitiveStringMultiline`
- `SDVN Load Image Url`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `SDVN Load Image Url`

## 关键参数

- `seed` = `999`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `16`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **70%**（19/27）

**有卡**：`VAEDecode`、`QwenImage21Cache`、`CLIPLoader`、`KSampler`、`SaveImage`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`SaveImageAdvanced`、`VAELoader`、`Int`、`UNETLoader`、`SDVN Load Image Url`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、QwenImage21Cache、UNETLoader
