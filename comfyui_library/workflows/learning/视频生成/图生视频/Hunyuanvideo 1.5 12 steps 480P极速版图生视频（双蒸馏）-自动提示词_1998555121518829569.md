---
key: 视频生成/图生视频/Hunyuanvideo 1.5 12 steps 480P极速版图生视频（双蒸馏）-自动提示词_1998555121518829569.json
name: Hunyuanvideo 1.5 12 steps 480P极速版图生视频（双蒸馏）-自动提示词_1998555121518829569.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Hunyuanvideo 1.5 12 steps 480P极速版图生视频（双蒸馏）-自动提示词_1998555121518829569.json
hash: 998b82f706190408
coverage: 0.846154
learned_at: 2026-10-15 22:33:32
nodes: [CLIPVisionLoader, DualCLIPLoader, VAELoader, EasyCache, Note, MarkdownNote, CLIPTextEncode, UNETLoader, BasicScheduler, HunyuanVideo15ImageToVideo, RandomNoise, KSamplerSelect, CLIPVisionEncode, CFGGuider, ModelSamplingSD3, VAEDecode, LayerUtility: PurgeVRAM, VAEDecodeTiled, AddLabel, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, JWInteger, Float, Seed (rgthree), SimpleMath+, SamplerCustomAdvanced, MarkdownNote, MarkdownNote, easy ifElse, CLIPTextEncode, LoadImage, Text, BatchTextReplace, AILab_QwenVL, easy showAnything, Text, PrimitiveBoolean, Text]
patterns: []
missing: []
---

# 视频生成/图生视频/Hunyuanvideo 1.5 12 steps 480P极速版图生视频（双蒸馏）-自动提示词_1998555121518829569.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1998555121518829569.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（39 个）：
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `VAELoader`
- `EasyCache`
- `Note`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `BasicScheduler`
- `HunyuanVideo15ImageToVideo`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CLIPVisionEncode`
- `CFGGuider`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `VAEDecodeTiled` ★核心
- `AddLabel`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `JWInteger`
- `Float`
- `Seed (rgthree)`
- `SimpleMath+`
- `SamplerCustomAdvanced` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `easy ifElse`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `Text`
- `BatchTextReplace`
- `AILab_QwenVL`
- `easy showAnything`
- `Text`
- `PrimitiveBoolean`
- `Text`

## 知识

覆盖率 **85%**（33/39）

**有卡**：`CLIPVisionLoader`、`DualCLIPLoader`、`VAELoader`、`EasyCache`、`CLIPTextEncode`、`UNETLoader`、`BasicScheduler`、`HunyuanVideo15ImageToVideo`、`RandomNoise`、`KSamplerSelect`、`CLIPVisionEncode`、`CFGGuider`、`ModelSamplingSD3`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`VAEDecodeTiled`、`AddLabel`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`Float`、`Seed (rgthree)`、`SimpleMath+`、`SamplerCustomAdvanced`、`LoadImage`、`Text`、`BatchTextReplace`、`AILab_QwenVL`、`PrimitiveBoolean`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
