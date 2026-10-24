---
key: 图片生成/图生图/SD1.5 XL 图生图学习基础工作流（用于学习）_2054894214500102145.json
name: SD1.5 XL 图生图学习基础工作流（用于学习）_2054894214500102145
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SD1.5 XL 图生图学习基础工作流（用于学习）_2054894214500102145.json
hash: 558f0a77079d70c1
coverage: 0.651685
learned_at: 2026-10-23 11:23:31
nodes: [VAEEncode, ColorMatch, ColorMatch, ColorMatch, PreviewImage, PreviewImage, ColorMatch, PreviewImage, ImageColorMatch+, Reroute, ImageColorMatch+, ImageColorMatch+, ImageColorMatch+, PreviewImage, ImageResizeKJv2, PreviewImage, ImageResizeKJv2, PreviewImage, PreviewImage, PreviewImage, PreviewImage, PreviewImage, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, ImageResizeKJv2, ConstrainImage|pysssss, PreviewImage, CLIPTextEncode, VAEDecode, LoadImage, CLIPTextEncode, KSampler, SaveImage, VAEDecode, CLIPTextEncode, CLIPTextEncode, LoadImage, VAEEncode, PreviewImage, PreviewImage, PreviewImage, PreviewImage, PreviewImage, PreviewImage, ImageResizeKJv2, ImageScale, PreviewImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, GetImageSize+, PreviewImage, LoadImage, Reroute, LoadImage, PreviewImage, PreviewImage, LoadImage, PreviewImage, SaveImage, KSamplerAdvanced, KSamplerAdvanced, KSampler, KSampler, KSampler SDXL (Eff.), ImageColorMatch+, ColorMatch, PreviewImage, PreviewImage, ImageColorMatchAdobe+, Fast Groups Bypasser (rgthree), Efficient Loader, LoraLoader, ImageColorMatchAdobe+, ColorMatch, ImageColorMatch+, KSampler (Efficient), KSampler Adv. (Efficient), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, LoadImage, CheckpointLoaderSimple, CheckpointLoaderSimple]
patterns: [image_to_image, lora]
missing: []
parameters: {"cfg": 20, "checkpoint": "RunDiffusionJuggernaut-XL-v9.safetensors", "denoise": "normal", "lora_name": "SDXL\\SDXL 厚涂艺术 LORA.safetensors", "sampler_name": 7, "scheduler": "euler", "seed": "enable", "steps": null, "strength_clip": 1, "strength_model": 1}
---

# 图片生成/图生图/SD1.5 XL 图生图学习基础工作流（用于学习）_2054894214500102145.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SD1.5 XL 图生图学习基础工作流（用于学习）_2054894214500102145.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（89 个）：
- `VAEEncode` ★核心
- `ColorMatch`
- `ColorMatch`
- `ColorMatch`
- `PreviewImage`
- `PreviewImage`
- `ColorMatch`
- `PreviewImage`
- `ImageColorMatch+`
- `Reroute`
- `ImageColorMatch+`
- `ImageColorMatch+`
- `ImageColorMatch+`
- `PreviewImage`
- `ImageResizeKJv2`
- `PreviewImage`
- `ImageResizeKJv2`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ConstrainImage|pysssss`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `VAEEncode` ★核心
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `ImageResizeKJv2`
- `ImageScale`
- `PreviewImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSize+`
- `PreviewImage`
- `LoadImage`
- `Reroute`
- `LoadImage`
- `PreviewImage`
- `PreviewImage`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler SDXL (Eff.)` ★核心
- `ImageColorMatch+`
- `ColorMatch`
- `PreviewImage`
- `PreviewImage`
- `ImageColorMatchAdobe+`
- `Fast Groups Bypasser (rgthree)`
- `Efficient Loader`
- `LoraLoader` ★核心
- `ImageColorMatchAdobe+`
- `ColorMatch`
- `ImageColorMatch+`
- `KSampler (Efficient)` ★核心
- `KSampler Adv. (Efficient)` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `CheckpointLoaderSimple` ★核心

**识别到的模式**：image_to_image、lora

## 关键参数

- `seed` = `enable`
- `steps` = `None`
- `cfg` = `20`
- `sampler_name` = `7`
- `scheduler` = `euler`
- `denoise` = `normal`
- `lora_name` = `SDXL\SDXL 厚涂艺术 LORA.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `checkpoint` = `RunDiffusionJuggernaut-XL-v9.safetensors`

## 知识

覆盖率 **65%**（58/89）

**有卡**：`VAEEncode`、`ColorMatch`、`ImageColorMatch+`、`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`、`ConstrainImage|pysssss`、`CLIPTextEncode`、`VAEDecode`、`LoadImage`、`KSampler`、`SaveImage`、`ImageScale`、`GetImageSize+`、`KSamplerAdvanced`、`KSampler SDXL (Eff.)`、`ImageColorMatchAdobe+`、`Efficient Loader`、`LoraLoader`、`KSampler (Efficient)`、`KSampler Adv. (Efficient)`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced、KSampler (Efficient)
