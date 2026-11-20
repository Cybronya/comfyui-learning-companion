---
key: 平台全量/nunchaku加速千问图像编辑-qwen-image-edit_1968144215802806274.json
name: nunchaku加速千问图像编辑-qwen-image-edit_1968144215802806274
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/nunchaku加速千问图像编辑-qwen-image-edit_1968144215802806274.json
hash: f161c986b4377f44
coverage: 0.842105
learned_at: 2026-11-14 01:15:35
nodes: [TextEncodeQwenImageEdit, VAEEncode, KSampler, MarkdownNote, VAEDecode, CLIPLoader, MarkdownNote, VAELoader, ModelSamplingAuraFlow, CFGNorm, NunchakuQwenImageDiTLoader, ImageScaleToTotalPixels, LayerUtility: ImageScaleByAspectRatio V2, ImageStitch, SaveImage, SaveImage, LoadImage, Note, TextEncodeQwenImageEdit]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 912255654023353, "steps": 20}
---

# 平台全量/nunchaku加速千问图像编辑-qwen-image-edit_1968144215802806274.json

> 来源文件 `comfyui_library/workflows/平台全量/nunchaku加速千问图像编辑-qwen-image-edit_1968144215802806274.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `TextEncodeQwenImageEdit`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `MarkdownNote`
- `VAEDecode` ★核心
- `CLIPLoader`
- `MarkdownNote`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `NunchakuQwenImageDiTLoader`
- `ImageScaleToTotalPixels`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageStitch`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `Note`
- `TextEncodeQwenImageEdit`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `912255654023353`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`TextEncodeQwenImageEdit`、`VAEEncode`、`KSampler`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`NunchakuQwenImageDiTLoader`、`ImageScaleToTotalPixels`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageStitch`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、LoadImage、CFGNorm、TextEncodeQwenImageEdit、VAEEncode
