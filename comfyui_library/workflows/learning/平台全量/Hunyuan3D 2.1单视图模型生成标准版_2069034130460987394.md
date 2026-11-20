---
key: 平台全量/Hunyuan3D 2.1单视图模型生成标准版_2069034130460987394.json
name: Hunyuan3D 2.1单视图模型生成标准版_2069034130460987394
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Hunyuan3D 2.1单视图模型生成标准版_2069034130460987394.json
hash: cecf3e370704769d
coverage: 0.923077
learned_at: 2026-11-14 00:32:08
nodes: [MarkdownNote, Hunyuan3Dv2Conditioning, CLIPVisionEncode, ModelSamplingAuraFlow, ImageOnlyCheckpointLoader, KSampler, EmptyLatentHunyuan3Dv2, VAEDecodeHunyuan3D, SaveGLB, VoxelToMesh, SaveImage, EmptyImage, LoadImage]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 5, "checkpoint": "hunyuan_3d_v2.1.safetensors", "denoise": 1, "height": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 1032480068818063, "steps": 50, "width": 8192}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 平台全量/Hunyuan3D 2.1单视图模型生成标准版_2069034130460987394.json

> 来源文件 `comfyui_library/workflows/平台全量/Hunyuan3D 2.1单视图模型生成标准版_2069034130460987394.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `MarkdownNote`
- `Hunyuan3Dv2Conditioning`
- `CLIPVisionEncode`
- `ModelSamplingAuraFlow`
- `ImageOnlyCheckpointLoader` ★核心
- `KSampler` ★核心
- `EmptyLatentHunyuan3Dv2` ★核心
- `VAEDecodeHunyuan3D` ★核心
- `SaveGLB`
- `VoxelToMesh`
- `SaveImage`
- `EmptyImage`
- `LoadImage`

## 关键参数

- `checkpoint` = `hunyuan_3d_v2.1.safetensors`
- `seed` = `1032480068818063`
- `steps` = `50`
- `cfg` = `5`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `width` = `8192`
- `height` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`Hunyuan3Dv2Conditioning`、`CLIPVisionEncode`、`ModelSamplingAuraFlow`、`ImageOnlyCheckpointLoader`、`KSampler`、`EmptyLatentHunyuan3Dv2`、`VAEDecodeHunyuan3D`、`SaveGLB`、`VoxelToMesh`、`SaveImage`、`EmptyImage`、`LoadImage`

**用到的条目**：KSampler、LoadImage、CLIPVisionEncode、EmptyLatentHunyuan3Dv2、VAEDecodeHunyuan3D、ImageOnlyCheckpointLoader、Hunyuan3Dv2Conditioning、SaveImage

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
