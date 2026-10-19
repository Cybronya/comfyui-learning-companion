---
key: 图片生成/文生图/Z-Image-De-Turbo去蒸馏和蒸馏版-文生图对比-Z-Image-Turbo_1997838656700354562.json
name: Z-Image-De-Turbo去蒸馏和蒸馏版-文生图对比-Z-Image-Turbo_1997838656700354562
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image-De-Turbo去蒸馏和蒸馏版-文生图对比-Z-Image-Turbo_1997838656700354562.json
hash: 86cea54b748e553e
coverage: 0.818182
learned_at: 2026-10-19 21:47:00
nodes: [UNETLoader, CLIPLoader, LayerUtility: PurgeVRAM, UNETLoader, ConditioningZeroOut, VAELoader, Anything Everywhere, GetNode, GetNode, EmptyLatentImage, KSampler, MuyeTextEditOutput, MuyeTextEditOutput, VAEDecode, Seed_, SetNode, KSampler, SaveImage, CR Overlay Text, CR Overlay Text, easy imageConcat, VAEDecode, SaveImage, SaveImage, SaveImage, easy imageConcat, LoraLoaderModelOnly, LoadImage, LoraLoaderModelOnly, PrimitiveNode, PrimitiveFloat, CLIPTextEncode, Text]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1680, "sampler_name": "dpmpp_2m_sde", "scheduler": "sgm_uniform", "seed": 243292566267486, "steps": 10, "width": 1080}
---

# 图片生成/文生图/Z-Image-De-Turbo去蒸馏和蒸馏版-文生图对比-Z-Image-Turbo_1997838656700354562.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image-De-Turbo去蒸馏和蒸馏版-文生图对比-Z-Image-Turbo_1997838656700354562.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `LayerUtility: PurgeVRAM`
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `VAELoader`
- `Anything Everywhere`
- `GetNode`
- `GetNode`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `MuyeTextEditOutput`
- `MuyeTextEditOutput`
- `VAEDecode` ★核心
- `Seed_`
- `SetNode`
- `KSampler` ★核心
- `SaveImage`
- `CR Overlay Text`
- `CR Overlay Text`
- `easy imageConcat`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `easy imageConcat`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveNode`
- `PrimitiveFloat`
- `CLIPTextEncode` ★核心
- `Text`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1080`
- `height` = `1680`
- `batch_size` = `1`
- `seed` = `243292566267486`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2m_sde`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **82%**（27/33）

**有卡**：`UNETLoader`、`CLIPLoader`、`LayerUtility: PurgeVRAM`、`ConditioningZeroOut`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`MuyeTextEditOutput`、`VAEDecode`、`Seed_`、`SaveImage`、`CR Overlay Text`、`easy imageConcat`、`LoraLoaderModelOnly`、`LoadImage`、`CLIPTextEncode`、`Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、SaveImage
