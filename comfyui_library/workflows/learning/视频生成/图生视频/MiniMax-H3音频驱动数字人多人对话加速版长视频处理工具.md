---
key: 视频生成/图生视频/MiniMax-H3音频驱动数字人多人对话加速版长视频处理工具.json
name: MiniMax-H3音频驱动数字人多人对话加速版长视频处理工具
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax-H3音频驱动数字人多人对话加速版长视频处理工具.json
hash: 26c7082042619de2
coverage: 0.92
learned_at: 2026-10-07 00:33:36
nodes: [CLIPLoader, VAELoader, VAELoader, ComfyMathExpression, UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, BasicGuider, RandomNoise, MiniMaxH3AVDecodeT8, VHS_VideoCombine, SamplerCustomAdvanced, LoraLoaderBypassModelOnly, PrimitiveFloat, ResolutionSelector, LoadImage, LoadImage, CR Prompt Text, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, SaveImage, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, LoadAudio, SolAttnMiniMax]
patterns: [text_to_image]
missing: [CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/MiniMax-H3音频驱动数字人多人对话加速版长视频处理工具.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax-H3音频驱动数字人多人对话加速版长视频处理工具.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（50 个）：
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `ComfyMathExpression`
- `UNETLoader` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `BasicGuider`
- `RandomNoise`
- `MiniMaxH3AVDecodeT8`
- `VHS_VideoCombine`
- `SamplerCustomAdvanced` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `PrimitiveFloat`
- `ResolutionSelector`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
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
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `LoadAudio`
- `SolAttnMiniMax`

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

覆盖率 **92%**（46/50）

**有卡**：`CLIPLoader`、`VAELoader`、`ComfyMathExpression`、`UNETLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ModelAttentionBackend`、`BasicGuider`、`RandomNoise`、`MiniMaxH3AVDecodeT8`、`VHS_VideoCombine`、`SamplerCustomAdvanced`、`LoraLoaderBypassModelOnly`、`ResolutionSelector`、`LoadImage`、`LoraLoaderModelOnly`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`VAEDecode`、`SaveImage`、`MiniMaxH3AudioConditioningT8`、`MiniMaxH3DualClockSamplerT8`、`LoadAudio`、`SolAttnMiniMax`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
