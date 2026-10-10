---
key: 视频生成/文生视频/Wan2.2smoothmix高动态文生视频V2_1979890524125564929.json
name: Wan2.2smoothmix高动态文生视频V2_1979890524125564929
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2smoothmix高动态文生视频V2_1979890524125564929.json
hash: d8ca762f894d5c16
coverage: 0.736842
learned_at: 2026-10-11 02:45:02
nodes: [CLIPLoader, VAELoader, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, UNETLoader, VAEDecode, VHS_VideoCombine, LayerUtility: PurgeVRAM V2, KSamplerAdvanced, KSamplerAdvanced, UNETLoader, EmptyHunyuanLatentVideo, ImageFromBatch+, VHS_VideoCombine, PrimitiveInt, PrimitiveInt, CR Text]
patterns: []
missing: [CR Text, ImageFromBatch+, LayerUtility: PurgeVRAM V2]
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1.1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Wan2.2smoothmix高动态文生视频V2_1979890524125564929.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2smoothmix高动态文生视频V2_1979890524125564929.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（19 个）：
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM V2`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `EmptyHunyuanLatentVideo`
- `ImageFromBatch+`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `PrimitiveInt`
- `CR Text`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1.1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **74%**（14/19）

**有卡**：`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`CLIPTextEncode`、`UNETLoader`、`VAEDecode`、`VHS_VideoCombine`、`KSamplerAdvanced`、`EmptyHunyuanLatentVideo`

**缺卡**（3）：`CR Text`、`ImageFromBatch+`、`LayerUtility: PurgeVRAM V2`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo、ModelSamplingSD3

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
