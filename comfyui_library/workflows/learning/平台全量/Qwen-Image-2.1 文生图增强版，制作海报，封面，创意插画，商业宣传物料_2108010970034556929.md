---
key: 平台全量/Qwen-Image-2.1 文生图增强版，制作海报，封面，创意插画，商业宣传物料_2108010970034556929.json
name: Qwen-Image-2.1 文生图增强版，制作海报，封面，创意插画，商业宣传物料_2108010970034556929
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-Image-2.1 文生图增强版，制作海报，封面，创意插画，商业宣传物料_2108010970034556929.json
hash: 23c827ee87296169
coverage: 0.8
learned_at: 2026-11-14 00:51:33
nodes: [CLIPLoader, VAELoader, VOSR2ModelLoader, ResolutionSelector, UNETLoader, SaveImage, MarkdownNote, TextEncodeQwenImage21, KSampler, easy imageScaleDownToSize, SimpleMath+, VAEDecode, EmptyLatentImage, ImpactInt, VOSR2Upscale, Image Comparer (rgthree), 孤海注释, GoohaiDisplayAny, PrimitiveStringMultiline, RHHiddenNodes]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 346740793982801, "steps": 25, "width": 1024}
---

# 平台全量/Qwen-Image-2.1 文生图增强版，制作海报，封面，创意插画，商业宣传物料_2108010970034556929.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-Image-2.1 文生图增强版，制作海报，封面，创意插画，商业宣传物料_2108010970034556929.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `CLIPLoader`
- `VAELoader`
- `VOSR2ModelLoader`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `SaveImage`
- `MarkdownNote`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `easy imageScaleDownToSize`
- `SimpleMath+`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `ImpactInt`
- `VOSR2Upscale`
- `Image Comparer (rgthree)`
- `孤海注释`
- `GoohaiDisplayAny`
- `PrimitiveStringMultiline`
- `RHHiddenNodes`

## 关键参数

- `seed` = `346740793982801`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **80%**（16/20）

**有卡**：`CLIPLoader`、`VAELoader`、`VOSR2ModelLoader`、`ResolutionSelector`、`UNETLoader`、`SaveImage`、`TextEncodeQwenImage21`、`KSampler`、`easy imageScaleDownToSize`、`SimpleMath+`、`VAEDecode`、`EmptyLatentImage`、`ImpactInt`、`VOSR2Upscale`、`GoohaiDisplayAny`、`RHHiddenNodes`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
