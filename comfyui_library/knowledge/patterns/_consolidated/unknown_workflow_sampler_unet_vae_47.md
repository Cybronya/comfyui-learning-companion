---
name: unknown_workflow_sampler_unet_vae_47
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.841867
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Minimax H3-t2v 官方提示词文生视频_2085182661756276737.json, 视频生成/文生视频/Minimax H3-t2v 官方版文生视频_2084192379581583362.json, 视频生成/文生视频/Minimax H3-文生视频（高动态去噪点）_2089345292486402050.json, 视频生成/文生视频/Minimax H3视频模型文生视频_2084169698551361537.json, 视频生成/文生视频/Minimax h3 4 步 lora2 加速版_2092076952441151490.json, 视频生成/文生视频/Minimax+H3+Multi-parameter+Reference+Raw+Video_2084191041938345986.json, 视频生成/文生视频/Minimax-H3-T2V 开源版本+文生视频_2084249084893945858.json, 视频生成/文生视频/Minimax-H3-文生视频（Lightx2v加速）_2085988885787660289.json, 视频生成/文生视频/Minimax-H3-文生视频（Lightx2v正式版）_2087549637837283330.json, 视频生成/文生视频/Minimax-H3_T2V（文生视频_本地可用）_2084287507390353409.json, 视频生成/文生视频/MinimaxH3-全能参考生视频-夏_2093873460580802561.json, 视频生成/文生视频/MinimaxH3参考生成视频工作流_2088693526279319553.json, 视频生成/文生视频/MinimaxH3开源版 9-3-3参考生视频_2095459758181535745.json, 视频生成/文生视频/Minmax H3参考加速工作流_2086695240752263170.json, 视频生成/文生视频/minimax-h3 单采_2100560974238535682.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_47

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/文生视频/Minimax H3-t2v 官方提示词文生视频_2085182661756276737.json、视频生成/文生视频/Minimax H3-t2v 官方版文生视频_2084192379581583362.json、视频生成/文生视频/Minimax H3-文生视频（高动态去噪点）_2089345292486402050.json、视频生成/文生视频/Minimax H3视频模型文生视频_2084169698551361537.json、视频生成/文生视频/Minimax h3 4 步 lora2 加速版_2092076952441151490.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ImageToVideo` —— 9/15 个有
- `LoraLoaderModelOnly` —— 8/15 个有
- `LoadImage` —— 7/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/15 个有
- `MiniMaxH3ReferenceToVideo` —— 6/15 个有
- `ModelAttentionBackend` —— 5/15 个有
- `PrimitiveStringMultiline` —— 5/15 个有
- `LoadAudio` —— 4/15 个有
- `LoadVideo` —— 4/15 个有
- `GetVideoComponents` —— 3/15 个有
- `CR Prompt Text` —— 2/15 个有
- `ExtendIntermediateSigmas` —— 2/15 个有
- `H3SigmaRefiner` —— 2/15 个有
- `GetNode` —— 1/15 个有
- `Int` —— 1/15 个有
- `ManualSigmas` —— 1/15 个有
- `MiniMaxChunkFeedForward` —— 1/15 个有
- `MiniMaxH3SigmaShift` —— 1/15 个有
- `MiniMaxLowVRAMAttention` —— 1/15 个有
- `Seed (rgthree)` —— 1/15 个有
- `SetNode` —— 1/15 个有
- `SigmasPreview` —— 1/15 个有
- `VHS_LoadVideo` —— 1/15 个有
- `easy showAnything` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
