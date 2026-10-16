---
key: 视频生成/图生视频/Wan2.2-REMIX V3-无审查-首尾帧视频_2061751615295680514.json
name: Wan2.2-REMIX V3-无审查-首尾帧视频_2061751615295680514.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2061751615295680514.json
hash: e3ecf038e133e367
coverage: 0.808824
learned_at: 2026-10-15 22:38:56
nodes: [llama_cpp_parameters, llama_cpp_instruct_adv, easy isNone, llama_cpp_model_loader, CR Text, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, DapaoSmartMemoryOptimizerNode, DapaoSmartMemoryOptimizerNode, PathchSageAttentionKJ, PathchSageAttentionKJ, Mute / Bypass Repeater (rgthree), Fast Bypasser (rgthree), CLIPLoader, VAELoader, SetNode, SetNode, SetNode, SetNode, ModelPatchTorchSettings, ModelPatchTorchSettings, WanMoeKSampler, ImpactInt, ImpactInt, easy setNode, VHS_VideoCombine, GetNode, PrimitiveInt, VHS_VideoCombine, RIFE VFI, VHS_VideoCombine, PrimitiveInt, Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), FlashVSRNode, Fast Bypasser (rgthree), Fast Bypasser (rgthree), CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, MathExpression|pysssss, CLIPVisionEncode, GetNode, GetNode, GetNode, MarkdownNote, PainterFLF2V, Mute / Bypass Repeater (rgthree), ImageResizeKJ, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, ImageConcanate, Fast Bypasser (rgthree), CustomAddLabel, VHS_VideoCombine, ImageConcanate, LoadImage, LoadImage, ImageConcanate, easy ifElse, easy showAnything, CR Text, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.875, "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2-REMIX V3-无审查-首尾帧视频_2061751615295680514.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2061751615295680514.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（68 个）：
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
- `easy setNode`
- `VHS_VideoCombine`
- `GetNode`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `RIFE VFI`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `FlashVSRNode`
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `MathExpression|pysssss`
- `CLIPVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MarkdownNote`
- `PainterFLF2V`
- `Mute / Bypass Repeater (rgthree)`
- `ImageResizeKJ`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `ImageConcanate`
- `Fast Bypasser (rgthree)`
- `CustomAddLabel`
- `VHS_VideoCombine`
- `ImageConcanate`
- `LoadImage`
- `LoadImage`
- `ImageConcanate`
- `easy ifElse`
- `easy showAnything`
- `CR Text`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `0.875`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **81%**（55/68）

**有卡**：`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`easy isNone`、`llama_cpp_model_loader`、`CR Text`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`DapaoSmartMemoryOptimizerNode`、`PathchSageAttentionKJ`、`Mute / Bypass Repeater (rgthree)`、`Fast Bypasser (rgthree)`、`CLIPLoader`、`VAELoader`、`ModelPatchTorchSettings`、`WanMoeKSampler`、`ImpactInt`、`easy setNode`、`VHS_VideoCombine`、`RIFE VFI`、`FlashVSRNode`、`CLIPTextEncode`、`CLIPVisionEncode`、`CLIPVisionLoader`、`MathExpression|pysssss`、`PainterFLF2V`、`ImageResizeKJ`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`ImageConcanate`、`CustomAddLabel`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
