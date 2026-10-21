---
name: unknown_workflow_video_sampler_unet_56
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.7155
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, INTConstant, KSamplerSelect, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/海螺480全能参考生视频_2086053849802039298.json, 视频生成/图生视频/海螺480全能参考生视频v2-带视频_2089973607303835649.json, 视频生成/图生视频/海螺480全能参考生视频v2-带音频_2089971327435370497.json, 视频生成/图生视频/海螺720全能参考生视频_2086044466351271938.json, 视频生成/文生视频/海螺h3文生视频1080_2088596323753881602.json, 视频生成/视频生视频/双模型加强版二采重绘_MinimaxH3全能参考_RH兼容版_2106029678061510657.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_56

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/海螺480全能参考生视频_2086053849802039298.json、视频生成/图生视频/海螺480全能参考生视频v2-带视频_2089973607303835649.json、视频生成/图生视频/海螺480全能参考生视频v2-带音频_2089971327435370497.json、视频生成/图生视频/海螺720全能参考生视频_2086044466351271938.json、视频生成/文生视频/海螺h3文生视频1080_2088596323753881602.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `INTConstant`
- `KSamplerSelect`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CM_IntToFloat` —— 5/6 个有
- `CR Prompt Text` —— 5/6 个有
- `FloatConstant` —— 5/6 个有
- `LoadAudio` —— 5/6 个有
- `LoadImage` —— 5/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/6 个有
- `ResizeShortestToNode` —— 5/6 个有
- `VHS_LoadVideo` —— 5/6 个有
- `EasyCache` —— 4/6 个有
- `LoraLoaderBypassModelOnly` —— 4/6 个有
- `ModelAttentionBackend` —— 4/6 个有
- `easy showAnything` —— 4/6 个有
- `ImageResizeKJv2` —— 3/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `PT_H3ConcatAVLatent` —— 3/6 个有
- `VAEEncode` —— 3/6 个有
- `VAEEncodeAudio` —— 3/6 个有
- `MiniMaxH3AVDecodeT8` —— 2/6 个有
- `MiniMaxH3AudioConditioningT8` —— 2/6 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 2/6 个有
- `MiniMaxH3SigmaShift` —— 2/6 个有
- `PathchSageAttentionKJ` —— 2/6 个有
- `SolAttnMiniMax` —— 2/6 个有
- `easy clearCacheAll` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `MiniMaxChunkFeedForward` —— 1/6 个有
- `MiniMaxLowVRAMAttention` —— 1/6 个有
- `PrimitiveFloat` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `TrimAudioDuration` —— 1/6 个有
- `UniBlockSwap` —— 1/6 个有
- `UniBlockSwapTE` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
