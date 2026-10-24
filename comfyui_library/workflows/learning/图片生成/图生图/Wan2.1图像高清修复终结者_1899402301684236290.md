---
key: 图片生成/图生图/Wan2.1图像高清修复终结者_1899402301684236290.json
name: Wan2.1图像高清修复终结者_1899402301684236290
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.1图像高清修复终结者_1899402301684236290.json
hash: b642e2aad363a62e
coverage: 0.882353
learned_at: 2026-10-23 11:27:50
nodes: [VAEDecode, KSampler, CLIPTextEncode, CLIPTextEncode, VAELoader, VAEEncode, LayerUtility: ImageScaleRestore V2, ImageUpscaleWithModel, UpscaleModelLoader, LoadImage, SaveImage, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, MarkdownNote, MarkdownNote]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.10000000000000002, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 1234571656, "steps": 10}
---

# 图片生成/图生图/Wan2.1图像高清修复终结者_1899402301684236290.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.1图像高清修复终结者_1899402301684236290.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `VAEDecode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleRestore V2`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `LoadImage`
- `SaveImage`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `MarkdownNote`
- `MarkdownNote`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1234571656`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`VAEDecode`、`KSampler`、`CLIPTextEncode`、`VAELoader`、`VAEEncode`、`LayerUtility: ImageScaleRestore V2`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`LoadImage`、`SaveImage`、`CLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
