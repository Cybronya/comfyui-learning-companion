---
key: 图片生成/图生图/SenseNova 1.5 SFT图像编辑_2093632408083058689.json
name: SenseNova 1.5 SFT图像编辑_2093632408083058689
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SenseNova 1.5 SFT图像编辑_2093632408083058689.json
hash: 24e58c76dbda4125
coverage: 1
learned_at: 2026-10-15 22:25:31
nodes: [SenseNovaSamplingOptions, CLIPTextEncode, SenseNovaReferenceImage, EmptySenseNovaLatentImage, SenseNovaU15Loader, KSampler, SaveImage, VAEDecode, ImageConcanate, SaveImage, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 3.5, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 42, "steps": 50}
---

# 图片生成/图生图/SenseNova 1.5 SFT图像编辑_2093632408083058689.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SenseNova 1.5 SFT图像编辑_2093632408083058689.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `SenseNovaSamplingOptions`
- `CLIPTextEncode` ★核心
- `SenseNovaReferenceImage`
- `EmptySenseNovaLatentImage`
- `SenseNovaU15Loader`
- `KSampler` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `ImageConcanate`
- `SaveImage`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `42`
- `steps` = `50`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`SenseNovaSamplingOptions`、`CLIPTextEncode`、`SenseNovaReferenceImage`、`EmptySenseNovaLatentImage`、`SenseNovaU15Loader`、`KSampler`、`SaveImage`、`VAEDecode`、`ImageConcanate`、`JWInteger`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、CLIPTextEncode、LoadImage、EmptySenseNovaLatentImage、SaveImage、ImageConcanate、JWInteger
