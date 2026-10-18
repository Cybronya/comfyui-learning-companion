---
key: 视频生成/图生视频/重大进步2_Wan2.2_PromptRelay多段提示词精准控制_2054717028392546306.json
name: 重大进步2_Wan2.2_PromptRelay多段提示词精准控制_2054717028392546306.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/重大进步2_Wan2.2_PromptRelay多段提示词精准控制_2054717028392546306.json
hash: 5de90cfb09a5b4bd
coverage: 0.909091
learned_at: 2026-10-15 22:37:50
nodes: [VAELoader, CLIPLoader, WanImageToVideo, UNETLoader, UNETLoader, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, ConditioningZeroOut, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, VHS_VideoCombine, MarkdownNote, PromptRelayEncodeTimeline, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, EmptyHunyuanLatentVideo, PromptRelayEncodeTimeline, Int, PrimitiveNode, ImageResizeKJv2]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "uni_pc", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/重大进步2_Wan2.2_PromptRelay多段提示词精准控制_2054717028392546306.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2054717028392546306.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（22 个）：
- `VAELoader`
- `CLIPLoader`
- `WanImageToVideo`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `ConditioningZeroOut`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `MarkdownNote`
- `PromptRelayEncodeTimeline`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `EmptyHunyuanLatentVideo`
- `PromptRelayEncodeTimeline`
- `Int`
- `PrimitiveNode`
- `ImageResizeKJv2`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `uni_pc`
- `denoise` = `simple`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`VAELoader`、`CLIPLoader`、`WanImageToVideo`、`UNETLoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`ConditioningZeroOut`、`KSamplerAdvanced`、`VAEDecode`、`VHS_VideoCombine`、`PromptRelayEncodeTimeline`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`EmptyHunyuanLatentVideo`、`Int`、`ImageResizeKJv2`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
