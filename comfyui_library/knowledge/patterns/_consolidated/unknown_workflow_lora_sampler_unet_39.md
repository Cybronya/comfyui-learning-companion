---
name: unknown_workflow_lora_sampler_unet_39
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.80275
common_nodes: [BasicGuider, BasicScheduler, Bjornulf_ShowFloat, CLIPLoader, ComfyMathExpression, CreateVideo, JjkText, JoinStrings, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, RH_LLMAPI_Pro_Node, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoInfoLoaded, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3 人物替换 单人稳定版_2086341252592783361.json, 视频生成/图生视频/Minimax H3 动作迁移 单人稳定版_2085382065066958850.json, 视频生成/图生视频/Minimax H3 深度引导动作迁移 单人版_2091353483743154177.json, 视频生成/图生视频/Minimax_H3_人物替换单人版_自动反推_2101085246136610818.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_39

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Minimax H3 人物替换 单人稳定版_2086341252592783361.json、视频生成/图生视频/Minimax H3 动作迁移 单人稳定版_2085382065066958850.json、视频生成/图生视频/Minimax H3 深度引导动作迁移 单人版_2091353483743154177.json、视频生成/图生视频/Minimax_H3_人物替换单人版_自动反推_2101085246136610818.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 4 个 workflow 都包含：
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
- `PrimitiveStringMultiline`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoInfoLoaded`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `EasyCache` —— 3/4 个有
- `SaveVideo` —— 3/4 个有
- `VAEDecodeAudio` —— 3/4 个有
- `PreviewImage` —— 2/4 个有
- `VHS_VideoCombine` —— 2/4 个有
- `VideoFrameSelector` —— 2/4 个有
- `AIO_Preprocessor` —— 1/4 个有
- `BiRefNet_Hugo` —— 1/4 个有
- `EmptyImage` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `SetNode` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
