---
key: 视频生成/图生视频/MiniMax H3 Singularity V2 R2VA 去油抗飘图生视频工具_2114080323918192641.json
name: MiniMax H3 Singularity V2 R2VA 去油抗飘图生视频工具_2114080323918192641
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3 Singularity V2 R2VA 去油抗飘图生视频工具_2114080323918192641.json
hash: 812035d0e573017a
coverage: 0.597403
learned_at: 2026-10-26 22:12:18
nodes: [ComfyMathExpression, SetNode, PrimitiveNode, CLIPLoader, VAELoader, SetNode, ResolutionSelector, SetNode, GetNode, GetNode, ImageScaleToTotalPixels, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, SetNode, GetNode, GetNode, PrimitiveFloat, LoraLoaderModelOnly, SetNode, GetNode, GetNode, KSamplerSelect, GetNode, ConditioningZeroOut, GetNode, SetNode, BasicScheduler, VAEDecode, GetNode, VAEDecodeAudio, VHS_VideoCombine, SelfLiftH3Sampler, VAELoader, UNETLoader, LoadImage, SetNode, ModelAttentionBackend, BlockSparseAttention, PrimitiveStringMultiline, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/MiniMax H3 Singularity V2 R2VA 去油抗飘图生视频工具_2114080323918192641.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3 Singularity V2 R2VA 去油抗飘图生视频工具_2114080323918192641.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（77 个）：
- `ComfyMathExpression`
- `SetNode`
- `PrimitiveNode`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `ResolutionSelector`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageScaleToTotalPixels`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `PrimitiveFloat`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `ConditioningZeroOut`
- `GetNode`
- `SetNode`
- `BasicScheduler`
- `VAEDecode` ★核心
- `GetNode`
- `VAEDecodeAudio` ★核心
- `VHS_VideoCombine`
- `SelfLiftH3Sampler` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `LoadImage`
- `SetNode`
- `ModelAttentionBackend`
- `BlockSparseAttention`
- `PrimitiveStringMultiline`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
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

覆盖率 **60%**（46/77）

**有卡**：`ComfyMathExpression`、`CLIPLoader`、`VAELoader`、`ResolutionSelector`、`ImageScaleToTotalPixels`、`LoraLoaderModelOnly`、`KSamplerSelect`、`ConditioningZeroOut`、`BasicScheduler`、`VAEDecode`、`VAEDecodeAudio`、`VHS_VideoCombine`、`SelfLiftH3Sampler`、`UNETLoader`、`LoadImage`、`ModelAttentionBackend`、`BlockSparseAttention`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxH3ReferenceToVideo`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
