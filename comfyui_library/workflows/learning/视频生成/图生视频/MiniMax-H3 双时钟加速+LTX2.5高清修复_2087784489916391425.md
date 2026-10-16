---
key: 视频生成/图生视频/MiniMax-H3 双时钟加速+LTX2.5高清修复_2087784489916391425.json
name: MiniMax-H3 双时钟加速+LTX2.5高清修复_2087784489916391425
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax-H3 双时钟加速+LTX2.5高清修复_2087784489916391425.json
hash: 94921ac74db85ae4
coverage: 0.929825
learned_at: 2026-10-16 21:27:43
nodes: [SolAttnPatch, MiniMaxH3DualClockSamplerT8, BasicGuider, VAELoader, LTXVLatentUpsampler, KSamplerSelect, LTXVConcatAVLatent, VAELoader, CLIPTextEncode, LTXVSeparateAVLatent, LTXVAudioVAEDecode, Reroute, LTXVConditioning, SamplerCustomAdvanced, LTXVDualCFGGuider, LTX2MemoryEfficientSageAttentionPatch, UNETLoader, CLIPLoader, VAELoader, PathchSageAttentionKJ, ModelAttentionBackend, LoraLoaderModelOnly, UNETLoader, VAELoader, CLIPLoader, LatentUpscaleModelLoader, VHS_VideoCombine, Reroute, VAEEncode, MiniMaxH3AVDecodeT8, CLIPTextEncode, RandomNoise, LTXVImgToVideoInplace, MiniMaxH3AudioConditioningT8, LoadImage, ComfyMathExpression, RandomNoise, VAEDecodeTiled, LoraLoaderBypassModelOnly, ModelPreviewOverrideKJ, VHS_VideoCombine, SamplerCustomAdvanced, ModelPreviewOverrideKJ, BasicScheduler, ManualSigmas, ManualSigmas, LTXVAudioVAEEncode, Fast Groups Bypasser (rgthree), LoraLoaderBypassModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, ImageResizeKJv2, PixaromaSizes, PixaromaDuration, LoadImage, TextInput_, ImageResizeKJv2, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax-H3 双时钟加速+LTX2.5高清修复_2087784489916391425.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax-H3 双时钟加速+LTX2.5高清修复_2087784489916391425.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（57 个）：
- `SolAttnPatch`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `BasicGuider`
- `VAELoader`
- `LTXVLatentUpsampler` ★核心
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `Reroute`
- `LTXVConditioning`
- `SamplerCustomAdvanced` ★核心
- `LTXVDualCFGGuider`
- `LTX2MemoryEfficientSageAttentionPatch`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `PathchSageAttentionKJ`
- `ModelAttentionBackend`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `LatentUpscaleModelLoader`
- `VHS_VideoCombine`
- `Reroute`
- `VAEEncode` ★核心
- `MiniMaxH3AVDecodeT8`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `LTXVImgToVideoInplace`
- `MiniMaxH3AudioConditioningT8`
- `LoadImage`
- `ComfyMathExpression`
- `RandomNoise`
- `VAEDecodeTiled` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `ModelPreviewOverrideKJ`
- `VHS_VideoCombine`
- `SamplerCustomAdvanced` ★核心
- `ModelPreviewOverrideKJ`
- `BasicScheduler`
- `ManualSigmas`
- `ManualSigmas`
- `LTXVAudioVAEEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `LoraLoaderBypassModelOnly` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ImageResizeKJv2`
- `PixaromaSizes`
- `PixaromaDuration`
- `LoadImage`
- `TextInput_`
- `ImageResizeKJv2`
- `MarkdownNote`

## 知识

覆盖率 **93%**（53/57）

**有卡**：`SolAttnPatch`、`MiniMaxH3DualClockSamplerT8`、`BasicGuider`、`VAELoader`、`LTXVLatentUpsampler`、`KSamplerSelect`、`LTXVConcatAVLatent`、`CLIPTextEncode`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`LTXVConditioning`、`SamplerCustomAdvanced`、`LTXVDualCFGGuider`、`LTX2MemoryEfficientSageAttentionPatch`、`UNETLoader`、`CLIPLoader`、`PathchSageAttentionKJ`、`ModelAttentionBackend`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`VHS_VideoCombine`、`VAEEncode`、`MiniMaxH3AVDecodeT8`、`RandomNoise`、`LTXVImgToVideoInplace`、`MiniMaxH3AudioConditioningT8`、`LoadImage`、`ComfyMathExpression`、`VAEDecodeTiled`、`LoraLoaderBypassModelOnly`、`ModelPreviewOverrideKJ`、`BasicScheduler`、`ManualSigmas`、`LTXVAudioVAEEncode`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ImageResizeKJv2`、`PixaromaSizes`、`PixaromaDuration`、`TextInput_`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
