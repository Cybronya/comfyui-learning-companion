---
name: unknown_workflow_video_lora_sampler_780
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.665
common_nodes: [Anything Everywhere3, Bjornulf_AnythingToText, CLIPVisionLoader, CR Simple Text Watermark, Compare, FL_PromptSelector, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, PrimitiveInt, PrimitiveStringMultiline, RegexReplace, RepeatImageBatch, SetNode, ShowText|pysssss, TextSplitByDelimiterEnhanced, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy ifElse, easy lengthAnything, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/SVI FILM长视频工作流_1986031148419743745.json, 视频生成/图生视频/SVI SHOT 长视频（适合变化小的）_1985646905449488386.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_780

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/SVI FILM长视频工作流_1986031148419743745.json、视频生成/图生视频/SVI SHOT 长视频（适合变化小的）_1985646905449488386.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：66%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `Bjornulf_AnythingToText`
- `CLIPVisionLoader`
- `CR Simple Text Watermark`
- `Compare`
- `FL_PromptSelector`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RegexReplace`
- `RepeatImageBatch`
- `SetNode`
- `ShowText|pysssss`
- `TextSplitByDelimiterEnhanced`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy ifElse`
- `easy lengthAnything`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `InvertMask` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `VRAM_Debug` —— 1/2 个有
- `WanVideoVACEStartToEndFrame` —— 1/2 个有
- `easy seed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
