---
key: 视频生成/图生视频/（电影感Zs05）Minimax H3+双采+加速+Lantent Upscaler参考生视频_2092882505149018113.json
name: （电影感Zs05）Minimax H3+双采+加速+Lantent Upscaler参考生视频_2092882505149018113
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/（电影感Zs05）Minimax H3+双采+加速+Lantent Upscaler参考生视频_2092882505149018113.json
hash: 3c69019064286b03
coverage: 0.8
learned_at: 2026-10-16 23:00:17
nodes: [CLIPLoader, MiniMaxH3DualClockSamplerT8, BasicGuider, SamplerCustomAdvanced, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, ComfyMathExpression, MarkdownNote, VAELoader, VAELoader, SolAttnMiniMax, ModelAttentionBackend, CR Prompt Text, ResolutionSelector, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, MiniMaxH3AudioConditioningT8, RandomNoise, MiniMaxH3AudioConditioningT8, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, MiniMaxH3AVDecodeT8, Float, Note, Note, UNETLoader, LoraLoaderModelOnly, LoraLoaderBypassModelOnly, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3TwoPassDetailMixerT8Advanced, BasicGuider, SamplerCustomAdvanced, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/（电影感Zs05）Minimax H3+双采+加速+Lantent Upscaler参考生视频_2092882505149018113.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/（电影感Zs05）Minimax H3+双采+加速+Lantent Upscaler参考生视频_2092882505149018113.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Process → Other

**节点**（45 个）：
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
- `ResolutionSelector`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
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
- `MiniMaxH3AVDecodeT8`
- `Float`
- `Note`
- `Note`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`

## 知识

覆盖率 **80%**（36/45）

**有卡**：`CLIPLoader`、`MiniMaxH3DualClockSamplerT8`、`BasicGuider`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`VAELoader`、`SolAttnMiniMax`、`ModelAttentionBackend`、`CR Prompt Text`、`ResolutionSelector`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxH3AudioConditioningT8`、`RandomNoise`、`LoadImage`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`MiniMaxH3AVDecodeT8`、`Float`、`UNETLoader`、`LoraLoaderModelOnly`、`LoraLoaderBypassModelOnly`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`VHS_VideoCombine`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8
