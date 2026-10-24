---
key: 图片生成/图生图/Wan2.2_图像精修放大修复增加写实质感-人物无改变_1982643467203551233.json
name: Wan2.2_图像精修放大修复增加写实质感-人物无改变_1982643467203551233
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2_图像精修放大修复增加写实质感-人物无改变_1982643467203551233.json
hash: a1df882318e5e028
coverage: 0.875
learned_at: 2026-10-23 11:28:11
nodes: [LayerUtility: PurgeVRAM V2, workflow>Wan2, KSampler, workflow>IMGVE, SaveImage, Image Comparer (rgthree), RHHiddenNodes, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 0.030000000000000006, "sampler_name": "euler", "scheduler": "simple", "seed": 701988752861408, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 图片生成/图生图/Wan2.2_图像精修放大修复增加写实质感-人物无改变_1982643467203551233.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2_图像精修放大修复增加写实质感-人物无改变_1982643467203551233.json`

## 结构

**生成流程**：Sampling → Output → Other

**节点**（8 个）：
- `LayerUtility: PurgeVRAM V2`
- `workflow>Wan2`
- `KSampler` ★核心
- `workflow>IMGVE`
- `SaveImage`
- `Image Comparer (rgthree)`
- `RHHiddenNodes`
- `LoadImage`

## 关键参数

- `seed` = `701988752861408`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.030000000000000006`

## 知识

覆盖率 **88%**（7/8）

**有卡**：`LayerUtility: PurgeVRAM V2`、`workflow>Wan2`、`KSampler`、`workflow>IMGVE`、`SaveImage`、`RHHiddenNodes`、`LoadImage`

**用到的条目**：KSampler、LoadImage、SaveImage、RHHiddenNodes、LayerUtility: PurgeVRAM V2、workflow>IMGVE、workflow>Wan2、sd15-t2i-basic

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
