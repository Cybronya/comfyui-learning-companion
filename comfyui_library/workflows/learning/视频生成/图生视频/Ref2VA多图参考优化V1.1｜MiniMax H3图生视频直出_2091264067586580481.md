---
key: 视频生成/图生视频/Ref2VA多图参考优化V1.1｜MiniMax H3图生视频直出_2091264067586580481.json
name: Ref2VA多图参考优化V1.1｜MiniMax H3图生视频直出_2091264067586580481
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Ref2VA多图参考优化V1.1｜MiniMax H3图生视频直出_2091264067586580481.json
hash: 70dfb16f89ad5c90
coverage: 0.916667
learned_at: 2026-10-16 22:30:42
nodes: [RHMiniMaxH3Ref2VATextEncoderLoader, RHMiniMaxH3Ref2VAModelLoader, RHMiniMaxH3Ref2VAVAELoader, LoadImage, RHMiniMaxH3DualSigmaSampler, LoadImage, RHMiniMaxH3Ref2VAImageReference, RHMiniMaxH3EmptyAVLatent, RHMiniMaxH3DecodeAV, CreateVideo, RHMiniMaxH3Ref2VAImageReference, RHMiniMaxH3Ref2VAImageReference, RHMiniMaxH3Ref2VAImageReference, LoadImage, RHMiniMaxH3Ref2VATarget, RHMiniMaxH3Ref2VAEncode, Label (rgthree), SaveVideo, LoadImage, 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Ref2VA多图参考优化V1.1｜MiniMax H3图生视频直出_2091264067586580481.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Ref2VA多图参考优化V1.1｜MiniMax H3图生视频直出_2091264067586580481.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `RHMiniMaxH3Ref2VATextEncoderLoader`
- `RHMiniMaxH3Ref2VAModelLoader`
- `RHMiniMaxH3Ref2VAVAELoader`
- `LoadImage`
- `RHMiniMaxH3DualSigmaSampler` ★核心
- `LoadImage`
- `RHMiniMaxH3Ref2VAImageReference`
- `RHMiniMaxH3EmptyAVLatent`
- `RHMiniMaxH3DecodeAV`
- `CreateVideo`
- `RHMiniMaxH3Ref2VAImageReference`
- `RHMiniMaxH3Ref2VAImageReference`
- `RHMiniMaxH3Ref2VAImageReference`
- `LoadImage`
- `RHMiniMaxH3Ref2VATarget`
- `RHMiniMaxH3Ref2VAEncode`
- `Label (rgthree)`
- `SaveVideo`
- `LoadImage`
- `孤海注释`
- `孤海注释`
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
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（44/48）

**有卡**：`RHMiniMaxH3Ref2VATextEncoderLoader`、`RHMiniMaxH3Ref2VAModelLoader`、`RHMiniMaxH3Ref2VAVAELoader`、`LoadImage`、`RHMiniMaxH3DualSigmaSampler`、`RHMiniMaxH3Ref2VAImageReference`、`RHMiniMaxH3EmptyAVLatent`、`RHMiniMaxH3DecodeAV`、`CreateVideo`、`RHMiniMaxH3Ref2VATarget`、`RHMiniMaxH3Ref2VAEncode`、`Label (rgthree)`、`SaveVideo`、`LoraLoaderModelOnly`、`UNETLoader`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`VAEDecode`、`VAELoader`、`CLIPLoader`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
