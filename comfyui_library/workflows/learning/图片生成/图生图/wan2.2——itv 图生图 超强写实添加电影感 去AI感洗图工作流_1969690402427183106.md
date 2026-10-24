---
key: 图片生成/图生图/wan2.2——itv 图生图 超强写实添加电影感 去AI感洗图工作流_1969690402427183106.json
name: wan2.2——itv 图生图 超强写实添加电影感 去AI感洗图工作流_1969690402427183106
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan2.2——itv 图生图 超强写实添加电影感 去AI感洗图工作流_1969690402427183106.json
hash: c8cc028891f09945
coverage: 0.888889
learned_at: 2026-10-23 11:46:01
nodes: [Note, EsesImageEffectBloom, Note, BetterFilmGrain, RH_Captioner, ShowText|pysssss, CR Text, VAEEncode, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, CLIPTextEncode, KSampler, VAEDecode, ModelSamplingSD3, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, CR Text Concatenate, CLIPTextEncode, ImageConcatMulti, SaveImage, ColorCorrect, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.4000000000000001, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 700391473753107, "steps": 10}
---

# 图片生成/图生图/wan2.2——itv 图生图 超强写实添加电影感 去AI感洗图工作流_1969690402427183106.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan2.2——itv 图生图 超强写实添加电影感 去AI感洗图工作流_1969690402427183106.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `Note`
- `EsesImageEffectBloom`
- `Note`
- `BetterFilmGrain`
- `RH_Captioner`
- `ShowText|pysssss`
- `CR Text`
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `CR Text Concatenate`
- `CLIPTextEncode` ★核心
- `ImageConcatMulti`
- `SaveImage`
- `ColorCorrect`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `700391473753107`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.4000000000000001`

## 知识

覆盖率 **89%**（24/27）

**有卡**：`EsesImageEffectBloom`、`BetterFilmGrain`、`RH_Captioner`、`CR Text`、`VAEEncode`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`KSampler`、`VAEDecode`、`ModelSamplingSD3`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`CR Text Concatenate`、`ImageConcatMulti`、`ColorCorrect`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
