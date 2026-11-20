---
name: unknown_workflow_sampler_unet_vae_108
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.857182
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CreateVideo, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3-长视频生成_2095517026205913089.json, 视频生成/图生视频/Minimax H3图生视频_2084833087787192322.json, 视频生成/图生视频/Minimax H3首尾帧生视频-In8加速版_2084502270833676289.json, 视频生成/图生视频/Minimax H3首尾帧视频生成_2085198810418077698.json, 视频生成/图生视频/Minimax-H3-R2V 开源版本 多参考生视频_2084285644305682434.json, 视频生成/图生视频/Minimax-H3-图生视频（Lightx2v加速）_2085944759729872898.json, 视频生成/图生视频/Minimax-H3-图生视频（Lightx2v正式版）_2087553566264356865.json, 视频生成/图生视频/Minimax-H3-多参考生成 官流_2095740048577744897.json, 视频生成/图生视频/MinimaxH3 4steps 九宫格漫剧工作流_2084470766388736001.json, 视频生成/图生视频/MinimaxH3 4steps 多参视频工作流_2084301091453362177.json, 视频生成/图生视频/minimax   h3 最强动作迁移_2089285244263424001.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_108

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/Minimax H3-长视频生成_2095517026205913089.json、视频生成/图生视频/Minimax H3图生视频_2084833087787192322.json、视频生成/图生视频/Minimax H3首尾帧生视频-In8加速版_2084502270833676289.json、视频生成/图生视频/Minimax H3首尾帧视频生成_2085198810418077698.json、视频生成/图生视频/Minimax-H3-R2V 开源版本 多参考生视频_2084285644305682434.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 11 个 workflow 都包含：
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
- `ComfyMathExpression` —— 10/11 个有
- `PrimitiveFloat` —— 10/11 个有
- `ResolutionSelector` —— 10/11 个有
- `LoraLoaderModelOnly` —— 6/11 个有
- `MiniMaxH3ReferenceToVideo` —— 6/11 个有
- `PrimitiveStringMultiline` —— 6/11 个有
- `MiniMaxH3ImageToVideo` —— 5/11 个有
- `CR Prompt Text` —— 3/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/11 个有
- `MiniMaxH3SigmaShift` —— 3/11 个有
- `ModelAttentionBackend` —— 3/11 个有
- `MiniMaxH3AddGuide` —— 2/11 个有
- `ModelPreviewOverrideKJ` —— 2/11 个有
- `PreviewAny` —— 2/11 个有
- `RHMiniMaxH3PromptOptimizer` —— 2/11 个有
- `GetNode` —— 1/11 个有
- `ImageFromBatch` —— 1/11 个有
- `ImageResizeKJv2` —— 1/11 个有
- `RHHiddenNodes` —— 1/11 个有
- `RTXVideoSuperResolution` —— 1/11 个有
- `SetNode` —— 1/11 个有
- `SolAttnMiniMax` —— 1/11 个有
- `UniBlockSwapTE` —— 1/11 个有
- `VHS_LoadVideo` —— 1/11 个有
- `easy promptConcat` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
