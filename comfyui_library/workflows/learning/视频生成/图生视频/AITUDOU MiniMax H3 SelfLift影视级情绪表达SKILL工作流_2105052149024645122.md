---
key: 视频生成/图生视频/AITUDOU MiniMax H3 SelfLift影视级情绪表达SKILL工作流_2105052149024645122.json
name: AITUDOU MiniMax H3 SelfLift影视级情绪表达SKILL工作流_2105052149024645122
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/AITUDOU MiniMax H3 SelfLift影视级情绪表达SKILL工作流_2105052149024645122.json
hash: ebcdd5b6e618bbfe
coverage: 0.563636
learned_at: 2026-10-17 02:43:39
nodes: [UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, SolAttnMiniMax, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, SetNode, VAELoader, SetNode, SetNode, LoadImage, LoadImage, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, LoadImage, LoadImage, SetNode, SetNode, LoadImage, LoadImage, LoadImage, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, ConditioningZeroOut, GetNode, GetNode, SetNode, GetNode, KSamplerSelect, GetNode, BasicScheduler, H3SigmaRefiner, GetNode, GetNode, VAEDecodeAudio, SelfLiftH3Sampler, ComfyMathExpression, SetNode, GetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, CLIPLoader, SetNode, MiniMaxH3ReferenceToVideo, VAEDecode, SetNode, Float, ResolutionSelector, VHS_VideoCombine, LoadImage, Fast Groups Bypasser (rgthree), Text, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/AITUDOU MiniMax H3 SelfLift影视级情绪表达SKILL工作流_2105052149024645122.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/AITUDOU MiniMax H3 SelfLift影视级情绪表达SKILL工作流_2105052149024645122.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（110 个）：
- `UNETLoader` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `SolAttnMiniMax`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `SetNode`
- `VAELoader`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ConditioningZeroOut`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `BasicScheduler`
- `H3SigmaRefiner`
- `GetNode`
- `GetNode`
- `VAEDecodeAudio` ★核心
- `SelfLiftH3Sampler` ★核心
- `ComfyMathExpression`
- `SetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `MiniMaxH3ReferenceToVideo`
- `VAEDecode` ★核心
- `SetNode`
- `Float`
- `ResolutionSelector`
- `VHS_VideoCombine`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Text`
- `LoadImage`
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

覆盖率 **56%**（62/110）

**有卡**：`UNETLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ModelAttentionBackend`、`SolAttnMiniMax`、`LoraLoaderModelOnly`、`VAELoader`、`LoadImage`、`ConditioningZeroOut`、`KSamplerSelect`、`BasicScheduler`、`H3SigmaRefiner`、`VAEDecodeAudio`、`SelfLiftH3Sampler`、`ComfyMathExpression`、`CLIPLoader`、`MiniMaxH3ReferenceToVideo`、`VAEDecode`、`Float`、`ResolutionSelector`、`VHS_VideoCombine`、`Text`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
