---
key: comfyui-workflow-templates-json/3d_hunyuan3d_image_to_model.json
name: 3d_hunyuan3d_image_to_model
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/3d_hunyuan3d_image_to_model.json
hash: 10908c83dc6964c5
official: true
coverage: 0.833333
learned_at: 2026-10-10 22:42:58
nodes: [KSampler, SaveGLB, VoxelToMesh, LoadImage, CLIPVisionEncode, EmptyLatentHunyuan3Dv2, ImageOnlyCheckpointLoader, ModelSamplingAuraFlow, Hunyuan3Dv2Conditioning, VAEDecodeHunyuan3D, MarkdownNote, MarkdownNote]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 8, "checkpoint": "hunyuan3d-dit-v2_fp16.safetensors", "denoise": 1, "height": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 242832339647017, "steps": 20, "width": 3072}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# comfyui-workflow-templates-json/3d_hunyuan3d_image_to_model.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/3d_hunyuan3d_image_to_model.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（12 个）：
- `KSampler` ★核心
- `SaveGLB`
- `VoxelToMesh`
- `LoadImage`
- `CLIPVisionEncode`
- `EmptyLatentHunyuan3Dv2` ★核心
- `ImageOnlyCheckpointLoader` ★核心
- `ModelSamplingAuraFlow`
- `Hunyuan3Dv2Conditioning`
- `VAEDecodeHunyuan3D` ★核心
- `MarkdownNote`
- `MarkdownNote`

## 关键参数

- `seed` = `242832339647017`
- `steps` = `20`
- `cfg` = `8`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `width` = `3072`
- `height` = `1`
- `checkpoint` = `hunyuan3d-dit-v2_fp16.safetensors`

## 知识

覆盖率 **83%**（10/12）

**有卡**：`KSampler`、`SaveGLB`、`VoxelToMesh`、`LoadImage`、`CLIPVisionEncode`、`EmptyLatentHunyuan3Dv2`、`ImageOnlyCheckpointLoader`、`ModelSamplingAuraFlow`、`Hunyuan3Dv2Conditioning`、`VAEDecodeHunyuan3D`

**用到的条目**：KSampler、LoadImage、CLIPVisionEncode、EmptyLatentHunyuan3Dv2、VAEDecodeHunyuan3D、ImageOnlyCheckpointLoader、Hunyuan3Dv2Conditioning、SaveGLB

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
