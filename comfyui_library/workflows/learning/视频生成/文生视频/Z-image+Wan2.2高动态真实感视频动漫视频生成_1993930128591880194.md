---
key: 视频生成/文生视频/Z-image+Wan2.2高动态真实感视频动漫视频生成_1993930128591880194.json
name: Z-image+Wan2.2高动态真实感视频动漫视频生成_1993930128591880194
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Z-image+Wan2.2高动态真实感视频动漫视频生成_1993930128591880194.json
hash: b8b8004004edb4ed
coverage: 0.941176
learned_at: 2026-10-15 22:47:17
nodes: [UNETLoader, CLIPLoader, ConditioningZeroOut, VAELoader, CLIPTextEncode, KSampler, EmptyLatentImage, VAEDecode, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, PrimitiveInt, ApplySageAttention, ApplySageAttention, WanMoeKSampler, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, CLIPVisionLoader, LoraLoaderModelOnly, SimpleMath+, CLIPVisionEncode, UNETLoader, PainterI2V, CR Text, PrimitiveInt, VHS_VideoCombine, VAEDecode, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 8, "denoise": "euler", "height": 1536, "sampler_name": 1, "scheduler": 1, "seed": 0.875, "steps": "randomize", "width": 1024}
---

# 视频生成/文生视频/Z-image+Wan2.2高动态真实感视频动漫视频生成_1993930128591880194.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Z-image+Wan2.2高动态真实感视频动漫视频生成_1993930128591880194.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（34 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `ConditioningZeroOut`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `PrimitiveInt`
- `ApplySageAttention`
- `ApplySageAttention`
- `WanMoeKSampler` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `LoraLoaderModelOnly` ★核心
- `SimpleMath+`
- `CLIPVisionEncode`
- `UNETLoader` ★核心
- `PainterI2V`
- `CR Text`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `0.875`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（32/34）

**有卡**：`UNETLoader`、`CLIPLoader`、`ConditioningZeroOut`、`VAELoader`、`CLIPTextEncode`、`KSampler`、`EmptyLatentImage`、`VAEDecode`、`ModelSamplingSD3`、`ApplySageAttention`、`WanMoeKSampler`、`LoraLoaderModelOnly`、`CLIPVisionLoader`、`SimpleMath+`、`CLIPVisionEncode`、`PainterI2V`、`CR Text`、`VHS_VideoCombine`、`ImageFromBatch+`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
