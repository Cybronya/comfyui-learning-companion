---
key: 图片生成/文生图/Anima_base+1.0+文生图 anima 动漫王者文生图_2057276484787720193.json
name: Anima_base+1.0+文生图 anima 动漫王者文生图_2057276484787720193
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima_base+1.0+文生图 anima 动漫王者文生图_2057276484787720193.json
hash: d958dc02cf309f02
coverage: 0.809524
learned_at: 2026-10-21 02:51:25
nodes: [CLIPLoader, UNETLoader, VAELoader, CLIPTextEncode, VAEDecode, KSampler, KSampler, VAEDecode, CLIPTextEncode, CR Text Concatenate, Int, EmptyLatentImage, SaveImage, SaveImage, JjkText, LoadImage, RH_Captioner, Fast Groups Bypasser (rgthree), ShowText|pysssss, Fast Groups Bypasser (rgthree), RH_Translator]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 2048, "sampler_name": "er_sde", "scheduler": "beta", "seed": 1052489663808341, "steps": 40, "width": 1024}
---

# 图片生成/文生图/Anima_base+1.0+文生图 anima 动漫王者文生图_2057276484787720193.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima_base+1.0+文生图 anima 动漫王者文生图_2057276484787720193.json`

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
- `CLIPTextEncode` ★核心
- `CR Text Concatenate`
- `Int`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `SaveImage`
- `JjkText`
- `LoadImage`
- `RH_Captioner`
- `Fast Groups Bypasser (rgthree)`
- `ShowText|pysssss`
- `Fast Groups Bypasser (rgthree)`
- `RH_Translator`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `1052489663808341`
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

**有卡**：`CLIPLoader`、`UNETLoader`、`VAELoader`、`CLIPTextEncode`、`VAEDecode`、`KSampler`、`CR Text Concatenate`、`Int`、`EmptyLatentImage`、`SaveImage`、`LoadImage`、`RH_Captioner`、`RH_Translator`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader
