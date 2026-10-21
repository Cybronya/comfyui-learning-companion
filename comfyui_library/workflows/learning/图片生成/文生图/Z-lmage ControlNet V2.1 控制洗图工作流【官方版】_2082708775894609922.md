---
key: 图片生成/文生图/Z-lmage ControlNet V2.1 控制洗图工作流【官方版】_2082708775894609922.json
name: Z-lmage ControlNet V2.1 控制洗图工作流【官方版】_2082708775894609922
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-lmage ControlNet V2.1 控制洗图工作流【官方版】_2082708775894609922.json
hash: 96be887b5dde485b
coverage: 1
learned_at: 2026-10-20 00:39:46
nodes: [ModelSamplingAuraFlow, QwenImageDiffsynthControlnet, EmptySD3LatentImage, ConditioningZeroOut, ModelPatchLoader, VAELoader, CLIPLoader, UNETLoader, VAEDecode, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, AIO_Preprocessor, LoadImage, KSampler, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 1016303453137347, "steps": 10}
---

# 图片生成/文生图/Z-lmage ControlNet V2.1 控制洗图工作流【官方版】_2082708775894609922.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-lmage ControlNet V2.1 控制洗图工作流【官方版】_2082708775894609922.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `ModelSamplingAuraFlow`
- `QwenImageDiffsynthControlnet`
- `EmptySD3LatentImage`
- `ConditioningZeroOut`
- `ModelPatchLoader`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `AIO_Preprocessor`
- `LoadImage`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `1016303453137347`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`ModelSamplingAuraFlow`、`QwenImageDiffsynthControlnet`、`EmptySD3LatentImage`、`ConditioningZeroOut`、`ModelPatchLoader`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`VAEDecode`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`AIO_Preprocessor`、`LoadImage`、`KSampler`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader
