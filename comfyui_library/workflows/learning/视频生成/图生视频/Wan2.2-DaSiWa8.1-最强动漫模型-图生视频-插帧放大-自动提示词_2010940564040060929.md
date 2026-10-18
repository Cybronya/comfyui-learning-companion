---
key: 视频生成/图生视频/Wan2.2-DaSiWa8.1-最强动漫模型-图生视频-插帧放大-自动提示词_2010940564040060929.json
name: Wan2.2-DaSiWa8.1-最强动漫模型-图生视频-插帧放大-自动提示词_2010940564040060929.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-DaSiWa8.1-最强动漫模型-图生视频-插帧放大-自动提示词_2010940564040060929.json
hash: 6a2fbd4b6acd5ffe
coverage: 0.75
learned_at: 2026-10-15 22:34:19
nodes: [GetNode, CLIPVisionLoader, ModelPatchTorchSettings, GetNode, GetNode, GetNode, VHS_VideoCombine, PathchSageAttentionKJ, CLIPTextEncode, SetNode, ModelPatchTorchSettings, VAELoader, PathchSageAttentionKJ, wanBlockSwap, LoraLoaderModelOnly, wanBlockSwap, SetNode, CLIPVisionEncode, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, LoraLoaderModelOnly, RIFE VFI, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, Wan22PromptSelector, Text Concatenate, Text Concatenate, FlashVSRNode, CLIPLoader, TextInput_, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, CLIPTextEncode, VAEDecode, LayerUtility: PurgeVRAM V2, KSamplerAdvanced, KSamplerAdvanced, Note, UNETLoader, UNETLoader, JWInteger, Qwen3_VQA, PainterI2V, easy showAnything, MarkdownNote, CR Text, LoadImage, JWInteger, Fast Groups Bypasser (rgthree), ImpactSwitch, MarkdownNote, VHS_VideoCombine, AddLabel]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2-DaSiWa8.1-最强动漫模型-图生视频-插帧放大-自动提示词_2010940564040060929.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2010940564040060929.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（56 个）：
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
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `Wan22PromptSelector`
- `Text Concatenate`
- `Text Concatenate`
- `FlashVSRNode`
- `CLIPLoader`
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
- `JWInteger`
- `Qwen3_VQA`
- `PainterI2V`
- `easy showAnything`
- `MarkdownNote`
- `CR Text`
- `LoadImage`
- `JWInteger`
- `Fast Groups Bypasser (rgthree)`
- `ImpactSwitch`
- `MarkdownNote`
- `VHS_VideoCombine`
- `AddLabel`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **75%**（42/56）

**有卡**：`CLIPVisionLoader`、`ModelPatchTorchSettings`、`VHS_VideoCombine`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`VAELoader`、`wanBlockSwap`、`LoraLoaderModelOnly`、`CLIPVisionEncode`、`ModelSamplingSD3`、`RIFE VFI`、`LayerUtility: ImageScaleByAspectRatio V2`、`Wan22PromptSelector`、`Text Concatenate`、`FlashVSRNode`、`CLIPLoader`、`TextInput_`、`MathExpression|pysssss`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`KSamplerAdvanced`、`UNETLoader`、`JWInteger`、`Qwen3_VQA`、`PainterI2V`、`CR Text`、`LoadImage`、`AddLabel`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
