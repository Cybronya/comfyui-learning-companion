---
name: unknown_workflow_video_sampler_unet_56
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.846
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/minimax H3巨物图生视频_2093886571169796098.json, 视频生成/图生视频/minimax H3巨物图生视频_2097867227113541634.json, 视频生成/图生视频/minimax_h3图生视频_2084523818936262657.json, 视频生成/图生视频/minimax_图生视频8步加速_2087371300875620353.json, 视频生成/图生视频/单图Minimax H3_2085688315197616129.json, 视频生成/图生视频/无限长视频流_2105728965766897665.json, 视频生成/图生视频/高尚无限长视频流_2098617968786763777.json, 视频生成/文生视频/MiniMax H3超长视频流 一次直出2分15秒视频 （135S）_2101639116063600641.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_56

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/minimax H3巨物图生视频_2093886571169796098.json、视频生成/图生视频/minimax H3巨物图生视频_2097867227113541634.json、视频生成/图生视频/minimax_h3图生视频_2084523818936262657.json、视频生成/图生视频/minimax_图生视频8步加速_2087371300875620353.json、视频生成/图生视频/单图Minimax H3_2085688315197616129.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 7/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/8 个有
- `Label (rgthree)` —— 4/8 个有
- `MiniMaxH3ImageToVideo` —— 4/8 个有
- `MiniMaxH3ReferenceToVideo` —— 4/8 个有
- `PrimitiveStringMultiline` —— 4/8 个有
- `AudioConcat` —— 3/8 个有
- `GetImageRangeFromBatch` —— 3/8 个有
- `ImageBatchMulti` —— 3/8 个有
- `LayerColor: ColorAdapter` —— 3/8 个有
- `MiniMaxH3AddGuide` —— 3/8 个有
- `SaveAudio` —— 3/8 个有
- `ManualSigmas` —— 2/8 个有
- `RHLLMChatNode` —— 2/8 个有
- `ShowText|pysssss` —— 2/8 个有
- `SplitSigmas` —— 2/8 个有
- `MuyeTextEditOutput` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
