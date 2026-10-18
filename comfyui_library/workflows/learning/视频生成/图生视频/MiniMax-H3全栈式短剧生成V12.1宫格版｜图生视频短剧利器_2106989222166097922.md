---
key: 视频生成/图生视频/MiniMax-H3全栈式短剧生成V12.1宫格版｜图生视频短剧利器_2106989222166097922.json
name: MiniMax-H3全栈式短剧生成V12.1宫格版｜图生视频短剧利器_2106989222166097922
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax-H3全栈式短剧生成V12.1宫格版｜图生视频短剧利器_2106989222166097922.json
hash: 3598d3acd079735b
coverage: 0.546667
learned_at: 2026-10-17 22:18:22
nodes: [GetNode, GetNode, GetNode, SetNode, YuanPrimitive, GetNode, GetNode, GetImage, GetImage, ResolutionSelector, YuanTool, SetNode, SetNode, SetNode, GetNode, SetNode, SetNode, StringConcatenate, GetNode, ComfyMathExpression, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, YUAN_TXTShotDurations, ComfyMathExpression, VOSR2ModelLoader, GetNode, VOSR2Upscale, ResizeImageMaskNode, GetNode, GetNode, GetNode, YuanAudioList, PrimitiveInt, KSamplerSelect, GetNode, GetNode, GetNode, GetNode, GetNode, Yuan_H3MotionContextTrim, SetNode, SetNode, SetNode, ResolutionSelector, SetNode, PrimitiveFloat, ComfySwitchNode, GetNode, SetNode, GetNode, SetNode, Yuan_MiniMaxH3Video, YuanAudioSplit, Fast Groups Bypasser (rgthree), YUAN_TXTPreviewContent, GetImage, GetNode, ComfyMathExpression, GetNode, PrimitiveStringMultiline, PrimitiveStringMultiline, ComfySwitchNode, YuanLoadImageOutput, GetImage, ComfySwitchNode, YuanAudioLoad, PreviewAudio, PrimitiveBoolean, GetNode, VHS_VideoCombine, PrimitiveStringMultiline, YUAN_TXTJsonSwitch, YUAN_TXTJsonExtractor, LoadImage, SetNode, SetNode, SetNode, SetNode, MiniMaxLowVRAMAttention, MiniMaxChunkFeedForward, ModelAttentionBackend, VAELoader, CLIPLoader, VAELoader, PrimitiveBoolean, PreviewImage, YuanImageGridComposite, LoraLoaderModelOnly, YuanMultiImage, PrimitiveStringMultiline, PrimitiveStringMultiline, UNETLoader, BasicScheduler, Yuan_H3ProgressiveSampler, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/MiniMax-H3全栈式短剧生成V12.1宫格版｜图生视频短剧利器_2106989222166097922.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax-H3全栈式短剧生成V12.1宫格版｜图生视频短剧利器_2106989222166097922.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（150 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `YuanPrimitive`
- `GetNode`
- `GetNode`
- `GetImage`
- `GetImage`
- `ResolutionSelector`
- `YuanTool`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `StringConcatenate`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `YUAN_TXTShotDurations`
- `ComfyMathExpression`
- `VOSR2ModelLoader`
- `GetNode`
- `VOSR2Upscale`
- `ResizeImageMaskNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `YuanAudioList`
- `PrimitiveInt`
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Yuan_H3MotionContextTrim`
- `SetNode`
- `SetNode`
- `SetNode`
- `ResolutionSelector`
- `SetNode`
- `PrimitiveFloat`
- `ComfySwitchNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `Yuan_MiniMaxH3Video`
- `YuanAudioSplit`
- `Fast Groups Bypasser (rgthree)`
- `YUAN_TXTPreviewContent`
- `GetImage`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `YuanLoadImageOutput`
- `GetImage`
- `ComfySwitchNode`
- `YuanAudioLoad`
- `PreviewAudio`
- `PrimitiveBoolean`
- `GetNode`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `YUAN_TXTJsonSwitch`
- `YUAN_TXTJsonExtractor`
- `LoadImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `MiniMaxLowVRAMAttention`
- `MiniMaxChunkFeedForward`
- `ModelAttentionBackend`
- `VAELoader`
- `CLIPLoader`
- `VAELoader`
- `PrimitiveBoolean`
- `PreviewImage`
- `YuanImageGridComposite`
- `LoraLoaderModelOnly` ★核心
- `YuanMultiImage`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `BasicScheduler`
- `Yuan_H3ProgressiveSampler` ★核心
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

覆盖率 **55%**（82/150）

**有卡**：`YuanPrimitive`、`GetImage`、`ResolutionSelector`、`YuanTool`、`StringConcatenate`、`ComfyMathExpression`、`YUAN_TXTShotDurations`、`VOSR2ModelLoader`、`VOSR2Upscale`、`ResizeImageMaskNode`、`YuanAudioList`、`KSamplerSelect`、`Yuan_H3MotionContextTrim`、`Yuan_MiniMaxH3Video`、`YuanAudioSplit`、`YUAN_TXTPreviewContent`、`YuanLoadImageOutput`、`YuanAudioLoad`、`PreviewAudio`、`PrimitiveBoolean`、`VHS_VideoCombine`、`YUAN_TXTJsonSwitch`、`YUAN_TXTJsonExtractor`、`LoadImage`、`MiniMaxLowVRAMAttention`、`MiniMaxChunkFeedForward`、`ModelAttentionBackend`、`VAELoader`、`CLIPLoader`、`YuanImageGridComposite`、`LoraLoaderModelOnly`、`YuanMultiImage`、`UNETLoader`、`BasicScheduler`、`Yuan_H3ProgressiveSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
