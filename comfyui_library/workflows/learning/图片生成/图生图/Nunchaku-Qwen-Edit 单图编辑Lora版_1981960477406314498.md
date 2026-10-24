---
key: 图片生成/图生图/Nunchaku-Qwen-Edit 单图编辑Lora版_1981960477406314498.json
name: Nunchaku-Qwen-Edit 单图编辑Lora版_1981960477406314498
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Nunchaku-Qwen-Edit 单图编辑Lora版_1981960477406314498.json
hash: 3837ff32a6e22e45
coverage: 0.916667
learned_at: 2026-10-23 11:09:59
nodes: [ConditioningZeroOut, CLIPLoader, NunchakuQwenImageDiTLoader, VAELoader, LoadImage, KSampler, VAEDecode, Image Comparer (rgthree), NunchakuQwenImageLoraStack, LoadImage, TextEncodeQwenImageEditPlusPro_lrzjason, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 469110792713879, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Nunchaku-Qwen-Edit 单图编辑Lora版_1981960477406314498.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Nunchaku-Qwen-Edit 单图编辑Lora版_1981960477406314498.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（12 个）：
- `ConditioningZeroOut`
- `CLIPLoader`
- `NunchakuQwenImageDiTLoader`
- `VAELoader`
- `LoadImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `NunchakuQwenImageLoraStack`
- `LoadImage`
- `TextEncodeQwenImageEditPlusPro_lrzjason`
- `SaveImage`

## 关键参数

- `seed` = `469110792713879`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`ConditioningZeroOut`、`CLIPLoader`、`NunchakuQwenImageDiTLoader`、`VAELoader`、`LoadImage`、`KSampler`、`VAEDecode`、`NunchakuQwenImageLoraStack`、`TextEncodeQwenImageEditPlusPro_lrzjason`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、ConditioningZeroOut、LoadImage、TextEncodeQwenImageEditPlusPro_lrzjason、NunchakuQwenImageLoraStack

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
