---
key: 视频生成/图生视频/4段合成-T8双时钟双采加速Lantent Upscaler公共参考-超真实minmaxh3_2093624760705044482.json
name: 4段合成-T8双时钟双采加速Lantent Upscaler公共参考-超真实minmaxh3_2093624760705044482
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/4段合成-T8双时钟双采加速Lantent Upscaler公共参考-超真实minmaxh3_2093624760705044482.json
hash: 8ee48888dbc143f2
coverage: 0.951923
learned_at: 2026-10-16 23:41:54
nodes: [VAELoader, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, SolAttnMiniMax, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, BasicGuider, RandomNoise, SamplerCustomAdvanced, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3AudioConditioningT8, MiniMaxH3TwoPassLatentReconcileT8Advanced, MiniMaxH3TwoPassDetailMixerT8Advanced, BasicGuider, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8, ComfyMathExpression, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, BasicGuider, RandomNoise, SamplerCustomAdvanced, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3AudioConditioningT8, MiniMaxH3TwoPassLatentReconcileT8Advanced, MiniMaxH3TwoPassDetailMixerT8Advanced, BasicGuider, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8, ComfyMathExpression, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, BasicGuider, RandomNoise, SamplerCustomAdvanced, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3AudioConditioningT8, MiniMaxH3TwoPassLatentReconcileT8Advanced, MiniMaxH3TwoPassDetailMixerT8Advanced, BasicGuider, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8, ComfyMathExpression, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, BasicGuider, RandomNoise, SamplerCustomAdvanced, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3AudioConditioningT8, MiniMaxH3TwoPassLatentReconcileT8Advanced, MiniMaxH3TwoPassDetailMixerT8Advanced, BasicGuider, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8, ComfyMathExpression, MiniMaxH3MotionContext, MiniMaxH3MotionContext, MiniMaxH3MotionContextTrim, MiniMaxH3MotionContext, MiniMaxH3MotionContext, MiniMaxH3MotionContextTrim, MiniMaxH3MotionContext, MiniMaxH3MotionContext, MiniMaxH3MotionContextTrim, ImageBatch, AudioConcat, ImageBatch, AudioConcat, ImageBatch, AudioConcat, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, MarkdownNote, LoraLoaderBypassModelOnly, LoadImage, ResolutionSelector, VAELoader, CLIPLoader, UNETLoader, LoadAudio, LoadImage, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, PrimitiveFloat, PrimitiveFloat, PrimitiveFloat, PrimitiveFloat]
patterns: []
missing: []
---

# 视频生成/图生视频/4段合成-T8双时钟双采加速Lantent Upscaler公共参考-超真实minmaxh3_2093624760705044482.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/4段合成-T8双时钟双采加速Lantent Upscaler公共参考-超真实minmaxh3_2093624760705044482.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Process → Other

**节点**（104 个）：
- `VAELoader`
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
- `MarkdownNote`
- `LoraLoaderBypassModelOnly` ★核心
- `LoadImage`
- `ResolutionSelector`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoadAudio`
- `LoadImage`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveFloat`

## 知识

覆盖率 **95%**（99/104）

**有卡**：`VAELoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ModelAttentionBackend`、`SolAttnMiniMax`、`LoadImage`、`MiniMaxH3AudioConditioningT8`、`MiniMaxH3DualClockSamplerT8`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`BasicGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`MiniMaxH3AVDecodeT8`、`ComfyMathExpression`、`MiniMaxH3MotionContext`、`MiniMaxH3MotionContextTrim`、`ImageBatch`、`AudioConcat`、`VHS_VideoCombine`、`LoraLoaderBypassModelOnly`、`ResolutionSelector`、`CLIPLoader`、`UNETLoader`、`LoadAudio`、`CR Prompt Text`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8、MiniMaxH3AVDecodeT8
