---
key: 图片生成/图生图/nunchaku双截棍加速 qwen-image-edit 千问姿态迁移工作流_1970131353419345921.json
name: nunchaku双截棍加速 qwen-image-edit 千问姿态迁移工作流_1970131353419345921
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/nunchaku双截棍加速 qwen-image-edit 千问姿态迁移工作流_1970131353419345921.json
hash: 8f7d509e17270dce
coverage: 0.869565
learned_at: 2026-10-23 11:41:26
nodes: [LoadImage, ModelSamplingAuraFlow, LoadImage, NunchakuQwenImageDiTLoader, CLIPLoader, VAELoader, CLIPTextEncode, ControlNetApplyAdvanced, VAEEncode, DWPreprocessor, PreviewImage, Note, MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, ImageConcatMulti, ImageConcatMulti, SaveImage, SaveImage, ControlNetLoader, TextEncodeQwenImageEdit, KSampler]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "controlnet_strength": 1.5000000000000002, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 866284345072483, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/nunchaku双截棍加速 qwen-image-edit 千问姿态迁移工作流_1970131353419345921.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/nunchaku双截棍加速 qwen-image-edit 千问姿态迁移工作流_1970131353419345921.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `LoadImage`
- `ModelSamplingAuraFlow`
- `LoadImage`
- `NunchakuQwenImageDiTLoader`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ControlNetApplyAdvanced` ★核心
- `VAEEncode` ★核心
- `DWPreprocessor`
- `PreviewImage`
- `Note`
- `MarkdownNote`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `ImageConcatMulti`
- `ImageConcatMulti`
- `SaveImage`
- `SaveImage`
- `ControlNetLoader`
- `TextEncodeQwenImageEdit`
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `controlnet_strength` = `1.5000000000000002`
- `seed` = `866284345072483`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（20/23）

**有卡**：`LoadImage`、`ModelSamplingAuraFlow`、`NunchakuQwenImageDiTLoader`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ControlNetApplyAdvanced`、`VAEEncode`、`DWPreprocessor`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`ImageConcatMulti`、`SaveImage`、`ControlNetLoader`、`TextEncodeQwenImageEdit`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、ControlNetApplyAdvanced、ControlNetLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
