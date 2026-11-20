---
key: 平台全量/图片评分过滤节点示例 image_reward_filter_example_1900560951572340737.json
name: 图片评分过滤节点示例 image_reward_filter_example_1900560951572340737
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/图片评分过滤节点示例 image_reward_filter_example_1900560951572340737.json
hash: 8db6b19cceeda774
coverage: 0.833333
learned_at: 2026-11-14 01:55:36
nodes: [CLIPTextEncode, KSampler, LayerUtility: ImageRewardFilter, VAEDecode, PreviewImage, CLIPTextEncode, DualCLIPLoader, VAELoader, EmptyLatentImage, UNETLoader, PreviewImage, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 9, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "normal", "seed": 45255951094504, "steps": 25, "width": 512}
---

# 平台全量/图片评分过滤节点示例 image_reward_filter_example_1900560951572340737.json

> 来源文件 `comfyui_library/workflows/平台全量/图片评分过滤节点示例 image_reward_filter_example_1900560951572340737.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output

**节点**（12 个）：
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `LayerUtility: ImageRewardFilter`
- `VAEDecode` ★核心
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `PreviewImage`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `45255951094504`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `9`

## 知识

覆盖率 **83%**（10/12）

**有卡**：`CLIPTextEncode`、`KSampler`、`LayerUtility: ImageRewardFilter`、`VAEDecode`、`DualCLIPLoader`、`VAELoader`、`EmptyLatentImage`、`UNETLoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、EmptyLatentImage、UNETLoader、SaveImage、DualCLIPLoader
