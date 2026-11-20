---
key: 视频生成/图生视频/MiniMax-H3全栈式短剧生成13.1（尾帧锚定版）_2115713278402973698.json
name: MiniMax-H3全栈式短剧生成13.1（尾帧锚定版）_2115713278402973698
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax-H3全栈式短剧生成13.1（尾帧锚定版）_2115713278402973698.json
hash: acdc26fea41a73cc
coverage: 0.393443
learned_at: 2026-11-02 19:18:01
nodes: [GetNode, GetNode, GetNode, SetNode, MarkdownNote, GetNode, GetNode, GetImage, GetImage, ResolutionSelector, YuanTool, SetNode, SetNode, PrimitiveStringMultiline, SetNode, GetNode, PrimitiveStringMultiline, SetNode, SetNode, StringConcatenate, GetNode, ComfyMathExpression, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, YUAN_TXTShotDurations, ComfyMathExpression, VOSR2ModelLoader, GetNode, VOSR2Upscale, ResizeImageMaskNode, GetNode, GetNode, YuanAudioList, PrimitiveInt, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, ResolutionSelector, SetNode, PrimitiveFloat, ComfySwitchNode, GetNode, SetNode, SetNode, MarkdownNote, YuanAudioSplit, PrimitiveStringMultiline, MiniMaxChunkFeedForward, SetNode, SetNode, SetNode, Fast Groups Bypasser (rgthree), YUAN_TXTPreviewContent, GetImage, GetNode, ComfyMathExpression, GetNode, PrimitiveStringMultiline, PrimitiveStringMultiline, ComfySwitchNode, YuanLoadImageOutput, GetImage, ComfySwitchNode, PrimitiveBoolean, YuanAudioLoad, PreviewAudio, PrimitiveBoolean, GetNode, YUAN_TXTJsonSwitch, YUAN_TXTJsonExtractor, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, MarkdownNote, LoadImage, Yuan_H3MotionContextTrim, YuanImageGridComposite, PreviewImage, VAELoader, CLIPLoader, VAELoader, MiniMaxLowVRAMAttention, LoraLoaderModelOnly, UNETLoader, ModelAttentionBackend, SetNode, LoraLoaderModelOnly, YuanMultiImage, YuanPrimitive, PrimitiveStringMultiline, GetNode, GetNode, LoraLoaderModelOnly, GetNode, GetNode, SetNode, SetNode, Yuan_MiniMaxH3Video, VHS_VideoCombine, Yuan_H3ProgressiveSampler, BasicScheduler, KSamplerSelect, VHS_LoadVideo, ImageFromBatch, MiniMaxH3AddGuide]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax-H3全栈式短剧生成13.1（尾帧锚定版）_2115713278402973698.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax-H3全栈式短剧生成13.1（尾帧锚定版）_2115713278402973698.json`

## 结构

**生成流程**：Model → Latent → Sampling → Process → Output → Other

**节点**（122 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
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
- `YuanAudioList`
- `PrimitiveInt`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ResolutionSelector`
- `SetNode`
- `PrimitiveFloat`
- `ComfySwitchNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `MarkdownNote`
- `YuanAudioSplit`
- `PrimitiveStringMultiline`
- `MiniMaxChunkFeedForward`
- `SetNode`
- `SetNode`
- `SetNode`
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
- `PrimitiveBoolean`
- `YuanAudioLoad`
- `PreviewAudio`
- `PrimitiveBoolean`
- `GetNode`
- `YUAN_TXTJsonSwitch`
- `YUAN_TXTJsonExtractor`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `LoadImage`
- `Yuan_H3MotionContextTrim`
- `YuanImageGridComposite`
- `PreviewImage`
- `VAELoader`
- `CLIPLoader`
- `VAELoader`
- `MiniMaxLowVRAMAttention`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ModelAttentionBackend`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `YuanMultiImage`
- `YuanPrimitive`
- `PrimitiveStringMultiline`
- `GetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `Yuan_MiniMaxH3Video`
- `VHS_VideoCombine`
- `Yuan_H3ProgressiveSampler` ★核心
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `VHS_LoadVideo`
- `ImageFromBatch`
- `MiniMaxH3AddGuide`

## 知识

覆盖率 **39%**（48/122）

**有卡**：`GetImage`、`ResolutionSelector`、`YuanTool`、`StringConcatenate`、`ComfyMathExpression`、`YUAN_TXTShotDurations`、`VOSR2ModelLoader`、`VOSR2Upscale`、`ResizeImageMaskNode`、`YuanAudioList`、`YuanAudioSplit`、`MiniMaxChunkFeedForward`、`YUAN_TXTPreviewContent`、`YuanLoadImageOutput`、`PrimitiveBoolean`、`YuanAudioLoad`、`PreviewAudio`、`YUAN_TXTJsonSwitch`、`YUAN_TXTJsonExtractor`、`LoadImage`、`Yuan_H3MotionContextTrim`、`YuanImageGridComposite`、`VAELoader`、`CLIPLoader`、`MiniMaxLowVRAMAttention`、`LoraLoaderModelOnly`、`UNETLoader`、`ModelAttentionBackend`、`YuanMultiImage`、`YuanPrimitive`、`Yuan_MiniMaxH3Video`、`VHS_VideoCombine`、`Yuan_H3ProgressiveSampler`、`BasicScheduler`、`KSamplerSelect`、`VHS_LoadVideo`、`ImageFromBatch`、`MiniMaxH3AddGuide`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、Yuan_H3ProgressiveSampler
