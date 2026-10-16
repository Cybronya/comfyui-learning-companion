---
key: 视频生成/图生视频/（均衡版）Minimax H3 Zs05+双采+加速+Lantent Upscaler参考生视频_2091931030046466050.json
name: （均衡版）Minimax H3 Zs05+双采+加速+Lantent Upscaler参考生视频_2091931030046466050
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/（均衡版）Minimax H3 Zs05+双采+加速+Lantent Upscaler参考生视频_2091931030046466050.json
hash: d49d37ea37dd0797
coverage: 0.795455
learned_at: 2026-10-16 22:31:17
nodes: [CLIPLoader, MiniMaxH3DualClockSamplerT8, BasicGuider, SamplerCustomAdvanced, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, ComfyMathExpression, MarkdownNote, VAELoader, VAELoader, SolAttnMiniMax, ModelAttentionBackend, CR Prompt Text, BasicGuider, ResolutionSelector, MiniMaxH3LearnedLatentUpscaleT8Advanced, UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderBypassModelOnly, PrimitiveFloat, MiniMaxH3AudioConditioningT8, RandomNoise, MiniMaxH3AudioConditioningT8, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3AVDecodeT8, SamplerCustomAdvanced, VHS_VideoCombine, Float, Note, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/（均衡版）Minimax H3 Zs05+双采+加速+Lantent Upscaler参考生视频_2091931030046466050.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/（均衡版）Minimax H3 Zs05+双采+加速+Lantent Upscaler参考生视频_2091931030046466050.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Process → Other

**节点**（44 个）：
- `CLIPLoader`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `ComfyMathExpression`
- `MarkdownNote`
- `VAELoader`
- `VAELoader`
- `SolAttnMiniMax`
- `ModelAttentionBackend`
- `CR Prompt Text`
- `BasicGuider`
- `ResolutionSelector`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `UNETLoader` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderBypassModelOnly` ★核心
- `PrimitiveFloat`
- `MiniMaxH3AudioConditioningT8`
- `RandomNoise`
- `MiniMaxH3AudioConditioningT8`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `MiniMaxH3AVDecodeT8`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `Float`
- `Note`
- `Note`

## 知识

覆盖率 **80%**（35/44）

**有卡**：`CLIPLoader`、`MiniMaxH3DualClockSamplerT8`、`BasicGuider`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`VAELoader`、`SolAttnMiniMax`、`ModelAttentionBackend`、`CR Prompt Text`、`ResolutionSelector`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`UNETLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderBypassModelOnly`、`MiniMaxH3AudioConditioningT8`、`RandomNoise`、`LoadImage`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`MiniMaxH3AVDecodeT8`、`VHS_VideoCombine`、`Float`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8、MiniMaxH3AVDecodeT8
