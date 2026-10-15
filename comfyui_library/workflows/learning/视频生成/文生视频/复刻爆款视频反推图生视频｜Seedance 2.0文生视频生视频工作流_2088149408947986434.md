---
key: 视频生成/文生视频/复刻爆款视频反推图生视频｜Seedance 2.0文生视频生视频工作流_2088149408947986434.json
name: 复刻爆款视频反推图生视频｜Seedance 2.0文生视频生视频工作流_2088149408947986434
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/复刻爆款视频反推图生视频｜Seedance 2.0文生视频生视频工作流_2088149408947986434.json
hash: 05b5a10d3813f464
coverage: 0.864407
learned_at: 2026-10-15 22:48:25
nodes: [Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), RH_LLMAPI_Pro_Node, easy showAnything, RH_LLMAPI_Pro_Node, Fast Groups Bypasser (rgthree), SaveVideoNode, LoadVideo, Label (rgthree), SaveVideoNode, RH_RhartVideoSparkvideo20MiniMultimodalVideo, RH_RhartVideoSparkvideo20MultimodalVideo, Fast Groups Bypasser (rgthree), Label (rgthree), easy showAnything, VHS_LoadVideo, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), easy saveText, LoadImage, easy saveText, LoadImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/复刻爆款视频反推图生视频｜Seedance 2.0文生视频生视频工作流_2088149408947986434.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/复刻爆款视频反推图生视频｜Seedance 2.0文生视频生视频工作流_2088149408947986434.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（59 个）：
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `RH_LLMAPI_Pro_Node`
- `easy showAnything`
- `RH_LLMAPI_Pro_Node`
- `Fast Groups Bypasser (rgthree)`
- `SaveVideoNode`
- `LoadVideo`
- `Label (rgthree)`
- `SaveVideoNode`
- `RH_RhartVideoSparkvideo20MiniMultimodalVideo`
- `RH_RhartVideoSparkvideo20MultimodalVideo`
- `Fast Groups Bypasser (rgthree)`
- `Label (rgthree)`
- `easy showAnything`
- `VHS_LoadVideo`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `easy saveText`
- `LoadImage`
- `easy saveText`
- `LoadImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
- `CLIPTextEncode` ★核心
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

覆盖率 **86%**（51/59）

**有卡**：`Label (rgthree)`、`RH_LLMAPI_Pro_Node`、`SaveVideoNode`、`LoadVideo`、`RH_RhartVideoSparkvideo20MiniMultimodalVideo`、`RH_RhartVideoSparkvideo20MultimodalVideo`、`VHS_LoadVideo`、`easy saveText`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
