---
key: 视频生成/图生视频/MiniMax-H3全栈式短剧生成V12.1（宫格版）_2105481384004505602.json
name: MiniMax-H3全栈式短剧生成V12.1（宫格版）_2105481384004505602
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax-H3全栈式短剧生成V12.1（宫格版）_2105481384004505602.json
hash: da6d9da5e5c478e9
coverage: 0.383929
learned_at: 2026-10-07 00:33:29
nodes: [GetNode, GetNode, GetNode, SetNode, YuanPrimitive, MarkdownNote, GetNode, GetNode, GetImage, GetImage, ResolutionSelector, YuanTool, SetNode, SetNode, PrimitiveStringMultiline, SetNode, GetNode, PrimitiveStringMultiline, SetNode, SetNode, StringConcatenate, GetNode, ComfyMathExpression, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, YUAN_TXTShotDurations, ComfyMathExpression, VOSR2ModelLoader, GetNode, VOSR2Upscale, ResizeImageMaskNode, GetNode, GetNode, GetNode, YuanAudioList, PrimitiveInt, KSamplerSelect, GetNode, GetNode, GetNode, GetNode, GetNode, Yuan_H3MotionContextTrim, SetNode, SetNode, SetNode, ResolutionSelector, SetNode, PrimitiveFloat, ComfySwitchNode, GetNode, SetNode, GetNode, SetNode, MarkdownNote, Yuan_MiniMaxH3Video, YuanAudioSplit, PrimitiveStringMultiline, Fast Groups Bypasser (rgthree), YUAN_TXTPreviewContent, GetImage, GetNode, ComfyMathExpression, GetNode, PrimitiveStringMultiline, PrimitiveStringMultiline, ComfySwitchNode, YuanLoadImageOutput, GetImage, ComfySwitchNode, YuanAudioLoad, PreviewAudio, PrimitiveBoolean, GetNode, VHS_VideoCombine, PrimitiveStringMultiline, YUAN_TXTJsonSwitch, YUAN_TXTJsonExtractor, LoadImage, SetNode, SetNode, SetNode, SetNode, MiniMaxLowVRAMAttention, MiniMaxChunkFeedForward, ModelAttentionBackend, VAELoader, CLIPLoader, VAELoader, PrimitiveBoolean, PreviewImage, YuanImageGridComposite, LoraLoaderModelOnly, YuanMultiImage, PrimitiveStringMultiline, PrimitiveStringMultiline, UNETLoader, BasicScheduler, Yuan_H3ProgressiveSampler]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax-H3全栈式短剧生成V12.1（宫格版）_2105481384004505602.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax-H3全栈式短剧生成V12.1（宫格版）_2105481384004505602.json`

## 结构

**生成流程**：Model → Latent → Sampling → Process → Output → Other

**节点**（112 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `YuanPrimitive`
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `GetImage`
- `GetImage`
- `ResolutionSelector`
- `YuanTool`
- `SetNode`
- `SetNode`
- `PrimitiveStringMultiline`
- `SetNode`
- `GetNode`
- `PrimitiveStringMultiline`
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
- `MarkdownNote`
- `Yuan_MiniMaxH3Video`
- `YuanAudioSplit`
- `PrimitiveStringMultiline`
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

## 知识

覆盖率 **38%**（43/112）

**有卡**：`YuanPrimitive`、`GetImage`、`ResolutionSelector`、`YuanTool`、`StringConcatenate`、`ComfyMathExpression`、`YUAN_TXTShotDurations`、`VOSR2ModelLoader`、`VOSR2Upscale`、`ResizeImageMaskNode`、`YuanAudioList`、`KSamplerSelect`、`Yuan_H3MotionContextTrim`、`Yuan_MiniMaxH3Video`、`YuanAudioSplit`、`YUAN_TXTPreviewContent`、`YuanLoadImageOutput`、`YuanAudioLoad`、`PreviewAudio`、`PrimitiveBoolean`、`VHS_VideoCombine`、`YUAN_TXTJsonSwitch`、`YUAN_TXTJsonExtractor`、`LoadImage`、`MiniMaxLowVRAMAttention`、`MiniMaxChunkFeedForward`、`ModelAttentionBackend`、`VAELoader`、`CLIPLoader`、`YuanImageGridComposite`、`LoraLoaderModelOnly`、`YuanMultiImage`、`UNETLoader`、`BasicScheduler`、`Yuan_H3ProgressiveSampler`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、Yuan_H3ProgressiveSampler
