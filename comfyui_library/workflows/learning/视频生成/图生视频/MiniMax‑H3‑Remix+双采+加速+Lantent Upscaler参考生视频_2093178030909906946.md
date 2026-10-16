---
key: 视频生成/图生视频/MiniMax‑H3‑Remix+双采+加速+Lantent Upscaler参考生视频_2093178030909906946.json
name: MiniMax‑H3‑Remix+双采+加速+Lantent Upscaler参考生视频_2093178030909906946
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax‑H3‑Remix+双采+加速+Lantent Upscaler参考生视频_2093178030909906946.json
hash: 126bfb5c87a26feb
coverage: 0.809524
learned_at: 2026-10-16 23:42:18
nodes: [MiniMaxH3DualClockSamplerT8, SamplerCustomAdvanced, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, ComfyMathExpression, MarkdownNote, VAELoader, SolAttnMiniMax, ModelAttentionBackend, BasicGuider, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, MiniMaxH3AudioConditioningT8, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, BasicGuider, MiniMaxH3AudioConditioningT8, MiniMaxH3AVDecodeT8, VHS_VideoCombine, MiniMaxH3TwoPassDetailMixerT8Advanced, VAELoader, CLIPLoader, UNETLoader, SamplerCustomAdvanced, LoraLoaderBypassModelOnly, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CR Prompt Text, MiniMaxH3LearnedLatentUpscaleT8Advanced, PrimitiveFloat, PrimitiveFloat, ResolutionSelector]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax‑H3‑Remix+双采+加速+Lantent Upscaler参考生视频_2093178030909906946.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax‑H3‑Remix+双采+加速+Lantent Upscaler参考生视频_2093178030909906946.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Process → Other

**节点**（42 个）：
- `MiniMaxH3DualClockSamplerT8` ★核心
- `SamplerCustomAdvanced` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `ComfyMathExpression`
- `MarkdownNote`
- `VAELoader`
- `SolAttnMiniMax`
- `ModelAttentionBackend`
- `BasicGuider`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `BasicGuider`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3AVDecodeT8`
- `VHS_VideoCombine`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `SamplerCustomAdvanced` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `ResolutionSelector`

## 知识

覆盖率 **81%**（34/42）

**有卡**：`MiniMaxH3DualClockSamplerT8`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`VAELoader`、`SolAttnMiniMax`、`ModelAttentionBackend`、`BasicGuider`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`RandomNoise`、`MiniMaxH3AudioConditioningT8`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`MiniMaxH3AVDecodeT8`、`VHS_VideoCombine`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`CLIPLoader`、`UNETLoader`、`LoraLoaderBypassModelOnly`、`LoadImage`、`CR Prompt Text`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`ResolutionSelector`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8、MiniMaxH3AVDecodeT8
