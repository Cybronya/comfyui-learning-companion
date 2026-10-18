---
key: 视频生成/图生视频/图生视频-最强Wan2.2动漫模型DaSiWa_2009346711700901890.json
name: 图生视频-最强Wan2.2动漫模型DaSiWa_2009346711700901890.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/图生视频-最强Wan2.2动漫模型DaSiWa_2009346711700901890.json
hash: b669c44ea79baeb3
coverage: 0.795918
learned_at: 2026-10-15 22:34:12
nodes: [CLIPVisionLoader, ModelPatchTorchSettings, GetNode, GetNode, GetNode, PathchSageAttentionKJ, SetNode, VAELoader, wanBlockSwap, LoraLoaderModelOnly, wanBlockSwap, SetNode, CLIPVisionEncode, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, LoraLoaderModelOnly, CLIPLoader, MathExpression|pysssss, SetNode, SetNode, KSamplerAdvanced, KSamplerAdvanced, UNETLoader, UNETLoader, PainterI2V, ModelPatchTorchSettings, PathchSageAttentionKJ, JWInteger, MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, GetNode, Qwen3_VQA, CLIPTextEncode, CLIPTextEncode, VAEDecode, TextInput_, TextInput_, TextInput_, TextInput_, VHS_VideoCombine, LoadImage, TextInput_, Text Concatenate, CR Text, easy showAnything, LoadImage, JWInteger, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/图生视频-最强Wan2.2动漫模型DaSiWa_2009346711700901890.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2009346711700901890.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（49 个）：
- `CLIPVisionLoader`
- `ModelPatchTorchSettings`
- `GetNode`
- `GetNode`
- `GetNode`
- `PathchSageAttentionKJ`
- `SetNode`
- `VAELoader`
- `wanBlockSwap`
- `LoraLoaderModelOnly` ★核心
- `wanBlockSwap`
- `SetNode`
- `CLIPVisionEncode`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `MathExpression|pysssss`
- `SetNode`
- `SetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PainterI2V`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `JWInteger`
- `MarkdownNote`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `Qwen3_VQA`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `TextInput_`
- `TextInput_`
- `TextInput_`
- `TextInput_`
- `VHS_VideoCombine`
- `LoadImage`
- `TextInput_`
- `Text Concatenate`
- `CR Text`
- `easy showAnything`
- `LoadImage`
- `JWInteger`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **80%**（39/49）

**有卡**：`CLIPVisionLoader`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`VAELoader`、`wanBlockSwap`、`LoraLoaderModelOnly`、`CLIPVisionEncode`、`ModelSamplingSD3`、`CLIPLoader`、`MathExpression|pysssss`、`KSamplerAdvanced`、`UNETLoader`、`PainterI2V`、`JWInteger`、`LayerUtility: ImageScaleByAspectRatio V2`、`Qwen3_VQA`、`CLIPTextEncode`、`VAEDecode`、`TextInput_`、`VHS_VideoCombine`、`LoadImage`、`Text Concatenate`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
