---
key: 图片生成/图生图/（（自用）-Lora支持版）Nunchaku Qwen Edit超级加速图像编辑（换装前置）_1982339249020256257.json
name: （（自用）-Lora支持版）Nunchaku Qwen Edit超级加速图像编辑（换装前置）_1982339249020256257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/（（自用）-Lora支持版）Nunchaku Qwen Edit超级加速图像编辑（换装前置）_1982339249020256257.json
hash: f27ba8af76ab90f9
coverage: 0.9375
learned_at: 2026-10-23 13:38:39
nodes: [ConditioningZeroOut, KSampler, CLIPLoader, VAELoader, NunchakuQwenImageDiTLoader, LoadImage, TextEncodeQwenImageEditPlusPro_lrzjason, CR Prompt Text, NunchakuQwenImageLoraStack, VAEDecode, CR Prompt Text, TT_img_enc, SaveImage, TT_img_enc_v2, SaveImage, Note]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 883681687924058, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/（（自用）-Lora支持版）Nunchaku Qwen Edit超级加速图像编辑（换装前置）_1982339249020256257.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/（（自用）-Lora支持版）Nunchaku Qwen Edit超级加速图像编辑（换装前置）_1982339249020256257.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `ConditioningZeroOut`
- `KSampler` ★核心
- `CLIPLoader`
- `VAELoader`
- `NunchakuQwenImageDiTLoader`
- `LoadImage`
- `TextEncodeQwenImageEditPlusPro_lrzjason`
- `CR Prompt Text`
- `NunchakuQwenImageLoraStack`
- `VAEDecode` ★核心
- `CR Prompt Text`
- `TT_img_enc`
- `SaveImage`
- `TT_img_enc_v2`
- `SaveImage`
- `Note`

## 关键参数

- `seed` = `883681687924058`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`ConditioningZeroOut`、`KSampler`、`CLIPLoader`、`VAELoader`、`NunchakuQwenImageDiTLoader`、`LoadImage`、`TextEncodeQwenImageEditPlusPro_lrzjason`、`CR Prompt Text`、`NunchakuQwenImageLoraStack`、`VAEDecode`、`TT_img_enc`、`SaveImage`、`TT_img_enc_v2`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、ConditioningZeroOut、LoadImage、TextEncodeQwenImageEditPlusPro_lrzjason、NunchakuQwenImageLoraStack

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
