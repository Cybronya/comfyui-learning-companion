---
key: Qwen Image 2.1 PE提示词优化 提取服装 3D展示 精修褶皱_2103745672011935746.json
name: Qwen Image 2.1 PE提示词优化 提取服装 3D展示 精修褶皱_2103745672011935746
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 PE提示词优化 提取服装 3D展示 精修褶皱_2103745672011935746.json
hash: 7b471e1ef79e68ce
coverage: 0.857143
learned_at: 2026-10-10 20:58:51
nodes: [LoadImage, VAELoader, VAEDecode, KSampler, ComfySwitchNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, easy seed, Text Multiline, ResolutionSelector, CLIPLoader, EmptyLatentImage, QwenPERewriteT8, Display Any (rgthree), UNETLoader, QwenImage21SageAttentionT8, TextEncodeQwenImage21, SaveImage, ImageStitch, SaveImage, LoadImage]
patterns: []
missing: [Display Any (rgthree), Text Multiline, easy seed]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 19960422, "steps": 40, "width": 1024}
discoveries: [次要节点 `Display Any (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# Qwen Image 2.1 PE提示词优化 提取服装 3D展示 精修褶皱_2103745672011935746.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 PE提示词优化 提取服装 3D展示 精修褶皱_2103745672011935746.json`

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
- `QwenImage21SpectrumT8`
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

覆盖率 **86%**（24/28）

**有卡**：`LoadImage`、`VAELoader`、`VAEDecode`、`KSampler`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`ResolutionSelector`、`CLIPLoader`、`EmptyLatentImage`、`QwenPERewriteT8`、`UNETLoader`、`QwenImage21SageAttentionT8`、`TextEncodeQwenImage21`、`SaveImage`、`ImageStitch`

**缺卡**（3）：`Display Any (rgthree)`、`Text Multiline`、`easy seed`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 学习发现

- 次要节点 `Display Any (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
