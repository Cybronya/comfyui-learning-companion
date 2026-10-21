---
key: 图片生成/文生图/千问多角度templates-qwen_multiangle+全节点注释_2055470741176504322.json
name: 千问多角度templates-qwen_multiangle+全节点注释_2055470741176504322
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/千问多角度templates-qwen_multiangle+全节点注释_2055470741176504322.json
hash: 88f83101490bb673
coverage: 0.388889
learned_at: 2026-10-21 02:59:19
nodes: [SaveImage, ModelSamplingAuraFlow, VAELoader, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, CFGNorm, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveFloat, VAEEncode, UNETLoader, CLIPLoader, ComfySwitchNode, PrimitiveInt, PrimitiveInt, PrimitiveBoolean, ComfySwitchNode, ComfySwitchNode, KSampler, VAEDecode, FluxKontextImageScale, LoraLoaderModelOnly, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, LoadImage, LoadImage, LoadImage, QwenMultiangleCameraNode]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 3, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 321432059051210, "steps": 40}
---

# 图片生成/文生图/千问多角度templates-qwen_multiangle+全节点注释_2055470741176504322.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/千问多角度templates-qwen_multiangle+全节点注释_2055470741176504322.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Output → Other

**节点**（54 个）：
- `SaveImage`
- `ModelSamplingAuraFlow`
- `VAELoader`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `CFGNorm`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveFloat`
- `PrimitiveFloat`
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `ComfySwitchNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveBoolean`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `FluxKontextImageScale`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `QwenMultiangleCameraNode`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `321432059051210`
- `steps` = `40`
- `cfg` = `3`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **39%**（21/54）

**有卡**：`SaveImage`、`ModelSamplingAuraFlow`、`VAELoader`、`FluxKontextMultiReferenceLatentMethod`、`TextEncodeQwenImageEditPlus`、`CFGNorm`、`LoraLoaderModelOnly`、`VAEEncode`、`UNETLoader`、`CLIPLoader`、`PrimitiveBoolean`、`KSampler`、`VAEDecode`、`FluxKontextImageScale`、`LoadImage`、`QwenMultiangleCameraNode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm
