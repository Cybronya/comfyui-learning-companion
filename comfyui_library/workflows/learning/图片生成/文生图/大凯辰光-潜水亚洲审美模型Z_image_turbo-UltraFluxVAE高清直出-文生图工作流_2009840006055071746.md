---
key: 图片生成/文生图/大凯辰光-潜水亚洲审美模型Z_image_turbo-UltraFluxVAE高清直出-文生图工作流_2009840006055071746.json
name: 大凯辰光-潜水亚洲审美模型Z_image_turbo-UltraFluxVAE高清直出-文生图工作流_2009840006055071746
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/大凯辰光-潜水亚洲审美模型Z_image_turbo-UltraFluxVAE高清直出-文生图工作流_2009840006055071746.json
hash: 0e4534d439a30f78
coverage: 1
learned_at: 2026-10-19 22:01:32
nodes: [VAELoader, CLIPLoader, ModelSamplingAuraFlow, MemoryCleaner, KSampler, CLIPTextEncode, EmptySD3LatentImage, INTConstant, VAEDecode, SaveImage, CLIPTextEncode, UNETLoader, INTConstant, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 533349322711620, "steps": 10}
---

# 图片生成/文生图/大凯辰光-潜水亚洲审美模型Z_image_turbo-UltraFluxVAE高清直出-文生图工作流_2009840006055071746.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/大凯辰光-潜水亚洲审美模型Z_image_turbo-UltraFluxVAE高清直出-文生图工作流_2009840006055071746.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `VAELoader`
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `MemoryCleaner`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `INTConstant`
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `INTConstant`
- `LoadImage`

## 关键参数

- `seed` = `533349322711620`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`VAELoader`、`CLIPLoader`、`ModelSamplingAuraFlow`、`MemoryCleaner`、`KSampler`、`CLIPTextEncode`、`EmptySD3LatentImage`、`INTConstant`、`VAEDecode`、`SaveImage`、`UNETLoader`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、SaveImage
