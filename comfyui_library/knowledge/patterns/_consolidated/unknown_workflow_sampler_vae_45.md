---
name: unknown_workflow_sampler_vae_45
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.8505
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax_H3图生视频V1_2087430143055847430.json, 视频生成/图生视频/Minimax H3 - 图生视频-首尾帧视频_2095067656989798402.json, 视频生成/图生视频/Minimax H3 人物替换 单人极速版_2109840033103568897.json, 视频生成/图生视频/Minimax H3 人物替换 单人稳定版_2086341252592783361.json, 视频生成/图生视频/Minimax H3 人物替换 双人极速版_2109844433255620610.json, 视频生成/图生视频/Minimax H3 动作迁移 单人稳定版_2085382065066958850.json, 视频生成/图生视频/Minimax H3 深度引导动作迁移 单人版_2091353483743154177.json, 视频生成/图生视频/Minimax_H3_人物替换单人版_自动反推_2101085246136610818.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_45

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/MiniMax_H3图生视频V1_2087430143055847430.json、视频生成/图生视频/Minimax H3 - 图生视频-首尾帧视频_2095067656989798402.json、视频生成/图生视频/Minimax H3 人物替换 单人极速版_2109840033103568897.json、视频生成/图生视频/Minimax H3 人物替换 单人稳定版_2086341252592783361.json、视频生成/图生视频/Minimax H3 人物替换 双人极速版_2109844433255620610.json…）

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
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 7/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/8 个有
- `UNETLoader` —— 7/8 个有
- `VAEDecodeAudio` —— 7/8 个有
- `CreateVideo` —— 6/8 个有
- `MiniMaxH3ReferenceToVideo` —— 6/8 个有
- `VHS_LoadVideo` —— 6/8 个有
- `VHS_VideoCombine` —— 6/8 个有
- `VHS_VideoInfoLoaded` —— 6/8 个有
- `PrimitiveStringMultiline` —— 5/8 个有
- `easy showAnything` —— 5/8 个有
- `Bjornulf_ShowFloat` —— 4/8 个有
- `JjkText` —— 4/8 个有
- `JoinStrings` —— 4/8 个有
- `RH_LLMAPI_Pro_Node` —— 4/8 个有
- `EasyCache` —— 3/8 个有
- `SaveVideo` —— 3/8 个有
- `MiniMaxH3ImageToVideo` —— 2/8 个有
- `MuyeTextEditOutput` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `PrimitiveFloat` —— 2/8 个有
- `VideoFrameSelector` —— 2/8 个有
- `AIO_Preprocessor` —— 1/8 个有
- `BiRefNet_Hugo` —— 1/8 个有
- `DiffusionModelLoaderKJ` —— 1/8 个有
- `EmptyImage` —— 1/8 个有
- `GetNode` —— 1/8 个有
- `SetNode` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
