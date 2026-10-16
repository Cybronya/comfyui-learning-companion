---
key: 视频生成/图生视频/wan2.2-5B图生视频 官方工作流_1950030033369874433.json
name: wan2.2-5B图生视频 官方工作流_1950030033369874433.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950030033369874433.json
hash: 1a32dd59719afae9
coverage: 1
learned_at: 2026-10-15 22:30:51
nodes: [ConstrainImage|pysssss, GetImageSizeAndCount, LoadImage, VAELoader, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, Wan22ImageToVideoLatent, KSampler, VAEDecodeTiled, CreateVideo, ImageResizeKJv2, CLIPLoader, MathExpression|pysssss, Int, SaveVideo, CR Text, UNETLoader]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 687274966167019, "steps": 25}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/wan2.2-5B图生视频 官方工作流_1950030033369874433.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950030033369874433.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `ConstrainImage|pysssss`
- `GetImageSizeAndCount`
- `LoadImage`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `Wan22ImageToVideoLatent`
- `KSampler` ★核心
- `VAEDecodeTiled` ★核心
- `CreateVideo`
- `ImageResizeKJv2`
- `CLIPLoader`
- `MathExpression|pysssss`
- `Int`
- `SaveVideo`
- `CR Text`
- `UNETLoader` ★核心

## 关键参数

- `seed` = `687274966167019`
- `steps` = `25`
- `cfg` = `5`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（18/18）

**有卡**：`ConstrainImage|pysssss`、`GetImageSizeAndCount`、`LoadImage`、`VAELoader`、`CLIPTextEncode`、`ModelSamplingSD3`、`Wan22ImageToVideoLatent`、`KSampler`、`VAEDecodeTiled`、`CreateVideo`、`ImageResizeKJv2`、`CLIPLoader`、`MathExpression|pysssss`、`Int`、`SaveVideo`、`CR Text`、`UNETLoader`

**用到的条目**：KSampler、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、VAEDecodeTiled、Wan22ImageToVideoLatent

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
