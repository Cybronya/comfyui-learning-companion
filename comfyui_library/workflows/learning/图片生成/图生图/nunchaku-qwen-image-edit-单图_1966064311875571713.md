---
key: 图片生成/图生图/nunchaku-qwen-image-edit-单图_1966064311875571713.json
name: nunchaku-qwen-image-edit-单图_1966064311875571713
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/nunchaku-qwen-image-edit-单图_1966064311875571713.json
hash: 53f5da2822e22c65
coverage: 0.894737
learned_at: 2026-10-23 11:41:20
nodes: [CLIPLoader, VAELoader, CFGNorm, LoadImage, NunchakuQwenImageDiTLoader, KSampler, easy clearCacheAll, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, easy clearCacheAll, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, SaveImage, AILab_ImageCompare, MarkdownNote, MarkdownNote, TextEncodeQwenImageEdit]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 96030403595016, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/nunchaku-qwen-image-edit-单图_1966064311875571713.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/nunchaku-qwen-image-edit-单图_1966064311875571713.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `CLIPLoader`
- `VAELoader`
- `CFGNorm`
- `LoadImage`
- `NunchakuQwenImageDiTLoader`
- `KSampler` ★核心
- `easy clearCacheAll`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `easy clearCacheAll`
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `SaveImage`
- `AILab_ImageCompare`
- `MarkdownNote`
- `MarkdownNote`
- `TextEncodeQwenImageEdit`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `96030403595016`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`CLIPLoader`、`VAELoader`、`CFGNorm`、`LoadImage`、`NunchakuQwenImageDiTLoader`、`KSampler`、`easy clearCacheAll`、`ModelSamplingAuraFlow`、`SaveImage`、`TextEncodeQwenImageEdit`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`AILab_ImageCompare`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、LoadImage、CFGNorm、TextEncodeQwenImageEdit、VAEEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
