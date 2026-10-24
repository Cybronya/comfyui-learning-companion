---
key: 图片生成/图生图/Qwen-image2.1-产品融图_2112741548281655298.json
name: Qwen-image2.1-产品融图_2112741548281655298
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-产品融图_2112741548281655298.json
hash: fb14283ca676c507
coverage: 0.933333
learned_at: 2026-10-23 11:18:24
nodes: [Image Comparer (rgthree), UNETLoader, CLIPLoader, VAEDecode, SaveImage, VAELoader, LoraLoaderModelOnly, KSampler, LoadImage, InspyrenetRembg, LayerUtility: ImageScaleByAspectRatio V2, YYZPack_yyz_canvasnodeTool, LoadImage, FastCanvas, TextEncodeQwenImage21]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1059523873099545, "steps": 25}
---

# 图片生成/图生图/Qwen-image2.1-产品融图_2112741548281655298.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-产品融图_2112741548281655298.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `LoadImage`
- `InspyrenetRembg`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `YYZPack_yyz_canvasnodeTool`
- `LoadImage`
- `FastCanvas`
- `TextEncodeQwenImage21`

## 关键参数

- `seed` = `1059523873099545`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAEDecode`、`SaveImage`、`VAELoader`、`LoraLoaderModelOnly`、`KSampler`、`LoadImage`、`InspyrenetRembg`、`LayerUtility: ImageScaleByAspectRatio V2`、`YYZPack_yyz_canvasnodeTool`、`FastCanvas`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader
