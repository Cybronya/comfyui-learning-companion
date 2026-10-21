---
key: 图片生成/图生图/SenseNova 1.5 SFT图像编辑_2093391746997768193.json
name: SenseNova 1.5 SFT图像编辑_2093391746997768193
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SenseNova 1.5 SFT图像编辑_2093391746997768193.json
hash: 2fa1ad3db48f54ee
coverage: 1
learned_at: 2026-10-21 00:44:33
nodes: [SenseNovaSamplingOptions, CLIPTextEncode, CLIPTextEncode, SenseNovaReferenceImage, EmptySenseNovaLatentImage, LoadImage, SenseNovaU15Loader, KSampler, SaveImage, VAEDecode, ImageConcanate, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, JWInteger]
patterns: []
missing: []
parameters: {"cfg": 3.5, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 42, "steps": 50}
---

# 图片生成/图生图/SenseNova 1.5 SFT图像编辑_2093391746997768193.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SenseNova 1.5 SFT图像编辑_2093391746997768193.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `SenseNovaSamplingOptions`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SenseNovaReferenceImage`
- `EmptySenseNovaLatentImage`
- `LoadImage`
- `SenseNovaU15Loader`
- `KSampler` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `ImageConcanate`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`

## 关键参数

- `seed` = `42`
- `steps` = `50`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`SenseNovaSamplingOptions`、`CLIPTextEncode`、`SenseNovaReferenceImage`、`EmptySenseNovaLatentImage`、`LoadImage`、`SenseNovaU15Loader`、`KSampler`、`SaveImage`、`VAEDecode`、`ImageConcanate`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`

**用到的条目**：KSampler、VAEDecode、CLIPTextEncode、LoadImage、EmptySenseNovaLatentImage、SaveImage、ImageConcanate、JWInteger
