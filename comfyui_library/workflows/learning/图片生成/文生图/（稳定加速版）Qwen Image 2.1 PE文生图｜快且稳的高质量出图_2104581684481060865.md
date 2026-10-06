---
key: 图片生成/文生图/（稳定加速版）Qwen Image 2.1 PE文生图｜快且稳的高质量出图_2104581684481060865.json
name: （稳定加速版）Qwen Image 2.1 PE文生图｜快且稳的高质量出图_2104581684481060865
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/（稳定加速版）Qwen Image 2.1 PE文生图｜快且稳的高质量出图_2104581684481060865.json
hash: 8b8b5ea7627efadc
coverage: 0.884058
learned_at: 2026-10-07 02:03:41
nodes: [CLIPLoader, VAELoader, QwenImage21Cache, CR Prompt Text, easy showAnything, TextEncodeQwenImage21, EmptyLatentImage, ResolutionSelector, ComfySwitchNode, QwenPERewriteT8, easy cleanGpuUsed, SaveImage, QwenImage21BlockCacheT8, QwenImage21SageAttentionT8, UNETLoader, QwenImage21SpectrumT8, KSampler, KSamplerSelect, ManualSigmas, VHS_VideoCombine, LTXVConcatAVLatent, VAEDecode, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEEncode, VAEDecode, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [easy cleanGpuUsed, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/（稳定加速版）Qwen Image 2.1 PE文生图｜快且稳的高质量出图_2104581684481060865.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/（稳定加速版）Qwen Image 2.1 PE文生图｜快且稳的高质量出图_2104581684481060865.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `CR Prompt Text`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `ComfySwitchNode`
- `QwenPERewriteT8`
- `easy cleanGpuUsed`
- `SaveImage`
- `QwenImage21BlockCacheT8`
- `QwenImage21SageAttentionT8`
- `UNETLoader` ★核心
- `QwenImage21SpectrumT8`
- `KSampler` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `VHS_VideoCombine`
- `LTXVConcatAVLatent`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
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

覆盖率 **88%**（61/69）

**有卡**：`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`ResolutionSelector`、`QwenPERewriteT8`、`SaveImage`、`QwenImage21BlockCacheT8`、`QwenImage21SageAttentionT8`、`UNETLoader`、`QwenImage21SpectrumT8`、`KSampler`、`KSamplerSelect`、`ManualSigmas`、`VHS_VideoCombine`、`LTXVConcatAVLatent`、`VAEDecode`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`VAEEncode`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**缺卡**（2）：`easy cleanGpuUsed`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
