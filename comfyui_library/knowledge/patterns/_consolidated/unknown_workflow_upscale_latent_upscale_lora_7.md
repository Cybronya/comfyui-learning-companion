---
name: unknown_workflow_upscale_latent_upscale_lora_7
type: Unknown Workflow
frequency: 21
level: moderate
coverage: 0.50381
common_nodes: [BasicGuider, CLIPLoader, CR Prompt Text, ComfyMathExpression, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【MINIMAX-H3】八月最强文戏-高配版_2098949863919673345.json, 图片生成/图生图/【MINIMAX-H3】八月最强文戏-高配版_2099061501553373185.json, 数字人/数字人/Minmax h3文戏——Reminx_10Eros模型_2094475274502103042.json, 视频生成/图生视频/MINIMAX-H3文戏工作流_2102802402159194114.json, 视频生成/图生视频/MINIMAX-H3文戏工作流_2106920065542213634.json, 视频生成/图生视频/MiniMax‑H3‑Remix+双采+加速+Lantent Upscaler参考生视频_2093178030909906946.json, 视频生成/图生视频/Minimax-H3 潜空间放大一采预览锁种版_2098361825124511746.json, 视频生成/图生视频/Minimax-H3 静态动画图直转视频_2102710150153981954.json, 视频生成/图生视频/Minimax-H3电商宣传广告_2095444521084608514.json, 视频生成/图生视频/MinimaxH3-场景图生视频丨短剧视频制作专用_2099413880610050049.json, 视频生成/图生视频/【MINIMAX-H3】9图3音多参二采.json, 视频生成/图生视频/【MINIMAX-H3】remix版 数字人工作流_2095430810085187586.json, 视频生成/图生视频/【MINIMAX-H3】九月最强-高配版_2095715690450874369.json, 视频生成/图生视频/【MINIMAX-H3】九月最强文戏-高配版_2095723665865400322.json, 视频生成/图生视频/【MINIMAX-H3】八月最强文戏-高配版-9x16竖屏720p版_2109859401766096897.json, 视频生成/图生视频/【MINIMAX-H3】八月最强文戏-高配版_2093430287630946306.json, 视频生成/图生视频/【MINIMAX-H3】八月最强文戏-高配版_2101959513443229697.json, 视频生成/图生视频/【MINIMAX-H3】文戏-高配版_2095322428657455106.json, 视频生成/图生视频/【MINIMAX-H3】文戏短剧工作流_2095794773864050689.json, 视频生成/图生视频/【MINIMAX-H3】文戏高配版_2109312312128663553.json, 视频生成/文生视频/啊癫 MINIMAX短剧工作流（去油版)_2094462071349014529.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_7

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/图生图/【MINIMAX-H3】八月最强文戏-高配版_2098949863919673345.json、图片生成/图生图/【MINIMAX-H3】八月最强文戏-高配版_2099061501553373185.json、数字人/数字人/Minmax h3文戏——Reminx_10Eros模型_2094475274502103042.json、视频生成/图生视频/MINIMAX-H3文戏工作流_2102802402159194114.json、视频生成/图生视频/MINIMAX-H3文戏工作流_2106920065542213634.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：50%

## 共有节点

全部 21 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 20/21 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 20/21 个有
- `SetNode` —— 20/21 个有
- `VHS_VideoCombine` —— 20/21 个有
- `LoadAudio` —— 19/21 个有
- `PreviewImage` —— 19/21 个有
- `SolAttnMiniMax` —— 15/21 个有
- `忽略多组孤海` —— 15/21 个有
- `Fast Groups Bypasser (rgthree)` —— 5/21 个有
- `MiniMaxChunkFeedForward` —— 3/21 个有
- `MiniMaxLowVRAMAttention` —— 3/21 个有
- `EmptyImage` —— 2/21 个有
- `Fast Groups Muter (rgthree)` —— 2/21 个有
- `Seed (rgthree)` —— 2/21 个有
- `CreateVideo` —— 1/21 个有
- `LoraLoaderModelOnly` —— 1/21 个有
- `ModelPreviewOverrideKJ` —— 1/21 个有
- `PlaySound|pysssss` —— 1/21 个有
- `SaveImage` —— 1/21 个有
- `SaveVideo` —— 1/21 个有
- `easy imageChooser` —— 1/21 个有
- `kkVideoFirstLastFrames` —— 1/21 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
