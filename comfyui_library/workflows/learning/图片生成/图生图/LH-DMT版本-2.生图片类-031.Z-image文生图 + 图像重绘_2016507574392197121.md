---
key: 图片生成/图生图/LH-DMT版本-2.生图片类-031.Z-image文生图 + 图像重绘_2016507574392197121.json
name: LH-DMT版本-2.生图片类-031.Z-image文生图 + 图像重绘_2016507574392197121
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/LH-DMT版本-2.生图片类-031.Z-image文生图 + 图像重绘_2016507574392197121.json
hash: 4f1cee2e581b52b8
coverage: 0.904762
learned_at: 2026-10-23 11:08:40
nodes: [UNETLoader, CLIPLoader, VAELoader, VAEDecode, SaveImage, KSampler, SaveImage, Note, ConditioningZeroOut, CLIPLoader, VAEDecode, ConditioningZeroOut, VAEEncode, UNETLoader, EmptyLatentImage, CLIPTextEncode, CLIPTextEncode, Fast Groups Muter (rgthree), KSampler, LoadImage, VAELoader]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.7, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 295004316667857, "steps": 10, "width": 720}
---

# 图片生成/图生图/LH-DMT版本-2.生图片类-031.Z-image文生图 + 图像重绘_2016507574392197121.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/LH-DMT版本-2.生图片类-031.Z-image文生图 + 图像重绘_2016507574392197121.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（21 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `SaveImage`
- `Note`
- `ConditioningZeroOut`
- `CLIPLoader`
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Fast Groups Muter (rgthree)`
- `KSampler` ★核心
- `LoadImage`
- `VAELoader`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `295004316667857`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.7`
- `width` = `720`
- `height` = `1280`
- `batch_size` = `1`

## 知识

覆盖率 **90%**（19/21）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`SaveImage`、`KSampler`、`ConditioningZeroOut`、`VAEEncode`、`EmptyLatentImage`、`CLIPTextEncode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage
