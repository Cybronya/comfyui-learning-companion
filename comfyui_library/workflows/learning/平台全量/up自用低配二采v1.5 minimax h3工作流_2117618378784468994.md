---
key: 平台全量/up自用低配二采v1.5 minimax h3工作流_2117618378784468994.json
name: up自用低配二采v1.5 minimax h3工作流_2117618378784468994
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/up自用低配二采v1.5 minimax h3工作流_2117618378784468994.json
hash: c4ce66f3a855613f
coverage: 0.911765
learned_at: 2026-11-14 01:18:28
nodes: [BasicGuider, RandomNoise, KSamplerSelect, VAELoader, VAELoader, LTXVConcatAVLatent, LTXVSeparateAVLatent, VAEDecode, VAEDecodeAudio, LoadAudio, Label (rgthree), Label (rgthree), Label (rgthree), MiniMaxH3MemoryEfficientSageAttentionPatch, Label (rgthree), Label (rgthree), VHS_LoadVideo, Label (rgthree), Label (rgthree), Label (rgthree), Fast Groups Bypasser (rgthree), LoadImage, Fast Bypasser (rgthree), MiniMaxH3SigmaShift, VAEDecodeAudio, Fast Bypasser (rgthree), LoadImage, LoadImage, LoadAudio, Fast Groups Bypasser (rgthree), ConditioningZeroOut, LoadImage, Fast Bypasser (rgthree), Seed (rgthree), ModelAttentionBackend, MinimaxH3LatentUpscaler3D, FloatConstant, VAEDecode, CLIPLoader, MiniMaxH3ReferenceToVideo, LoadImage, LoadAudio, Fast Bypasser (rgthree), INTConstant, Label (rgthree), PrimitiveFloat, VHS_VideoCombine, VHS_VideoCombine, Fast Groups Bypasser (rgthree), LoadImage, MarkdownNote, VRGDG_VideoCompareSlider, ResolutionSelector, ComfyMathExpression, SamplerCustomAdvanced, BlockSparseAttention, LoraLoaderModelOnly, BasicScheduler, MMH3TemporalSplitParams, MMH3UltimateUpscale, Reroute, 1b8be6e1-aed6-4837-86b8-ed822f6269ee, UNETLoader, VRAM_Debug, ModelPreviewOverrideKJ, Label (rgthree), Label (rgthree), Lora Loader Stack (rgthree)]
patterns: []
missing: []
---

# 平台全量/up自用低配二采v1.5 minimax h3工作流_2117618378784468994.json

> 来源文件 `comfyui_library/workflows/平台全量/up自用低配二采v1.5 minimax h3工作流_2117618378784468994.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（68 个）：
- `BasicGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `VAELoader`
- `VAELoader`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `LoadAudio`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `Label (rgthree)`
- `Label (rgthree)`
- `VHS_LoadVideo`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `Fast Bypasser (rgthree)`
- `MiniMaxH3SigmaShift`
- `VAEDecodeAudio` ★核心
- `Fast Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadAudio`
- `Fast Groups Bypasser (rgthree)`
- `ConditioningZeroOut`
- `LoadImage`
- `Fast Bypasser (rgthree)`
- `Seed (rgthree)`
- `ModelAttentionBackend`
- `MinimaxH3LatentUpscaler3D`
- `FloatConstant`
- `VAEDecode` ★核心
- `CLIPLoader`
- `MiniMaxH3ReferenceToVideo`
- `LoadImage`
- `LoadAudio`
- `Fast Bypasser (rgthree)`
- `INTConstant`
- `Label (rgthree)`
- `PrimitiveFloat`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `MarkdownNote`
- `VRGDG_VideoCompareSlider`
- `ResolutionSelector`
- `ComfyMathExpression`
- `SamplerCustomAdvanced` ★核心
- `BlockSparseAttention`
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `MMH3TemporalSplitParams`
- `MMH3UltimateUpscale`
- `Reroute`
- `1b8be6e1-aed6-4837-86b8-ed822f6269ee`
- `UNETLoader` ★核心
- `VRAM_Debug`
- `ModelPreviewOverrideKJ`
- `Label (rgthree)`
- `Label (rgthree)`
- `Lora Loader Stack (rgthree)`

## 知识

覆盖率 **91%**（62/68）

**有卡**：`BasicGuider`、`RandomNoise`、`KSamplerSelect`、`VAELoader`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`VAEDecode`、`VAEDecodeAudio`、`LoadAudio`、`Label (rgthree)`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`VHS_LoadVideo`、`LoadImage`、`Fast Bypasser (rgthree)`、`MiniMaxH3SigmaShift`、`ConditioningZeroOut`、`Seed (rgthree)`、`ModelAttentionBackend`、`MinimaxH3LatentUpscaler3D`、`FloatConstant`、`CLIPLoader`、`MiniMaxH3ReferenceToVideo`、`INTConstant`、`VHS_VideoCombine`、`VRGDG_VideoCompareSlider`、`ResolutionSelector`、`ComfyMathExpression`、`SamplerCustomAdvanced`、`BlockSparseAttention`、`LoraLoaderModelOnly`、`BasicScheduler`、`MMH3TemporalSplitParams`、`MMH3UltimateUpscale`、`1b8be6e1-aed6-4837-86b8-ed822f6269ee`、`UNETLoader`、`VRAM_Debug`、`ModelPreviewOverrideKJ`、`Lora Loader Stack (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader
