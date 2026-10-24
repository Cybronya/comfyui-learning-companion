---
key: 图片生成/图生图/（Lora支持版）Nunchaku Qwen Edit超级加速版图像编辑（丰胸）_1982319824099524609.json
name: （Lora支持版）Nunchaku Qwen Edit超级加速版图像编辑（丰胸）_1982319824099524609
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/（Lora支持版）Nunchaku Qwen Edit超级加速版图像编辑（丰胸）_1982319824099524609.json
hash: 25d649cf358b58b0
coverage: 0.928571
learned_at: 2026-10-23 13:37:14
nodes: [ConditioningZeroOut, KSampler, SaveImage, VAEDecode, ImageConcanate, SaveImage, Image Comparer (rgthree), CLIPLoader, VAELoader, NunchakuQwenImageLoraStack, NunchakuQwenImageDiTLoader, CR Prompt Text, LoadImage, TextEncodeQwenImageEditPlusPro_lrzjason]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 49963367767054, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/（Lora支持版）Nunchaku Qwen Edit超级加速版图像编辑（丰胸）_1982319824099524609.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/（Lora支持版）Nunchaku Qwen Edit超级加速版图像编辑（丰胸）_1982319824099524609.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `ConditioningZeroOut`
- `KSampler` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `ImageConcanate`
- `SaveImage`
- `Image Comparer (rgthree)`
- `CLIPLoader`
- `VAELoader`
- `NunchakuQwenImageLoraStack`
- `NunchakuQwenImageDiTLoader`
- `CR Prompt Text`
- `LoadImage`
- `TextEncodeQwenImageEditPlusPro_lrzjason`

## 关键参数

- `seed` = `49963367767054`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`ConditioningZeroOut`、`KSampler`、`SaveImage`、`VAEDecode`、`ImageConcanate`、`CLIPLoader`、`VAELoader`、`NunchakuQwenImageLoraStack`、`NunchakuQwenImageDiTLoader`、`CR Prompt Text`、`LoadImage`、`TextEncodeQwenImageEditPlusPro_lrzjason`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、ConditioningZeroOut、LoadImage、TextEncodeQwenImageEditPlusPro_lrzjason、NunchakuQwenImageLoraStack

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
