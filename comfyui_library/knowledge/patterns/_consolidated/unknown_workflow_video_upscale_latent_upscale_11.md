---
name: unknown_workflow_video_upscale_latent_upscale_11
type: Unknown Workflow
frequency: 21
level: moderate
coverage: 0.655238
common_nodes: [BasicGuider, CLIPLoader, CR Prompt Text, ComfyMathExpression, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler参考生视频v2_2090687227016863745.json, 视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler参考生视频v2_2091039164530778113.json, 视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler参考生视频v2_2094625265921126401.json, 视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler图生视频V2_2090690174513664001.json, 视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler图生视频V2_2090981502527037441.json, 视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler图生视频_2090280306870931457.json, 视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler图生视频_2090767546290106369.json, 视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler图生视频_2093200891477319681.json, 视频生成/图生视频/Minimax H3横版文生视频Lantent Upscaler2_2091776496015863809.json, 视频生成/图生视频/Minimax+H3+Zs05+双采+加速+Lantent+Upscaler参考生视频_2092271863945846785.json, 视频生成/图生视频/Minimax-H3 潜空间放大一采预览锁种版_2098361825124511746.json, 视频生成/图生视频/Minimax-H3 静态动画图直转视频_2102710150153981954.json, 视频生成/图生视频/Minimax-H3电商宣传广告_2095444521084608514.json, 视频生成/图生视频/MinimaxH3-场景图生视频丨短剧视频制作专用_2099413880610050049.json, 视频生成/图生视频/【MINIMAX-H3】9图3音多参二采.json, 视频生成/图生视频/【MINIMAX-H3】remix版 数字人工作流_2095430810085187586.json, 视频生成/图生视频/【MINIMAX-H3】九月最强-高配版_2095715690450874369.json, 视频生成/图生视频/【MINIMAX-H3】九月最强文戏-高配版_2095723665865400322.json, 视频生成/图生视频/【MINIMAX-H3】八月最强文戏(修改版）_2103351056783728641.json, 视频生成/图生视频/【MINIMAX-H3】八月最强文戏-高配版-9x16竖屏720p版_2109859401766096897.json, 视频生成/文生视频/MINIMAX-H3文戏_2100864974695526401.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_11

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler参考生视频v2_2090687227016863745.json、视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler参考生视频v2_2091039164530778113.json、视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler参考生视频v2_2094625265921126401.json、视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler图生视频V2_2090690174513664001.json、视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler图生视频V2_2090981502527037441.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：66%

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
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `SolAttnMiniMax` —— 17/21 个有
- `GetNode` —— 11/21 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/21 个有
- `SetNode` —— 11/21 个有
- `LoadAudio` —— 10/21 个有
- `PreviewImage` —— 10/21 个有
- `忽略多组孤海` —— 8/21 个有
- `Fast Groups Bypasser (rgthree)` —— 4/21 个有
- `MiniMaxChunkFeedForward` —— 3/21 个有
- `MiniMaxLowVRAMAttention` —— 3/21 个有
- `BasicScheduler` —— 2/21 个有
- `Fast Groups Muter (rgthree)` —— 2/21 个有
- `ImageResizeKJv2` —— 2/21 个有
- `KSamplerSelect` —— 2/21 个有
- `LoraLoaderModelOnly` —— 2/21 个有
- `Seed (rgthree)` —— 2/21 个有
- `VAEDecode` —— 2/21 个有
- `CFGGuider` —— 1/21 个有
- `CLIPTextEncode` —— 1/21 个有
- `ComfyNumberConvert` —— 1/21 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/21 个有
- `EmptyMiniMaxH3LatentAV` —— 1/21 个有
- `FlashVSRNode` —— 1/21 个有
- `GIMMVFI_interpolate` —— 1/21 个有
- `LTXVConcatAVLatent` —— 1/21 个有
- `LTXVSeparateAVLatent` —— 1/21 个有
- `MiniMaxH3AddGuide` —— 1/21 个有
- `MiniMaxH3SigmaShift` —— 1/21 个有
- `ModelPreviewOverrideKJ` —— 1/21 个有
- `PrimitiveInt` —— 1/21 个有
- `PrimitiveStringMultiline` —— 1/21 个有
- `VAEDecodeAudio` —— 1/21 个有
- `VAEEncode` —— 1/21 个有
- `VAEEncodeAudio` —— 1/21 个有
- `easy cleanGpuUsed` —— 1/21 个有
- `easy showAnything` —— 1/21 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
