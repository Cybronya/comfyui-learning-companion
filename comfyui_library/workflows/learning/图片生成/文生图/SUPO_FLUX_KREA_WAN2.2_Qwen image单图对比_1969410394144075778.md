---
key: 图片生成/文生图/SUPO_FLUX_KREA_WAN2.2_Qwen image单图对比_1969410394144075778.json
name: SUPO_FLUX_KREA_WAN2.2_Qwen image单图对比_1969410394144075778
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/SUPO_FLUX_KREA_WAN2.2_Qwen image单图对比_1969410394144075778.json
hash: e6cbed66b4957108
coverage: 0.837838
learned_at: 2026-10-10 20:59:12
nodes: [ModelSamplingSD3, CLIPLoader, VAELoader, CLIPTextEncode, EmptyHunyuanLatentVideo, VAELoader, ModelSamplingAuraFlow, CLIPLoader, UNETLoader, UNETLoader, EmptySD3LatentImage, UNETLoader, PatchModelAddDownscale, PatchModelAddDownscale, PatchModelAddDownscale, KSampler, UNETLoader, PatchModelAddDownscale, Int, ModelSamplingFlux, BasicGuider, BasicScheduler, SamplerCustomAdvanced, VAEDecode, PreviewImage, AddLabel, PreviewImage, UNETLoader, PatchModelAddDownscale, ModelSamplingFlux, BasicGuider, BasicScheduler, SamplerCustomAdvanced, VAEDecode, PreviewImage, AddLabel, PreviewImage, UNETLoader, ModelSamplingFlux, BasicGuider, BasicScheduler, SamplerCustomAdvanced, PreviewImage, VAEDecode, PreviewImage, AddLabel, ModelSamplingSD3, PreviewImage, PreviewImage, VAEDecode, AddLabel, KSampler, VAEDecode, PreviewImage, CLIPTextEncode, CLIPTextEncode, VAELoader, Int, EmptyLatentImage, DualCLIPLoader, CLIPTextEncode, KSamplerSelect, DetailDaemonSamplerNode, Seed_, RandomNoise, PreviewImage, AddLabel, PreviewImage, PatchModelAddDownscale, CLIPTextEncode, KSampler, ImageBatchMulti, PreviewImage, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 3.5, "denoise": 1, "height": 512, "sampler_name": "res_2s", "scheduler": "beta57", "seed": 905514555295785, "steps": 25, "width": 512}
---

# 图片生成/文生图/SUPO_FLUX_KREA_WAN2.2_Qwen image单图对比_1969410394144075778.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/SUPO_FLUX_KREA_WAN2.2_Qwen image单图对比_1969410394144075778.json`

## 结构

**节点**（74 个）：
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `UNETLoader`
- `UNETLoader`
- `EmptySD3LatentImage`
- `UNETLoader`
- `PatchModelAddDownscale`
- `PatchModelAddDownscale`
- `PatchModelAddDownscale`
- `KSampler`
- `UNETLoader`
- `PatchModelAddDownscale`
- `Int`
- `ModelSamplingFlux`
- `BasicGuider`
- `BasicScheduler`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `PreviewImage`
- `AddLabel`
- `PreviewImage`
- `UNETLoader`
- `PatchModelAddDownscale`
- `ModelSamplingFlux`
- `BasicGuider`
- `BasicScheduler`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `PreviewImage`
- `AddLabel`
- `PreviewImage`
- `UNETLoader`
- `ModelSamplingFlux`
- `BasicGuider`
- `BasicScheduler`
- `SamplerCustomAdvanced`
- `PreviewImage`
- `VAEDecode`
- `PreviewImage`
- `AddLabel`
- `ModelSamplingSD3`
- `PreviewImage`
- `PreviewImage`
- `VAEDecode`
- `AddLabel`
- `KSampler`
- `VAEDecode`
- `PreviewImage`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `VAELoader`
- `Int`
- `EmptyLatentImage`
- `DualCLIPLoader`
- `CLIPTextEncode`
- `KSamplerSelect`
- `DetailDaemonSamplerNode`
- `Seed_`
- `RandomNoise`
- `PreviewImage`
- `AddLabel`
- `PreviewImage`
- `PatchModelAddDownscale`
- `CLIPTextEncode`
- `KSampler`
- `ImageBatchMulti`
- `PreviewImage`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `3.5`
- `denoise` = `1`
- `height` = `512`
- `sampler_name` = `res_2s`
- `scheduler` = `beta57`
- `seed` = `905514555295785`
- `steps` = `25`
- `width` = `512`

## 知识

覆盖率 **84%**（62/74）

**有卡**：`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`ModelSamplingAuraFlow`、`UNETLoader`、`EmptySD3LatentImage`、`PatchModelAddDownscale`、`KSampler`、`Int`、`ModelSamplingFlux`、`BasicGuider`、`BasicScheduler`、`SamplerCustomAdvanced`、`VAEDecode`、`PreviewImage`、`AddLabel`、`EmptyLatentImage`、`DualCLIPLoader`、`KSamplerSelect`
