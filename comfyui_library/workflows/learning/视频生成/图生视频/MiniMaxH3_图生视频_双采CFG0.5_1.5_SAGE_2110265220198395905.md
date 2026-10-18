---
key: 视频生成/图生视频/MiniMaxH3_图生视频_双采CFG0.5_1.5_SAGE_2110265220198395905.json
name: MiniMaxH3_图生视频_双采CFG0.5_1.5_SAGE_2110265220198395905
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMaxH3_图生视频_双采CFG0.5_1.5_SAGE_2110265220198395905.json
hash: 0f7e72cc8e9912d8
coverage: 0.9375
learned_at: 2026-10-18 00:23:29
nodes: [PathchSageAttentionKJ, BasicScheduler, VAEDecode, SamplerCustomAdvanced, MiniMaxLowVRAMAttention, RandomNoise, KSamplerSelect, CFGGuider, MiniMaxH3SigmaShift, LTXVSeparateAVLatent, VAEDecodeAudio, VAELoader, CreateVideo, LTXVConcatAVLatent, SaveVideo, SamplerCustomAdvanced, VRAM_Debug, VRAM_Debug, SplitSigmas, LoraLoaderModelOnly, ConditioningZeroOut, CFGGuider, MarkdownNote, UNETLoader, CLIPLoader, VAELoader, ComfyMathExpression, PrimitiveFloat, LoadImage, LoadImage, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMaxH3_图生视频_双采CFG0.5_1.5_SAGE_2110265220198395905.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMaxH3_图生视频_双采CFG0.5_1.5_SAGE_2110265220198395905.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `PathchSageAttentionKJ`
- `BasicScheduler`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `MiniMaxLowVRAMAttention`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `MiniMaxH3SigmaShift`
- `LTXVSeparateAVLatent`
- `VAEDecodeAudio` ★核心
- `VAELoader`
- `CreateVideo`
- `LTXVConcatAVLatent`
- `SaveVideo`
- `SamplerCustomAdvanced` ★核心
- `VRAM_Debug`
- `VRAM_Debug`
- `SplitSigmas`
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `CFGGuider`
- `MarkdownNote`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `LoadImage`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`

## 知识

覆盖率 **94%**（30/32）

**有卡**：`PathchSageAttentionKJ`、`BasicScheduler`、`VAEDecode`、`SamplerCustomAdvanced`、`MiniMaxLowVRAMAttention`、`RandomNoise`、`KSamplerSelect`、`CFGGuider`、`MiniMaxH3SigmaShift`、`LTXVSeparateAVLatent`、`VAEDecodeAudio`、`VAELoader`、`CreateVideo`、`LTXVConcatAVLatent`、`SaveVideo`、`VRAM_Debug`、`SplitSigmas`、`LoraLoaderModelOnly`、`ConditioningZeroOut`、`UNETLoader`、`CLIPLoader`、`ComfyMathExpression`、`LoadImage`、`MiniMaxH3ReferenceToVideo`、`MinimaxH3LatentUpscaler3D`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、CFGGuider
