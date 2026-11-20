---
key: 平台全量/Sana_ 英伟达高效图像生成 Efficient High-Resolution_1873991929280286722.json
name: Sana_ 英伟达高效图像生成 Efficient High-Resolution_1873991929280286722
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Sana_ 英伟达高效图像生成 Efficient High-Resolution_1873991929280286722.json
hash: 75f38d1f75513258
coverage: 1
learned_at: 2026-11-14 00:56:55
nodes: [SanaTextEncode, VAEDecode, EmptySanaLatentImage, SanaResolutionSelect, SaveImage, SanaTextEncode, SanaCheckpointLoader, ExtraVAELoader, KSampler, GemmaLoader]
patterns: []
missing: []
parameters: {"cfg": 4, "checkpoint": "SanaMS_1600M_P1_D20", "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 20, "steps": 20}
---

# 平台全量/Sana_ 英伟达高效图像生成 Efficient High-Resolution_1873991929280286722.json

> 来源文件 `comfyui_library/workflows/平台全量/Sana_ 英伟达高效图像生成 Efficient High-Resolution_1873991929280286722.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（10 个）：
- `SanaTextEncode`
- `VAEDecode` ★核心
- `EmptySanaLatentImage`
- `SanaResolutionSelect`
- `SaveImage`
- `SanaTextEncode`
- `SanaCheckpointLoader` ★核心
- `ExtraVAELoader`
- `KSampler` ★核心
- `GemmaLoader`

## 关键参数

- `checkpoint` = `SanaMS_1600M_P1_D20`
- `seed` = `20`
- `steps` = `20`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`SanaTextEncode`、`VAEDecode`、`EmptySanaLatentImage`、`SanaResolutionSelect`、`SaveImage`、`SanaCheckpointLoader`、`ExtraVAELoader`、`KSampler`、`GemmaLoader`

**用到的条目**：KSampler、VAEDecode、EmptySanaLatentImage、ExtraVAELoader、SanaTextEncode、SanaCheckpointLoader、SanaResolutionSelect、SaveImage
