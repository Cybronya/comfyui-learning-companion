---
key: 图片生成/图生图/WAN2.1图生图_1949144078248812546.json
name: WAN2.1图生图_1949144078248812546
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/WAN2.1图生图_1949144078248812546.json
hash: 6a38b6fe925b9f67
coverage: 0.904762
learned_at: 2026-10-23 11:27:25
nodes: [easy cleanGpuUsed, CLIPTextEncode, easy cleanGpuUsed, VAEEncode, CLIPTextEncode, SaveImage, KSampler, easy cleanGpuUsed, VAEDecode, ImageScale, LoadImage, UNETLoader, RH_Captioner, VAELoader, CLIPLoader, FilmGrain, LoadImage, LoadImage, Primitive float [Crystools], Image Comparer (rgthree), PreviewImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.30000000000000004, "sampler_name": "deis", "scheduler": "sgm_uniform", "seed": 354010616257776, "steps": 20}
---

# 图片生成/图生图/WAN2.1图生图_1949144078248812546.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/WAN2.1图生图_1949144078248812546.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `ImageScale`
- `LoadImage`
- `UNETLoader` ★核心
- `RH_Captioner`
- `VAELoader`
- `CLIPLoader`
- `FilmGrain`
- `LoadImage`
- `LoadImage`
- `Primitive float [Crystools]`
- `Image Comparer (rgthree)`
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `354010616257776`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `deis`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.30000000000000004`

## 知识

覆盖率 **90%**（19/21）

**有卡**：`easy cleanGpuUsed`、`CLIPTextEncode`、`VAEEncode`、`SaveImage`、`KSampler`、`VAEDecode`、`ImageScale`、`LoadImage`、`UNETLoader`、`RH_Captioner`、`VAELoader`、`CLIPLoader`、`FilmGrain`、`Primitive float [Crystools]`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、VAEEncode
