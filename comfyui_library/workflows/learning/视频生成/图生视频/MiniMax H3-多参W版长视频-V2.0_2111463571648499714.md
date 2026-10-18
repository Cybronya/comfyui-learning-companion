---
key: 视频生成/图生视频/MiniMax H3-多参W版长视频-V2.0_2111463571648499714.json
name: MiniMax H3-多参W版长视频-V2.0_2111463571648499714
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3-多参W版长视频-V2.0_2111463571648499714.json
hash: c324297b2074bfb8
coverage: 0.942857
learned_at: 2026-10-18 00:43:29
nodes: [KSamplerSelect, MiniMaxH3ChainLoopStart, MiniMaxH3ChainCurrent, RandomNoise, MiniMaxH3ReferenceToVideo, MiniMaxH3ChainContext, BasicGuider, BasicScheduler, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, MiniMaxH3ChainPlanModern, MiniMaxH3ChainManifestLoad, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ChainAssemble, MiniMaxH3ChainSegmentSave, MiniMaxH3ChainLoopEnd, MiniMaxH3SigmaShift, CLIPLoader, VAELoader, VAELoader, UNETLoader, LoraLoaderModelOnly, LoadImage, LoadImage, MiniMaxH3LoopTrim, MiniMaxH3ChainScenePromptEditor, MarkdownNote, ResolutionSelector, PrimitiveFloat, MiniMaxH3ChainReview, MiniMaxH3ChainAssemble, easy saveText, LoadImage, MiniMaxH3ChainPlan]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax H3-多参W版长视频-V2.0_2111463571648499714.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3-多参W版长视频-V2.0_2111463571648499714.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（35 个）：
- `KSamplerSelect` ★核心
- `MiniMaxH3ChainLoopStart`
- `MiniMaxH3ChainCurrent`
- `RandomNoise`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3ChainContext`
- `BasicGuider`
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `MiniMaxH3ChainPlanModern`
- `MiniMaxH3ChainManifestLoad`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ChainAssemble`
- `MiniMaxH3ChainSegmentSave`
- `MiniMaxH3ChainLoopEnd`
- `MiniMaxH3SigmaShift`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `MiniMaxH3LoopTrim`
- `MiniMaxH3ChainScenePromptEditor`
- `MarkdownNote`
- `ResolutionSelector`
- `PrimitiveFloat`
- `MiniMaxH3ChainReview`
- `MiniMaxH3ChainAssemble`
- `easy saveText`
- `LoadImage`
- `MiniMaxH3ChainPlan`

## 知识

覆盖率 **94%**（33/35）

**有卡**：`KSamplerSelect`、`MiniMaxH3ChainLoopStart`、`MiniMaxH3ChainCurrent`、`RandomNoise`、`MiniMaxH3ReferenceToVideo`、`MiniMaxH3ChainContext`、`BasicGuider`、`BasicScheduler`、`SamplerCustomAdvanced`、`VAEDecode`、`VAEDecodeAudio`、`MiniMaxH3ChainPlanModern`、`MiniMaxH3ChainManifestLoad`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxH3ChainAssemble`、`MiniMaxH3ChainSegmentSave`、`MiniMaxH3ChainLoopEnd`、`MiniMaxH3SigmaShift`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`、`MiniMaxH3LoopTrim`、`MiniMaxH3ChainScenePromptEditor`、`ResolutionSelector`、`MiniMaxH3ChainReview`、`easy saveText`、`MiniMaxH3ChainPlan`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
