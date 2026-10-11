---
key: 视频生成/文生视频/MiniMax-H3全栈式短剧V4.2.2｜1分钟短剧直出｜注释齐全改起来省心_2104818075840368642.json
name: MiniMax-H3全栈式短剧V4.2.2｜1分钟短剧直出｜注释齐全改起来省心_2104818075840368642
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax-H3全栈式短剧V4.2.2｜1分钟短剧直出｜注释齐全改起来省心_2104818075840368642.json
hash: 1aa1d556cb162f90
coverage: 0.838384
learned_at: 2026-10-11 22:12:43
nodes: [PrimitiveFloat, ResolutionSelector, ResolutionSelector, PrimitiveInt, VHS_VideoCombine, KSamplerSelect, ModelAttentionBackend, MiniMaxChunkFeedForward, VAELoader, CLIPLoader, VAELoader, ComfyMathExpression, YuanAudioSplit, GetImage, GetImage, GetImage, BasicScheduler, UNETLoader, MiniMaxLowVRAMAttention, LoraLoaderModelOnly, RandomNoise, YUAN_TXTJsonSwitch, YuanAudioList, YUAN_TXTPreviewContent, ComfyMathExpression, YuanTool, YUAN_TXTJsonExtractor, SamplerCustomAdvanced, BasicGuider, KSamplerSelect, BasicScheduler, Yuan_H3Upscale3D, SamplerCustomAdvanced, Yuan_MiniMaxH3Video, BasicGuider, Yuan_H3MotionContextTrim, Yuan_H3MotionContext, CR Text, RandomNoise, AudioConcat, Int, Int, If ANY execute A else B, easy forLoopStart, EmptyAudio, easy isNone, easy batchAnything, easy forLoopEnd, easy mathInt, PreviewImage, YuanMultiImage, Int, Int, PrimitiveStringMultiline, YuanMultiImage, PrimitiveNode, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [CR Text, If ANY execute A else B, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy isNone, easy mathInt]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `If ANY execute A else B` 知识库中没有该节点类型的任何知识, 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, 次要节点 `easy isNone` 知识库中没有该节点类型的任何知识, 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/MiniMax-H3全栈式短剧V4.2.2｜1分钟短剧直出｜注释齐全改起来省心_2104818075840368642.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax-H3全栈式短剧V4.2.2｜1分钟短剧直出｜注释齐全改起来省心_2104818075840368642.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（99 个）：
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
- `PrimitiveStringMultiline`
- `YuanMultiImage`
- `PrimitiveNode`
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

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **84%**（83/99）

**有卡**：`ResolutionSelector`、`VHS_VideoCombine`、`KSamplerSelect`、`ModelAttentionBackend`、`MiniMaxChunkFeedForward`、`VAELoader`、`CLIPLoader`、`ComfyMathExpression`、`YuanAudioSplit`、`GetImage`、`BasicScheduler`、`UNETLoader`、`MiniMaxLowVRAMAttention`、`LoraLoaderModelOnly`、`RandomNoise`、`YUAN_TXTJsonSwitch`、`YuanAudioList`、`YUAN_TXTPreviewContent`、`YuanTool`、`YUAN_TXTJsonExtractor`、`SamplerCustomAdvanced`、`BasicGuider`、`Yuan_H3Upscale3D`、`Yuan_MiniMaxH3Video`、`Yuan_H3MotionContextTrim`、`Yuan_H3MotionContext`、`AudioConcat`、`Int`、`EmptyAudio`、`YuanMultiImage`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`

**缺卡**（7）：`CR Text`、`If ANY execute A else B`、`easy batchAnything`、`easy forLoopEnd`、`easy forLoopStart`、`easy isNone`、`easy mathInt`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `If ANY execute A else B` 知识库中没有该节点类型的任何知识
- 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
- 次要节点 `easy isNone` 知识库中没有该节点类型的任何知识
- 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
