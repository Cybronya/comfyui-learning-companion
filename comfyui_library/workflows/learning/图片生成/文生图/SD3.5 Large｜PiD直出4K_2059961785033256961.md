---
key: 图片生成/文生图/SD3.5 Large｜PiD直出4K_2059961785033256961.json
name: SD3.5 Large｜PiD直出4K_2059961785033256961
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/SD3.5 Large｜PiD直出4K_2059961785033256961.json
hash: 36d6a48b5808024f
coverage: 0.923077
learned_at: 2026-10-19 23:02:46
nodes: [CheckpointLoaderSimple, CLIPTextEncode, CLIPTextEncode, EmptySD3LatentImage, PiDPrepare, PiDSample, PiDFinalize, SaveImage, Note, PiDTextPrompt, SaveImage, PiDKSamplerCapture, VAEDecode]
patterns: []
missing: []
parameters: {"cfg": 4.4, "checkpoint": "sd3.5_large_fp8_scaled.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 191166039668422, "steps": 25}
---

# 图片生成/文生图/SD3.5 Large｜PiD直出4K_2059961785033256961.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/SD3.5 Large｜PiD直出4K_2059961785033256961.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `PiDPrepare`
- `PiDSample`
- `PiDFinalize`
- `SaveImage`
- `Note`
- `PiDTextPrompt`
- `SaveImage`
- `PiDKSamplerCapture` ★核心
- `VAEDecode` ★核心

## 关键参数

- `checkpoint` = `sd3.5_large_fp8_scaled.safetensors`
- `seed` = `191166039668422`
- `steps` = `25`
- `cfg` = `4.4`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`CheckpointLoaderSimple`、`CLIPTextEncode`、`EmptySD3LatentImage`、`PiDPrepare`、`PiDSample`、`PiDFinalize`、`SaveImage`、`PiDTextPrompt`、`PiDKSamplerCapture`、`VAEDecode`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、PiDKSamplerCapture、PiDTextPrompt、SaveImage、EmptySD3LatentImage、PiDFinalize
