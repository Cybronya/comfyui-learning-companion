---
name: unknown_workflow_lora_sampler_unet_249
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.902333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CreateVideo, GetVideoComponents, ImpactConditionalBranch, ImpactExecutionOrderController, ImpactQueueTrigger, ImpactSetWidgetValue, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3MotionContext, MiniMaxH3MotionContextLoadLatent, MiniMaxH3MotionContextSaveLatent, MiniMaxH3MotionContextTrim, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MiniMaxH3TurboLoRA, MiniMaxH3TurboSampler, MiniMaxLowVRAMAttention, PathchSageAttentionKJ, PreviewImage, PrimitiveInt, RTXVideoSuperResolution, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImageKJ, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAEEncode, VAELoader, easy indexAnything]
problems: []
missing: []
members: [视频生成/文生视频/H3分段参考生视频_Impact_V6_双采_整合提示词版本_2090022476851007490.json, 视频生成/文生视频/H3分段参考生视频导播台_2093263724256784386.json, 视频生成/文生视频/参考生视频_2090901194595196929.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_249

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/H3分段参考生视频_Impact_V6_双采_整合提示词版本_2090022476851007490.json、视频生成/文生视频/H3分段参考生视频导播台_2093263724256784386.json、视频生成/文生视频/参考生视频_2090901194595196929.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CreateVideo`
- `GetVideoComponents`
- `ImpactConditionalBranch`
- `ImpactExecutionOrderController`
- `ImpactQueueTrigger`
- `ImpactSetWidgetValue`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3MotionContext`
- `MiniMaxH3MotionContextLoadLatent`
- `MiniMaxH3MotionContextSaveLatent`
- `MiniMaxH3MotionContextTrim`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `MiniMaxH3TurboLoRA`
- `MiniMaxH3TurboSampler`
- `MiniMaxLowVRAMAttention`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PrimitiveInt`
- `RTXVideoSuperResolution`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImageKJ`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAEEncode`
- `VAELoader`
- `easy indexAnything`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 2/3 个有
- `ImagePass` —— 2/3 个有
- `JoinStrings` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `PrimitiveString` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `SomethingToString` —— 2/3 个有
- `TextSplitByDelimiter` —— 2/3 个有
- `easy blocker` —— 2/3 个有
- `easy compare` —— 2/3 个有
- `easy convertAnything` —— 2/3 个有
- `easy isFileExist` —— 2/3 个有
- `easy mathInt` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `SaveImage` —— 1/3 个有
- `TheodoreDirector_CommitResult` —— 1/3 个有
- `TheodoreDirector_H3Adapter` —— 1/3 个有
- `TheodoreDirector_OutputPaths` —— 1/3 个有
- `TheodoreDirector_PostprocessSecondPassSource` —— 1/3 个有
- `TheodoreDirector_Project` —— 1/3 个有
- `TheodoreDirector_SaveSecondPass` —— 1/3 个有
- `TheodoreDirector_SelectShot` —— 1/3 个有
- `VAEEncodeAudio` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
