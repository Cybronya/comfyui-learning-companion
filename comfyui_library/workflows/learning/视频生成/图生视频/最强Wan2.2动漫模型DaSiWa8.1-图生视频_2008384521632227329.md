---
key: 视频生成/图生视频/最强Wan2.2动漫模型DaSiWa8.1-图生视频_2008384521632227329.json
name: 最强Wan2.2动漫模型DaSiWa8.1-图生视频_2008384521632227329.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2008384521632227329.json
hash: db95a516094fc6f4
coverage: 0.777778
learned_at: 2026-10-15 22:34:07
nodes: [GetNode, CLIPVisionLoader, ModelPatchTorchSettings, GetNode, GetNode, GetNode, VHS_VideoCombine, PathchSageAttentionKJ, CLIPTextEncode, SetNode, ModelPatchTorchSettings, VAELoader, PathchSageAttentionKJ, wanBlockSwap, LoraLoaderModelOnly, wanBlockSwap, SetNode, CLIPVisionEncode, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, LoraLoaderModelOnly, RIFE VFI, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, Fast Groups Bypasser (rgthree), VHS_VideoCombine, CR Text, Wan22PromptSelector, Text Concatenate, Text Concatenate, FlashVSRNode, CLIPLoader, Note, TextInput_, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, ImpactSwitch, CLIPTextEncode, VAEDecode, LayerUtility: PurgeVRAM V2, KSamplerAdvanced, KSamplerAdvanced, Note, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, LoadVideo, VHS_VideoCombine, UNETLoader, UNETLoader, LoadImage, JWInteger, JWInteger, Qwen3_VQA, PainterI2V, MarkdownNote, easy showAnything, LoadVideo, LoadVideo, LoadVideo]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/最强Wan2.2动漫模型DaSiWa8.1-图生视频_2008384521632227329.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2008384521632227329.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（63 个）：
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
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `CR Text`
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
- `ImpactSwitch`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Note`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadVideo`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `JWInteger`
- `JWInteger`
- `Qwen3_VQA`
- `PainterI2V`
- `MarkdownNote`
- `easy showAnything`
- `LoadVideo`
- `LoadVideo`
- `LoadVideo`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **78%**（49/63）

**有卡**：`CLIPVisionLoader`、`ModelPatchTorchSettings`、`VHS_VideoCombine`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`VAELoader`、`wanBlockSwap`、`LoraLoaderModelOnly`、`CLIPVisionEncode`、`ModelSamplingSD3`、`RIFE VFI`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Text`、`Wan22PromptSelector`、`Text Concatenate`、`FlashVSRNode`、`CLIPLoader`、`TextInput_`、`MathExpression|pysssss`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`KSamplerAdvanced`、`LoadVideo`、`UNETLoader`、`LoadImage`、`JWInteger`、`Qwen3_VQA`、`PainterI2V`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
