---
name: unknown_workflow_video_lora_sampler_970
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.891
common_nodes: [AudioConcat, BasicScheduler, BatchImagesNode, BerniniConditioning, CLIPLoader, CLIPTextEncode, DiffusionModelLoaderKJ, FloatConstant, INTConstant, ImageFromBatch, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PreviewAny, SamplerCustom, SimpleCalculatorKJ, SimpleMath+, SplitSigmas, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, VantageWanBlockSwap, easy batchAnything, easy forLoopEnd, easy forLoopStart]
problems: []
missing: []
members: [平台全量/Bernini_testing_video_edit+flashvsr放大，适合小显存_2069055524376764418.json, 平台全量/Bernini_testing_video_edit循环工作流，适合小显存_2067846777507762178.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_970

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Bernini_testing_video_edit+flashvsr放大，适合小显存_2069055524376764418.json、平台全量/Bernini_testing_video_edit循环工作流，适合小显存_2067846777507762178.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioConcat`
- `BasicScheduler`
- `BatchImagesNode`
- `BerniniConditioning`
- `CLIPLoader`
- `CLIPTextEncode`
- `DiffusionModelLoaderKJ`
- `FloatConstant`
- `INTConstant`
- `ImageFromBatch`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `SamplerCustom`
- `SimpleCalculatorKJ`
- `SimpleMath+`
- `SplitSigmas`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `VantageWanBlockSwap`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `WanVideoAddFlashVSRInput` —— 1/2 个有
- `WanVideoBlockSwap` —— 1/2 个有
- `WanVideoContextOptions` —— 1/2 个有
- `WanVideoDecode` —— 1/2 个有
- `WanVideoEmptyEmbeds` —— 1/2 个有
- `WanVideoExtraModelSelect` —— 1/2 个有
- `WanVideoFlashVSRDecoderLoader` —— 1/2 个有
- `WanVideoModelLoader` —— 1/2 个有
- `WanVideoSamplerExtraArgs` —— 1/2 个有
- `WanVideoSamplerv2` —— 1/2 个有
- `WanVideoSchedulerv2` —— 1/2 个有
- `WanVideoTextEncodeCached` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
