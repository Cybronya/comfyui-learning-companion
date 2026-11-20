---
name: unknown_workflow_upscale_latent_upscale_sampler_7
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.46425
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3-单模双采放大工作流（8G显存版）_2106241845180329986.json, 视频生成/图生视频/MiniMax H3-多参考生视频-优化版_2098769440409219073.json, 视频生成/图生视频/MinimaxH3满血FP16+剪枝int8+浅空间放大二采工作流v4_2092911777758662657.json, 视频生成/文生视频/H3 数字人口播工作流｜人物场景图 + 音频生成自然 Vlog 口播视频_2103802643083780098.json, 视频生成/文生视频/MiniMax H3-多参生视频二采15秒，24g可跑_2098839012025917442.json, 视频生成/文生视频/MiniMax H3-多参考生视频-优化版_2096048331687555073.json, 视频生成/文生视频/MiniMax H3-多参考生视频-优化版_2104154909896699906.json, 视频生成/文生视频/MiniMax H3-多参考生视频-最新优化版_2104888496719745025.json, 视频生成/文生视频/MiniMax H3-多参考生视频_2095195704401682433.json, 视频生成/文生视频/MiniMax H3-多图多音频视频参考生视频-无水印优化版_2095090395578462210.json, 视频生成/文生视频/MiniMax+H3-多参考生视频（9图片+3视频+3音频）_2101587742454009857.json, 视频生成/文生视频/Minimax H3 双采万能流_2094836628819894274.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_7

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3-单模双采放大工作流（8G显存版）_2106241845180329986.json、视频生成/图生视频/MiniMax H3-多参考生视频-优化版_2098769440409219073.json、视频生成/图生视频/MinimaxH3满血FP16+剪枝int8+浅空间放大二采工作流v4_2092911777758662657.json、视频生成/文生视频/H3 数字人口播工作流｜人物场景图 + 音频生成自然 Vlog 口播视频_2103802643083780098.json、视频生成/文生视频/MiniMax H3-多参生视频二采15秒，24g可跑_2098839012025917442.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：46%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 11/12 个有
- `LoadAudio` —— 11/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 11/12 个有
- `SetNode` —— 11/12 个有
- `VAEDecodeAudio` —— 11/12 个有
- `VHS_VideoCombine` —— 11/12 个有
- `LoraLoaderModelOnly` —— 10/12 个有
- `VHS_LoadVideo` —— 10/12 个有
- `easy float` —— 10/12 个有
- `Text` —— 9/12 个有
- `忽略多组孤海` —— 7/12 个有
- `ModelAttentionBackend` —— 4/12 个有
- `ModelPreviewOverrideKJ` —— 4/12 个有
- `Fast Groups Bypasser (rgthree)` —— 3/12 个有
- `easy cleanGpuUsed` —— 3/12 个有
- `CreateVideo` —— 2/12 个有
- `PathchSageAttentionKJ` —— 2/12 个有
- `SaveVideo` —— 2/12 个有
- `Text Multiline` —— 2/12 个有
- `easy loraStack` —— 2/12 个有
- `easy loraStackApply` —— 2/12 个有
- `H3SigmaRefiner` —— 1/12 个有
- `PrimitiveStringMultiline` —— 1/12 个有
- `easy getNode` —— 1/12 个有
- `easy int` —— 1/12 个有
- `easy setNode` —— 1/12 个有
- `easy sleep` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
