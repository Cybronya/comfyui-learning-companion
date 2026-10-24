---
name: unknown_workflow_video_lora_sampler_763
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7745
common_nodes: [BasicGuider, BasicScheduler, Bjornulf_ShowFloat, CLIPLoader, ComfyMathExpression, CreateVideo, JjkText, JoinStrings, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PreviewImage, PrimitiveStringMultiline, RH_LLMAPI_Pro_Node, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3 深度引导动作迁移 单人版_2091353483743154177.json, 视频生成/图生视频/Minimax_H3_人物替换单人版_自动反推_2101085246136610818.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_763

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Minimax H3 深度引导动作迁移 单人版_2091353483743154177.json、视频生成/图生视频/Minimax_H3_人物替换单人版_自动反推_2101085246136610818.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `Bjornulf_ShowFloat`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `JjkText`
- `JoinStrings`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `BiRefNet_Hugo` —— 1/2 个有
- `EasyCache` —— 1/2 个有
- `EmptyImage` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `SaveVideo` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `VAEDecodeAudio` —— 1/2 个有
- `VideoFrameSelector` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
