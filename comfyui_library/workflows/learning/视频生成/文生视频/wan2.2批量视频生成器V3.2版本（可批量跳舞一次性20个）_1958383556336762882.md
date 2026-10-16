---
key: 视频生成/文生视频/wan2.2批量视频生成器V3.2版本（可批量跳舞一次性20个）_1958383556336762882.json
name: wan2.2批量视频生成器V3.2版本（可批量跳舞一次性20个）_1958383556336762882.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1958383556336762882.json
hash: 4662c069027e2e50
coverage: 0.835616
learned_at: 2026-10-15 22:43:42
nodes: [LoraLoader, VAELoader, CFGZeroStarAndInit, CLIPTextEncode, LoraLoader, Text Concatenate, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSampler, WanVideoSampler, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoTextEncode, WanVideoLoraSelect, Note, Note, Note, Note, WanVideoVAELoader, WanVideoModelLoader, Primitive integer [Crystools], Primitive integer [Crystools], CreateCFGScheduleFloatList, WanVideoBlockSwap, WanVideoSetLoRAs, Primitive integer [Crystools], Primitive integer [Crystools], KSampler, VAEDecode, GetImageSizeAndCount, CLIPLoader, RHBatchImages:, Bjornulf_ShowInt, Primitive integer [Crystools], LoadWanVideoT5TextEncoder, CLIPTextEncode, Wan_video_prompt_generator, easy imageCount, RH_LLMAPI_NODE, ShowText|pysssss, UNETLoader, JWInteger, WanVideoImageToVideoEncode, WanVideoTorchCompileSettings, MathExpression|pysssss, JWInteger, LayerUtility: PurgeVRAM V2, Note, RHHiddenNodes, ImageResizeKJv2, PreviewImage, RHHiddenNodes, WanVideoModelLoader, LoadVideo, WanVideoDecode, easy int, easy mathInt, easy forLoopStart, easy showAnything, VHS_VideoCombine, easy forLoopEnd, easy showAnything, PreviewImage, SaveImage, Text Concatenate, Text Multiline, RHHiddenNodes, ShowText|pysssss, ShowText|pysssss, RHHiddenNodes, CR Integer To String, Text Multiline, EmptyLatentImage]
patterns: [text_to_image, lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 20, "cfg": 1, "denoise": 1, "height": 512, "lora_name": "Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors", "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 247103638351656, "steps": 8, "strength_clip": 0.4000000000000001, "strength_model": 0.4000000000000001, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/wan2.2批量视频生成器V3.2版本（可批量跳舞一次性20个）_1958383556336762882.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1958383556336762882.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（73 个）：
- `LoraLoader` ★核心
- `VAELoader`
- `CFGZeroStarAndInit`
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `Text Concatenate`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `Note`
- `Note`
- `Note`
- `Note`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `CreateCFGScheduleFloatList`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `GetImageSizeAndCount`
- `CLIPLoader`
- `RHBatchImages:`
- `Bjornulf_ShowInt`
- `Primitive integer [Crystools]`
- `LoadWanVideoT5TextEncoder`
- `CLIPTextEncode` ★核心
- `Wan_video_prompt_generator`
- `easy imageCount`
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `UNETLoader` ★核心
- `JWInteger`
- `WanVideoImageToVideoEncode`
- `WanVideoTorchCompileSettings`
- `MathExpression|pysssss`
- `JWInteger`
- `LayerUtility: PurgeVRAM V2`
- `Note`
- `RHHiddenNodes`
- `ImageResizeKJv2`
- `PreviewImage`
- `RHHiddenNodes`
- `WanVideoModelLoader`
- `LoadVideo`
- `WanVideoDecode`
- `easy int`
- `easy mathInt`
- `easy forLoopStart`
- `easy showAnything`
- `VHS_VideoCombine`
- `easy forLoopEnd`
- `easy showAnything`
- `PreviewImage`
- `SaveImage`
- `Text Concatenate`
- `Text Multiline`
- `RHHiddenNodes`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `RHHiddenNodes`
- `CR Integer To String`
- `Text Multiline`
- `EmptyLatentImage` ★核心

**识别到的模式**：text_to_image、lora

## 关键参数

- `lora_name` = `Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors`
- `strength_model` = `0.4000000000000001`
- `strength_clip` = `0.4000000000000001`
- `seed` = `247103638351656`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `20`

## 知识

覆盖率 **84%**（61/73）

**有卡**：`LoraLoader`、`VAELoader`、`CFGZeroStarAndInit`、`CLIPTextEncode`、`Text Concatenate`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSampler`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`WanVideoVAELoader`、`WanVideoModelLoader`、`Primitive integer [Crystools]`、`CreateCFGScheduleFloatList`、`WanVideoBlockSwap`、`KSampler`、`VAEDecode`、`GetImageSizeAndCount`、`CLIPLoader`、`RHBatchImages:`、`Bjornulf_ShowInt`、`LoadWanVideoT5TextEncoder`、`Wan_video_prompt_generator`、`easy imageCount`、`RH_LLMAPI_NODE`、`UNETLoader`、`JWInteger`、`WanVideoImageToVideoEncode`、`WanVideoTorchCompileSettings`、`MathExpression|pysssss`、`LayerUtility: PurgeVRAM V2`、`RHHiddenNodes`、`ImageResizeKJv2`、`LoadVideo`、`WanVideoDecode`、`easy int`、`easy mathInt`、`easy forLoopStart`、`VHS_VideoCombine`、`easy forLoopEnd`、`SaveImage`、`Text Multiline`、`CR Integer To String`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、CFGZeroStarAndInit

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
