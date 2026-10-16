---
key: 视频生成/图生视频/图生视频Wan2.2动漫模型DaSiWa_2048449800865058818.json
name: 图生视频Wan2.2动漫模型DaSiWa_2048449800865058818.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2048449800865058818.json
hash: 56b35cde1ccb9ae9
coverage: 0.745455
learned_at: 2026-10-15 22:37:09
nodes: [GetNode, CLIPVisionLoader, ModelPatchTorchSettings, GetNode, GetNode, GetNode, VHS_VideoCombine, PathchSageAttentionKJ, CLIPTextEncode, SetNode, ModelPatchTorchSettings, VAELoader, PathchSageAttentionKJ, wanBlockSwap, LoraLoaderModelOnly, wanBlockSwap, SetNode, CLIPVisionEncode, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, LoraLoaderModelOnly, RIFE VFI, VHS_VideoCombine, Wan22PromptSelector, Text Concatenate, Text Concatenate, FlashVSRNode, CLIPLoader, Note, TextInput_, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, CLIPTextEncode, VAEDecode, LayerUtility: PurgeVRAM V2, KSamplerAdvanced, KSamplerAdvanced, Note, UNETLoader, UNETLoader, Qwen3_VQA, MarkdownNote, easy showAnything, JWInteger, PainterI2V, CR Text, ImpactSwitch, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, VHS_VideoCombine, Fast Groups Bypasser (rgthree), JWInteger]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/图生视频Wan2.2动漫模型DaSiWa_2048449800865058818.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2048449800865058818.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（55 个）：
- `GetNode`
- `CLIPVisionLoader`
- `ModelPatchTorchSettings`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `SetNode`
- `ModelPatchTorchSettings`
- `VAELoader`
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `LoraLoaderModelOnly` ★核心
- `wanBlockSwap`
- `SetNode`
- `CLIPVisionEncode`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `RIFE VFI`
- `VHS_VideoCombine`
- `Wan22PromptSelector`
- `Text Concatenate`
- `Text Concatenate`
- `FlashVSRNode`
- `CLIPLoader`
- `Note`
- `TextInput_`
- `MathExpression|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Note`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Qwen3_VQA`
- `MarkdownNote`
- `easy showAnything`
- `JWInteger`
- `PainterI2V`
- `CR Text`
- `ImpactSwitch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `JWInteger`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **75%**（41/55）

**有卡**：`CLIPVisionLoader`、`ModelPatchTorchSettings`、`VHS_VideoCombine`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`VAELoader`、`wanBlockSwap`、`LoraLoaderModelOnly`、`CLIPVisionEncode`、`ModelSamplingSD3`、`RIFE VFI`、`Wan22PromptSelector`、`Text Concatenate`、`FlashVSRNode`、`CLIPLoader`、`TextInput_`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`KSamplerAdvanced`、`UNETLoader`、`Qwen3_VQA`、`JWInteger`、`PainterI2V`、`CR Text`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
