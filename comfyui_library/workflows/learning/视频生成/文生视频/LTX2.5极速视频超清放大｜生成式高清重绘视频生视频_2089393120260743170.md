---
key: 视频生成/文生视频/LTX2.5极速视频超清放大｜生成式高清重绘视频生视频_2089393120260743170.json
name: LTX2.5极速视频超清放大｜生成式高清重绘视频生视频_2089393120260743170
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.5极速视频超清放大｜生成式高清重绘视频生视频_2089393120260743170.json
hash: b80e72ae3c888fb8
coverage: 0.911111
learned_at: 2026-10-15 22:45:18
nodes: [LTXVLoopingSampler, CFGGuider, LTXVConditioning, VAEEncodeTiled, CreateVideo, LTXVSpatioTemporalTiledVAEDecode, UNETLoader, RandomNoise, KSamplerSelect, VAELoader, CLIPLoader, GetVideoComponents, LoadVideo, SaveVideo, Yuan_RTXVideoUpscaleH3, CLIPTextEncode, LoraLoaderModelOnly, ManualSigmas, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/LTX2.5极速视频超清放大｜生成式高清重绘视频生视频_2089393120260743170.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.5极速视频超清放大｜生成式高清重绘视频生视频_2089393120260743170.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `LTXVLoopingSampler` ★核心
- `CFGGuider`
- `LTXVConditioning`
- `VAEEncodeTiled` ★核心
- `CreateVideo`
- `LTXVSpatioTemporalTiledVAEDecode` ★核心
- `UNETLoader` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `VAELoader`
- `CLIPLoader`
- `GetVideoComponents`
- `LoadVideo`
- `SaveVideo`
- `Yuan_RTXVideoUpscaleH3`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `ManualSigmas`
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

覆盖率 **91%**（41/45）

**有卡**：`LTXVLoopingSampler`、`CFGGuider`、`LTXVConditioning`、`VAEEncodeTiled`、`CreateVideo`、`LTXVSpatioTemporalTiledVAEDecode`、`UNETLoader`、`RandomNoise`、`KSamplerSelect`、`VAELoader`、`CLIPLoader`、`GetVideoComponents`、`LoadVideo`、`SaveVideo`、`Yuan_RTXVideoUpscaleH3`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`ManualSigmas`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
