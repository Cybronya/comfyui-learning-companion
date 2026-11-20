---
key: 图片生成/图生图/MiniMax-H3全栈式短剧生成V14.3（双模切换版）_2116687369645678594.json
name: MiniMax-H3全栈式短剧生成V14.3（双模切换版）_2116687369645678594
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/MiniMax-H3全栈式短剧生成V14.3（双模切换版）_2116687369645678594.json
hash: 79b9d360d81f9de7
coverage: 0.396552
learned_at: 2026-11-02 19:12:38
nodes: [GetNode, GetNode, GetNode, SetNode, YuanPrimitive, MarkdownNote, GetNode, ResolutionSelector, YuanTool, SetNode, SetNode, PrimitiveStringMultiline, SetNode, GetNode, PrimitiveStringMultiline, SetNode, SetNode, StringConcatenate, GetNode, ComfyMathExpression, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, YUAN_TXTShotDurations, ComfyMathExpression, VOSR2ModelLoader, GetNode, VOSR2Upscale, ResizeImageMaskNode, GetNode, GetNode, GetNode, YuanAudioList, PrimitiveInt, KSamplerSelect, GetNode, GetNode, GetNode, GetNode, GetNode, Yuan_H3MotionContextTrim, SetNode, SetNode, SetNode, ResolutionSelector, SetNode, PrimitiveFloat, ComfySwitchNode, GetNode, SetNode, SetNode, BasicScheduler, MarkdownNote, Yuan_MiniMaxH3Video, YuanAudioSplit, ModelAttentionBackend, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, SetNode, SetNode, SetNode, YuanImageGridComposite, YUAN_TXTPreviewContent, GetNode, ComfyMathExpression, GetNode, PrimitiveStringMultiline, PrimitiveStringMultiline, ComfySwitchNode, YuanLoadImageOutput, GetImage, ComfySwitchNode, PrimitiveBoolean, PreviewImage, YuanAudioLoad, PreviewAudio, LoadImage, PrimitiveBoolean, GetNode, PrimitiveStringMultiline, YUAN_TXTJsonSwitch, YuanMultiImage, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, Yuan_H3ProgressiveSampler, SetNode, GetNode, SetNode, GetNode, ComfyMathExpression, YUAN_TXTJsonExtractor, GetNode, GetImage, GetImage, GetImage, ComfySwitchNode, LoraLoaderModelOnly, UNETLoader, VAELoader, CLIPLoader, VAELoader, UNETLoader, LoraLoaderModelOnly, VHS_VideoCombine]
patterns: []
missing: []
---

# 图片生成/图生图/MiniMax-H3全栈式短剧生成V14.3（双模切换版）_2116687369645678594.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/MiniMax-H3全栈式短剧生成V14.3（双模切换版）_2116687369645678594.json`

## 结构

**生成流程**：Model → Latent → Sampling → Process → Output → Other

**节点**（116 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `YuanPrimitive`
- `MarkdownNote`
- `GetNode`
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
- `SetNode`
- `BasicScheduler`
- `MarkdownNote`
- `Yuan_MiniMaxH3Video`
- `YuanAudioSplit`
- `ModelAttentionBackend`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `SetNode`
- `SetNode`
- `SetNode`
- `YuanImageGridComposite`
- `YUAN_TXTPreviewContent`
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
- `PreviewImage`
- `YuanAudioLoad`
- `PreviewAudio`
- `LoadImage`
- `PrimitiveBoolean`
- `GetNode`
- `PrimitiveStringMultiline`
- `YUAN_TXTJsonSwitch`
- `YuanMultiImage`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `Yuan_H3ProgressiveSampler` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `ComfyMathExpression`
- `YUAN_TXTJsonExtractor`
- `GetNode`
- `GetImage`
- `GetImage`
- `GetImage`
- `ComfySwitchNode`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`

## 知识

覆盖率 **40%**（46/116）

**有卡**：`YuanPrimitive`、`ResolutionSelector`、`YuanTool`、`StringConcatenate`、`ComfyMathExpression`、`YUAN_TXTShotDurations`、`VOSR2ModelLoader`、`VOSR2Upscale`、`ResizeImageMaskNode`、`YuanAudioList`、`KSamplerSelect`、`Yuan_H3MotionContextTrim`、`BasicScheduler`、`Yuan_MiniMaxH3Video`、`YuanAudioSplit`、`ModelAttentionBackend`、`MiniMaxChunkFeedForward`、`MiniMaxLowVRAMAttention`、`YuanImageGridComposite`、`YUAN_TXTPreviewContent`、`YuanLoadImageOutput`、`GetImage`、`PrimitiveBoolean`、`YuanAudioLoad`、`PreviewAudio`、`LoadImage`、`YUAN_TXTJsonSwitch`、`YuanMultiImage`、`Yuan_H3ProgressiveSampler`、`YUAN_TXTJsonExtractor`、`LoraLoaderModelOnly`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`VHS_VideoCombine`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、Yuan_H3ProgressiveSampler
