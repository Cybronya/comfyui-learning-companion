---
key: 视频生成/图生视频/Wan2.2-14B图生视频｜阿里旗舰模型画质稳定出片_2111113599828713473.json
name: Wan2.2-14B图生视频｜阿里旗舰模型画质稳定出片_2111113599828713473
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-14B图生视频｜阿里旗舰模型画质稳定出片_2111113599828713473.json
hash: 9d88f05d59737282
coverage: 0.810219
learned_at: 2026-10-18 00:43:52
nodes: [Int, WanVideoLoraSelect, CreateCFGScheduleFloatList, PrimitiveNode, WanVideoVAELoader, Int, RH_LLMAPI_NODE, RH_LLMAPI_NODE, easy showAnything, JjkShowText, WanVideoSampler, easy cleanGpuUsed, WanVideoDecode, WanVideoTextEncode, RH_Captioner, JjkText, JjkText, easy showAnything, TextCombinerTwo, TextCombinerTwo, CR Text Concatenate, RH_Prompter, RH_Prompter, ShowText, Int, Int, Int, Int, Int, Int, Int, Int, Int, Int, Int, MathExpression|pysssss, JWInteger, WanVideoSetLoRAs, ImageFromBatch+, Int, Int, Int, RH_Translator, WanVideoSetLoRAs, ImpactSwitch, ImpactSwitch, ImpactSwitch, ImpactSwitch, ImpactSwitch, ImpactSwitch, RunningHub ThinkSound, Bjornulf_ShowInt, ImageResize+, WanVideoSampler, WanVideoImageToVideoEncode, VHS_VideoCombine, CreateVideo, Fast Groups Muter (rgthree), Bjornulf_ShowInt, PreviewImage, PreviewImage, ImpactSwitch, ImageResizeKJv2, ImageResize+, PreviewImage, Bjornulf_ShowInt, Bjornulf_ShowInt, Bjornulf_ShowInt, ImpactSwitch, ImpactSwitch, Bjornulf_ShowInt, ImpactSwitch, ShowText, TextCombinerTwo, JjkText, SaveVideo, Int, WanVideoModelLoader, WanVideoModelLoader, Int, Int, Int, Int, Int, Int, Int, LoadWanVideoT5TextEncoder, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, easy anythingIndexSwitch, LoadImage, ImpactSwitch, JjkText, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2-14B图生视频｜阿里旗舰模型画质稳定出片_2111113599828713473.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Wan2.2-14B图生视频｜阿里旗舰模型画质稳定出片_2111113599828713473.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（137 个）：
- `Int`
- `WanVideoLoraSelect`
- `CreateCFGScheduleFloatList`
- `PrimitiveNode`
- `WanVideoVAELoader`
- `Int`
- `RH_LLMAPI_NODE`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `JjkShowText`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `WanVideoTextEncode`
- `RH_Captioner`
- `JjkText`
- `JjkText`
- `easy showAnything`
- `TextCombinerTwo`
- `TextCombinerTwo`
- `CR Text Concatenate`
- `RH_Prompter`
- `RH_Prompter`
- `ShowText`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `MathExpression|pysssss`
- `JWInteger`
- `WanVideoSetLoRAs`
- `ImageFromBatch+`
- `Int`
- `Int`
- `Int`
- `RH_Translator`
- `WanVideoSetLoRAs`
- `ImpactSwitch`
- `ImpactSwitch`
- `ImpactSwitch`
- `ImpactSwitch`
- `ImpactSwitch`
- `ImpactSwitch`
- `RunningHub ThinkSound`
- `Bjornulf_ShowInt`
- `ImageResize+`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoEncode`
- `VHS_VideoCombine`
- `CreateVideo`
- `Fast Groups Muter (rgthree)`
- `Bjornulf_ShowInt`
- `PreviewImage`
- `PreviewImage`
- `ImpactSwitch`
- `ImageResizeKJv2`
- `ImageResize+`
- `PreviewImage`
- `Bjornulf_ShowInt`
- `Bjornulf_ShowInt`
- `Bjornulf_ShowInt`
- `ImpactSwitch`
- `ImpactSwitch`
- `Bjornulf_ShowInt`
- `ImpactSwitch`
- `ShowText`
- `TextCombinerTwo`
- `JjkText`
- `SaveVideo`
- `Int`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `LoadWanVideoT5TextEncoder`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `easy anythingIndexSwitch`
- `LoadImage`
- `ImpactSwitch`
- `JjkText`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **81%**（111/137）

**有卡**：`Int`、`WanVideoLoraSelect`、`CreateCFGScheduleFloatList`、`WanVideoVAELoader`、`RH_LLMAPI_NODE`、`JjkShowText`、`WanVideoSampler`、`easy cleanGpuUsed`、`WanVideoDecode`、`WanVideoTextEncode`、`RH_Captioner`、`TextCombinerTwo`、`CR Text Concatenate`、`RH_Prompter`、`ShowText`、`MathExpression|pysssss`、`JWInteger`、`WanVideoSetLoRAs`、`ImageFromBatch+`、`RH_Translator`、`RunningHub ThinkSound`、`Bjornulf_ShowInt`、`ImageResize+`、`WanVideoImageToVideoEncode`、`VHS_VideoCombine`、`CreateVideo`、`ImageResizeKJv2`、`SaveVideo`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`easy anythingIndexSwitch`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
