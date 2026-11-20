---
key: 平台全量/【阡陌】Qwen-Image-Edit-2509升级Plus版nunchaku加速证件照生成_1971036322481770497.json
name: 【阡陌】Qwen-Image-Edit-2509升级Plus版nunchaku加速证件照生成_1971036322481770497
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/【阡陌】Qwen-Image-Edit-2509升级Plus版nunchaku加速证件照生成_1971036322481770497.json
hash: 842ac737c2e40da1
coverage: 0.9375
learned_at: 2026-11-14 01:26:11
nodes: [VAEDecode, SaveImage, UNETLoader, ConditioningZeroOut, VAELoader, CLIPLoader, LoadImage, KSampler, Image Comparer (rgthree), LoraLoaderModelOnly, LoadImage, VAEEncode, EmptyLatentImage, NunchakuQwenImageDiTLoader, ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus_lrzjason]
patterns: [image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 2.5, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 137031707093058, "steps": 20, "width": 768}
---

# 平台全量/【阡陌】Qwen-Image-Edit-2509升级Plus版nunchaku加速证件照生成_1971036322481770497.json

> 来源文件 `comfyui_library/workflows/平台全量/【阡陌】Qwen-Image-Edit-2509升级Plus版nunchaku加速证件照生成_1971036322481770497.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（16 个）：
- `VAEDecode` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `VAELoader`
- `CLIPLoader`
- `LoadImage`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `VAEEncode` ★核心
- `EmptyLatentImage` ★核心
- `NunchakuQwenImageDiTLoader`
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEditPlus_lrzjason`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `137031707093058`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`VAEDecode`、`SaveImage`、`UNETLoader`、`ConditioningZeroOut`、`VAELoader`、`CLIPLoader`、`LoadImage`、`KSampler`、`LoraLoaderModelOnly`、`VAEEncode`、`EmptyLatentImage`、`NunchakuQwenImageDiTLoader`、`ModelSamplingAuraFlow`、`TextEncodeQwenImageEditPlus_lrzjason`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage
