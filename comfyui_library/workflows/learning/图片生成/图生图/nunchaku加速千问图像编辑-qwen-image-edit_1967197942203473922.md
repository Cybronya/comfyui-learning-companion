---
key: 图片生成/图生图/nunchaku加速千问图像编辑-qwen-image-edit_1967197942203473922.json
name: nunchaku加速千问图像编辑-qwen-image-edit_1967197942203473922
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/nunchaku加速千问图像编辑-qwen-image-edit_1967197942203473922.json
hash: 747fd6a1e11627aa
coverage: 0.888889
learned_at: 2026-10-23 11:41:24
nodes: [TextEncodeQwenImageEdit, CFGNorm, CLIPLoader, VAEEncode, KSampler, MarkdownNote, MarkdownNote, NunchakuQwenImageDiTLoader, TextEncodeQwenImageEdit, ModelSamplingAuraFlow, SaveImage, VAEDecode, ImageStitch, SaveImage, VAELoader, LoadImage, ImageScaleToTotalPixels, LayerUtility: ImageScaleByAspectRatio V2]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 669698559194854, "steps": 20}
---

# 图片生成/图生图/nunchaku加速千问图像编辑-qwen-image-edit_1967197942203473922.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/nunchaku加速千问图像编辑-qwen-image-edit_1967197942203473922.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `TextEncodeQwenImageEdit`
- `CFGNorm`
- `CLIPLoader`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `NunchakuQwenImageDiTLoader`
- `TextEncodeQwenImageEdit`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode` ★核心
- `ImageStitch`
- `SaveImage`
- `VAELoader`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `LayerUtility: ImageScaleByAspectRatio V2`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `669698559194854`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`TextEncodeQwenImageEdit`、`CFGNorm`、`CLIPLoader`、`VAEEncode`、`KSampler`、`NunchakuQwenImageDiTLoader`、`ModelSamplingAuraFlow`、`SaveImage`、`VAEDecode`、`ImageStitch`、`VAELoader`、`LoadImage`、`ImageScaleToTotalPixels`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、LoadImage、CFGNorm、TextEncodeQwenImageEdit、VAEEncode
