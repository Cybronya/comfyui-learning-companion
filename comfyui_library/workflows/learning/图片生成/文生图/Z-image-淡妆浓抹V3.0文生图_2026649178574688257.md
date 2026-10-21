---
key: 图片生成/文生图/Z-image-淡妆浓抹V3.0文生图_2026649178574688257.json
name: Z-image-淡妆浓抹V3.0文生图_2026649178574688257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image-淡妆浓抹V3.0文生图_2026649178574688257.json
hash: 85760728a4670186
coverage: 1
learned_at: 2026-10-19 22:30:05
nodes: [CLIPLoader, VAELoader, ConditioningZeroOut, UNETLoader, ModelSamplingAuraFlow, EmptySD3LatentImage, SaveImage, CLIPTextEncode, VAEDecode, LayerUtility: PurgeVRAM V2, KSampler]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 46663935436376, "steps": 15}
---

# 图片生成/文生图/Z-image-淡妆浓抹V3.0文生图_2026649178574688257.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image-淡妆浓抹V3.0文生图_2026649178574688257.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（11 个）：
- `CLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `EmptySD3LatentImage`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `KSampler` ★核心

## 关键参数

- `seed` = `46663935436376`
- `steps` = `15`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`CLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`UNETLoader`、`ModelSamplingAuraFlow`、`EmptySD3LatentImage`、`SaveImage`、`CLIPTextEncode`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、UNETLoader、SaveImage
