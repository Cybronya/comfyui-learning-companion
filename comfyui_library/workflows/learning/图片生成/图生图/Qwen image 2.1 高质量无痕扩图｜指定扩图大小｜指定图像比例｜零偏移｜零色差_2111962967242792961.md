---
key: 图片生成/图生图/Qwen image 2.1 高质量无痕扩图｜指定扩图大小｜指定图像比例｜零偏移｜零色差_2111962967242792961.json
name: Qwen image 2.1 高质量无痕扩图｜指定扩图大小｜指定图像比例｜零偏移｜零色差_2111962967242792961
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 高质量无痕扩图｜指定扩图大小｜指定图像比例｜零偏移｜零色差_2111962967242792961.json
hash: ade494225e86ce91
coverage: 0.769231
learned_at: 2026-10-23 11:13:59
nodes: [CLIPLoader, KSampler, UNETLoader, VAELoader, SaveImage, LoraLoaderModelOnly, TextEncodeQwenImage21, 长边短边, 孤海注释, Switch any [Crystools], ImpactInt, 孤海注释, DapaoImagePadDirectionNode, ImpactInt, ImpactInt, ImpactInt, LayerUtility: ImageScaleByAspectRatio V2, ImpactInt, 孤海注释, 孤海注释, LayerUtility: ImageScaleByAspectRatio V2, 忽略多组孤海, LoadImage, VAEDecode, Image Comparer (rgthree), Any Switch (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1014216909746375, "steps": 25}
---

# 图片生成/图生图/Qwen image 2.1 高质量无痕扩图｜指定扩图大小｜指定图像比例｜零偏移｜零色差_2111962967242792961.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 高质量无痕扩图｜指定扩图大小｜指定图像比例｜零偏移｜零色差_2111962967242792961.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `CLIPLoader`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImage21`
- `长边短边`
- `孤海注释`
- `Switch any [Crystools]`
- `ImpactInt`
- `孤海注释`
- `DapaoImagePadDirectionNode`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImpactInt`
- `孤海注释`
- `孤海注释`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `忽略多组孤海`
- `LoadImage`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `Any Switch (rgthree)`

## 关键参数

- `seed` = `1014216909746375`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（20/26）

**有卡**：`CLIPLoader`、`KSampler`、`UNETLoader`、`VAELoader`、`SaveImage`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`、`长边短边`、`Switch any [Crystools]`、`ImpactInt`、`DapaoImagePadDirectionNode`、`LayerUtility: ImageScaleByAspectRatio V2`、`忽略多组孤海`、`LoadImage`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader
