---
key: 平台全量/3d_hunyuan3d-v2.1_2014495028529336321.json
name: 3d_hunyuan3d-v2.1_2014495028529336321
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/3d_hunyuan3d-v2.1_2014495028529336321.json
hash: 2bf7b9a10553d928
coverage: 1
learned_at: 2026-11-14 00:12:26
nodes: [ImageOnlyCheckpointLoader, Hunyuan3Dv2Conditioning, ModelSamplingAuraFlow, VoxelToMesh, VAEDecodeHunyuan3D, KSampler, LoadImage, SaveImage, SaveGLB, CLIPVisionEncode, EmptyLatentHunyuan3Dv2]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 5, "checkpoint": "hunyuan_3d_v2.1.safetensors", "denoise": 1, "height": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 86148219532869, "steps": 30, "width": 4096}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 平台全量/3d_hunyuan3d-v2.1_2014495028529336321.json

> 来源文件 `comfyui_library/workflows/平台全量/3d_hunyuan3d-v2.1_2014495028529336321.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（11 个）：
- `ImageOnlyCheckpointLoader` ★核心
- `Hunyuan3Dv2Conditioning`
- `ModelSamplingAuraFlow`
- `VoxelToMesh`
- `VAEDecodeHunyuan3D` ★核心
- `KSampler` ★核心
- `LoadImage`
- `SaveImage`
- `SaveGLB`
- `CLIPVisionEncode`
- `EmptyLatentHunyuan3Dv2` ★核心

## 关键参数

- `checkpoint` = `hunyuan_3d_v2.1.safetensors`
- `seed` = `86148219532869`
- `steps` = `30`
- `cfg` = `5`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `width` = `4096`
- `height` = `1`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`ImageOnlyCheckpointLoader`、`Hunyuan3Dv2Conditioning`、`ModelSamplingAuraFlow`、`VoxelToMesh`、`VAEDecodeHunyuan3D`、`KSampler`、`LoadImage`、`SaveImage`、`SaveGLB`、`CLIPVisionEncode`、`EmptyLatentHunyuan3Dv2`

**用到的条目**：KSampler、LoadImage、CLIPVisionEncode、EmptyLatentHunyuan3Dv2、VAEDecodeHunyuan3D、ImageOnlyCheckpointLoader、Hunyuan3Dv2Conditioning、SaveImage

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
