---
key: 视频生成/文生视频/Qwen3 VL视频反推+Wan2.2 SmoothMix文生视频 无需输入提示词_1981207594238992386.json
name: Qwen3 VL视频反推+Wan2.2 SmoothMix文生视频 无需输入提示词_1981207594238992386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Qwen3 VL视频反推+Wan2.2 SmoothMix文生视频 无需输入提示词_1981207594238992386.json
hash: 10c1f873ca75f27b
coverage: 0.5625
learned_at: 2026-10-11 02:45:01
nodes: [CLIPLoader, VAELoader, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, PrimitiveInt, KSamplerAdvanced, KSamplerAdvanced, PrimitiveInt, PrimitiveInt, EmptyHunyuanLatentVideo, SimpleMath+, VAEDecode, ImageFromBatch+, CR Text Concatenate, CR Text, String, VHS_VideoCombine, CR Text Concatenate, VHS_VideoCombine, UNETLoader, UNETLoader, LayerUtility: PurgeVRAM V2, AILab_QwenVL, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, ShowText|pysssss, VHS_LoadVideo, CR Text, MarkdownNote, LoadImage]
patterns: []
missing: [CR Text, CR Text, CR Text Concatenate, CR Text Concatenate, ImageFromBatch+, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, SimpleMath+]
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "uni_pc", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Qwen3 VL视频反推+Wan2.2 SmoothMix文生视频 无需输入提示词_1981207594238992386.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Qwen3 VL视频反推+Wan2.2 SmoothMix文生视频 无需输入提示词_1981207594238992386.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（32 个）：
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `PrimitiveInt`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `EmptyHunyuanLatentVideo`
- `SimpleMath+`
- `VAEDecode` ★核心
- `ImageFromBatch+`
- `CR Text Concatenate`
- `CR Text`
- `String`
- `VHS_VideoCombine`
- `CR Text Concatenate`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LayerUtility: PurgeVRAM V2`
- `AILab_QwenVL`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `ShowText|pysssss`
- `VHS_LoadVideo`
- `CR Text`
- `MarkdownNote`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `uni_pc`
- `denoise` = `simple`

## 知识

覆盖率 **56%**（18/32）

**有卡**：`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`CLIPTextEncode`、`KSamplerAdvanced`、`EmptyHunyuanLatentVideo`、`VAEDecode`、`String`、`VHS_VideoCombine`、`UNETLoader`、`AILab_QwenVL`、`VHS_LoadVideo`、`LoadImage`

**缺卡**（9）：`CR Text`、`CR Text`、`CR Text Concatenate`、`CR Text Concatenate`、`ImageFromBatch+`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`SimpleMath+`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
