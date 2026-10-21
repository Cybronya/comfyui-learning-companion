---
key: 图片生成/文生图/ZIT_v20.safetensors，小日子模型升级版_2058925000341671937.json
name: ZIT_v20.safetensors，小日子模型升级版_2058925000341671937
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/ZIT_v20.safetensors，小日子模型升级版_2058925000341671937.json
hash: d422f532e12bb586
coverage: 0.740741
learned_at: 2026-10-19 23:03:03
nodes: [easy int, easy int, CLIPLoaderGGUF, VAELoader, EmptyLatentImage, easy int, KSampler, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CR Text, VAEDecode, LoadImage, MarkdownNote, MarkdownNote, MarkdownNote, SaveImage, ProcessString, CLIPTextEncode, CLIPTextEncode, DeepTranslatorTextNode, easy showAnything, LoraLoaderModelOnly, LoraLoaderModelOnly, PrimitiveFloat, Note, Note]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler_ancestral", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 673185717402076, "steps": 30, "width": 512}
---

# 图片生成/文生图/ZIT_v20.safetensors，小日子模型升级版_2058925000341671937.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/ZIT_v20.safetensors，小日子模型升级版_2058925000341671937.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（27 个）：
- `easy int`
- `easy int`
- `CLIPLoaderGGUF`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `easy int`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Text`
- `VAEDecode` ★核心
- `LoadImage`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `SaveImage`
- `ProcessString`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `DeepTranslatorTextNode`
- `easy showAnything`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveFloat`
- `Note`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `673185717402076`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **74%**（20/27）

**有卡**：`easy int`、`CLIPLoaderGGUF`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`UNETLoader`、`LoraLoaderModelOnly`、`CR Text`、`VAEDecode`、`LoadImage`、`SaveImage`、`ProcessString`、`CLIPTextEncode`、`DeepTranslatorTextNode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、EmptyLatentImage、LoadImage、UNETLoader
