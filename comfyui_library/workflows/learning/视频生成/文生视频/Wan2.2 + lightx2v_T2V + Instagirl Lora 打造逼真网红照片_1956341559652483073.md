---
key: 视频生成/文生视频/Wan2.2 + lightx2v_T2V + Instagirl Lora 打造逼真网红照片_1956341559652483073.json
name: Wan2.2 + lightx2v_T2V + Instagirl Lora 打造逼真网红照片_1956341559652483073
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 + lightx2v_T2V + Instagirl Lora 打造逼真网红照片_1956341559652483073.json
hash: 4fe9796acb7138fa
coverage: 0.76
learned_at: 2026-10-15 22:47:08
nodes: [CLIPTextEncode, SetNode, CLIPTextEncode, SetNode, SetNode, SetNode, VAEDecode, SaveImage, ttN seed, GetNode, LoraLoaderModelOnly, ttN text, GetNode, Text Concatenate, UnetLoaderGGUF, UnetLoaderGGUF, VAELoader, CLIPLoaderGGUF, KSamplerAdvanced, LoraLoaderModelOnly, ttN text, EmptyHunyuanLatentVideo, KSamplerAdvanced, ttN text, Power Lora Loader (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "beta57", "sampler_name": 1, "scheduler": "res_2s", "seed": "enable", "steps": "fixed"}
---

# 视频生成/文生视频/Wan2.2 + lightx2v_T2V + Instagirl Lora 打造逼真网红照片_1956341559652483073.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 + lightx2v_T2V + Instagirl Lora 打造逼真网红照片_1956341559652483073.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（25 个）：
- `CLIPTextEncode` ★核心
- `SetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `SaveImage`
- `ttN seed`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `ttN text`
- `GetNode`
- `Text Concatenate`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `VAELoader`
- `CLIPLoaderGGUF`
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `ttN text`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced` ★核心
- `ttN text`
- `Power Lora Loader (rgthree)`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `res_2s`
- `denoise` = `beta57`

## 知识

覆盖率 **76%**（19/25）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`SaveImage`、`ttN seed`、`LoraLoaderModelOnly`、`ttN text`、`Text Concatenate`、`UnetLoaderGGUF`、`VAELoader`、`CLIPLoaderGGUF`、`KSamplerAdvanced`、`EmptyHunyuanLatentVideo`、`Power Lora Loader (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、KSamplerAdvanced、ttN seed、EmptyHunyuanLatentVideo、Power Lora Loader (rgthree)
