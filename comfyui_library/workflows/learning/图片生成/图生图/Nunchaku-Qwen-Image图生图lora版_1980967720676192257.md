---
key: 图片生成/图生图/Nunchaku-Qwen-Image图生图lora版_1980967720676192257.json
name: Nunchaku-Qwen-Image图生图lora版_1980967720676192257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Nunchaku-Qwen-Image图生图lora版_1980967720676192257.json
hash: f292072949cefa1b
coverage: 0.866667
learned_at: 2026-10-23 11:10:00
nodes: [CLIPTextEncode, ConditioningZeroOut, SDXLEmptyLatentSizePicker+, VAEDecode, SaveImage, RH_Captioner, NunchakuQwenImageLoraLoader, CLIPLoader, VAELoader, KSampler, NunchakuQwenImageLoraStack, PreviewAny, LoadImage, NunchakuQwenImageDiTLoader, PreviewImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 0, "cfg": 1, "denoise": 1, "height": 1, "sampler_name": "euler", "scheduler": "kl_optimal", "seed": 410729605062063, "steps": 8, "width": "1024x1024 (1.0)"}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Nunchaku-Qwen-Image图生图lora版_1980967720676192257.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Nunchaku-Qwen-Image图生图lora版_1980967720676192257.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `SDXLEmptyLatentSizePicker+` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `RH_Captioner`
- `NunchakuQwenImageLoraLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `NunchakuQwenImageLoraStack`
- `PreviewAny`
- `LoadImage`
- `NunchakuQwenImageDiTLoader`
- `PreviewImage`

## 关键参数

- `width` = `1024x1024 (1.0)`
- `height` = `1`
- `batch_size` = `0`
- `seed` = `410729605062063`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `kl_optimal`
- `denoise` = `1`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`CLIPTextEncode`、`ConditioningZeroOut`、`SDXLEmptyLatentSizePicker+`、`VAEDecode`、`SaveImage`、`RH_Captioner`、`NunchakuQwenImageLoraLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`NunchakuQwenImageLoraStack`、`LoadImage`、`NunchakuQwenImageDiTLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、SDXLEmptyLatentSizePicker+

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
