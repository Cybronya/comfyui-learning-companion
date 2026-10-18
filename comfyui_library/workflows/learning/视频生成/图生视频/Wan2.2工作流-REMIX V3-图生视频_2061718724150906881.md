---
key: 视频生成/图生视频/Wan2.2工作流-REMIX V3-图生视频_2061718724150906881.json
name: Wan2.2工作流-REMIX V3-图生视频_2061718724150906881.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2工作流-REMIX V3-图生视频_2061718724150906881.json
hash: db6b4018df4007be
coverage: 0.786885
learned_at: 2026-10-15 22:38:56
nodes: [llama_cpp_parameters, llama_cpp_instruct_adv, easy isNone, llama_cpp_model_loader, CR Text, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, DapaoSmartMemoryOptimizerNode, DapaoSmartMemoryOptimizerNode, PathchSageAttentionKJ, PathchSageAttentionKJ, Mute / Bypass Repeater (rgthree), Fast Bypasser (rgthree), CLIPLoader, VAELoader, SetNode, SetNode, SetNode, SetNode, ModelPatchTorchSettings, ModelPatchTorchSettings, WanMoeKSampler, ImpactInt, ImpactInt, easy ifElse, easy showAnything, easy setNode, VHS_VideoCombine, GetNode, GetNode, PainterI2V, MarkdownNote, GetNode, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionLoader, CLIPTextEncode, CLIPTextEncode, GetNode, CLIPVisionEncode, MathExpression|pysssss, PrimitiveInt, LoadImage, VAEDecode, VHS_VideoCombine, RIFE VFI, VHS_VideoCombine, PrimitiveInt, Mute / Bypass Repeater (rgthree), ImageConcanate, CustomAddLabel, Mute / Bypass Repeater (rgthree), FlashVSRNode, Fast Bypasser (rgthree), Fast Bypasser (rgthree), CR Text, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.875, "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2工作流-REMIX V3-图生视频_2061718724150906881.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2061718724150906881.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（61 个）：
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `easy isNone`
- `llama_cpp_model_loader`
- `CR Text`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `DapaoSmartMemoryOptimizerNode`
- `DapaoSmartMemoryOptimizerNode`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `Mute / Bypass Repeater (rgthree)`
- `Fast Bypasser (rgthree)`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `WanMoeKSampler` ★核心
- `ImpactInt`
- `ImpactInt`
- `easy ifElse`
- `easy showAnything`
- `easy setNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `PainterI2V`
- `MarkdownNote`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPVisionLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `CLIPVisionEncode`
- `MathExpression|pysssss`
- `PrimitiveInt`
- `LoadImage`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `RIFE VFI`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `Mute / Bypass Repeater (rgthree)`
- `ImageConcanate`
- `CustomAddLabel`
- `Mute / Bypass Repeater (rgthree)`
- `FlashVSRNode`
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `CR Text`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `0.875`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **79%**（48/61）

**有卡**：`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`easy isNone`、`llama_cpp_model_loader`、`CR Text`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`DapaoSmartMemoryOptimizerNode`、`PathchSageAttentionKJ`、`Mute / Bypass Repeater (rgthree)`、`Fast Bypasser (rgthree)`、`CLIPLoader`、`VAELoader`、`ModelPatchTorchSettings`、`WanMoeKSampler`、`ImpactInt`、`easy setNode`、`VHS_VideoCombine`、`PainterI2V`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionLoader`、`CLIPTextEncode`、`CLIPVisionEncode`、`MathExpression|pysssss`、`LoadImage`、`VAEDecode`、`RIFE VFI`、`ImageConcanate`、`CustomAddLabel`、`FlashVSRNode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler
