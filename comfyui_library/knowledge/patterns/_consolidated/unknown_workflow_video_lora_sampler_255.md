---
name: unknown_workflow_video_lora_sampler_255
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.926375
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CR Text, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3Unified, ModelAttentionBackend, ModelPreviewOverrideKJ, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax_H3_All-in-One_Accelerated_V3_一体化工作流_2099771065894522882.json, 视频生成/图生视频/MiniMax_H3_All-in-One_Accelerated_V3_一体化工作流_2100032213063659521.json, 视频生成/图生视频/MinimaxH3自定义sigam工作流_2109984744522993665.json, 视频生成/图生视频/商业级360度环绕镜头展示工作流_2110737948009385985.json, 视频生成/图生视频/商业级360度环绕镜头展示工作流_2111237385672544258.json, 视频生成/文生视频/minimaxH3全能黑科技工作流（10s只需5分钟）_2098047284964585473.json, 视频生成/文生视频/minimaxH3单采_双采工作流_2100606405177856002.json, 视频生成/文生视频/【变态加速高清版】MinMaxH3 全能参考-推荐_2098434067468476417.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_255

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/MiniMax_H3_All-in-One_Accelerated_V3_一体化工作流_2099771065894522882.json、视频生成/图生视频/MiniMax_H3_All-in-One_Accelerated_V3_一体化工作流_2100032213063659521.json、视频生成/图生视频/MinimaxH3自定义sigam工作流_2109984744522993665.json、视频生成/图生视频/商业级360度环绕镜头展示工作流_2110737948009385985.json、视频生成/图生视频/商业级360度环绕镜头展示工作流_2111237385672544258.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CR Text`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3Unified`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 7/8 个有
- `MiniMaxChunkFeedForward` —— 6/8 个有
- `MiniMaxLowVRAMAttention` —— 6/8 个有
- `VAEDecode` —— 6/8 个有
- `VAEDecodeAudio` —— 6/8 个有
- `H3SigmaRefiner` —— 5/8 个有
- `MiniMaxH3AVDecodeT8` —— 5/8 个有
- `ConditioningZeroOut` —— 3/8 个有
- `Fast Groups Bypasser (rgthree)` —— 3/8 个有
- `PreviewImage` —— 3/8 个有
- `SelfLiftH3Sampler` —— 3/8 个有
- `SetNode` —— 3/8 个有
- `VHS_SelectImages` —— 3/8 个有
- `MemoryCleaner` —— 2/8 个有
- `BlockSparseAttention` —— 1/8 个有
- `ComfyMathExpression` —— 1/8 个有
- `Float` —— 1/8 个有
- `GetNode` —— 1/8 个有
- `ManualSigmas` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
