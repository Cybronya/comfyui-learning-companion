---
key: 视频生成/图生视频/minimax h3 i2v fastH3 contextmotion longvideo 图生视频_2105127145923244034.json
name: minimax h3 i2v fastH3 contextmotion longvideo 图生视频_2105127145923244034
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/minimax h3 i2v fastH3 contextmotion longvideo 图生视频_2105127145923244034.json
hash: c06e270ce8801105
coverage: 0.772727
learned_at: 2026-10-17 22:19:15
nodes: [VAEDecode, VAEDecodeAudio, VAELoader, MiniMaxH3ImageToVideo, PrimitiveFloat, CLIPLoader, ComfyMathExpression, SamplerCustomAdvanced, KSamplerSelect, BasicGuider, RandomNoise, VAELoader, UNETLoader, MiniMaxH3SigmaShift, ModelAttentionBackend, BlockSparseAttention, BasicScheduler, ResolutionSelector, VHS_VideoCombine, PrimitiveNode, SetNode, SetNode, SetNode, SetNode, SetNode, MiniMaxH3MotionContext, GetNode, GetNode, MiniMaxH3MotionContextChain, MiniMaxH3MotionContextTrim, SetNode, PrimitiveStringMultiline, LoadImage, LoadImage, MiniMaxH3MotionContextLoadLatent, MiniMaxH3MotionContextSaveLatent, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/minimax h3 i2v fastH3 contextmotion longvideo 图生视频_2105127145923244034.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/minimax h3 i2v fastH3 contextmotion longvideo 图生视频_2105127145923244034.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（66 个）：
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `VAELoader`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `CLIPLoader`
- `ComfyMathExpression`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `BasicGuider`
- `RandomNoise`
- `VAELoader`
- `UNETLoader` ★核心
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `BlockSparseAttention`
- `BasicScheduler`
- `ResolutionSelector`
- `VHS_VideoCombine`
- `PrimitiveNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `MiniMaxH3MotionContext`
- `GetNode`
- `GetNode`
- `MiniMaxH3MotionContextChain`
- `MiniMaxH3MotionContextTrim`
- `SetNode`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadImage`
- `MiniMaxH3MotionContextLoadLatent`
- `MiniMaxH3MotionContextSaveLatent`
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

覆盖率 **77%**（51/66）

**有卡**：`VAEDecode`、`VAEDecodeAudio`、`VAELoader`、`MiniMaxH3ImageToVideo`、`CLIPLoader`、`ComfyMathExpression`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicGuider`、`RandomNoise`、`UNETLoader`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`BlockSparseAttention`、`BasicScheduler`、`ResolutionSelector`、`VHS_VideoCombine`、`MiniMaxH3MotionContext`、`MiniMaxH3MotionContextChain`、`MiniMaxH3MotionContextTrim`、`LoadImage`、`MiniMaxH3MotionContextLoadLatent`、`MiniMaxH3MotionContextSaveLatent`、`LoraLoaderModelOnly`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
