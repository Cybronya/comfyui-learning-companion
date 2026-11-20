---
name: unknown_workflow_video_lora_sampler_575
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9068
common_nodes: [BasicScheduler, CLIPLoader, CR Text, ConditioningZeroOut, H3SigmaRefiner, KSamplerSelect, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3Unified, ModelAttentionBackend, ResolutionSelector, SelfLiftH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/MinimaxH3动态迁移_2107344337523798018.json, 平台全量/MinimaxH3动态迁移黑科技工作流_2104527126065139713.json, 视频生成/文生视频/minimaxH3全能黑科技工作流（10s只需5分钟）_2098047284964585473.json, 视频生成/文生视频/minimaxH3单采_双采工作流_2100606405177856002.json, 视频生成/文生视频/【变态加速高清版】MinMaxH3 全能参考-推荐_2098434067468476417.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_575

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/MinimaxH3动态迁移_2107344337523798018.json、平台全量/MinimaxH3动态迁移黑科技工作流_2104527126065139713.json、视频生成/文生视频/minimaxH3全能黑科技工作流（10s只需5分钟）_2098047284964585473.json、视频生成/文生视频/minimaxH3单采_双采工作流_2100606405177856002.json、视频生成/文生视频/【变态加速高清版】MinMaxH3 全能参考-推荐_2098434067468476417.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CR Text`
- `ConditioningZeroOut`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3Unified`
- `ModelAttentionBackend`
- `ResolutionSelector`
- `SelfLiftH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 4/5 个有
- `MiniMaxLowVRAMAttention` —— 4/5 个有
- `ModelPreviewOverrideKJ` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `VHS_SelectImages` —— 4/5 个有
- `BasicGuider` —— 3/5 个有
- `Label (rgthree)` —— 3/5 个有
- `MiniMaxH3AVDecodeT8` —— 3/5 个有
- `RandomNoise` —— 3/5 个有
- `SamplerCustomAdvanced` —— 3/5 个有
- `DepthAnything_V2` —— 2/5 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 2/5 个有
- `VHS_LoadVideo` —— 2/5 个有
- `ComfyMathExpression` —— 1/5 个有
- `Float` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `SetNode` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
