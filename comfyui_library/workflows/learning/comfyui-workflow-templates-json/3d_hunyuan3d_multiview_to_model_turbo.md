---
key: comfyui-workflow-templates-json/3d_hunyuan3d_multiview_to_model_turbo.json
name: 3d_hunyuan3d_multiview_to_model_turbo
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/3d_hunyuan3d_multiview_to_model_turbo.json
hash: cce7786008b53d3c
official: true
coverage: 0.894737
learned_at: 2026-10-07 21:33:12
nodes: [CLIPVisionEncode, LoadImage, CLIPVisionEncode, LoadImage, LoadImage, CLIPVisionEncode, CLIPVisionEncode, FluxGuidance, EmptyLatentHunyuan3Dv2, Hunyuan3Dv2ConditioningMultiView, VAEDecodeHunyuan3D, VoxelToMesh, SaveGLB, LoadImage, KSampler, MarkdownNote, ModelSamplingAuraFlow, ImageOnlyCheckpointLoader, MarkdownNote]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 4, "checkpoint": "hunyuan3d-dit-v2-mv-turbo_fp16.safetensors", "denoise": 1, "height": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 528364197559477, "steps": 20, "width": 3072}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# comfyui-workflow-templates-json/3d_hunyuan3d_multiview_to_model_turbo.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/3d_hunyuan3d_multiview_to_model_turbo.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（19 个）：
- `CLIPVisionEncode`
- `LoadImage`
- `CLIPVisionEncode`
- `LoadImage`
- `LoadImage`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `FluxGuidance`
- `EmptyLatentHunyuan3Dv2` ★核心
- `Hunyuan3Dv2ConditioningMultiView`
- `VAEDecodeHunyuan3D` ★核心
- `VoxelToMesh`
- `SaveGLB`
- `LoadImage`
- `KSampler` ★核心
- `MarkdownNote`
- `ModelSamplingAuraFlow`
- `ImageOnlyCheckpointLoader` ★核心
- `MarkdownNote`

## 关键参数

- `width` = `3072`
- `height` = `1`
- `seed` = `528364197559477`
- `steps` = `20`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `checkpoint` = `hunyuan3d-dit-v2-mv-turbo_fp16.safetensors`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`CLIPVisionEncode`、`LoadImage`、`FluxGuidance`、`EmptyLatentHunyuan3Dv2`、`Hunyuan3Dv2ConditioningMultiView`、`VAEDecodeHunyuan3D`、`VoxelToMesh`、`SaveGLB`、`KSampler`、`ModelSamplingAuraFlow`、`ImageOnlyCheckpointLoader`

**用到的条目**：KSampler、LoadImage、FluxGuidance、CLIPVisionEncode、EmptyLatentHunyuan3Dv2、VAEDecodeHunyuan3D、ImageOnlyCheckpointLoader、Hunyuan3Dv2ConditioningMultiView

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
