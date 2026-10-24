---
key: 图片生成/图生图/Qwen-Edit-2509 Consistance Edit（图像一致性） workflow v4.0_1989864091101614081.json
name: Qwen-Edit-2509 Consistance Edit（图像一致性） workflow v4.0_1989864091101614081
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Edit-2509 Consistance Edit（图像一致性） workflow v4.0_1989864091101614081.json
hash: 211bcc2438ccb656
coverage: 0.8125
learned_at: 2026-10-23 11:15:23
nodes: [LoadImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, ConditioningZeroOut, LoraLoaderModelOnly, CLIPLoader, LoraLoaderModelOnly, UNETLoader, VAELoader, SaveImage, KSampler, LoadImage, VAEDecode, PreviewImage, easy imageConcat, Image Comparer (rgthree), PreviewImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "er_sde", "scheduler": "beta57", "seed": 810617380969503, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Edit-2509 Consistance Edit（图像一致性） workflow v4.0_1989864091101614081.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Edit-2509 Consistance Edit（图像一致性） workflow v4.0_1989864091101614081.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `LoadImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `SaveImage`
- `KSampler` ★核心
- `LoadImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `easy imageConcat`
- `Image Comparer (rgthree)`
- `PreviewImage`

## 关键参数

- `seed` = `810617380969503`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`LoadImage`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`ConditioningZeroOut`、`LoraLoaderModelOnly`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`SaveImage`、`KSampler`、`VAEDecode`、`easy imageConcat`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
