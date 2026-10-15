---
key: 图片生成/文生图/Wan2.2文生图 扣子api调用_1963968525272498177.json
name: Wan2.2文生图 扣子api调用_1963968525272498177
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2文生图 扣子api调用_1963968525272498177.json
hash: 8be20ff811f265ec
coverage: 0.820513
learned_at: 2026-10-15 22:27:36
nodes: [ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, PathchSageAttentionKJ, KSamplerAdvanced, PathchSageAttentionKJ, ModelSamplingSD3, Any Switch (rgthree), KSamplerAdvanced, Any Switch (rgthree), CLIPTextEncode, CLIPTextEncode, EmptyHunyuanLatentVideo, SimpleMath+, easy showAnything, UnetLoaderGGUF, UnetLoaderGGUF, easy negative, Int, easy int, PlaySound|pysssss, easy int, VAEDecode, UNETLoader, UNETLoader, Int, Note, Fast Groups Bypasser (rgthree), Wan_video_prompt_generator, Any Switch (rgthree), SaveImage, Any Switch (rgthree), RunningHub SeedXPro Translator, easy positive]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 2.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 图片生成/文生图/Wan2.2文生图 扣子api调用_1963968525272498177.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2文生图 扣子api调用_1963968525272498177.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（39 个）：
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `PathchSageAttentionKJ`
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `Any Switch (rgthree)`
- `KSamplerAdvanced` ★核心
- `Any Switch (rgthree)`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `SimpleMath+`
- `easy showAnything`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `easy negative`
- `Int`
- `easy int`
- `PlaySound|pysssss`
- `easy int`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Int`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `Wan_video_prompt_generator`
- `Any Switch (rgthree)`
- `SaveImage`
- `Any Switch (rgthree)`
- `RunningHub SeedXPro Translator`
- `easy positive`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `12`
- `sampler_name` = `2.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **82%**（32/39）

**有卡**：`ModelSamplingSD3`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`PathchSageAttentionKJ`、`KSamplerAdvanced`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`SimpleMath+`、`UnetLoaderGGUF`、`easy negative`、`Int`、`easy int`、`PlaySound|pysssss`、`VAEDecode`、`UNETLoader`、`Wan_video_prompt_generator`、`SaveImage`、`RunningHub SeedXPro Translator`、`easy positive`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、RunningHub SeedXPro Translator
