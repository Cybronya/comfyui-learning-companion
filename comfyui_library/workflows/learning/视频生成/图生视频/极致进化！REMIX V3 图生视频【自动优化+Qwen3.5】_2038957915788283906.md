---
key: 视频生成/图生视频/极致进化！REMIX V3 图生视频【自动优化+Qwen3.5】_2038957915788283906.json
name: 极致进化！REMIX V3 图生视频【自动优化+Qwen3.5】_2038957915788283906.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2038957915788283906.json
hash: ad88a5aa849b7757
coverage: 0.763636
learned_at: 2026-10-15 22:36:06
nodes: [ModelSamplingSD3, ModelSamplingSD3, ModelPatchTorchSettings, ModelPatchTorchSettings, PathchSageAttentionKJ, PathchSageAttentionKJ, SetNode, SetNode, VAELoader, SetNode, CLIPVisionEncode, MathExpression|pysssss, GetNode, GetNode, easy getNode, RIFE VFI, easy getNode, easy setNode, PainterI2V, GetNode, GetNode, WanMoeKSampler, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionLoader, CLIPTextEncode, ImpactInt, Mute / Bypass Repeater (rgthree), Fast Bypasser (rgthree), CLIPLoader, SetNode, MarkdownNote, VAEDecode, DapaoSmartMemoryOptimizerNode, DapaoSmartMemoryOptimizerNode, UNETLoader, UNETLoader, VHS_VideoCombine, CLIPTextEncode, easy ifElse, ImpactInt, llama_cpp_parameters, llama_cpp_instruct_adv, CR Text, CR Text, easy isNone, VHS_VideoCombine, easy showAnything, MarkdownNote, llama_cpp_model_loader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, LoadImage, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.875, "steps": "randomize"}
---

# 视频生成/图生视频/极致进化！REMIX V3 图生视频【自动优化+Qwen3.5】_2038957915788283906.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2038957915788283906.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（55 个）：
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `SetNode`
- `SetNode`
- `VAELoader`
- `SetNode`
- `CLIPVisionEncode`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `easy getNode`
- `RIFE VFI`
- `easy getNode`
- `easy setNode`
- `PainterI2V`
- `GetNode`
- `GetNode`
- `WanMoeKSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPVisionLoader`
- `CLIPTextEncode` ★核心
- `ImpactInt`
- `Mute / Bypass Repeater (rgthree)`
- `Fast Bypasser (rgthree)`
- `CLIPLoader`
- `SetNode`
- `MarkdownNote`
- `VAEDecode` ★核心
- `DapaoSmartMemoryOptimizerNode`
- `DapaoSmartMemoryOptimizerNode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `easy ifElse`
- `ImpactInt`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `CR Text`
- `CR Text`
- `easy isNone`
- `VHS_VideoCombine`
- `easy showAnything`
- `MarkdownNote`
- `llama_cpp_model_loader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `MarkdownNote`

## 关键参数

- `seed` = `0.875`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **76%**（42/55）

**有卡**：`ModelSamplingSD3`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`VAELoader`、`CLIPVisionEncode`、`MathExpression|pysssss`、`easy getNode`、`RIFE VFI`、`easy setNode`、`PainterI2V`、`WanMoeKSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionLoader`、`CLIPTextEncode`、`ImpactInt`、`Mute / Bypass Repeater (rgthree)`、`Fast Bypasser (rgthree)`、`CLIPLoader`、`VAEDecode`、`DapaoSmartMemoryOptimizerNode`、`UNETLoader`、`VHS_VideoCombine`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`CR Text`、`easy isNone`、`llama_cpp_model_loader`、`LoraLoaderModelOnly`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler
