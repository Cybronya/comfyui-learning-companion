---
key: 视频生成/图生视频/5段合成-T8双时钟双采加速Lantent Upscaler公共参考-超真实minmaxh3_2093631803813879809.json
name: 5段合成-T8双时钟双采加速Lantent Upscaler公共参考-超真实minmaxh3_2093631803813879809
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/5段合成-T8双时钟双采加速Lantent Upscaler公共参考-超真实minmaxh3_2093631803813879809.json
hash: 4841d306cf1a290f
coverage: 0.952381
learned_at: 2026-10-16 23:41:54
nodes: [VAELoader, CLIPLoader, UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, SolAttnMiniMax, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, BasicGuider, RandomNoise, SamplerCustomAdvanced, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3AudioConditioningT8, MiniMaxH3TwoPassLatentReconcileT8Advanced, MiniMaxH3TwoPassDetailMixerT8Advanced, BasicGuider, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8, ComfyMathExpression, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, BasicGuider, RandomNoise, SamplerCustomAdvanced, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3AudioConditioningT8, MiniMaxH3TwoPassLatentReconcileT8Advanced, MiniMaxH3TwoPassDetailMixerT8Advanced, BasicGuider, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8, ComfyMathExpression, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, BasicGuider, RandomNoise, SamplerCustomAdvanced, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3AudioConditioningT8, MiniMaxH3TwoPassLatentReconcileT8Advanced, MiniMaxH3TwoPassDetailMixerT8Advanced, BasicGuider, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8, ComfyMathExpression, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, BasicGuider, RandomNoise, SamplerCustomAdvanced, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3AudioConditioningT8, MiniMaxH3TwoPassLatentReconcileT8Advanced, MiniMaxH3TwoPassDetailMixerT8Advanced, BasicGuider, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8, ComfyMathExpression, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, BasicGuider, RandomNoise, SamplerCustomAdvanced, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3AudioConditioningT8, MiniMaxH3TwoPassLatentReconcileT8Advanced, MiniMaxH3TwoPassDetailMixerT8Advanced, BasicGuider, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8, ComfyMathExpression, MiniMaxH3MotionContext, MiniMaxH3MotionContext, MiniMaxH3MotionContextTrim, MiniMaxH3MotionContext, MiniMaxH3MotionContext, MiniMaxH3MotionContextTrim, MiniMaxH3MotionContext, MiniMaxH3MotionContext, MiniMaxH3MotionContextTrim, MiniMaxH3MotionContext, MiniMaxH3MotionContext, MiniMaxH3MotionContextTrim, ImageBatch, AudioConcat, ImageBatch, AudioConcat, ImageBatch, AudioConcat, ImageBatch, AudioConcat, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, MarkdownNote, LoraLoaderBypassModelOnly, VAELoader, ResolutionSelector, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, LoadAudio, CR Prompt Text, PrimitiveFloat, PrimitiveFloat, PrimitiveFloat, PrimitiveFloat, PrimitiveFloat]
patterns: []
missing: []
---

# 视频生成/图生视频/5段合成-T8双时钟双采加速Lantent Upscaler公共参考-超真实minmaxh3_2093631803813879809.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/5段合成-T8双时钟双采加速Lantent Upscaler公共参考-超真实minmaxh3_2093631803813879809.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Process → Other

**节点**（126 个）：
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `SolAttnMiniMax`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `BasicGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3AVDecodeT8`
- `ComfyMathExpression`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `BasicGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3AVDecodeT8`
- `ComfyMathExpression`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `BasicGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3AVDecodeT8`
- `ComfyMathExpression`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `BasicGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3AVDecodeT8`
- `ComfyMathExpression`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `BasicGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3AVDecodeT8`
- `ComfyMathExpression`
- `MiniMaxH3MotionContext`
- `MiniMaxH3MotionContext`
- `MiniMaxH3MotionContextTrim`
- `MiniMaxH3MotionContext`
- `MiniMaxH3MotionContext`
- `MiniMaxH3MotionContextTrim`
- `MiniMaxH3MotionContext`
- `MiniMaxH3MotionContext`
- `MiniMaxH3MotionContextTrim`
- `MiniMaxH3MotionContext`
- `MiniMaxH3MotionContext`
- `MiniMaxH3MotionContextTrim`
- `ImageBatch`
- `AudioConcat`
- `ImageBatch`
- `AudioConcat`
- `ImageBatch`
- `AudioConcat`
- `ImageBatch`
- `AudioConcat`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `MarkdownNote`
- `LoraLoaderBypassModelOnly` ★核心
- `VAELoader`
- `ResolutionSelector`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `LoadAudio`
- `CR Prompt Text`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveFloat`

## 知识

覆盖率 **95%**（120/126）

**有卡**：`VAELoader`、`CLIPLoader`、`UNETLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ModelAttentionBackend`、`SolAttnMiniMax`、`LoadImage`、`MiniMaxH3AudioConditioningT8`、`MiniMaxH3DualClockSamplerT8`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`BasicGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`MiniMaxH3AVDecodeT8`、`ComfyMathExpression`、`MiniMaxH3MotionContext`、`MiniMaxH3MotionContextTrim`、`ImageBatch`、`AudioConcat`、`VHS_VideoCombine`、`LoraLoaderBypassModelOnly`、`ResolutionSelector`、`CR Prompt Text`、`LoadAudio`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8、MiniMaxH3AVDecodeT8
