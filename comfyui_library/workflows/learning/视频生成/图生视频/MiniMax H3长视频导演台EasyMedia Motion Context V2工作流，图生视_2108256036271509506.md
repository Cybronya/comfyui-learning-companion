---
key: 视频生成/图生视频/MiniMax H3长视频导演台EasyMedia Motion Context V2工作流，图生视_2108256036271509506.json
name: MiniMax H3长视频导演台EasyMedia Motion Context V2工作流，图生视_2108256036271509506
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3长视频导演台EasyMedia Motion Context V2工作流，图生视_2108256036271509506.json
hash: bd6e0457222c98df
coverage: 0.932432
learned_at: 2026-10-17 22:18:16
nodes: [ManualSigmas, KSamplerSelect, KSamplerSelect, BasicScheduler, MiniMaxH3MemoryEfficientSageAttentionPatch, CLIPLoader, UNETLoader, VAELoader, VAELoader, LoraLoaderModelOnly, easy modelLoaderPack, ModelPreviewOverrideKJ, ModelAttentionBackend, SaveVideo, easy multitrackProjectVideoCombine, easy saveVideo, easy multitrackProject, easy multiTrackEditor, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/MiniMax H3长视频导演台EasyMedia Motion Context V2工作流，图生视_2108256036271509506.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3长视频导演台EasyMedia Motion Context V2工作流，图生视_2108256036271509506.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（74 个）：
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `easy modelLoaderPack`
- `ModelPreviewOverrideKJ`
- `ModelAttentionBackend`
- `SaveVideo`
- `easy multitrackProjectVideoCombine`
- `easy saveVideo`
- `easy multitrackProject`
- `easy multiTrackEditor`
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
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `SaveImage`
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
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
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

覆盖率 **93%**（69/74）

**有卡**：`ManualSigmas`、`KSamplerSelect`、`BasicScheduler`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`LoraLoaderModelOnly`、`easy modelLoaderPack`、`ModelPreviewOverrideKJ`、`ModelAttentionBackend`、`SaveVideo`、`easy multitrackProjectVideoCombine`、`easy saveVideo`、`easy multitrackProject`、`easy multiTrackEditor`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
