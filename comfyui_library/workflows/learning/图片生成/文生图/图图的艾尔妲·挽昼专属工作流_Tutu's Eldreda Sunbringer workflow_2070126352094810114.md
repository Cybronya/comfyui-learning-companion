---
key: 图片生成/文生图/图图的艾尔妲·挽昼专属工作流_Tutu's Eldreda Sunbringer workflow_2070126352094810114.json
name: 图图的艾尔妲·挽昼专属工作流_Tutu's Eldreda Sunbringer workflow_2070126352094810114
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/图图的艾尔妲·挽昼专属工作流_Tutu's Eldreda Sunbringer workflow_2070126352094810114.json
hash: d7b773772e967560
coverage: 0.928571
learned_at: 2026-10-19 23:43:12
nodes: [CLIPLoader, VAELoader, VAEDecode, Note, CLIPTextEncode, LoraLoaderModelOnly, KSampler, EmptyLatentImage, LoraLoaderModelOnly, SaveImage, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4, "denoise": 1, "height": 1520, "sampler_name": "er_sde", "scheduler": "simple", "seed": 855897515879469, "steps": 45, "width": 1024}
---

# 图片生成/文生图/图图的艾尔妲·挽昼专属工作流_Tutu's Eldreda Sunbringer workflow_2070126352094810114.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/图图的艾尔妲·挽昼专属工作流_Tutu's Eldreda Sunbringer workflow_2070126352094810114.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `Note`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `855897515879469`
- `steps` = `45`
- `cfg` = `4`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1520`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`CLIPLoader`、`VAELoader`、`VAEDecode`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`KSampler`、`EmptyLatentImage`、`SaveImage`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader
