---
key: 平台全量/Lucy Edit 1.1 修改_替换_添加视频对象_1995530964526891010.json
name: Lucy Edit 1.1 修改_替换_添加视频对象_1995530964526891010
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Lucy Edit 1.1 修改_替换_添加视频对象_1995530964526891010.json
hash: fe8cbc7c60221ec1
coverage: 0.457143
learned_at: 2026-11-14 00:39:33
nodes: [PrimitiveInt, ImageResizeKJv2, SetNode, GetNode, GetNode, SetNode, GetNode, VAEEncode, LucyConditionConcatNode, ModelSamplingSD3, GetNode, CLIPLoader, SetNode, SetNode, CLIPTextEncode, VAEDecodeTiled, GetNode, MarkdownNote, KSampler, MarkdownNote, UNETLoader, LoraLoaderModelOnly, SetNode, VAELoader, VHS_VideoCombine, DF_Int_to_Float, GetNode, PrimitiveInt, SetNode, VHS_LoadVideoFFmpeg, PrimitiveInt, PrimitiveInt, UnetLoaderGGUF, MarkdownNote, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 627621851428134, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 平台全量/Lucy Edit 1.1 修改_替换_添加视频对象_1995530964526891010.json

> 来源文件 `comfyui_library/workflows/平台全量/Lucy Edit 1.1 修改_替换_添加视频对象_1995530964526891010.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（35 个）：
- `PrimitiveInt`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `VAEEncode` ★核心
- `LucyConditionConcatNode`
- `ModelSamplingSD3`
- `GetNode`
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `VAEDecodeTiled` ★核心
- `GetNode`
- `MarkdownNote`
- `KSampler` ★核心
- `MarkdownNote`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `VAELoader`
- `VHS_VideoCombine`
- `DF_Int_to_Float`
- `GetNode`
- `PrimitiveInt`
- `SetNode`
- `VHS_LoadVideoFFmpeg`
- `PrimitiveInt`
- `PrimitiveInt`
- `UnetLoaderGGUF` ★核心
- `MarkdownNote`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `627621851428134`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **46%**（16/35）

**有卡**：`ImageResizeKJv2`、`VAEEncode`、`LucyConditionConcatNode`、`ModelSamplingSD3`、`CLIPLoader`、`CLIPTextEncode`、`VAEDecodeTiled`、`KSampler`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`VHS_VideoCombine`、`DF_Int_to_Float`、`VHS_LoadVideoFFmpeg`、`UnetLoaderGGUF`

**用到的条目**：KSampler、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、VAEDecodeTiled、VAEEncode

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
