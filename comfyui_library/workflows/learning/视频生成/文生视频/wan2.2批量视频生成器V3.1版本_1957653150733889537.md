---
key: 视频生成/文生视频/wan2.2批量视频生成器V3.1版本_1957653150733889537.json
name: wan2.2批量视频生成器V3.1版本_1957653150733889537.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2批量视频生成器V3.1版本_1957653150733889537.json
hash: 7581285af6379669
coverage: 0.833333
learned_at: 2026-10-15 22:43:41
nodes: [LoraLoader, VAELoader, CFGZeroStarAndInit, CLIPTextEncode, LoraLoader, Text Concatenate, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSampler, WanVideoSampler, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoTextEncode, WanVideoLoraSelect, Note, Note, Note, Note, WanVideoVAELoader, WanVideoModelLoader, Primitive integer [Crystools], Primitive integer [Crystools], CreateCFGScheduleFloatList, WanVideoBlockSwap, WanVideoSetLoRAs, Primitive integer [Crystools], Primitive integer [Crystools], KSampler, VAEDecode, GetImageSizeAndCount, CLIPLoader, ShowText|pysssss, RHBatchImages:, Bjornulf_ShowInt, Primitive integer [Crystools], LoadWanVideoT5TextEncoder, Text Multiline, CLIPTextEncode, Wan_video_prompt_generator, easy imageCount, RH_LLMAPI_NODE, ShowText|pysssss, UNETLoader, JWInteger, ShowText|pysssss, WanVideoImageToVideoEncode, WanVideoTorchCompileSettings, MathExpression|pysssss, JWInteger, LayerUtility: PurgeVRAM V2, Note, RHHiddenNodes, RHHiddenNodes, ImageResizeKJv2, PreviewImage, RHHiddenNodes, WanVideoModelLoader, LoadVideo, WanVideoDecode, EmptyLatentImage, Text Multiline, easy int, easy mathInt, easy forLoopStart, CR Integer To String, easy showAnything, VHS_VideoCombine, easy forLoopEnd, easy showAnything, PreviewImage, SaveImage, RHHiddenNodes]
patterns: [text_to_image, lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 2, "cfg": 1, "denoise": 1, "height": 512, "lora_name": "Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors", "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 247103638351656, "steps": 8, "strength_clip": 0.4000000000000001, "strength_model": 0.4000000000000001, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/wan2.2批量视频生成器V3.1版本_1957653150733889537.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1957653150733889537.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（72 个）：
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
- `ShowText|pysssss`
- `RHBatchImages:`
- `Bjornulf_ShowInt`
- `Primitive integer [Crystools]`
- `LoadWanVideoT5TextEncoder`
- `Text Multiline`
- `CLIPTextEncode` ★核心
- `Wan_video_prompt_generator`
- `easy imageCount`
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `UNETLoader` ★核心
- `JWInteger`
- `ShowText|pysssss`
- `WanVideoImageToVideoEncode`
- `WanVideoTorchCompileSettings`
- `MathExpression|pysssss`
- `JWInteger`
- `LayerUtility: PurgeVRAM V2`
- `Note`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `ImageResizeKJv2`
- `PreviewImage`
- `RHHiddenNodes`
- `WanVideoModelLoader`
- `LoadVideo`
- `WanVideoDecode`
- `EmptyLatentImage` ★核心
- `Text Multiline`
- `easy int`
- `easy mathInt`
- `easy forLoopStart`
- `CR Integer To String`
- `easy showAnything`
- `VHS_VideoCombine`
- `easy forLoopEnd`
- `easy showAnything`
- `PreviewImage`
- `SaveImage`
- `RHHiddenNodes`

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
- `batch_size` = `2`

## 知识

覆盖率 **83%**（60/72）

**有卡**：`LoraLoader`、`VAELoader`、`CFGZeroStarAndInit`、`CLIPTextEncode`、`Text Concatenate`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSampler`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`WanVideoVAELoader`、`WanVideoModelLoader`、`Primitive integer [Crystools]`、`CreateCFGScheduleFloatList`、`WanVideoBlockSwap`、`KSampler`、`VAEDecode`、`GetImageSizeAndCount`、`CLIPLoader`、`RHBatchImages:`、`Bjornulf_ShowInt`、`LoadWanVideoT5TextEncoder`、`Text Multiline`、`Wan_video_prompt_generator`、`easy imageCount`、`RH_LLMAPI_NODE`、`UNETLoader`、`JWInteger`、`WanVideoImageToVideoEncode`、`WanVideoTorchCompileSettings`、`MathExpression|pysssss`、`LayerUtility: PurgeVRAM V2`、`RHHiddenNodes`、`ImageResizeKJv2`、`LoadVideo`、`WanVideoDecode`、`EmptyLatentImage`、`easy int`、`easy mathInt`、`easy forLoopStart`、`CR Integer To String`、`VHS_VideoCombine`、`easy forLoopEnd`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、CFGZeroStarAndInit

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
