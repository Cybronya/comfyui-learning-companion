---
key: 视频生成/图生视频/2段合成-T8双时钟双采加速Lantent Upscaler公共参考-超真实minmaxh3_2093604508910833665.json
name: 2段合成-T8双时钟双采加速Lantent Upscaler公共参考-超真实minmaxh3_2093604508910833665
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2段合成-T8双时钟双采加速Lantent Upscaler公共参考-超真实minmaxh3_2093604508910833665.json
hash: e0c05a31b22434d6
coverage: 0.95
learned_at: 2026-10-16 23:41:53
nodes: [VAELoader, CLIPLoader, UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, SolAttnMiniMax, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, BasicGuider, RandomNoise, SamplerCustomAdvanced, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3AudioConditioningT8, MiniMaxH3TwoPassLatentReconcileT8Advanced, MiniMaxH3TwoPassDetailMixerT8Advanced, BasicGuider, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8, ComfyMathExpression, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, BasicGuider, RandomNoise, SamplerCustomAdvanced, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3AudioConditioningT8, MiniMaxH3TwoPassLatentReconcileT8Advanced, MiniMaxH3TwoPassDetailMixerT8Advanced, BasicGuider, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8, ComfyMathExpression, MiniMaxH3MotionContext, MiniMaxH3MotionContext, MiniMaxH3MotionContextTrim, ImageBatch, AudioConcat, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, MarkdownNote, VAELoader, LoraLoaderBypassModelOnly, ResolutionSelector, LoadAudio, CR Prompt Text, CR Prompt Text, LoadImage, LoadImage, PrimitiveFloat, PrimitiveFloat]
patterns: []
missing: []
---

# 视频生成/图生视频/2段合成-T8双时钟双采加速Lantent Upscaler公共参考-超真实minmaxh3_2093604508910833665.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2段合成-T8双时钟双采加速Lantent Upscaler公共参考-超真实minmaxh3_2093604508910833665.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Process → Other

**节点**（60 个）：
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
- `ImageBatch`
- `AudioConcat`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `MarkdownNote`
- `VAELoader`
- `LoraLoaderBypassModelOnly` ★核心
- `ResolutionSelector`
- `LoadAudio`
- `CR Prompt Text`
- `CR Prompt Text`
- `LoadImage`
- `LoadImage`
- `PrimitiveFloat`
- `PrimitiveFloat`

## 知识

覆盖率 **95%**（57/60）

**有卡**：`VAELoader`、`CLIPLoader`、`UNETLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ModelAttentionBackend`、`SolAttnMiniMax`、`LoadImage`、`MiniMaxH3AudioConditioningT8`、`MiniMaxH3DualClockSamplerT8`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`BasicGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`MiniMaxH3AVDecodeT8`、`ComfyMathExpression`、`MiniMaxH3MotionContext`、`MiniMaxH3MotionContextTrim`、`ImageBatch`、`AudioConcat`、`VHS_VideoCombine`、`LoraLoaderBypassModelOnly`、`ResolutionSelector`、`LoadAudio`、`CR Prompt Text`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8、MiniMaxH3AVDecodeT8
