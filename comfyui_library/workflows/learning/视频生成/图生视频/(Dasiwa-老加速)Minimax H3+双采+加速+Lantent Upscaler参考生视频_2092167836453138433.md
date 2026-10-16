---
key: 视频生成/图生视频/(Dasiwa-老加速)Minimax H3+双采+加速+Lantent Upscaler参考生视频_2092167836453138433.json
name: (Dasiwa-老加速)Minimax H3+双采+加速+Lantent Upscaler参考生视频_2092167836453138433
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(Dasiwa-老加速)Minimax H3+双采+加速+Lantent Upscaler参考生视频_2092167836453138433.json
hash: e5dcc568fd494857
coverage: 0.829268
learned_at: 2026-10-16 22:58:49
nodes: [MiniMaxH3DualClockSamplerT8, SamplerCustomAdvanced, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, ComfyMathExpression, MarkdownNote, VAELoader, SolAttnMiniMax, ModelAttentionBackend, BasicGuider, ResolutionSelector, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, MiniMaxH3AudioConditioningT8, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, BasicGuider, MiniMaxH3AudioConditioningT8, MiniMaxH3TwoPassDetailMixerT8Advanced, VAELoader, CLIPLoader, SamplerCustomAdvanced, CR Prompt Text, UNETLoader, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/(Dasiwa-老加速)Minimax H3+双采+加速+Lantent Upscaler参考生视频_2092167836453138433.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/(Dasiwa-老加速)Minimax H3+双采+加速+Lantent Upscaler参考生视频_2092167836453138433.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Process → Other

**节点**（41 个）：
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
- `ResolutionSelector`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
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
- `BasicGuider`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `VAELoader`
- `CLIPLoader`
- `SamplerCustomAdvanced` ★核心
- `CR Prompt Text`
- `UNETLoader` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `MiniMaxH3AVDecodeT8`
- `VHS_VideoCombine`

## 知识

覆盖率 **83%**（34/41）

**有卡**：`MiniMaxH3DualClockSamplerT8`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`VAELoader`、`SolAttnMiniMax`、`ModelAttentionBackend`、`BasicGuider`、`ResolutionSelector`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`RandomNoise`、`MiniMaxH3AudioConditioningT8`、`LoadImage`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`CLIPLoader`、`CR Prompt Text`、`UNETLoader`、`LoraLoaderBypassModelOnly`、`MiniMaxH3AVDecodeT8`、`VHS_VideoCombine`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8、MiniMaxH3AVDecodeT8
