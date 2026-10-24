---
key: 图片生成/图生图/Qwen edit-Rapid-v7.1 单人+多人智能编辑 低配置运行版_1984198272912867330.json
name: Qwen edit-Rapid-v7.1 单人+多人智能编辑 低配置运行版_1984198272912867330
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen edit-Rapid-v7.1 单人+多人智能编辑 低配置运行版_1984198272912867330.json
hash: 53b683d0b8dbb0eb
coverage: 0.954545
learned_at: 2026-10-23 11:13:51
nodes: [TextEncodeQwenImageEditPlus_lrzjason, ConditioningZeroOut, SaveImage, SaveImage, CFGNorm, ModelSamplingAuraFlow, ImageScaleToTotalPixels, LoadImage, LoadImage, LoadImage, LoadImage, ImageConcanate, KSampler, ImageConcatMulti, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecode, VAELoader, UnetLoaderGGUF, LoadImage, CLIPLoader, Note]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "lcm", "scheduler": "beta", "seed": 838667638205786, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen edit-Rapid-v7.1 单人+多人智能编辑 低配置运行版_1984198272912867330.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen edit-Rapid-v7.1 单人+多人智能编辑 低配置运行版_1984198272912867330.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `TextEncodeQwenImageEditPlus_lrzjason`
- `ConditioningZeroOut`
- `SaveImage`
- `SaveImage`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ImageConcanate`
- `KSampler` ★核心
- `ImageConcatMulti`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `LoadImage`
- `CLIPLoader`
- `Note`

## 关键参数

- `seed` = `838667638205786`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **95%**（21/22）

**有卡**：`TextEncodeQwenImageEditPlus_lrzjason`、`ConditioningZeroOut`、`SaveImage`、`CFGNorm`、`ModelSamplingAuraFlow`、`ImageScaleToTotalPixels`、`LoadImage`、`ImageConcanate`、`KSampler`、`ImageConcatMulti`、`LoraLoaderModelOnly`、`VAEDecode`、`VAELoader`、`UnetLoaderGGUF`、`CLIPLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
