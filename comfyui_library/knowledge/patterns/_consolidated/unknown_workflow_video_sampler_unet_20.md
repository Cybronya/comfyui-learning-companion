---
name: unknown_workflow_video_sampler_unet_20
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.455778
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3-视频模仿_2088128829062729729.json, 视频生成/图生视频/MiniMax-H3开源 8step+高动态加速流图生视频_2088598452845506561.json, 视频生成/图生视频/Minimax H3 N宫格视频_2098678084865183745.json, 视频生成/图生视频/MinimaxH3-满血int8单采八部加速Sigma版V4_2092900303573180418.json, 视频生成/图生视频/MinimaxH3满血FP16+剪枝int8+浅空间放大二采工作流v4_2092911777758662657.json, 视频生成/文生视频/MiniMax H3-多参生视频二采15秒，24g可跑_2098839012025917442.json, 视频生成/文生视频/MiniMax H3-多参考7P3A2V生视频-二采优化版_2100164228442316802.json, 视频生成/文生视频/MiniMax H3-多参考7P3A2V生视频-优化版_2100173828486950913.json, 视频生成/文生视频/MiniMax H3-多参考生视频-优化版_2094671259807338497.json, 视频生成/文生视频/MiniMax H3-多参考生视频-优化版_2095111201637359618.json, 视频生成/文生视频/MiniMax H3-多参考生视频-优化版_2095422044593811457.json, 视频生成/文生视频/MiniMax H3-多参考生视频-优化版_2096048331687555073.json, 视频生成/文生视频/MiniMax H3-多参考生视频-优化版_2104154909896699906.json, 视频生成/文生视频/MiniMax H3-多参考生视频-最新优化版_2104888496719745025.json, 视频生成/文生视频/MiniMax H3-多参考生视频_2095195704401682433.json, 视频生成/文生视频/MiniMax H3-多图多音频视频参考生视频-无水印优化版_2095090395578462210.json, 视频生成/文生视频/MiniMax+H3-多参考生视频（9图片+3视频+3音频）_2101587742454009857.json, 视频生成/文生视频/Minimax H3 双采万能流_2094836628819894274.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_20

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3-视频模仿_2088128829062729729.json、视频生成/图生视频/MiniMax-H3开源 8step+高动态加速流图生视频_2088598452845506561.json、视频生成/图生视频/Minimax H3 N宫格视频_2098678084865183745.json、视频生成/图生视频/MinimaxH3-满血int8单采八部加速Sigma版V4_2092900303573180418.json、视频生成/图生视频/MinimaxH3满血FP16+剪枝int8+浅空间放大二采工作流v4_2092911777758662657.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：46%

## 共有节点

全部 18 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 17/18 个有
- `LoraLoaderModelOnly` —— 17/18 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 17/18 个有
- `SetNode` —— 17/18 个有
- `VHS_LoadVideo` —— 17/18 个有
- `LoadAudio` —— 16/18 个有
- `PrimitiveFloat` —— 15/18 个有
- `Text` —— 15/18 个有
- `LTXVConcatAVLatent` —— 14/18 个有
- `LTXVSeparateAVLatent` —— 14/18 个有
- `MinimaxH3LatentUpscaler3D` —— 14/18 个有
- `SplitSigmas` —— 14/18 个有
- `easy float` —— 13/18 个有
- `忽略多组孤海` —— 12/18 个有
- `ModelPreviewOverrideKJ` —— 5/18 个有
- `ModelAttentionBackend` —— 4/18 个有
- `PathchSageAttentionKJ` —— 3/18 个有
- `Fast Groups Bypasser (rgthree)` —— 2/18 个有
- `Float` —— 2/18 个有
- `H3SigmaRefiner` —— 2/18 个有
- `Text Multiline` —— 2/18 个有
- `CR Prompt Text` —— 1/18 个有
- `EasyCache` —— 1/18 个有
- `SigmasGraph` —— 1/18 个有
- `easy cleanGpuUsed` —— 1/18 个有
- `easy getNode` —— 1/18 个有
- `easy setNode` —— 1/18 个有
- `easy sleep` —— 1/18 个有
- `图像缩放范围孤海` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
