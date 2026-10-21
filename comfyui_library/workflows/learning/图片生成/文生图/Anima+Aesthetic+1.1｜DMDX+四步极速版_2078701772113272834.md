---
key: 图片生成/文生图/Anima+Aesthetic+1.1｜DMDX+四步极速版_2078701772113272834.json
name: Anima+Aesthetic+1.1｜DMDX+四步极速版_2078701772113272834
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima+Aesthetic+1.1｜DMDX+四步极速版_2078701772113272834.json
hash: b9aa714508b25a08
coverage: 0.894737
learned_at: 2026-10-20 00:18:46
nodes: [PreviewImage, VAEDecode, SaveImage, XB_UNetNameBroadcaster, UNETLoader, ModelSamplingAuraFlow, LoraLoaderModelOnly, FluxResolutionNode, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, VAEDecode, SaveImage, PreviewImage, VAELoader, CLIPLoader, ClownsharKSampler_Beta]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4, "denoise": 1.0000000000000002, "height": 1024, "sampler_name": -1, "scheduler": 1, "seed": 0.5, "steps": "beta57", "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Anima+Aesthetic+1.1｜DMDX+四步极速版_2078701772113272834.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima+Aesthetic+1.1｜DMDX+四步极速版_2078701772113272834.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（19 个）：
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `XB_UNetNameBroadcaster`
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `FluxResolutionNode`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `VAELoader`
- `CLIPLoader`
- `ClownsharKSampler_Beta` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `0.5`
- `steps` = `beta57`
- `cfg` = `4`
- `sampler_name` = `-1`
- `scheduler` = `1`
- `denoise` = `1.0000000000000002`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`VAEDecode`、`SaveImage`、`XB_UNetNameBroadcaster`、`UNETLoader`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`FluxResolutionNode`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`VAELoader`、`CLIPLoader`、`ClownsharKSampler_Beta`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
