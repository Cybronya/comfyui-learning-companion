---
key: 图片生成/图生图/Flux.2-Klein9b极限超分增加细节 模糊变高清_2064348600515256322.json
name: Flux.2-Klein9b极限超分增加细节 模糊变高清_2064348600515256322
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.2-Klein9b极限超分增加细节 模糊变高清_2064348600515256322.json
hash: 47d7423ff3edca32
coverage: 0.909091
learned_at: 2026-10-21 00:39:35
nodes: [CLIPLoader, ConditioningZeroOut, VAELoader, VAEDecodeTiled, VAEEncodeTiled, ReferenceLatent, ReferenceLatent, Seed (rgthree), VAEEncodeTiled, SaveImage, Image Comparer (rgthree), SimpleMath+, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, 孤海注释, LoadImage, ColorMatchToReference, SZ_KleinTiledKSampler, CLIPTextEncode, Int, UNETLoader, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "sa_solver", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 326840076437412, "steps": 4}
---

# 图片生成/图生图/Flux.2-Klein9b极限超分增加细节 模糊变高清_2064348600515256322.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.2-Klein9b极限超分增加细节 模糊变高清_2064348600515256322.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `CLIPLoader`
- `ConditioningZeroOut`
- `VAELoader`
- `VAEDecodeTiled` ★核心
- `VAEEncodeTiled` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `Seed (rgthree)`
- `VAEEncodeTiled` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `SimpleMath+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `孤海注释`
- `LoadImage`
- `ColorMatchToReference`
- `SZ_KleinTiledKSampler` ★核心
- `CLIPTextEncode` ★核心
- `Int`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `326840076437412`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`CLIPLoader`、`ConditioningZeroOut`、`VAELoader`、`VAEDecodeTiled`、`VAEEncodeTiled`、`ReferenceLatent`、`Seed (rgthree)`、`SaveImage`、`SimpleMath+`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`ColorMatchToReference`、`SZ_KleinTiledKSampler`、`CLIPTextEncode`、`Int`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、SZ_KleinTiledKSampler
