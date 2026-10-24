---
name: unknown_workflow_video_upscale_latent_upscale_49
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.49325
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MinimaxH3全能参考高清放大工作流_2110689506868424706.json, 视频生成/图生视频/MinimaxH3动作迁移-人物替换！完美优化_2110384977471954946.json, 视频生成/图生视频/MinimaxH3满血FP16+剪枝int8+浅空间放大二采工作流v4_2092911777758662657.json, 视频生成/图生视频/YZ金鱼-MiniMax H3-多参考生视频-优化版-9图全开_2099011685452439553.json, 视频生成/图生视频/h3图生视频gy_2087784031445413890.json, 视频生成/图生视频/minimax h3电商产品_2095444070079492097.json, 视频生成/图生视频/双倍高清放大MiniMax H3-多参考生视频-字节DMAD加速版_2106606807736209409.json, 视频生成/文生视频/MiniMax H3 武戏全能视频V3_2095388978387185666.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_49

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3全能参考高清放大工作流_2110689506868424706.json、视频生成/图生视频/MinimaxH3动作迁移-人物替换！完美优化_2110384977471954946.json、视频生成/图生视频/MinimaxH3满血FP16+剪枝int8+浅空间放大二采工作流v4_2092911777758662657.json、视频生成/图生视频/YZ金鱼-MiniMax H3-多参考生视频-优化版-9图全开_2099011685452439553.json、视频生成/图生视频/h3图生视频gy_2087784031445413890.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：49%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 7/8 个有
- `PrimitiveFloat` —— 7/8 个有
- `SetNode` —— 7/8 个有
- `LoadAudio` —— 6/8 个有
- `SplitSigmas` —— 6/8 个有
- `Text` —— 6/8 个有
- `easy float` —— 6/8 个有
- `VHS_LoadVideo` —— 5/8 个有
- `忽略多组孤海` —— 5/8 个有
- `H3SigmaRefiner` —— 3/8 个有
- `ModelAttentionBackend` —— 2/8 个有
- `Astra` —— 1/8 个有
- `ExtendIntermediateSigmas` —— 1/8 个有
- `ImageFromBatch` —— 1/8 个有
- `Int` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `LoadVideo` —— 1/8 个有
- `MiniMaxH3AVDecodeT8` —— 1/8 个有
- `ModelPreviewOverrideKJ` —— 1/8 个有
- `PathchSageAttentionKJ` —— 1/8 个有
- `SaveVideo` —— 1/8 个有
- `Text Multiline` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有
- `easy int` —— 1/8 个有
- `easy showAnything` —— 1/8 个有
- `孤海注释` —— 1/8 个有
- `获取视频信息` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
