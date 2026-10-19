---
name: unknown_workflow_sampler_unet_vae_76
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.883667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CreateVideo, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3-长视频生成_2095517026205913089.json, 视频生成/图生视频/Minimax H3首尾帧生视频-In8加速版_2084502270833676289.json, 视频生成/图生视频/Minimax H3首尾帧视频生成_2085198810418077698.json, 视频生成/图生视频/Minimax-H3-图生视频（Lightx2v加速）_2085944759729872898.json, 视频生成/图生视频/Minimax-H3-图生视频（Lightx2v正式版）_2087553566264356865.json, 视频生成/图生视频/Minimax-H3-多参考生成 官流_2095740048577744897.json, 视频生成/图生视频/MinimaxH3 4steps 九宫格漫剧工作流_2084470766388736001.json, 视频生成/图生视频/MinimaxH3 4steps 多参视频工作流_2084301091453362177.json, 视频生成/文生视频/FS-video_minimax_h3_r2v_2105628001928044546.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_76

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/Minimax H3-长视频生成_2095517026205913089.json、视频生成/图生视频/Minimax H3首尾帧生视频-In8加速版_2084502270833676289.json、视频生成/图生视频/Minimax H3首尾帧视频生成_2085198810418077698.json、视频生成/图生视频/Minimax-H3-图生视频（Lightx2v加速）_2085944759729872898.json、视频生成/图生视频/Minimax-H3-图生视频（Lightx2v正式版）_2087553566264356865.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 8/9 个有
- `PrimitiveFloat` —— 8/9 个有
- `ResolutionSelector` —— 8/9 个有
- `LoraLoaderModelOnly` —— 5/9 个有
- `MiniMaxH3ReferenceToVideo` —— 5/9 个有
- `MiniMaxH3ImageToVideo` —— 4/9 个有
- `PrimitiveStringMultiline` —— 4/9 个有
- `CR Prompt Text` —— 3/9 个有
- `MiniMaxH3SigmaShift` —— 3/9 个有
- `ModelAttentionBackend` —— 3/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/9 个有
- `PreviewAny` —— 2/9 个有
- `RHMiniMaxH3PromptOptimizer` —— 2/9 个有
- `BlockSparseAttention` —— 1/9 个有
- `ImageFromBatch` —— 1/9 个有
- `Label (rgthree)` —— 1/9 个有
- `MiniMaxH3AddGuide` —— 1/9 个有
- `ModelPreviewOverrideKJ` —— 1/9 个有
- `RHHiddenNodes` —— 1/9 个有
- `easy promptConcat` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
