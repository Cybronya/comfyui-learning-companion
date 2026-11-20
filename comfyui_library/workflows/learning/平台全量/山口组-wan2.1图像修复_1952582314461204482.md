---
key: 平台全量/山口组-wan2.1图像修复_1952582314461204482.json
name: 山口组-wan2.1图像修复_1952582314461204482
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/山口组-wan2.1图像修复_1952582314461204482.json
hash: 3b3acf2a95a26f71
coverage: 0.772727
learned_at: 2026-11-14 02:02:08
nodes: [UpscaleModelLoader, ImageUpscaleWithModel, VAEEncode, CLIPLoader, CLIPTextEncode, CLIPTextEncode, ShowText|pysssss, Joy_caption_load, LayerUtility: ImageScaleRestore V2, VAELoader, Joy_caption, LoadImage, Image Comparer (rgthree), LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, VAEDecode, UNETLoader, SaveImage, MarkdownNote, MarkdownNote, MarkdownNote]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.06000000000000001, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 589348749251981, "steps": 10}
---

# 平台全量/山口组-wan2.1图像修复_1952582314461204482.json

> 来源文件 `comfyui_library/workflows/平台全量/山口组-wan2.1图像修复_1952582314461204482.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `VAEEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ShowText|pysssss`
- `Joy_caption_load`
- `LayerUtility: ImageScaleRestore V2`
- `VAELoader`
- `Joy_caption`
- `LoadImage`
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `589348749251981`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.06000000000000001`

## 知识

覆盖率 **77%**（17/22）

**有卡**：`UpscaleModelLoader`、`ImageUpscaleWithModel`、`VAEEncode`、`CLIPLoader`、`CLIPTextEncode`、`Joy_caption_load`、`LayerUtility: ImageScaleRestore V2`、`VAELoader`、`Joy_caption`、`LoadImage`、`LoraLoaderModelOnly`、`KSampler`、`VAEDecode`、`UNETLoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader
