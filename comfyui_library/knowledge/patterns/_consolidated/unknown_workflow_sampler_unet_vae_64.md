---
name: unknown_workflow_sampler_unet_vae_64
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8878
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3-lightx2v不同版加速lora测试_2096422700070817794.json, 视频生成/图生视频/Minimax H3-t2v 多图参考生视频_2084205760405397505.json, 视频生成/图生视频/Minimax H3-最佳动态战斗版V2_2096214859611467777.json, 视频生成/图生视频/Minimax-H3-多参考生成 官流_2095740048577744897.json, 视频生成/图生视频/MinimaxH3 4steps 九宫格漫剧工作流_2084470766388736001.json, 视频生成/图生视频/MinimaxH3 4steps 多参视频工作流_2084301091453362177.json, 视频生成/文生视频/minimaxH3文生视频武器打斗转用工作流_2095690809084571649.json, 视频生成/文生视频/【遇见AI】minimax H3 高动态打斗场景武术动作二采修复+提示词skill工作流_2095684866888257537.json, 视频生成/文生视频/剑斗多参模式_2094373732667187201.json, 视频生成/文生视频/战斗双采首尾帧模式_2094373774731862018.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_64

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/Minimax H3-lightx2v不同版加速lora测试_2096422700070817794.json、视频生成/图生视频/Minimax H3-t2v 多图参考生视频_2084205760405397505.json、视频生成/图生视频/Minimax H3-最佳动态战斗版V2_2096214859611467777.json、视频生成/图生视频/Minimax-H3-多参考生成 官流_2095740048577744897.json、视频生成/图生视频/MinimaxH3 4steps 九宫格漫剧工作流_2084470766388736001.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
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
- `MiniMaxH3ReferenceToVideo` —— 9/10 个有
- `LoraLoaderModelOnly` —— 8/10 个有
- `PrimitiveStringMultiline` —— 7/10 个有
- `DisableNoise` —— 5/10 个有
- `ExtendIntermediateSigmas` —— 4/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/10 个有
- `SplitSigmasDenoise` —— 4/10 个有
- `easy cleanGpuUsed` —— 4/10 个有
- `CR Prompt Text` —— 3/10 个有
- `CLIPTextEncode` —— 2/10 个有
- `ModelAttentionBackend` —— 2/10 个有
- `PreviewAny` —— 2/10 个有
- `RHMiniMaxH3PromptOptimizer` —— 2/10 个有
- `AddLabel` —— 1/10 个有
- `ImageConcatMulti` —— 1/10 个有
- `MiniMaxH3ImageToVideo` —— 1/10 个有
- `ModelPreviewOverrideKJ` —— 1/10 个有
- `SplitSigmas` —— 1/10 个有
- `VHS_VideoCombine` —— 1/10 个有
- `easy promptConcat` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
