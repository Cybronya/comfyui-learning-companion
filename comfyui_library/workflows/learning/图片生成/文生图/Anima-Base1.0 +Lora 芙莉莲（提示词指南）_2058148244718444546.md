---
key: 图片生成/文生图/Anima-Base1.0 +Lora 芙莉莲（提示词指南）_2058148244718444546.json
name: Anima-Base1.0 +Lora 芙莉莲（提示词指南）_2058148244718444546
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima-Base1.0 +Lora 芙莉莲（提示词指南）_2058148244718444546.json
hash: f555f93fdd1d2554
coverage: 0.928571
learned_at: 2026-10-19 22:45:22
nodes: [VAELoader, CLIPLoader, CLIPTextEncode, CLIPTextEncode, VAEDecode, KSampler, EmptyLatentImage, MarkdownNote, SaveImage, Int, UNETLoader, LoraLoaderModelOnly, CR Text, Int]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4, "denoise": 1, "height": 1024, "sampler_name": "er_sde", "scheduler": "simple", "seed": 358445935856117, "steps": 30, "width": 1024}
---

# 图片生成/文生图/Anima-Base1.0 +Lora 芙莉莲（提示词指南）_2058148244718444546.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima-Base1.0 +Lora 芙莉莲（提示词指南）_2058148244718444546.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `MarkdownNote`
- `SaveImage`
- `Int`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Text`
- `Int`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `358445935856117`
- `steps` = `30`
- `cfg` = `4`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`VAEDecode`、`KSampler`、`EmptyLatentImage`、`SaveImage`、`Int`、`UNETLoader`、`LoraLoaderModelOnly`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader
