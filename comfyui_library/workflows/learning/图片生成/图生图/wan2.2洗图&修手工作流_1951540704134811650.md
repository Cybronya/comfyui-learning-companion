---
key: 图片生成/图生图/wan2.2洗图&修手工作流_1951540704134811650.json
name: wan2.2洗图&修手工作流_1951540704134811650
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan2.2洗图&修手工作流_1951540704134811650.json
hash: 97d92710b92d9440
coverage: 0.875
learned_at: 2026-10-23 11:46:07
nodes: [Label (rgthree), Note Plus (mtb), easy clearCacheAll, Image Comparer (rgthree), FastLaplacianSharpen, FastFilmGrain, SaveImage, easy cleanGpuUsed, VAEDecode, RHHiddenNodes, LayerUtility: ImageScaleByAspectRatio V2, KSampler, Label (rgthree), SaveImage, MarkdownNote, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 0.6000000000000001, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 991679633479302, "steps": 10}
---

# 图片生成/图生图/wan2.2洗图&修手工作流_1951540704134811650.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan2.2洗图&修手工作流_1951540704134811650.json`

## 结构

**生成流程**：Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `Label (rgthree)`
- `Note Plus (mtb)`
- `easy clearCacheAll`
- `Image Comparer (rgthree)`
- `FastLaplacianSharpen`
- `FastFilmGrain`
- `SaveImage`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `RHHiddenNodes`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `Label (rgthree)`
- `SaveImage`
- `MarkdownNote`
- `LoadImage`

## 关键参数

- `seed` = `991679633479302`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.6000000000000001`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`Label (rgthree)`、`Note Plus (mtb)`、`easy clearCacheAll`、`FastLaplacianSharpen`、`FastFilmGrain`、`SaveImage`、`easy cleanGpuUsed`、`VAEDecode`、`RHHiddenNodes`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、LoadImage、SaveImage、FastFilmGrain、RHHiddenNodes、FastLaplacianSharpen、easy cleanGpuUsed
