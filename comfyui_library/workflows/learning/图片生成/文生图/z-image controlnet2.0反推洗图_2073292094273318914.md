---
key: 图片生成/文生图/z-image controlnet2.0反推洗图_2073292094273318914.json
name: z-image controlnet2.0反推洗图_2073292094273318914
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/z-image controlnet2.0反推洗图_2073292094273318914.json
hash: fc39830beaf14291
coverage: 0.833333
learned_at: 2026-10-20 00:02:08
nodes: [UNETLoader, ConditioningZeroOut, EmptySD3LatentImage, CLIPLoader, CLIPTextEncode, ModelPatchLoader, QwenImageDiffsynthControlnet, LoadImage, AIO_Preprocessor, GetImageSize, SeedVR2ExtraArgs, easy cleanGpuUsed, SeedVR2, KSampler, VAEDecode, ModelSamplingAuraFlow, Note, Note, RH_Captioner, Note, PreviewImage, SaveImage, VAELoader, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 326943942401040, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/z-image controlnet2.0反推洗图_2073292094273318914.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/z-image controlnet2.0反推洗图_2073292094273318914.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ModelPatchLoader`
- `QwenImageDiffsynthControlnet`
- `LoadImage`
- `AIO_Preprocessor`
- `GetImageSize`
- `SeedVR2ExtraArgs`
- `easy cleanGpuUsed`
- `SeedVR2`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ModelSamplingAuraFlow`
- `Note`
- `Note`
- `RH_Captioner`
- `Note`
- `PreviewImage`
- `SaveImage`
- `VAELoader`
- `SaveImage`

## 关键参数

- `seed` = `326943942401040`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（20/24）

**有卡**：`UNETLoader`、`ConditioningZeroOut`、`EmptySD3LatentImage`、`CLIPLoader`、`CLIPTextEncode`、`ModelPatchLoader`、`QwenImageDiffsynthControlnet`、`LoadImage`、`AIO_Preprocessor`、`GetImageSize`、`SeedVR2ExtraArgs`、`easy cleanGpuUsed`、`SeedVR2`、`KSampler`、`VAEDecode`、`ModelSamplingAuraFlow`、`RH_Captioner`、`SaveImage`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
