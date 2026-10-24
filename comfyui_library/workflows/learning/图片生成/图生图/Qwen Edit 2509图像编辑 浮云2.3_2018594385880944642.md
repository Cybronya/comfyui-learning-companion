---
key: 图片生成/图生图/Qwen Edit 2509图像编辑 浮云2.3_2018594385880944642.json
name: Qwen Edit 2509图像编辑 浮云2.3_2018594385880944642
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Edit 2509图像编辑 浮云2.3_2018594385880944642.json
hash: 926c7307a7fb138e
coverage: 0.954545
learned_at: 2026-10-23 11:11:53
nodes: [VAELoader, ConditioningZeroOut, QwenEditOutputExtractor, UNETLoader, LoraLoaderModelOnly, VAEDecode, QwenEditAdaptiveLongestEdge, SaveImage, SaveImage, SaveImage, QwenEditConfigPreparer, CLIPLoader, ImageScaleBy, KSampler, CropWithPadInfo, ImpactSwitch, TextEncodeQwenImageEditPlusCustom_lrzjason, SaveImage, LoadImage, EmptyLatentImage, FluxResolutionNode, CR Prompt Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "beta57", "seed": 1091359629774735, "steps": 8, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Edit 2509图像编辑 浮云2.3_2018594385880944642.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Edit 2509图像编辑 浮云2.3_2018594385880944642.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `VAELoader`
- `ConditioningZeroOut`
- `QwenEditOutputExtractor`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `QwenEditAdaptiveLongestEdge`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `QwenEditConfigPreparer`
- `CLIPLoader`
- `ImageScaleBy`
- `KSampler` ★核心
- `CropWithPadInfo`
- `ImpactSwitch`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `SaveImage`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `FluxResolutionNode`
- `CR Prompt Text`

## 关键参数

- `seed` = `1091359629774735`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（21/22）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`QwenEditOutputExtractor`、`UNETLoader`、`LoraLoaderModelOnly`、`VAEDecode`、`QwenEditAdaptiveLongestEdge`、`SaveImage`、`QwenEditConfigPreparer`、`CLIPLoader`、`ImageScaleBy`、`KSampler`、`CropWithPadInfo`、`TextEncodeQwenImageEditPlusCustom_lrzjason`、`LoadImage`、`EmptyLatentImage`、`FluxResolutionNode`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
