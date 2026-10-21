---
key: 图片生成/文生图/Red-Z image Distilled Base加速版文生图V1_2018000841084506113.json
name: Red-Z image Distilled Base加速版文生图V1_2018000841084506113
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Red-Z image Distilled Base加速版文生图V1_2018000841084506113.json
hash: 3d025c3825cac2cf
coverage: 0.785714
learned_at: 2026-10-19 22:15:19
nodes: [CLIPTextEncode, KSampler, VAELoader, PrimitiveNode, LayerUtility: PurgeVRAM, VAEDecode, CLIPTextEncode, PrimitiveInt, PrimitiveInt, EmptyLatentImage, CLIPLoader, UNETLoader, CR Prompt Text, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 952127631713820, "steps": 15, "width": 1080}
---

# 图片生成/文生图/Red-Z image Distilled Base加速版文生图V1_2018000841084506113.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Red-Z image Distilled Base加速版文生图V1_2018000841084506113.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAELoader`
- `PrimitiveNode`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `CR Prompt Text`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `952127631713820`
- `steps` = `15`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **79%**（11/14）

**有卡**：`CLIPTextEncode`、`KSampler`、`VAELoader`、`LayerUtility: PurgeVRAM`、`VAEDecode`、`EmptyLatentImage`、`CLIPLoader`、`UNETLoader`、`CR Prompt Text`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、CR Prompt Text
