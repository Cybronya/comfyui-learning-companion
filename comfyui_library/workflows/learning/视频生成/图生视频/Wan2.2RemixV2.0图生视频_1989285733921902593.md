---
key: 视频生成/图生视频/Wan2.2RemixV2.0图生视频_1989285733921902593.json
name: Wan2.2RemixV2.0图生视频_1989285733921902593.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2RemixV2.0图生视频_1989285733921902593.json
hash: 39c20b65af2e37f6
coverage: 0.857143
learned_at: 2026-10-15 22:33:06
nodes: [ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, LoadImage, PrimitiveInt, MarkdownNote, CLIPLoader, ApplySageAttention, VAELoader, ApplySageAttention, SimpleMath+, VAEDecode, VHS_VideoCombine, CLIPVisionEncode, CLIPVisionLoader, PainterI2V, WanMoeKSampler, LoadImage, CR Text, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, PrimitiveInt, PrimitiveInt]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "euler", "sampler_name": 1, "scheduler": 1, "seed": 0.875, "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2RemixV2.0图生视频_1989285733921902593.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1989285733921902593.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（28 个）：
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `LoadImage`
- `PrimitiveInt`
- `MarkdownNote`
- `CLIPLoader`
- `ApplySageAttention`
- `VAELoader`
- `ApplySageAttention`
- `SimpleMath+`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `PainterI2V`
- `WanMoeKSampler` ★核心
- `LoadImage`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `PrimitiveInt`
- `PrimitiveInt`

## 关键参数

- `seed` = `0.875`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **86%**（24/28）

**有卡**：`ModelSamplingSD3`、`CLIPTextEncode`、`LoadImage`、`CLIPLoader`、`ApplySageAttention`、`VAELoader`、`SimpleMath+`、`VAEDecode`、`VHS_VideoCombine`、`CLIPVisionEncode`、`CLIPVisionLoader`、`PainterI2V`、`WanMoeKSampler`、`CR Text`、`LoraLoaderModelOnly`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler
