---
key: 图片生成/文生图/Z image的Controlnet的openpose_1995081250421583873.json
name: Z image的Controlnet的openpose_1995081250421583873
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z image的Controlnet的openpose_1995081250421583873.json
hash: 05975085b85c3278
coverage: 1
learned_at: 2026-10-19 21:32:47
nodes: [CR SDXL Aspect Ratio, KSampler, VAEDecode, ConditioningZeroOut, CLIPLoader, ModelPatchLoader, UNETLoader, ModelSamplingAuraFlow, VAELoader, QwenImageDiffsynthControlnet, OpenposePreprocessor, LoadImage, EmptyLatentImage, SaveImage, CLIPTextEncode]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1036914790101191, "steps": 10, "width": 1024}
---

# 图片生成/文生图/Z image的Controlnet的openpose_1995081250421583873.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z image的Controlnet的openpose_1995081250421583873.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（15 个）：
- `CR SDXL Aspect Ratio`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `CLIPLoader`
- `ModelPatchLoader`
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `VAELoader`
- `QwenImageDiffsynthControlnet`
- `OpenposePreprocessor`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `1036914790101191`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`CR SDXL Aspect Ratio`、`KSampler`、`VAEDecode`、`ConditioningZeroOut`、`CLIPLoader`、`ModelPatchLoader`、`UNETLoader`、`ModelSamplingAuraFlow`、`VAELoader`、`QwenImageDiffsynthControlnet`、`OpenposePreprocessor`、`LoadImage`、`EmptyLatentImage`、`SaveImage`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
