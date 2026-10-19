---
name: unknown_workflow_video_upscale_lora_30
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.383
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ComfySwitchNode, Fast Groups Bypasser (rgthree), GetImage, GetNode, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, ModelAttentionBackend, PreviewAudio, PreviewImage, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, ResizeImageMaskNode, ResolutionSelector, SetNode, StringConcatenate, UNETLoader, VAELoader, VHS_VideoCombine, VOSR2ModelLoader, VOSR2Upscale, YUAN_TXTJsonExtractor, YUAN_TXTJsonSwitch, YUAN_TXTPreviewContent, YUAN_TXTShotDurations, YuanAudioList, YuanAudioLoad, YuanAudioSplit, YuanImageGridComposite, YuanLoadImageOutput, YuanMultiImage, YuanPrimitive, YuanTool, Yuan_H3MotionContextTrim, Yuan_H3ProgressiveSampler, Yuan_MiniMaxH3Video]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax-H3全栈式短剧生成V11.2（宫格版）_2102198063224942594.json, 视频生成/图生视频/MiniMax-H3全栈式短剧生成V12.1（宫格版）_2105481384004505602.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_30

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3全栈式短剧生成V11.2（宫格版）_2102198063224942594.json、视频生成/图生视频/MiniMax-H3全栈式短剧生成V12.1（宫格版）_2105481384004505602.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：38%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `Fast Groups Bypasser (rgthree)`
- `GetImage`
- `GetNode`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `PreviewAudio`
- `PreviewImage`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `ResizeImageMaskNode`
- `ResolutionSelector`
- `SetNode`
- `StringConcatenate`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `YUAN_TXTJsonExtractor`
- `YUAN_TXTJsonSwitch`
- `YUAN_TXTPreviewContent`
- `YUAN_TXTShotDurations`
- `YuanAudioList`
- `YuanAudioLoad`
- `YuanAudioSplit`
- `YuanImageGridComposite`
- `YuanLoadImageOutput`
- `YuanMultiImage`
- `YuanPrimitive`
- `YuanTool`
- `Yuan_H3MotionContextTrim`
- `Yuan_H3ProgressiveSampler`
- `Yuan_MiniMaxH3Video`

**可变部分**（部分 workflow 才有）：
- `easy clearCacheAll` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
