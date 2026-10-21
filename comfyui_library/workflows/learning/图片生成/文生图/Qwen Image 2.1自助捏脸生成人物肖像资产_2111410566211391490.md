---
key: 图片生成/文生图/Qwen Image 2.1自助捏脸生成人物肖像资产_2111410566211391490.json
name: Qwen Image 2.1自助捏脸生成人物肖像资产_2111410566211391490
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1自助捏脸生成人物肖像资产_2111410566211391490.json
hash: 147542b628c73e92
coverage: 0.789474
learned_at: 2026-10-21 02:54:14
nodes: [EmptyLatentImage, VAEDecode, ComfySwitchNode, QwenImage21Cache, KSampler, SaveImageAdvanced, TextEncodeQwenImage21, 孤海注释, QwenImage21_T2IPromptRewrite, easy showAnything, easy showAnything, easy cleanGpuUsed, SaveImage, UNETLoader, CLIPLoader, VAELoader, CLIPLoader, ResolutionSelector, FacialCustomization]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 742491479977912, "steps": 40, "width": 1024}
---

# 图片生成/文生图/Qwen Image 2.1自助捏脸生成人物肖像资产_2111410566211391490.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1自助捏脸生成人物肖像资产_2111410566211391490.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（19 个）：
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `KSampler` ★核心
- `SaveImageAdvanced`
- `TextEncodeQwenImage21`
- `孤海注释`
- `QwenImage21_T2IPromptRewrite`
- `easy showAnything`
- `easy showAnything`
- `easy cleanGpuUsed`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `ResolutionSelector`
- `FacialCustomization`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `742491479977912`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（15/19）

**有卡**：`EmptyLatentImage`、`VAEDecode`、`QwenImage21Cache`、`KSampler`、`SaveImageAdvanced`、`TextEncodeQwenImage21`、`QwenImage21_T2IPromptRewrite`、`easy cleanGpuUsed`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ResolutionSelector`、`FacialCustomization`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache
