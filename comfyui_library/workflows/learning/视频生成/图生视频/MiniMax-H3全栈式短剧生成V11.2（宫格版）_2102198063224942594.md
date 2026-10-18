---
key: 视频生成/图生视频/MiniMax-H3全栈式短剧生成V11.2（宫格版）_2102198063224942594.json
name: MiniMax-H3全栈式短剧生成V11.2（宫格版）_2102198063224942594
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax-H3全栈式短剧生成V11.2（宫格版）_2102198063224942594.json
hash: 65de4f013dfbd627
coverage: 0.381818
learned_at: 2026-10-17 02:29:07
nodes: [GetNode, GetNode, GetNode, SetNode, YuanPrimitive, MarkdownNote, GetNode, GetNode, GetImage, GetImage, ResolutionSelector, YuanTool, SetNode, SetNode, SetNode, PrimitiveStringMultiline, SetNode, GetNode, PrimitiveStringMultiline, SetNode, SetNode, SetNode, StringConcatenate, GetNode, PreviewAudio, ComfyMathExpression, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, YUAN_TXTShotDurations, ComfyMathExpression, VOSR2ModelLoader, YuanAudioLoad, GetNode, SetNode, VOSR2Upscale, Fast Groups Bypasser (rgthree), SetNode, ResizeImageMaskNode, GetImage, GetNode, GetNode, GetNode, YuanAudioList, PrimitiveInt, GetNode, KSamplerSelect, GetNode, GetNode, GetNode, YuanAudioSplit, YUAN_TXTJsonExtractor, GetNode, ComfyMathExpression, GetNode, GetNode, SetNode, SetNode, easy clearCacheAll, MiniMaxLowVRAMAttention, MiniMaxChunkFeedForward, SetNode, ResolutionSelector, SetNode, PrimitiveFloat, ModelAttentionBackend, YUAN_TXTJsonSwitch, ComfySwitchNode, GetNode, SetNode, GetNode, SetNode, GetNode, PrimitiveStringMultiline, VHS_VideoCombine, YuanImageGridComposite, BasicScheduler, PrimitiveBoolean, YuanLoadImageOutput, ComfySwitchNode, MarkdownNote, ComfySwitchNode, PrimitiveStringMultiline, YUAN_TXTPreviewContent, PrimitiveStringMultiline, PrimitiveStringMultiline, Yuan_H3ProgressiveSampler, YuanMultiImage, VAELoader, CLIPLoader, VAELoader, UNETLoader, LoraLoaderModelOnly, Yuan_H3MotionContextTrim, PreviewImage, LoadImage, Yuan_MiniMaxH3Video]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax-H3全栈式短剧生成V11.2（宫格版）_2102198063224942594.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax-H3全栈式短剧生成V11.2（宫格版）_2102198063224942594.json`

## 结构

**生成流程**：Model → Latent → Sampling → Process → Output → Other

**节点**（110 个）：
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
- `SetNode`
- `PrimitiveStringMultiline`
- `SetNode`
- `GetNode`
- `PrimitiveStringMultiline`
- `SetNode`
- `SetNode`
- `SetNode`
- `StringConcatenate`
- `GetNode`
- `PreviewAudio`
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
- `GetNode`
- `SetNode`
- `YUAN_TXTShotDurations`
- `ComfyMathExpression`
- `VOSR2ModelLoader`
- `YuanAudioLoad`
- `GetNode`
- `SetNode`
- `VOSR2Upscale`
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `ResizeImageMaskNode`
- `GetImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `YuanAudioList`
- `PrimitiveInt`
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `YuanAudioSplit`
- `YUAN_TXTJsonExtractor`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `easy clearCacheAll`
- `MiniMaxLowVRAMAttention`
- `MiniMaxChunkFeedForward`
- `SetNode`
- `ResolutionSelector`
- `SetNode`
- `PrimitiveFloat`
- `ModelAttentionBackend`
- `YUAN_TXTJsonSwitch`
- `ComfySwitchNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `YuanImageGridComposite`
- `BasicScheduler`
- `PrimitiveBoolean`
- `YuanLoadImageOutput`
- `ComfySwitchNode`
- `MarkdownNote`
- `ComfySwitchNode`
- `PrimitiveStringMultiline`
- `YUAN_TXTPreviewContent`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `Yuan_H3ProgressiveSampler` ★核心
- `YuanMultiImage`
- `VAELoader`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Yuan_H3MotionContextTrim`
- `PreviewImage`
- `LoadImage`
- `Yuan_MiniMaxH3Video`

## 知识

覆盖率 **38%**（42/110）

**有卡**：`YuanPrimitive`、`GetImage`、`ResolutionSelector`、`YuanTool`、`StringConcatenate`、`PreviewAudio`、`ComfyMathExpression`、`YUAN_TXTShotDurations`、`VOSR2ModelLoader`、`YuanAudioLoad`、`VOSR2Upscale`、`ResizeImageMaskNode`、`YuanAudioList`、`KSamplerSelect`、`YuanAudioSplit`、`YUAN_TXTJsonExtractor`、`easy clearCacheAll`、`MiniMaxLowVRAMAttention`、`MiniMaxChunkFeedForward`、`ModelAttentionBackend`、`YUAN_TXTJsonSwitch`、`VHS_VideoCombine`、`YuanImageGridComposite`、`BasicScheduler`、`PrimitiveBoolean`、`YuanLoadImageOutput`、`YUAN_TXTPreviewContent`、`Yuan_H3ProgressiveSampler`、`YuanMultiImage`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`Yuan_H3MotionContextTrim`、`LoadImage`、`Yuan_MiniMaxH3Video`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、Yuan_H3ProgressiveSampler
