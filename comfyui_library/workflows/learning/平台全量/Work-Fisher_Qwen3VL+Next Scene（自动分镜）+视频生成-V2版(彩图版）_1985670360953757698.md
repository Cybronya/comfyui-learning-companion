---
key: 平台全量/Work-Fisher_Qwen3VL+Next Scene（自动分镜）+视频生成-V2版(彩图版）_1985670360953757698.json
name: Work-Fisher_Qwen3VL+Next Scene（自动分镜）+视频生成-V2版(彩图版）_1985670360953757698
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Work-Fisher_Qwen3VL+Next Scene（自动分镜）+视频生成-V2版(彩图版）_1985670360953757698.json
hash: b6d02e85808e3cc0
coverage: 0.783019
learned_at: 2026-11-14 01:07:26
nodes: [Note, Note, PathchSageAttentionKJ, Note, Fast Groups Bypasser (rgthree), CLIPLoader, ModelPatchTorchSettings, wanBlockSwap, WanMoeKSampler, CLIPTextEncode, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionEncode, CLIPVisionEncode, INTConstant, Int, ImageResizeKJv2, Note, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, WanFirstLastFrameToVideo, Int, easy cleanGpuUsed, UNETLoader, UNETLoader, wanBlockSwap, PathchSageAttentionKJ, ModelPatchTorchSettings, VAEDecode, CLIPTextEncode, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, Note, CLIPVisionEncode, SimpleMath+, Note, Note, Note, Note, easy cleanGpuUsed, WanMoeKSampler, WanImageToVideo, ImageResizeKJv2, Fast Groups Bypasser (rgthree), INTConstant, wanBlockSwap, wanBlockSwap, Int, Int, LoadImage, LoadImage, CLIPTextEncode, LoadImage, CLIPTextEncode, CLIPVisionLoader, CLIPLoader, UNETLoader, UNETLoader, CLIPVisionLoader, VAELoader, VAELoader, easy promptLine, ConditioningZeroOut, Reroute, Reroute, Reroute, Reroute, TextEncodeQwenImageEditPlusAdvance_lrzjason, easy showAnything, JWStringConcat, easy showAnything, ProcessString, Qwen3_VQA, easy clearCacheAll, Reroute, Reroute, Reroute, LoraLoaderModelOnly, KSampler, Fast Groups Bypasser (rgthree), CR Prompt Text, TT_img_enc_v2, ImageFromBatch+, RIFE VFI, DF_Integer, SaveImage, Fast Groups Bypasser (rgthree), CR Prompt Text, TT_img_enc_v2, ImageFromBatch+, RIFE VFI, SaveImage, Fast Groups Bypasser (rgthree), TT_img_enc_v2, VAEDecode, CR Prompt Text, SaveImage, Text Multiline, DifferentialDiffusion, LoraLoaderModelOnly, CheckpointLoaderSimple, LoadImage, CR Prompt Text, LoraLoaderModelOnly]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Rapid-AIO-NSFW-v5.3.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 214, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Work-Fisher_Qwen3VL+Next Scene（自动分镜）+视频生成-V2版(彩图版）_1985670360953757698.json

> 来源文件 `comfyui_library/workflows/平台全量/Work-Fisher_Qwen3VL+Next Scene（自动分镜）+视频生成-V2版(彩图版）_1985670360953757698.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（106 个）：
- `Note`
- `Note`
- `PathchSageAttentionKJ`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `CLIPLoader`
- `ModelPatchTorchSettings`
- `wanBlockSwap`
- `WanMoeKSampler` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `INTConstant`
- `Int`
- `ImageResizeKJv2`
- `Note`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanFirstLastFrameToVideo`
- `Int`
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `Note`
- `CLIPVisionEncode`
- `SimpleMath+`
- `Note`
- `Note`
- `Note`
- `Note`
- `easy cleanGpuUsed`
- `WanMoeKSampler` ★核心
- `WanImageToVideo`
- `ImageResizeKJv2`
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `wanBlockSwap`
- `wanBlockSwap`
- `Int`
- `Int`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPVisionLoader`
- `VAELoader`
- `VAELoader`
- `easy promptLine`
- `ConditioningZeroOut`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `easy showAnything`
- `JWStringConcat`
- `easy showAnything`
- `ProcessString`
- `Qwen3_VQA`
- `easy clearCacheAll`
- `Reroute`
- `Reroute`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `Fast Groups Bypasser (rgthree)`
- `CR Prompt Text`
- `TT_img_enc_v2`
- `ImageFromBatch+`
- `RIFE VFI`
- `DF_Integer`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `CR Prompt Text`
- `TT_img_enc_v2`
- `ImageFromBatch+`
- `RIFE VFI`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `TT_img_enc_v2`
- `VAEDecode` ★核心
- `CR Prompt Text`
- `SaveImage`
- `Text Multiline`
- `DifferentialDiffusion`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `CR Prompt Text`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `214`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v5.3.safetensors`

## 知识

覆盖率 **78%**（83/106）

**有卡**：`PathchSageAttentionKJ`、`CLIPLoader`、`ModelPatchTorchSettings`、`wanBlockSwap`、`WanMoeKSampler`、`CLIPTextEncode`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionEncode`、`INTConstant`、`Int`、`ImageResizeKJv2`、`WanFirstLastFrameToVideo`、`easy cleanGpuUsed`、`UNETLoader`、`SimpleMath+`、`WanImageToVideo`、`LoadImage`、`CLIPVisionLoader`、`VAELoader`、`easy promptLine`、`ConditioningZeroOut`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`JWStringConcat`、`ProcessString`、`Qwen3_VQA`、`easy clearCacheAll`、`LoraLoaderModelOnly`、`KSampler`、`CR Prompt Text`、`TT_img_enc_v2`、`ImageFromBatch+`、`RIFE VFI`、`DF_Integer`、`SaveImage`、`Text Multiline`、`DifferentialDiffusion`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPLoader、CLIPTextEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
