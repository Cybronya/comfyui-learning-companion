---
name: unknown_workflow_video_sampler_unet_28
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.723
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CM_IntToFloat, CR Prompt Text, ComfyMathExpression, FloatConstant, GetNode, INTConstant, KSamplerSelect, LoadAudio, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, RandomNoise, ResizeShortestToNode, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/海螺1080全能参考生视频v2-带视频_2089977803579150337.json, 视频生成/图生视频/海螺1080全能参考生视频v2-带音频_2089977775015948289.json, 视频生成/图生视频/海螺1080全能参考生视频v2_2088548493907550210.json, 视频生成/图生视频/海螺480全能参考生视频_2086053849802039298.json, 视频生成/图生视频/海螺480全能参考生视频v2-带视频_2089973607303835649.json, 视频生成/图生视频/海螺480全能参考生视频v2-带音频_2089971327435370497.json, 视频生成/图生视频/海螺480全能参考生视频v2_2088511013770584066.json, 视频生成/图生视频/海螺720全能参考生视频_2086044466351271938.json, 视频生成/图生视频/海螺720全能参考生视频v2-带视频_2089977416050630658.json, 视频生成/图生视频/海螺720全能参考生视频v2-带音频_2089977064664424450.json, 视频生成/图生视频/海螺720全能参考生视频v2_2088533399135932418.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_28

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/海螺1080全能参考生视频v2-带视频_2089977803579150337.json、视频生成/图生视频/海螺1080全能参考生视频v2-带音频_2089977775015948289.json、视频生成/图生视频/海螺1080全能参考生视频v2_2088548493907550210.json、视频生成/图生视频/海螺480全能参考生视频_2086053849802039298.json、视频生成/图生视频/海螺480全能参考生视频v2-带视频_2089973607303835649.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CM_IntToFloat`
- `CR Prompt Text`
- `ComfyMathExpression`
- `FloatConstant`
- `GetNode`
- `INTConstant`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResizeShortestToNode`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderBypassModelOnly` —— 9/11 个有
- `LoraLoaderModelOnly` —— 9/11 个有
- `MiniMaxH3SigmaShift` —— 9/11 个有
- `ModelAttentionBackend` —— 9/11 个有
- `SolAttnMiniMax` —— 9/11 个有
- `H3SigmaRefiner` —— 7/11 个有
- `LTXVConcatAVLatent` —— 7/11 个有
- `LTXVSeparateAVLatent` —— 7/11 个有
- `ManualSigmas` —— 7/11 个有
- `MinimaxH3LatentUpscaler3D` —— 7/11 个有
- `SplitSigmas` —— 7/11 个有
- `EasyCache` —— 2/11 个有
- `MiniMaxH3AVDecodeT8` —— 2/11 个有
- `MiniMaxH3AudioConditioningT8` —— 2/11 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 2/11 个有
- `PathchSageAttentionKJ` —— 2/11 个有
- `ImageResizeKJv2` —— 1/11 个有
- `PT_H3ConcatAVLatent` —— 1/11 个有
- `VAEEncode` —— 1/11 个有
- `VAEEncodeAudio` —— 1/11 个有
- `easy clearCacheAll` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
