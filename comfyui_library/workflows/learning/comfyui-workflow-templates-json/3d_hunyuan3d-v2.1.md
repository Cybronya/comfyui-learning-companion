---
key: comfyui-workflow-templates-json/3d_hunyuan3d-v2.1.json
name: 3d_hunyuan3d-v2.1
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/3d_hunyuan3d-v2.1.json
hash: 150c7ee7870f466b
official: true
coverage: 0.909091
learned_at: 2026-10-10 22:42:54
nodes: [ImageOnlyCheckpointLoader, LoadImage, ModelSamplingAuraFlow, KSampler, SaveGLB, VAEDecodeHunyuan3D, VoxelToMesh, CLIPVisionEncode, Hunyuan3Dv2Conditioning, EmptyLatentHunyuan3Dv2, MarkdownNote]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 5, "checkpoint": "hunyuan_3d_v2.1.safetensors", "denoise": 1, "height": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 952805179515179, "steps": 30, "width": 4096}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# comfyui-workflow-templates-json/3d_hunyuan3d-v2.1.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/3d_hunyuan3d-v2.1.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（11 个）：
- `ImageOnlyCheckpointLoader` ★核心
- `LoadImage`
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `SaveGLB`
- `VAEDecodeHunyuan3D` ★核心
- `VoxelToMesh`
- `CLIPVisionEncode`
- `Hunyuan3Dv2Conditioning`
- `EmptyLatentHunyuan3Dv2` ★核心
- `MarkdownNote`

## 关键参数

- `checkpoint` = `hunyuan_3d_v2.1.safetensors`
- `seed` = `952805179515179`
- `steps` = `30`
- `cfg` = `5`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `width` = `4096`
- `height` = `1`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`ImageOnlyCheckpointLoader`、`LoadImage`、`ModelSamplingAuraFlow`、`KSampler`、`SaveGLB`、`VAEDecodeHunyuan3D`、`VoxelToMesh`、`CLIPVisionEncode`、`Hunyuan3Dv2Conditioning`、`EmptyLatentHunyuan3Dv2`

**用到的条目**：KSampler、LoadImage、CLIPVisionEncode、EmptyLatentHunyuan3Dv2、VAEDecodeHunyuan3D、ImageOnlyCheckpointLoader、Hunyuan3Dv2Conditioning、SaveGLB

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
