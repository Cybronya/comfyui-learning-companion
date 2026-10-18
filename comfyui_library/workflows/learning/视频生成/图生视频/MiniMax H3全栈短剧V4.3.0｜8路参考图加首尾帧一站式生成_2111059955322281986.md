---
key: 视频生成/图生视频/MiniMax H3全栈短剧V4.3.0｜8路参考图加首尾帧一站式生成_2111059955322281986.json
name: MiniMax H3全栈短剧V4.3.0｜8路参考图加首尾帧一站式生成_2111059955322281986
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3全栈短剧V4.3.0｜8路参考图加首尾帧一站式生成_2111059955322281986.json
hash: f593edc1a74ccbd4
coverage: 0.924812
learned_at: 2026-10-18 00:43:30
nodes: [PrimitiveFloat, ResolutionSelector, ResolutionSelector, PrimitiveInt, VHS_VideoCombine, KSamplerSelect, ModelAttentionBackend, MiniMaxChunkFeedForward, VAELoader, CLIPLoader, VAELoader, ComfyMathExpression, YuanAudioSplit, GetImage, GetImage, GetImage, BasicScheduler, UNETLoader, MiniMaxLowVRAMAttention, LoraLoaderModelOnly, RandomNoise, YUAN_TXTJsonSwitch, YuanAudioList, YUAN_TXTPreviewContent, ComfyMathExpression, YuanTool, YUAN_TXTJsonExtractor, SamplerCustomAdvanced, BasicGuider, KSamplerSelect, BasicScheduler, Yuan_H3Upscale3D, SamplerCustomAdvanced, Yuan_MiniMaxH3Video, BasicGuider, Yuan_H3MotionContextTrim, Yuan_H3MotionContext, CR Text, RandomNoise, AudioConcat, Int, Int, If ANY execute A else B, easy forLoopStart, EmptyAudio, easy isNone, easy batchAnything, easy forLoopEnd, easy mathInt, PreviewImage, YuanMultiImage, Int, Int, PrimitiveNode, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, SaveImage, GetImage, GetImage, GetImage, GetImage, GetImage, easy convertAnything, MiniMaxH3ResolutionSelector, YuanMultiImage, PrimitiveStringMultiline, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/MiniMax H3全栈短剧V4.3.0｜8路参考图加首尾帧一站式生成_2111059955322281986.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3全栈短剧V4.3.0｜8路参考图加首尾帧一站式生成_2111059955322281986.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（133 个）：
- `PrimitiveFloat`
- `ResolutionSelector`
- `ResolutionSelector`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `KSamplerSelect` ★核心
- `ModelAttentionBackend`
- `MiniMaxChunkFeedForward`
- `VAELoader`
- `CLIPLoader`
- `VAELoader`
- `ComfyMathExpression`
- `YuanAudioSplit`
- `GetImage`
- `GetImage`
- `GetImage`
- `BasicScheduler`
- `UNETLoader` ★核心
- `MiniMaxLowVRAMAttention`
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `YUAN_TXTJsonSwitch`
- `YuanAudioList`
- `YUAN_TXTPreviewContent`
- `ComfyMathExpression`
- `YuanTool`
- `YUAN_TXTJsonExtractor`
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `Yuan_H3Upscale3D`
- `SamplerCustomAdvanced` ★核心
- `Yuan_MiniMaxH3Video`
- `BasicGuider`
- `Yuan_H3MotionContextTrim`
- `Yuan_H3MotionContext`
- `CR Text`
- `RandomNoise`
- `AudioConcat`
- `Int`
- `Int`
- `If ANY execute A else B`
- `easy forLoopStart`
- `EmptyAudio`
- `easy isNone`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy mathInt`
- `PreviewImage`
- `YuanMultiImage`
- `Int`
- `Int`
- `PrimitiveNode`
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
- `SaveImage`
- `GetImage`
- `GetImage`
- `GetImage`
- `GetImage`
- `GetImage`
- `easy convertAnything`
- `MiniMaxH3ResolutionSelector`
- `YuanMultiImage`
- `PrimitiveStringMultiline`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
- `Note`

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

覆盖率 **92%**（123/133）

**有卡**：`ResolutionSelector`、`VHS_VideoCombine`、`KSamplerSelect`、`ModelAttentionBackend`、`MiniMaxChunkFeedForward`、`VAELoader`、`CLIPLoader`、`ComfyMathExpression`、`YuanAudioSplit`、`GetImage`、`BasicScheduler`、`UNETLoader`、`MiniMaxLowVRAMAttention`、`LoraLoaderModelOnly`、`RandomNoise`、`YUAN_TXTJsonSwitch`、`YuanAudioList`、`YUAN_TXTPreviewContent`、`YuanTool`、`YUAN_TXTJsonExtractor`、`SamplerCustomAdvanced`、`BasicGuider`、`Yuan_H3Upscale3D`、`Yuan_MiniMaxH3Video`、`Yuan_H3MotionContextTrim`、`Yuan_H3MotionContext`、`CR Text`、`AudioConcat`、`Int`、`If ANY execute A else B`、`easy forLoopStart`、`EmptyAudio`、`easy isNone`、`easy batchAnything`、`easy forLoopEnd`、`easy mathInt`、`YuanMultiImage`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`VAEDecode`、`SaveImage`、`easy convertAnything`、`MiniMaxH3ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
