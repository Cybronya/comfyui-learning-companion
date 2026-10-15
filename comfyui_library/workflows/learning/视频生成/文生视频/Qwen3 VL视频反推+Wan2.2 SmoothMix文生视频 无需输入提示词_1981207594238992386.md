---
key: 视频生成/文生视频/Qwen3 VL视频反推+Wan2.2 SmoothMix文生视频 无需输入提示词_1981207594238992386.json
name: Qwen3 VL视频反推+Wan2.2 SmoothMix文生视频 无需输入提示词_1981207594238992386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Qwen3 VL视频反推+Wan2.2 SmoothMix文生视频 无需输入提示词_1981207594238992386.json
hash: 10c1f873ca75f27b
coverage: 0.84375
learned_at: 2026-10-15 22:46:51
nodes: [CLIPLoader, VAELoader, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, PrimitiveInt, KSamplerAdvanced, KSamplerAdvanced, PrimitiveInt, PrimitiveInt, EmptyHunyuanLatentVideo, SimpleMath+, VAEDecode, ImageFromBatch+, CR Text Concatenate, CR Text, String, VHS_VideoCombine, CR Text Concatenate, VHS_VideoCombine, UNETLoader, UNETLoader, LayerUtility: PurgeVRAM V2, AILab_QwenVL, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, ShowText|pysssss, VHS_LoadVideo, CR Text, MarkdownNote, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "uni_pc", "seed": "disable", "steps": "fixed"}
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

覆盖率 **84%**（27/32）

**有卡**：`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`CLIPTextEncode`、`KSamplerAdvanced`、`EmptyHunyuanLatentVideo`、`SimpleMath+`、`VAEDecode`、`ImageFromBatch+`、`CR Text Concatenate`、`CR Text`、`String`、`VHS_VideoCombine`、`UNETLoader`、`LayerUtility: PurgeVRAM V2`、`AILab_QwenVL`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
