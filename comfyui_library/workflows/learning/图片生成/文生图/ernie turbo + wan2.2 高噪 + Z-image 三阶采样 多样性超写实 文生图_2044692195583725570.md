---
key: 图片生成/文生图/ernie turbo + wan2.2 高噪 + Z-image 三阶采样 多样性超写实 文生图_2044692195583725570.json
name: ernie turbo + wan2.2 高噪 + Z-image 三阶采样 多样性超写实 文生图_2044692195583725570
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/ernie turbo + wan2.2 高噪 + Z-image 三阶采样 多样性超写实 文生图_2044692195583725570.json
hash: eb736383c93193fa
coverage: 0.821429
learned_at: 2026-10-21 02:56:44
nodes: [LoraLoaderModelOnly, PathchSageAttentionKJ, CLIPLoader, CLIPTextEncode, LoraLoaderModelOnly, CLIPTextEncode, VAELoader, KSampler, Note, CLIPLoader, INTConstant, VAELoader, ModelSamplingSD3, EmptyLatentImage, VAEDecode, CR Text, VAEEncode, UNETLoader, CheckpointLoaderSimple, UNETLoader, CLIPTextEncode, InversionDemoLazyIndexSwitch, LoraLoaderModelOnly, CLIPLoader, CLIPTextEncode, CLIPTextEncode, VAEEncode, PreviewImage, KSamplerAdvanced, PreviewImage, INTConstant, Note, INTConstant, Note, INTConstant, INTConstant, INTConstant, Text, Note, Note, Note, Note, LoraLoaderModelOnly, CLIPTextEncode, KSamplerAdvanced, VAEDecode, VAELoader, RH_LLMAPI_Pro_Node, RH_LLMAPI_NODE, InversionDemoLazyIndexSwitch, easy showAnything, CR Text, INTConstant, CheckpointLoaderSimple, SaveImage, VAEDecode]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 6, "cfg": 10, "checkpoint": "redcraft_ernieRedmix.safetensors", "denoise": "sgm_uniform", "height": 1536, "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize", "width": 960}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/ernie turbo + wan2.2 高噪 + Z-image 三阶采样 多样性超写实 文生图_2044692195583725570.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/ernie turbo + wan2.2 高噪 + Z-image 三阶采样 多样性超写实 文生图_2044692195583725570.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（56 个）：
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `KSampler` ★核心
- `Note`
- `CLIPLoader`
- `INTConstant`
- `VAELoader`
- `ModelSamplingSD3`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `CR Text`
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `CheckpointLoaderSimple` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `InversionDemoLazyIndexSwitch`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `PreviewImage`
- `KSamplerAdvanced` ★核心
- `PreviewImage`
- `INTConstant`
- `Note`
- `INTConstant`
- `Note`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `Text`
- `Note`
- `Note`
- `Note`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `RH_LLMAPI_Pro_Node`
- `RH_LLMAPI_NODE`
- `InversionDemoLazyIndexSwitch`
- `easy showAnything`
- `CR Text`
- `INTConstant`
- `CheckpointLoaderSimple` ★核心
- `SaveImage`
- `VAEDecode` ★核心

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
- `batch_size` = `6`
- `checkpoint` = `redcraft_ernieRedmix.safetensors`

## 知识

覆盖率 **82%**（46/56）

**有卡**：`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`KSampler`、`INTConstant`、`ModelSamplingSD3`、`EmptyLatentImage`、`VAEDecode`、`CR Text`、`VAEEncode`、`UNETLoader`、`CheckpointLoaderSimple`、`InversionDemoLazyIndexSwitch`、`KSamplerAdvanced`、`Text`、`RH_LLMAPI_Pro_Node`、`RH_LLMAPI_NODE`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
