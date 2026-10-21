---
key: 图片生成/图生图/Qwen Image2.1姿态编辑_2101935950074048514.json
name: Qwen Image2.1姿态编辑_2101935950074048514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image2.1姿态编辑_2101935950074048514.json
hash: 4876efd9deb4d9f7
coverage: 0.576923
learned_at: 2026-10-21 00:42:51
nodes: [Image Comparer (rgthree), OpenposePreprocessor, Note, Reroute, GetImageSize, NuiKr.OpenPoseEditor, ResolutionSelector, EmptyLatentImage, Reroute, GroupSwitcher, Reroute, PreviewImage, PreviewImage, Reroute, Reroute, SaveImage, PrimitiveStringMultiline, PrimitiveBoolean, UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, ComfySwitchNode, KSampler, VAEDecode, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 962693857590706, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen Image2.1姿态编辑_2101935950074048514.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image2.1姿态编辑_2101935950074048514.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `Image Comparer (rgthree)`
- `OpenposePreprocessor`
- `Note`
- `Reroute`
- `GetImageSize`
- `NuiKr.OpenPoseEditor`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `Reroute`
- `GroupSwitcher`
- `Reroute`
- `PreviewImage`
- `PreviewImage`
- `Reroute`
- `Reroute`
- `SaveImage`
- `PrimitiveStringMultiline`
- `PrimitiveBoolean`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `962693857590706`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **58%**（15/26）

**有卡**：`OpenposePreprocessor`、`GetImageSize`、`NuiKr.OpenPoseEditor`、`ResolutionSelector`、`EmptyLatentImage`、`GroupSwitcher`、`SaveImage`、`PrimitiveBoolean`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
