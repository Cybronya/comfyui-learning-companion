---
key: 图片生成/文生图/Anima_base+1.0+文生图_2069591838113226754.json
name: Anima_base+1.0+文生图_2069591838113226754
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima_base+1.0+文生图_2069591838113226754.json
hash: 3150631ce257d507
coverage: 0.809524
learned_at: 2026-10-19 23:40:52
nodes: [CLIPLoader, UNETLoader, VAELoader, CLIPTextEncode, VAEDecode, KSampler, KSampler, VAEDecode, CR Text Concatenate, Int, EmptyLatentImage, SaveImage, SaveImage, RH_Captioner, Fast Groups Bypasser (rgthree), ShowText|pysssss, Fast Groups Bypasser (rgthree), RH_Translator, LoadImage, CLIPTextEncode, JjkText]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 2048, "sampler_name": "er_sde", "scheduler": "beta", "seed": 1089274719616978, "steps": 40, "width": 1024}
---

# 图片生成/文生图/Anima_base+1.0+文生图_2069591838113226754.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima_base+1.0+文生图_2069591838113226754.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（21 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CR Text Concatenate`
- `Int`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `SaveImage`
- `RH_Captioner`
- `Fast Groups Bypasser (rgthree)`
- `ShowText|pysssss`
- `Fast Groups Bypasser (rgthree)`
- `RH_Translator`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `JjkText`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `1089274719616978`
- `steps` = `40`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `1024`
- `height` = `2048`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（17/21）

**有卡**：`CLIPLoader`、`UNETLoader`、`VAELoader`、`CLIPTextEncode`、`VAEDecode`、`KSampler`、`CR Text Concatenate`、`Int`、`EmptyLatentImage`、`SaveImage`、`RH_Captioner`、`RH_Translator`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader
