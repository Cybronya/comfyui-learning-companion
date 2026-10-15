---
key: 视频生成/文生视频/MiniMax H3_多参极简工作流V3.0（多参考长视频续接）_2094855892327026689.json
name: MiniMax H3_多参极简工作流V3.0（多参考长视频续接）_2094855892327026689
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3_多参极简工作流V3.0（多参考长视频续接）_2094855892327026689.json
hash: 6adf3eda35534505
coverage: 0.716667
learned_at: 2026-10-15 22:45:45
nodes: [孤海注释, 孤海注释, VAELoader, MiniMaxH3MemoryEfficientSageAttentionPatch, LTXVSeparateAVLatent, CLIPLoader, VAELoader, 孤海注释, SamplerCustomAdvanced, ConditioningZeroOut, VAEDecodeAudio, VAEDecode, ComfyMathExpression, RandomNoise, LoraLoaderModelOnly, UNETLoader, MiniMaxH3MotionContext, Seed (rgthree), BasicGuider, KSamplerSelect, BasicScheduler, CreateVideo, ResolutionSelector, MiniMaxH3MotionContextTrim, KSampler, MinimaxH3LatentUpscaler3D, Int, LoadVideo, LoadVideo, LoadImage, MarkdownNote, Fast Groups Bypasser (rgthree), MiniMaxH3ReferenceToVideo, LTXVConcatAVLatent, VAEDecode, VAEDecodeAudio, FlashVSRNode, VHS_VideoCombine, Fast Groups Bypasser (rgthree), 孤海注释, 孤海注释, 孤海注释, 孤海注释, 孤海注释, RH_LLMAPI_NODE, CR Text, PreviewAny, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, 孤海注释, Text Multiline, Fast Groups Bypasser (rgthree), LoadVideoUI, PreviewVideoNode, Text Multiline, PrimitiveFloat, LoadAudioUI, LoadAudioUI, Text Multiline, CS-MultiImageLoader]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.3, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 819327788865639, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/MiniMax H3_多参极简工作流V3.0（多参考长视频续接）_2094855892327026689.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3_多参极简工作流V3.0（多参考长视频续接）_2094855892327026689.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（60 个）：
- `孤海注释`
- `孤海注释`
- `VAELoader`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LTXVSeparateAVLatent`
- `CLIPLoader`
- `VAELoader`
- `孤海注释`
- `SamplerCustomAdvanced` ★核心
- `ConditioningZeroOut`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `ComfyMathExpression`
- `RandomNoise`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `MiniMaxH3MotionContext`
- `Seed (rgthree)`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `CreateVideo`
- `ResolutionSelector`
- `MiniMaxH3MotionContextTrim`
- `KSampler` ★核心
- `MinimaxH3LatentUpscaler3D`
- `Int`
- `LoadVideo`
- `LoadVideo`
- `LoadImage`
- `MarkdownNote`
- `Fast Groups Bypasser (rgthree)`
- `MiniMaxH3ReferenceToVideo`
- `LTXVConcatAVLatent`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `FlashVSRNode`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `RH_LLMAPI_NODE`
- `CR Text`
- `PreviewAny`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `孤海注释`
- `Text Multiline`
- `Fast Groups Bypasser (rgthree)`
- `LoadVideoUI`
- `PreviewVideoNode`
- `Text Multiline`
- `PrimitiveFloat`
- `LoadAudioUI`
- `LoadAudioUI`
- `Text Multiline`
- `CS-MultiImageLoader`

## 关键参数

- `seed` = `819327788865639`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `0.3`

## 知识

覆盖率 **72%**（43/60）

**有卡**：`VAELoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LTXVSeparateAVLatent`、`CLIPLoader`、`SamplerCustomAdvanced`、`ConditioningZeroOut`、`VAEDecodeAudio`、`VAEDecode`、`ComfyMathExpression`、`RandomNoise`、`LoraLoaderModelOnly`、`UNETLoader`、`MiniMaxH3MotionContext`、`Seed (rgthree)`、`BasicGuider`、`KSamplerSelect`、`BasicScheduler`、`CreateVideo`、`ResolutionSelector`、`MiniMaxH3MotionContextTrim`、`KSampler`、`MinimaxH3LatentUpscaler3D`、`Int`、`LoadVideo`、`LoadImage`、`MiniMaxH3ReferenceToVideo`、`LTXVConcatAVLatent`、`FlashVSRNode`、`VHS_VideoCombine`、`RH_LLMAPI_NODE`、`CR Text`、`Text Multiline`、`LoadVideoUI`、`PreviewVideoNode`、`LoadAudioUI`、`CS-MultiImageLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
