---
key: 视频生成/文生视频/4步lora加速版（批量短剧专用）Minimax_h3_导演台插件3.0万象AI_2085854413360558081.json
name: 4步lora加速版（批量短剧专用）Minimax_h3_导演台插件3.0万象AI_2085854413360558081
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/4步lora加速版（批量短剧专用）Minimax_h3_导演台插件3.0万象AI_2085854413360558081.json
hash: 1f46041e17548d78
coverage: 0.848485
learned_at: 2026-10-11 20:53:34
nodes: [LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, UNETLoader, CLIPLoader, solarL_SaveImagesToZip, VAELoader, CLIPTextEncode, CLIPTextEncode, JjkText, VAEDecode, EmptyLatentImage, Note, 孤海注释, 孤海注释, VAEDecodeAudio, VAEDecode, BasicScheduler, SamplerCustomAdvanced, VHS_VideoCombine, BasicGuider, KSamplerSelect, VAELoader, VAELoader, CLIPLoader, RandomNoise, LoadImage, PrimitiveStringMultiline, SFH3MultimodalDirector, UNETLoader, UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderBypassModelOnly]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/4步lora加速版（批量短剧专用）Minimax_h3_导演台插件3.0万象AI_2085854413360558081.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/4步lora加速版（批量短剧专用）Minimax_h3_导演台插件3.0万象AI_2085854413360558081.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（33 个）：
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `solarL_SaveImagesToZip`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `Note`
- `孤海注释`
- `孤海注释`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `RandomNoise`
- `LoadImage`
- `PrimitiveStringMultiline`
- `SFH3MultimodalDirector`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderBypassModelOnly` ★核心

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

覆盖率 **85%**（28/33）

**有卡**：`LoraLoaderModelOnly`、`KSampler`、`UNETLoader`、`CLIPLoader`、`solarL_SaveImagesToZip`、`VAELoader`、`CLIPTextEncode`、`VAEDecode`、`EmptyLatentImage`、`VAEDecodeAudio`、`BasicScheduler`、`SamplerCustomAdvanced`、`VHS_VideoCombine`、`BasicGuider`、`KSamplerSelect`、`RandomNoise`、`LoadImage`、`SFH3MultimodalDirector`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderBypassModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
