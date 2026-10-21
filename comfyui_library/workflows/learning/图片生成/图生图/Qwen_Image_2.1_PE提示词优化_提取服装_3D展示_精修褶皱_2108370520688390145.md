---
key: 图片生成/图生图/Qwen_Image_2.1_PE提示词优化_提取服装_3D展示_精修褶皱_2108370520688390145.json
name: Qwen_Image_2.1_PE提示词优化_提取服装_3D展示_精修褶皱_2108370520688390145
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_Image_2.1_PE提示词优化_提取服装_3D展示_精修褶皱_2108370520688390145.json
hash: cfd8fc4dba5694c0
coverage: 0.964286
learned_at: 2026-10-21 00:43:56
nodes: [LoadImage, VAELoader, VAEDecode, KSampler, ComfySwitchNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, QwenImage21BlockCacheT8, easy seed, Text Multiline, ResolutionSelector, CLIPLoader, EmptyLatentImage, QwenPERewriteT8, Display Any (rgthree), UNETLoader, QwenImage21SageAttentionT8, TextEncodeQwenImage21, SaveImage, ImageStitch, SaveImage, LoadImage, QwenImage21SpectrumT8]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 19960422, "steps": 40, "width": 1024}
---

# 图片生成/图生图/Qwen_Image_2.1_PE提示词优化_提取服装_3D展示_精修褶皱_2108370520688390145.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_Image_2.1_PE提示词优化_提取服装_3D展示_精修褶皱_2108370520688390145.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `LoadImage`
- `VAELoader`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `QwenImage21BlockCacheT8`
- `easy seed`
- `Text Multiline`
- `ResolutionSelector`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `QwenPERewriteT8`
- `Display Any (rgthree)`
- `UNETLoader` ★核心
- `QwenImage21SageAttentionT8`
- `TextEncodeQwenImage21`
- `SaveImage`
- `ImageStitch`
- `SaveImage`
- `LoadImage`
- `QwenImage21SpectrumT8`

## 关键参数

- `seed` = `19960422`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **96%**（27/28）

**有卡**：`LoadImage`、`VAELoader`、`VAEDecode`、`KSampler`、`QwenImage21BlockCacheT8`、`easy seed`、`Text Multiline`、`ResolutionSelector`、`CLIPLoader`、`EmptyLatentImage`、`QwenPERewriteT8`、`Display Any (rgthree)`、`UNETLoader`、`QwenImage21SageAttentionT8`、`TextEncodeQwenImage21`、`SaveImage`、`ImageStitch`、`QwenImage21SpectrumT8`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
