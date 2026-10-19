---
key: 图片生成/文生图/Dark Beast Z 黑兽 V2.5_2009627862525026305.json
name: Dark Beast Z 黑兽 V2.5_2009627862525026305
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Dark Beast Z 黑兽 V2.5_2009627862525026305.json
hash: 4ce073b764aeeeec
coverage: 1
learned_at: 2026-10-19 22:00:28
nodes: [JWInteger, SaveImage, VAEDecode, EmptySD3LatentImage, JWInteger, CLIPTextEncode, VAELoader, CLIPLoader, UNETLoader, KSampler, CLIPTextEncode, CR Prompt Text, CR Prompt Text]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 710564933618468, "steps": 10}
---

# 图片生成/文生图/Dark Beast Z 黑兽 V2.5_2009627862525026305.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Dark Beast Z 黑兽 V2.5_2009627862525026305.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `JWInteger`
- `SaveImage`
- `VAEDecode` ★核心
- `EmptySD3LatentImage`
- `JWInteger`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CR Prompt Text`
- `CR Prompt Text`

## 关键参数

- `seed` = `710564933618468`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`JWInteger`、`SaveImage`、`VAEDecode`、`EmptySD3LatentImage`、`CLIPTextEncode`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`KSampler`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、CR Prompt Text、SaveImage
