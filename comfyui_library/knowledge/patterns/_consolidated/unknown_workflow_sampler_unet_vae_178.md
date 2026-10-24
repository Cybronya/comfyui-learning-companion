---
name: unknown_workflow_sampler_unet_vae_178
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.747
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax h3 故事多分镜图处理_2096523123339386881.json, 视频生成/图生视频/Minimax h3 高一致性-故事多分镜图处理_2103117440178810882.json, 视频生成/图生视频/Minimax+H3+多图生视频声音一致性工作流_2084677543038377986.json, 视频生成/图生视频/Minimax-H3 整合流程_2086427491039801346.json, 视频生成/图生视频/Minimax-H3-多参-长视频-原版-736p直出_2096509767048060930.json, 视频生成/文生视频/Minimax-H3-✅文生长视频-原版-736p直出_2101978013062746113.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_178

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/Minimax h3 故事多分镜图处理_2096523123339386881.json、视频生成/图生视频/Minimax h3 高一致性-故事多分镜图处理_2103117440178810882.json、视频生成/图生视频/Minimax+H3+多图生视频声音一致性工作流_2084677543038377986.json、视频生成/图生视频/Minimax-H3 整合流程_2086427491039801346.json、视频生成/图生视频/Minimax-H3-多参-长视频-原版-736p直出_2096509767048060930.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 5/6 个有
- `LoadImage` —— 5/6 个有
- `MiniMaxH3ReferenceToVideo` —— 5/6 个有
- `VHS_VideoCombine` —— 5/6 个有
- `ModelAttentionBackend` —— 4/6 个有
- `CreateVideo` —— 3/6 个有
- `LoadAudio` —— 3/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/6 个有
- `GetImagesFromBatchIndexed` —— 2/6 个有
- `GetVideoComponents` —— 2/6 个有
- `LoadVideoUI` —— 2/6 个有
- `MiniMaxH3ImageToVideo` —— 2/6 个有
- `MiniMaxH3MotionContext` —— 2/6 个有
- `MiniMaxH3MotionContextTrim` —— 2/6 个有
- `MiniMaxH3SigmaShift` —— 2/6 个有
- `SaveImage` —— 2/6 个有
- `孤海注释` —— 2/6 个有
- `BlockSparseAttention` —— 1/6 个有
- `SaveVideo` —— 1/6 个有
- `UniBlockSwap` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有
- `easy int` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
