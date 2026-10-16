---
key: 视频生成/图生视频/动作迁移视频WAN2.2 BERNINI图生视频视频换脸工作流_2088388446917324801.json
name: 动作迁移视频WAN2.2 BERNINI图生视频视频换脸工作流_2088388446917324801
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移视频WAN2.2 BERNINI图生视频视频换脸工作流_2088388446917324801.json
hash: 15c79070f8250c44
coverage: 0.828125
learned_at: 2026-10-16 21:43:49
nodes: [ImageConcanate, VHS_LoadVideo, LoadImage, PrimitiveInt, PrimitiveInt, TextConcatenate, BerniniPromptEnhancer, PreviewAny, UNETLoader, UNETLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, VHS_VideoCombine, VHS_VideoCombine, JjkText, VHS_VideoInfo, CLIPTextEncode, CLIPTextEncode, KSamplerSelect, PreviewAny, CLIPLoader, VAEDecode, BasicScheduler, llama_cpp_model_loader, SplitSigmas, llama_cpp_parameters, llama_cpp_instruct_adv, PreviewAny, PreviewAny, SamplerCustom, SamplerCustom, BerniniConditioning, VAELoader, 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/动作迁移视频WAN2.2 BERNINI图生视频视频换脸工作流_2088388446917324801.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移视频WAN2.2 BERNINI图生视频视频换脸工作流_2088388446917324801.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（64 个）：
- `ImageConcanate`
- `VHS_LoadVideo`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `TextConcatenate`
- `BerniniPromptEnhancer`
- `PreviewAny`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `JjkText`
- `VHS_VideoInfo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `PreviewAny`
- `CLIPLoader`
- `VAEDecode` ★核心
- `BasicScheduler`
- `llama_cpp_model_loader`
- `SplitSigmas`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `PreviewAny`
- `PreviewAny`
- `SamplerCustom` ★核心
- `SamplerCustom` ★核心
- `BerniniConditioning`
- `VAELoader`
- `孤海注释`
- `孤海注释`
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
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（53/64）

**有卡**：`ImageConcanate`、`VHS_LoadVideo`、`LoadImage`、`TextConcatenate`、`BerniniPromptEnhancer`、`UNETLoader`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`VHS_VideoInfo`、`CLIPTextEncode`、`KSamplerSelect`、`CLIPLoader`、`VAEDecode`、`BasicScheduler`、`llama_cpp_model_loader`、`SplitSigmas`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`SamplerCustom`、`BerniniConditioning`、`VAELoader`、`KSampler`、`solarL_SaveImagesToZip`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
