---
key: 图片生成/文生图/QWEN-IMAGE2.1+全能文生图4K放大_2102084941440962561.json
name: QWEN-IMAGE2.1+全能文生图4K放大_2102084941440962561
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/QWEN-IMAGE2.1+全能文生图4K放大_2102084941440962561.json
hash: 085b97444f7767a3
coverage: 0.814815
learned_at: 2026-10-20 01:50:48
nodes: [VAELoader, UNETLoader, CLIPLoader, CLIPLoader, EmptyLatentImage, ShowAnything|Mie, ShowAnything|Mie, TextGenerate, Fast Groups Bypasser (rgthree), RegexExtract, TextEncodeQwenImage21, ComfySwitchNode, StringFormat, PrimitiveStringMultiline, PrimitiveStringMultiline, SaveImage, KSampler, VOSR2ModelLoader, SaveImage, ResolutionSelector, PrimitiveStringMultiline, VAEDecode, easy cleanGpuUsed, VOSR2Upscale, Image Remove Alpha JK, ImageApplyLUT+, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 103131211231145, "steps": 40, "width": 1024}
---

# 图片生成/文生图/QWEN-IMAGE2.1+全能文生图4K放大_2102084941440962561.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/QWEN-IMAGE2.1+全能文生图4K放大_2102084941440962561.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `ShowAnything|Mie`
- `ShowAnything|Mie`
- `TextGenerate`
- `Fast Groups Bypasser (rgthree)`
- `RegexExtract`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `StringFormat`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `SaveImage`
- `KSampler` ★核心
- `VOSR2ModelLoader`
- `SaveImage`
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `VOSR2Upscale`
- `Image Remove Alpha JK`
- `ImageApplyLUT+`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `103131211231145`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（22/27）

**有卡**：`VAELoader`、`UNETLoader`、`CLIPLoader`、`EmptyLatentImage`、`ShowAnything|Mie`、`TextGenerate`、`RegexExtract`、`TextEncodeQwenImage21`、`StringFormat`、`SaveImage`、`KSampler`、`VOSR2ModelLoader`、`ResolutionSelector`、`VAEDecode`、`easy cleanGpuUsed`、`VOSR2Upscale`、`Image Remove Alpha JK`、`ImageApplyLUT+`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
