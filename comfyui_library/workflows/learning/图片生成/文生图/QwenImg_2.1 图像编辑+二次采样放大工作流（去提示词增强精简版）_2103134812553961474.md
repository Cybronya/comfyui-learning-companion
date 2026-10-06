---
key: 图片生成/文生图/QwenImg_2.1 图像编辑+二次采样放大工作流（去提示词增强精简版）_2103134812553961474.json
name: QwenImg_2.1 图像编辑+二次采样放大工作流（去提示词增强精简版）_2103134812553961474
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/QwenImg_2.1 图像编辑+二次采样放大工作流（去提示词增强精简版）_2103134812553961474.json
hash: ebb18e546136afaf
coverage: 0.645833
learned_at: 2026-10-07 02:30:40
nodes: [GetNode, QwenImage21Cache, GetImageSizeAndCount, easy cleanGpuUsed, easy clearCacheAll, ComfyMathExpression, GetNode, GetNode, GetNode, TextEncodeQwenImage21, EmptyLatentImage, PathchSageAttentionKJ, QwenImage21Cache, KSampler, GetNode, GetNode, UNETLoader, CLIPLoader, VAELoader, GetNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, KSampler, GetNode, ComfyMathExpression, TextEncodeQwenImage21, PathchSageAttentionKJ, SetNode, SetNode, SetNode, SetNode, Label (rgthree), LoadImage, LoadImage, EmptyLatentImage, VAEDecode, ResolutionSelector, Textbox, CLIPLoader, PreviewImage, VAEDecode, SaveImage, PrimitiveFloat]
patterns: []
missing: [Label (rgthree), easy cleanGpuUsed, easy clearCacheAll]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1051358414675475, "steps": 30, "width": 1024}
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/QwenImg_2.1 图像编辑+二次采样放大工作流（去提示词增强精简版）_2103134812553961474.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/QwenImg_2.1 图像编辑+二次采样放大工作流（去提示词增强精简版）_2103134812553961474.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `GetNode`
- `QwenImage21Cache`
- `GetImageSizeAndCount`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `PathchSageAttentionKJ`
- `QwenImage21Cache`
- `KSampler` ★核心
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `KSampler` ★核心
- `GetNode`
- `ComfyMathExpression`
- `TextEncodeQwenImage21`
- `PathchSageAttentionKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Label (rgthree)`
- `LoadImage`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `ResolutionSelector`
- `Textbox`
- `CLIPLoader`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `PrimitiveFloat`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1051358414675475`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **65%**（31/48）

**有卡**：`QwenImage21Cache`、`GetImageSizeAndCount`、`ComfyMathExpression`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`PathchSageAttentionKJ`、`KSampler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`VAEDecode`、`ResolutionSelector`、`Textbox`、`SaveImage`

**缺卡**（3）：`Label (rgthree)`、`easy cleanGpuUsed`、`easy clearCacheAll`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
