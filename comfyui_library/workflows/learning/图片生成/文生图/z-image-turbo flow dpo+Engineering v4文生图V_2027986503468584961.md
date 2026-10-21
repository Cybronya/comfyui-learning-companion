---
key: 图片生成/文生图/z-image-turbo flow dpo+Engineering v4文生图V_2027986503468584961.json
name: z-image-turbo flow dpo+Engineering v4文生图V_2027986503468584961
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/z-image-turbo flow dpo+Engineering v4文生图V_2027986503468584961.json
hash: 022fc63a674bb234
coverage: 1
learned_at: 2026-10-19 22:46:15
nodes: [ConditioningZeroOut, VAELoader, easy seed, UNETLoader, CLIPTextEncode, VAEDecode, CR Prompt Text, CLIPLoaderGGUF, LoraLoaderModelOnly, EmptyLatentImage, KSampler, SaveImage, LoadImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 449316776546657, "steps": 10, "width": 1920}
---

# 图片生成/文生图/z-image-turbo flow dpo+Engineering v4文生图V_2027986503468584961.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/z-image-turbo flow dpo+Engineering v4文生图V_2027986503468584961.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `ConditioningZeroOut`
- `VAELoader`
- `easy seed`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CR Prompt Text`
- `CLIPLoaderGGUF`
- `LoraLoaderModelOnly` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `SaveImage`
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`
- `seed` = `449316776546657`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`ConditioningZeroOut`、`VAELoader`、`easy seed`、`UNETLoader`、`CLIPTextEncode`、`VAEDecode`、`CR Prompt Text`、`CLIPLoaderGGUF`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`KSampler`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage
