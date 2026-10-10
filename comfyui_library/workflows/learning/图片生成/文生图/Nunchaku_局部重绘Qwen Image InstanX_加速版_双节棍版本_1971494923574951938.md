---
key: Nunchaku_局部重绘Qwen Image InstanX_加速版_双节棍版本_1971494923574951938.json
name: Nunchaku_局部重绘Qwen Image InstanX_加速版_双节棍版本_1971494923574951938
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Nunchaku_局部重绘Qwen Image InstanX_加速版_双节棍版本_1971494923574951938.json
hash: f454185eb7c57c5a
coverage: 0.833333
learned_at: 2026-10-10 20:58:48
nodes: [VAELoader, CLIPLoader, MarkdownNote, CLIPTextEncode, ControlNetLoader, ControlNetInpaintingAliMamaApply, ModelSamplingAuraFlow, VAEDecode, MaskToImage, PreviewImage, SaveImage, VAEEncode, LoadImage, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, NunchakuQwenImageDiTLoader, KSampler, UNETLoader]
patterns: [image_to_image]
missing: [LayerUtility: ImageScaleByAspectRatio V2]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 974024003577922, "steps": 8}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# Nunchaku_局部重绘Qwen Image InstanX_加速版_双节棍版本_1971494923574951938.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Nunchaku_局部重绘Qwen Image InstanX_加速版_双节棍版本_1971494923574951938.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `VAELoader`
- `CLIPLoader`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `ControlNetLoader`
- `ControlNetInpaintingAliMamaApply`
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `VAEEncode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `NunchakuQwenImageDiTLoader`
- `KSampler` ★核心
- `UNETLoader` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `974024003577922`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`ControlNetLoader`、`ControlNetInpaintingAliMamaApply`、`ModelSamplingAuraFlow`、`VAEDecode`、`MaskToImage`、`SaveImage`、`VAEEncode`、`LoadImage`、`NunchakuQwenImageDiTLoader`、`KSampler`、`UNETLoader`

**缺卡**（1）：`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、ControlNetInpaintingAliMamaApply

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
