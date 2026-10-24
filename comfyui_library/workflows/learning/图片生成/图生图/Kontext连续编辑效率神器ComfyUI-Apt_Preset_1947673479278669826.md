---
key: 图片生成/图生图/Kontext连续编辑效率神器ComfyUI-Apt_Preset_1947673479278669826.json
name: Kontext连续编辑效率神器ComfyUI-Apt_Preset_1947673479278669826
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Kontext连续编辑效率神器ComfyUI-Apt_Preset_1947673479278669826.json
hash: ecf0fea2eb1e3863
coverage: 0.758621
learned_at: 2026-10-23 11:07:28
nodes: [LoadImage, chx_Ksampler_Kontext, chx_Ksampler_Kontext, DeepTranslatorTextNode, DeepTranslatorTextNode, DeepTranslatorTextNode, chx_Ksampler_Kontext_inpaint, PreviewImage, chx_Ksampler_refine, PreviewImage, PreviewImage, LoadImage, Mask_split_mulMask, Image Comparer (rgthree), MaskPreview+, pre_Kontext_mul, MaskPreview+, basic_Ksampler_simple, PreviewImage, LoadImage, sum_load_adv, chx_Ksampler_Kontext, easy showAnything, chx_Ksampler_Kontext, PreviewImage, LoadImage, DeepTranslatorTextNode, text_sum, SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/Kontext连续编辑效率神器ComfyUI-Apt_Preset_1947673479278669826.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Kontext连续编辑效率神器ComfyUI-Apt_Preset_1947673479278669826.json`

## 结构

**生成流程**：Sampling → Output → Other

**节点**（29 个）：
- `LoadImage`
- `chx_Ksampler_Kontext` ★核心
- `chx_Ksampler_Kontext` ★核心
- `DeepTranslatorTextNode`
- `DeepTranslatorTextNode`
- `DeepTranslatorTextNode`
- `chx_Ksampler_Kontext_inpaint` ★核心
- `PreviewImage`
- `chx_Ksampler_refine` ★核心
- `PreviewImage`
- `PreviewImage`
- `LoadImage`
- `Mask_split_mulMask`
- `Image Comparer (rgthree)`
- `MaskPreview+`
- `pre_Kontext_mul`
- `MaskPreview+`
- `basic_Ksampler_simple` ★核心
- `PreviewImage`
- `LoadImage`
- `sum_load_adv`
- `chx_Ksampler_Kontext` ★核心
- `easy showAnything`
- `chx_Ksampler_Kontext` ★核心
- `PreviewImage`
- `LoadImage`
- `DeepTranslatorTextNode`
- `text_sum`
- `SaveImage`

## 知识

覆盖率 **76%**（22/29）

**有卡**：`LoadImage`、`chx_Ksampler_Kontext`、`DeepTranslatorTextNode`、`chx_Ksampler_Kontext_inpaint`、`chx_Ksampler_refine`、`Mask_split_mulMask`、`MaskPreview+`、`pre_Kontext_mul`、`basic_Ksampler_simple`、`sum_load_adv`、`text_sum`、`SaveImage`

**用到的条目**：LoadImage、basic_Ksampler_simple、chx_Ksampler_Kontext、chx_Ksampler_Kontext_inpaint、chx_Ksampler_refine、SaveImage、MaskPreview+、MaskPreview+
