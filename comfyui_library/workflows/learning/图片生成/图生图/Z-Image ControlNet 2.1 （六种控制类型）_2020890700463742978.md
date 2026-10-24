---
key: 图片生成/图生图/Z-Image ControlNet 2.1 （六种控制类型）_2020890700463742978.json
name: Z-Image ControlNet 2.1 （六种控制类型）_2020890700463742978
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-Image ControlNet 2.1 （六种控制类型）_2020890700463742978.json
hash: e62961d746bdb49c
coverage: 0.954545
learned_at: 2026-10-23 11:29:18
nodes: [VAEDecode, AIO_Preprocessor, AIO_Preprocessor, AIO_Preprocessor, AIO_Preprocessor, AIO_Preprocessor, AIO_Preprocessor, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, ModelSamplingAuraFlow, ConditioningZeroOut, CLIPLoader, VAELoader, CLIPTextEncode, KSampler, EmptySD3LatentImage, UNETLoader, AIO_Preprocessor, QwenImageDiffsynthControlnet, ModelPatchLoader, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 192912803585991, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Z-Image ControlNet 2.1 （六种控制类型）_2020890700463742978.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-Image ControlNet 2.1 （六种控制类型）_2020890700463742978.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `VAEDecode` ★核心
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `ModelSamplingAuraFlow`
- `ConditioningZeroOut`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `EmptySD3LatentImage`
- `UNETLoader` ★核心
- `AIO_Preprocessor`
- `QwenImageDiffsynthControlnet`
- `ModelPatchLoader`
- `LoadImage`

## 关键参数

- `seed` = `192912803585991`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（21/22）

**有卡**：`VAEDecode`、`AIO_Preprocessor`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`ModelSamplingAuraFlow`、`ConditioningZeroOut`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`KSampler`、`EmptySD3LatentImage`、`UNETLoader`、`QwenImageDiffsynthControlnet`、`ModelPatchLoader`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
