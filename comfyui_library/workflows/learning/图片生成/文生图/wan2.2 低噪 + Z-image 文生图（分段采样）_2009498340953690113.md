---
key: 图片生成/文生图/wan2.2 低噪 + Z-image 文生图（分段采样）_2009498340953690113.json
name: wan2.2 低噪 + Z-image 文生图（分段采样）_2009498340953690113
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2 低噪 + Z-image 文生图（分段采样）_2009498340953690113.json
hash: 9429e8d687ff4e95
coverage: 0.837209
learned_at: 2026-10-19 22:01:14
nodes: [CLIPLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, CLIPLoader, CLIPTextEncode, KSampler, VAEDecode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, VAELoader, VAELoader, LoraLoaderModelOnly, CR Text, UNETLoader, LayerFilter: HDREffects, SaveImage, Note, Note, INTConstant, Note, PreviewImage, INTConstant, INTConstant, INTConstant, INTConstant, Note, EmptyLatentImage, KSamplerAdvanced, VAEDecode, VAEEncode, RH_LLMAPI_NODE, RH_LLMAPI_Pro_Node, InversionDemoLazyIndexSwitch, easy showAnything, InversionDemoLazyIndexSwitch, UNETLoader, CheckpointLoaderSimple, LoraLoaderModelOnly, Text, Text, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 4, "cfg": 10, "checkpoint": "redcraftRedzimageUpdatedDEC03_redzimage15AIO.safetensors", "denoise": "sgm_uniform", "height": 1536, "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize", "width": 960}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/wan2.2 低噪 + Z-image 文生图（分段采样）_2009498340953690113.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2 低噪 + Z-image 文生图（分段采样）_2009498340953690113.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（43 个）：
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `CR Text`
- `UNETLoader` ★核心
- `LayerFilter: HDREffects`
- `SaveImage`
- `Note`
- `Note`
- `INTConstant`
- `Note`
- `PreviewImage`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `Note`
- `EmptyLatentImage` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `RH_LLMAPI_NODE`
- `RH_LLMAPI_Pro_Node`
- `InversionDemoLazyIndexSwitch`
- `easy showAnything`
- `InversionDemoLazyIndexSwitch`
- `UNETLoader` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `Text`
- `Text`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `sgm_uniform`
- `width` = `960`
- `height` = `1536`
- `batch_size` = `4`
- `checkpoint` = `redcraftRedzimageUpdatedDEC03_redzimage15AIO.safetensors`

## 知识

覆盖率 **84%**（36/43）

**有卡**：`CLIPLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPTextEncode`、`KSampler`、`VAEDecode`、`VAELoader`、`CR Text`、`UNETLoader`、`LayerFilter: HDREffects`、`SaveImage`、`INTConstant`、`EmptyLatentImage`、`KSamplerAdvanced`、`VAEEncode`、`RH_LLMAPI_NODE`、`RH_LLMAPI_Pro_Node`、`InversionDemoLazyIndexSwitch`、`CheckpointLoaderSimple`、`Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
