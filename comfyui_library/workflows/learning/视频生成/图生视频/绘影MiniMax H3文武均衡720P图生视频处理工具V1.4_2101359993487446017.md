---
key: 视频生成/图生视频/绘影MiniMax H3文武均衡720P图生视频处理工具V1.4_2101359993487446017.json
name: 绘影MiniMax H3文武均衡720P图生视频处理工具V1.4_2101359993487446017
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/绘影MiniMax H3文武均衡720P图生视频处理工具V1.4_2101359993487446017.json
hash: dc7709dbc9e0681c
coverage: 0.813084
learned_at: 2026-10-17 02:15:09
nodes: [BasicGuider, SamplerCustomAdvanced, VHS_VideoCombine, VHS_VideoCombine, MiniMaxH3DualClockSamplerT8, LoraLoaderModelOnly, BasicGuider, MiniMaxH3TwoPassLatentReconcileT8Advanced, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3AVDecodeT8, SamplerCustomAdvanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, GetNode, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ComfyMathExpression, ComfySwitchNode, ComfySwitchNode, easy ifElse, easy showAnything, ComfyMathExpression, ComfyMathExpression, easy ifElse, easy showAnything, ComfyNumberConvert, SplitStringByDelimiter, Compare, ComfyNumberConvert, Int, Int, SetNode, SetNode, SetNode, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ratio_selector, PrimitiveFloat, VAELoader, CLIPLoader, SolAttnMiniMax, MiniMaxH3ReferenceToVideo, SetNode, easy showAnything, ComfyMathExpression, GetNode, GetNode, RandomNoise, Float, UNETLoader, UNETLoader, MiniMaxChunkFeedForward, LoraLoaderModelOnly, LoraLoaderBypassModelOnly, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, LoraLoaderBypassModelOnly, CR Prompt Text, LoraLoaderModelOnly, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadAudio, LoadAudio, LoadImage, LoadImage, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/绘影MiniMax H3文武均衡720P图生视频处理工具V1.4_2101359993487446017.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/绘影MiniMax H3文武均衡720P图生视频处理工具V1.4_2101359993487446017.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（107 个）：
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `LoraLoaderModelOnly` ★核心
- `BasicGuider`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `MiniMaxH3AVDecodeT8`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `GetNode`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `easy ifElse`
- `easy showAnything`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `easy ifElse`
- `easy showAnything`
- `ComfyNumberConvert`
- `SplitStringByDelimiter`
- `Compare`
- `ComfyNumberConvert`
- `Int`
- `Int`
- `SetNode`
- `SetNode`
- `SetNode`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ratio_selector`
- `PrimitiveFloat`
- `VAELoader`
- `CLIPLoader`
- `SolAttnMiniMax`
- `MiniMaxH3ReferenceToVideo`
- `SetNode`
- `easy showAnything`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `Float`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `MiniMaxChunkFeedForward`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `CR Prompt Text`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadAudio`
- `LoadAudio`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（87/107）

**有卡**：`BasicGuider`、`SamplerCustomAdvanced`、`VHS_VideoCombine`、`MiniMaxH3DualClockSamplerT8`、`LoraLoaderModelOnly`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`MiniMaxH3AVDecodeT8`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`MiniMaxH3ReferenceToVideo`、`MiniMaxLowVRAMAttention`、`ComfyMathExpression`、`ComfyNumberConvert`、`SplitStringByDelimiter`、`Compare`、`Int`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ModelAttentionBackend`、`VAELoader`、`ratio_selector`、`CLIPLoader`、`SolAttnMiniMax`、`RandomNoise`、`Float`、`UNETLoader`、`MiniMaxChunkFeedForward`、`LoraLoaderBypassModelOnly`、`CR Prompt Text`、`LoadImage`、`LoadAudio`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
