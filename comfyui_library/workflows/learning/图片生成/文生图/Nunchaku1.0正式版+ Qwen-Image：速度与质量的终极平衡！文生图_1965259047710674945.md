---
key: 图片生成/文生图/Nunchaku1.0正式版+ Qwen-Image：速度与质量的终极平衡！文生图_1965259047710674945.json
name: Nunchaku1.0正式版+ Qwen-Image：速度与质量的终极平衡！文生图_1965259047710674945
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Nunchaku1.0正式版+ Qwen-Image：速度与质量的终极平衡！文生图_1965259047710674945.json
hash: 0d41439ab8859c46
coverage: 1
learned_at: 2026-10-10 20:58:48
nodes: [CLIPLoader, VAELoader, CLIPTextEncode, ModelSamplingAuraFlow, KSampler, VAEDecode, NunchakuQwenImageDiTLoader, SaveImage, CLIPTextEncode, Text, EmptySD3LatentImage]
patterns: []
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1030870340626888, "steps": 30}
---

# 图片生成/文生图/Nunchaku1.0正式版+ Qwen-Image：速度与质量的终极平衡！文生图_1965259047710674945.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Nunchaku1.0正式版+ Qwen-Image：速度与质量的终极平衡！文生图_1965259047710674945.json`

## 结构

**节点**（11 个）：
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode`
- `ModelSamplingAuraFlow`
- `KSampler`
- `VAEDecode`
- `NunchakuQwenImageDiTLoader`
- `SaveImage`
- `CLIPTextEncode`
- `Text`
- `EmptySD3LatentImage`

## 关键参数

- `cfg` = `2.5`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `1030870340626888`
- `steps` = `30`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ModelSamplingAuraFlow`、`KSampler`、`VAEDecode`、`NunchakuQwenImageDiTLoader`、`SaveImage`、`Text`、`EmptySD3LatentImage`
