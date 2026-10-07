---
key: comfyui-workflow-templates-json/3d_hunyuan3d_multiview_to_model.json
name: 3d_hunyuan3d_multiview_to_model
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/3d_hunyuan3d_multiview_to_model.json
hash: 6daa56ca1aa06529
official: true
coverage: 0.888889
learned_at: 2026-10-07 21:33:11
nodes: [VAEDecodeHunyuan3D, VoxelToMesh, SaveGLB, KSampler, CLIPVisionEncode, LoadImage, CLIPVisionEncode, LoadImage, CLIPVisionEncode, CLIPVisionEncode, LoadImage, LoadImage, Hunyuan3Dv2ConditioningMultiView, EmptyLatentHunyuan3Dv2, MarkdownNote, ModelSamplingAuraFlow, ImageOnlyCheckpointLoader, MarkdownNote]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 7.5, "checkpoint": "hunyuan3d-dit-v2-mv_fp16.safetensors", "denoise": 1, "height": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 502126049100058, "steps": 20, "width": 3072}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# comfyui-workflow-templates-json/3d_hunyuan3d_multiview_to_model.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/3d_hunyuan3d_multiview_to_model.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（18 个）：
- `VAEDecodeHunyuan3D` ★核心
- `VoxelToMesh`
- `SaveGLB`
- `KSampler` ★核心
- `CLIPVisionEncode`
- `LoadImage`
- `CLIPVisionEncode`
- `LoadImage`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `LoadImage`
- `LoadImage`
- `Hunyuan3Dv2ConditioningMultiView`
- `EmptyLatentHunyuan3Dv2` ★核心
- `MarkdownNote`
- `ModelSamplingAuraFlow`
- `ImageOnlyCheckpointLoader` ★核心
- `MarkdownNote`

## 关键参数

- `seed` = `502126049100058`
- `steps` = `20`
- `cfg` = `7.5`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `width` = `3072`
- `height` = `1`
- `checkpoint` = `hunyuan3d-dit-v2-mv_fp16.safetensors`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`VAEDecodeHunyuan3D`、`VoxelToMesh`、`SaveGLB`、`KSampler`、`CLIPVisionEncode`、`LoadImage`、`Hunyuan3Dv2ConditioningMultiView`、`EmptyLatentHunyuan3Dv2`、`ModelSamplingAuraFlow`、`ImageOnlyCheckpointLoader`

**用到的条目**：KSampler、LoadImage、CLIPVisionEncode、EmptyLatentHunyuan3Dv2、VAEDecodeHunyuan3D、ImageOnlyCheckpointLoader、Hunyuan3Dv2ConditioningMultiView、SaveGLB

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
