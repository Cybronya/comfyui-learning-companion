---
key: 图片生成/文生图/造相ControlNet2.0局部重绘_2000809405283266562.json
name: 造相ControlNet2.0局部重绘_2000809405283266562
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/造相ControlNet2.0局部重绘_2000809405283266562.json
hash: f90f82a9140a91f1
coverage: 0.904762
learned_at: 2026-10-19 21:47:52
nodes: [CLIPLoader, Note, MarkdownNote, KSampler, UNETLoader, QwenImageDiffsynthControlnet, ModelSamplingAuraFlow, VAEDecode, ModelPatchLoader, ImageLoader, VAELoader, CLIPTextEncode, ConditioningZeroOut, VAEEncode, SetLatentNoiseMask, GrowMaskWithBlur, String Literal, ImageResizeKJv2, AIO_Preprocessor, SaveImage, Seed (rgthree), CLIPLoader, Note, MarkdownNote, KSampler, UNETLoader, QwenImageDiffsynthControlnet, ModelSamplingAuraFlow, VAEDecode, VAELoader, CLIPTextEncode, ConditioningZeroOut, VAEEncode, SetLatentNoiseMask, Seed (rgthree), AIO_Preprocessor, String Literal, SaveImage, ImageLoader, GrowMaskWithBlur, ModelPatchLoader, ImageResizeKJv2]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 687074114277629, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/造相ControlNet2.0局部重绘_2000809405283266562.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/造相ControlNet2.0局部重绘_2000809405283266562.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `CLIPLoader`
- `Note`
- `MarkdownNote`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `QwenImageDiffsynthControlnet`
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `ModelPatchLoader`
- `ImageLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `SetLatentNoiseMask`
- `GrowMaskWithBlur`
- `String Literal`
- `ImageResizeKJv2`
- `AIO_Preprocessor`
- `SaveImage`
- `Seed (rgthree)`
- `CLIPLoader`
- `Note`
- `MarkdownNote`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `QwenImageDiffsynthControlnet`
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `SetLatentNoiseMask`
- `Seed (rgthree)`
- `AIO_Preprocessor`
- `String Literal`
- `SaveImage`
- `ImageLoader`
- `GrowMaskWithBlur`
- `ModelPatchLoader`
- `ImageResizeKJv2`

## 关键参数

- `seed` = `687074114277629`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（38/42）

**有卡**：`CLIPLoader`、`KSampler`、`UNETLoader`、`QwenImageDiffsynthControlnet`、`ModelSamplingAuraFlow`、`VAEDecode`、`ModelPatchLoader`、`ImageLoader`、`VAELoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`VAEEncode`、`SetLatentNoiseMask`、`GrowMaskWithBlur`、`String Literal`、`ImageResizeKJv2`、`AIO_Preprocessor`、`SaveImage`、`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、UNETLoader、QwenImageDiffsynthControlnet

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
