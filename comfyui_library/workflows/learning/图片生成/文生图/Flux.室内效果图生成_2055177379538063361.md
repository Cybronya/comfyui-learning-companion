---
key: 图片生成/文生图/Flux.室内效果图生成_2055177379538063361.json
name: Flux.室内效果图生成_2055177379538063361
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.室内效果图生成_2055177379538063361.json
hash: a1c81edacd0f2771
coverage: 1
learned_at: 2026-10-21 02:52:07
nodes: [CLIPTextEncode, UNETLoader, CLIPTextEncode, ConditioningZeroOut, LoraLoaderModelOnly, DualCLIPLoader, VAELoader, KSampler, BaiduTranslateNode, ttN concat, EmptyLatentImage, VAEDecode, SaveImage, Text]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 4, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1106470354491351, "steps": 20, "width": 768}
---

# 图片生成/文生图/Flux.室内效果图生成_2055177379538063361.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.室内效果图生成_2055177379538063361.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `BaiduTranslateNode`
- `ttN concat`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Text`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `1106470354491351`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `768`
- `height` = `1024`
- `batch_size` = `4`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`CLIPTextEncode`、`UNETLoader`、`ConditioningZeroOut`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`VAELoader`、`KSampler`、`BaiduTranslateNode`、`ttN concat`、`EmptyLatentImage`、`VAEDecode`、`SaveImage`、`Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、UNETLoader
