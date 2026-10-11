---
key: 视频生成/文生视频/MiniMax H3 Motion Context长视频生成工作流V2，文生视频图生视频方案_2103897957832683522.json
name: MiniMax H3 Motion Context长视频生成工作流V2，文生视频图生视频方案_2103897957832683522
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3 Motion Context长视频生成工作流V2，文生视频图生视频方案_2103897957832683522.json
hash: 72bcf31dce668bdd
coverage: 0.8125
learned_at: 2026-10-11 22:12:36
nodes: [ModelPreviewOverrideKJ, easy modelLoaderPack, ModelAttentionBackend, VAELoader, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderModelOnly, easy multitrackProject, ManualSigmas, KSamplerSelect, KSamplerSelect, BasicScheduler, easy multiTrackEditor, VAELoader, UNETLoader, CLIPLoader, easy multitrackProjectVideoCombine, SaveVideo, easy saveVideo, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, SaveImage]
patterns: [text_to_image]
missing: [easy modelLoaderPack, easy multiTrackEditor, easy multitrackProject, easy multitrackProjectVideoCombine, easy saveVideo]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `easy modelLoaderPack` 知识库中没有该节点类型的任何知识, 次要节点 `easy multiTrackEditor` 知识库中没有该节点类型的任何知识, 次要节点 `easy multitrackProject` 知识库中没有该节点类型的任何知识, 次要节点 `easy multitrackProjectVideoCombine` 知识库中没有该节点类型的任何知识, 次要节点 `easy saveVideo` 仅有 SaveImage 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/MiniMax H3 Motion Context长视频生成工作流V2，文生视频图生视频方案_2103897957832683522.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3 Motion Context长视频生成工作流V2，文生视频图生视频方案_2103897957832683522.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（48 个）：
- `ModelPreviewOverrideKJ`
- `easy modelLoaderPack`
- `ModelAttentionBackend`
- `VAELoader`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderModelOnly` ★核心
- `easy multitrackProject`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `easy multiTrackEditor`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `easy multitrackProjectVideoCombine`
- `SaveVideo`
- `easy saveVideo`
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

覆盖率 **81%**（39/48）

**有卡**：`ModelPreviewOverrideKJ`、`ModelAttentionBackend`、`VAELoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderModelOnly`、`ManualSigmas`、`KSamplerSelect`、`BasicScheduler`、`UNETLoader`、`CLIPLoader`、`SaveVideo`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`VAEDecode`、`SaveImage`

**缺卡**（5）：`easy modelLoaderPack`、`easy multiTrackEditor`、`easy multitrackProject`、`easy multitrackProjectVideoCombine`、`easy saveVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy modelLoaderPack` 知识库中没有该节点类型的任何知识
- 次要节点 `easy multiTrackEditor` 知识库中没有该节点类型的任何知识
- 次要节点 `easy multitrackProject` 知识库中没有该节点类型的任何知识
- 次要节点 `easy multitrackProjectVideoCombine` 知识库中没有该节点类型的任何知识
- 次要节点 `easy saveVideo` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
