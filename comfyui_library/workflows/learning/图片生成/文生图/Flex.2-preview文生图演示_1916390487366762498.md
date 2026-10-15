---
key: 图片生成/文生图/Flex.2-preview文生图演示_1916390487366762498.json
name: Flex.2-preview文生图演示_1916390487366762498
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flex.2-preview文生图演示_1916390487366762498.json
hash: 857a07bacf4fa0d7
coverage: 1
learned_at: 2026-10-15 22:26:21
nodes: [KSampler, VAEDecode, SaveImage, VAELoader, UNETLoader, DualCLIPLoader, Flex2Conditioner, CLIPTextEncode, CLIPTextEncode, CR SDXL Aspect Ratio]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "deis", "scheduler": "beta", "seed": 645445586904259, "steps": 25}
---

# 图片生成/文生图/Flex.2-preview文生图演示_1916390487366762498.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flex.2-preview文生图演示_1916390487366762498.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（10 个）：
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `VAELoader`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `Flex2Conditioner`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CR SDXL Aspect Ratio`

## 关键参数

- `seed` = `645445586904259`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `deis`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`KSampler`、`VAEDecode`、`SaveImage`、`VAELoader`、`UNETLoader`、`DualCLIPLoader`、`Flex2Conditioner`、`CLIPTextEncode`、`CR SDXL Aspect Ratio`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、DualCLIPLoader、CR SDXL Aspect Ratio、SaveImage
