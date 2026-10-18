---
key: 视频生成/图生视频/MinimaxH3文戏V1.0版 图生视频自然质感直出_2110365604116000770.json
name: MinimaxH3文戏V1.0版 图生视频自然质感直出_2110365604116000770
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MinimaxH3文戏V1.0版 图生视频自然质感直出_2110365604116000770.json
hash: 0537695cdaf73bbd
coverage: 0.774194
learned_at: 2026-10-18 00:23:42
nodes: [SetNode, SetNode, SetNode, SetNode, easy clearCacheAll, ConditioningZeroOut, GetNode, GetNode, H3SigmaRefiner, FeiHouEasyH3RHLoader, SetNode, LoraLoaderModelOnly, FeiHouEasyH3RHLoader, FeiHouEasyH3RHOutput, GetNode, MiniMaxH3SemanticBridgeApplyT8, LoraLoaderModelOnly, ModelAttentionBackend, LoraLoaderModelOnly, ModelPreviewOverrideKJ, MiniMaxH3SemanticBridgeConfigT8, GetNode, VAEDecodeAudio, GetNode, VAEDecode, VHS_VideoCombine, RunningHub Deepcleaner, VRAM_Debug, FeiHouEasyH3RH, BasicScheduler, KSamplerSelect, SelfLiftAvatarH3Sampler, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/MinimaxH3文戏V1.0版 图生视频自然质感直出_2110365604116000770.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MinimaxH3文戏V1.0版 图生视频自然质感直出_2110365604116000770.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（62 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy clearCacheAll`
- `ConditioningZeroOut`
- `GetNode`
- `GetNode`
- `H3SigmaRefiner`
- `FeiHouEasyH3RHLoader`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `FeiHouEasyH3RHLoader`
- `FeiHouEasyH3RHOutput`
- `GetNode`
- `MiniMaxH3SemanticBridgeApplyT8`
- `LoraLoaderModelOnly` ★核心
- `ModelAttentionBackend`
- `LoraLoaderModelOnly` ★核心
- `ModelPreviewOverrideKJ`
- `MiniMaxH3SemanticBridgeConfigT8`
- `GetNode`
- `VAEDecodeAudio` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `RunningHub Deepcleaner`
- `VRAM_Debug`
- `FeiHouEasyH3RH`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `SelfLiftAvatarH3Sampler` ★核心
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
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
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
- `Note`
- `SaveImage`

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

覆盖率 **77%**（48/62）

**有卡**：`easy clearCacheAll`、`ConditioningZeroOut`、`H3SigmaRefiner`、`FeiHouEasyH3RHLoader`、`LoraLoaderModelOnly`、`FeiHouEasyH3RHOutput`、`MiniMaxH3SemanticBridgeApplyT8`、`ModelAttentionBackend`、`ModelPreviewOverrideKJ`、`MiniMaxH3SemanticBridgeConfigT8`、`VAEDecodeAudio`、`VAEDecode`、`VHS_VideoCombine`、`RunningHub Deepcleaner`、`VRAM_Debug`、`FeiHouEasyH3RH`、`BasicScheduler`、`KSamplerSelect`、`SelfLiftAvatarH3Sampler`、`UNETLoader`、`KSampler`、`CLIPTextEncode`、`CLIPLoader`、`EmptyLatentImage`、`VAELoader`、`solarL_SaveImagesToZip`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
