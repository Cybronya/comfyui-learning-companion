---
key: 图片生成/图生图/F.2Klein极限超分增加细节 小图变大图_2062158009069031426.json
name: F.2Klein极限超分增加细节 小图变大图_2062158009069031426
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.2Klein极限超分增加细节 小图变大图_2062158009069031426.json
hash: 2d014dc22e7dd980
coverage: 0.909091
learned_at: 2026-10-21 00:38:58
nodes: [CLIPLoader, ConditioningZeroOut, VAELoader, VAEDecodeTiled, VAEEncodeTiled, ReferenceLatent, ReferenceLatent, Seed (rgthree), VAEEncodeTiled, Image Comparer (rgthree), SimpleMath+, LayerUtility: ImageScaleByAspectRatio V2, 孤海注释, LoadImage, ColorMatchToReference, UNETLoader, LoraLoaderModelOnly, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, Int, SZ_KleinTiledKSampler]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "sa_solver", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 307327578218599, "steps": 4}
---

# 图片生成/图生图/F.2Klein极限超分增加细节 小图变大图_2062158009069031426.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.2Klein极限超分增加细节 小图变大图_2062158009069031426.json`

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
- `Image Comparer (rgthree)`
- `SimpleMath+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `孤海注释`
- `LoadImage`
- `ColorMatchToReference`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `Int`
- `SZ_KleinTiledKSampler` ★核心

## 关键参数

- `seed` = `307327578218599`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`CLIPLoader`、`ConditioningZeroOut`、`VAELoader`、`VAEDecodeTiled`、`VAEEncodeTiled`、`ReferenceLatent`、`Seed (rgthree)`、`SimpleMath+`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`ColorMatchToReference`、`UNETLoader`、`LoraLoaderModelOnly`、`SaveImage`、`CLIPTextEncode`、`Int`、`SZ_KleinTiledKSampler`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、SZ_KleinTiledKSampler
