---
name: unknown_workflow_sampler_unet_vae_4
type: Unknown Workflow
frequency: 32
level: moderate
coverage: 0.845969
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/MiniMax H3 加速版-文生视频_2084834194160701441.json, 图片生成/文生图/Minimax H3-t2v 创意时装大片文生视频_2084847961032454145.json, 图片生成/文生图/Minimax H3-t2v 官方提示词文生视频_2084933973188366337.json, 图片生成/文生图/video_minimax_h3_t2v_2087382436262006785.json, 图片生成/文生图/【1】文生视频（无参考图模式）video_minimax_h3_i2v_2087195498171158529.json, 平台全量/(2倍速！量化加速版)Minimax多参生视频V2_2086298342648279042.json, 平台全量/(768P)Minimax多参生视频BF16高质量加速版V2_2086315027027554306.json, 平台全量/(8步加速-768P)Minimax参考生视频V1(第四版加速模型)_2086307246572662785.json, 平台全量/(8步加速-768P)Minimax参考生视频V1_2086134653450285057.json, 数字人/数字人/H3数字人_2092831814367924225.json, 视频生成/图生视频/(10Eros-Max V3)Minimax参考生视频BF16高质量加速版V3_2086185973813174274.json, 视频生成/图生视频/(10Eros-Max V3)Minimax图生视频BF16高质量加速版V3_2086166525018464258.json, 视频生成/图生视频/(10Eros-Max)MinimaxH3开源版 图生视频BF16高质量加速版_2085691291077271554.json, 视频生成/图生视频/(10Eros-Max)Minimax图生视频BF16高质量加速版V2_2085552878504206337.json, 视频生成/图生视频/(10Eros-Max)Minimax图生视频BF16高质量加速版V2_2086152176455475202.json, 视频生成/图生视频/(2倍速！量化加速版)Minimax图生视频V2_2084645396885893122.json, 视频生成/图生视频/(2倍速！量化加速版)Minimax图生视频V3_2086292345061994498.json, 视频生成/图生视频/(2倍速！量化加速版)Minimax图生视频V5_2084169932362838018.json, 视频生成/图生视频/(768P)Minimax图生视频BF16高质量加速版V2_2084908118156337154.json, 视频生成/图生视频/(768P)Minimax图生视频BF16高质量加速版V2_2085000443465396225.json, 视频生成/图生视频/(768P)Minimax图生视频BF16高质量加速版V2_2085606934639636481.json, 视频生成/图生视频/(8步加速-768P)Minimax参考生视频V1(第四版加速模型)_2086148083527798786.json, 视频生成/图生视频/(8步加速-768P)Minimax参考生视频V1(第四版加速模型)_2086156036376977410.json, 视频生成/图生视频/(8步加速-768P)Minimax参考生视频V1_2085215256233725953.json, 视频生成/图生视频/(8步加速-768P)Minimax参考生视频V1_2085648828052631554.json, 视频生成/图生视频/(8步加速-768P)Minimax图生视频V1_2085258096615710722.json, 视频生成/图生视频/(8步加速-768P)Minimax图生视频V1_2085265592797450241.json, 视频生成/图生视频/2倍速！加速版Minimax H3多参生视频sag+backend+block cache_2087475848759832577.json, 视频生成/图生视频/【2】图生视频（首帧图生视频）video_minimax_h3_i2v_2087199971459289090.json, 视频生成/图生视频/【3】图生视频（尾帧图生视频）video_minimax_h3_i2v_2087202435805827073.json, 视频生成/图生视频/【4】图生视频（首尾帧模式）video_minimax_h3_i2v_2087205422599073793.json, 视频生成/文生视频/MiniMax H3 lightx2v 4步加速图生视频工作流_2086324212742049794.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_4

> 由 `engine/knowledge_consolidation` 从 32 个 workflow 归纳得出（图片生成/文生图/MiniMax H3 加速版-文生视频_2084834194160701441.json、图片生成/文生图/Minimax H3-t2v 创意时装大片文生视频_2084847961032454145.json、图片生成/文生图/Minimax H3-t2v 官方提示词文生视频_2084933973188366337.json、图片生成/文生图/video_minimax_h3_t2v_2087382436262006785.json、图片生成/文生图/【1】文生视频（无参考图模式）video_minimax_h3_i2v_2087195498171158529.json…）

- **类型**：Unknown Workflow
- **样本数**：32
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 32 个 workflow 都包含：
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
- `LoadImage` —— 27/32 个有
- `PathchSageAttentionKJ` —— 22/32 个有
- `PrimitiveStringMultiline` —— 22/32 个有
- `MiniMaxH3ImageToVideo` —— 18/32 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 18/32 个有
- `CR Prompt Text` —— 14/32 个有
- `LoraLoaderModelOnly` —— 14/32 个有
- `MiniMaxH3BlockCacheT8` —— 14/32 个有
- `MiniMaxH3ReferenceToVideo` —— 14/32 个有
- `GetImageSize` —— 11/32 个有
- `ImageScaleToTotalPixels` —— 11/32 个有
- `EasyCache` —— 6/32 个有
- `LayerUtility: PurgeVRAM V2` —— 5/32 个有
- `Label (rgthree)` —— 4/32 个有
- `LoadAudio` —— 2/32 个有
- `ModelAttentionBackend` —— 2/32 个有
- `JjkText` —— 1/32 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/32 个有
- `SpectrumSDXL` —— 1/32 个有
- `TrimAudioDuration` —— 1/32 个有
- `VHS_VideoCombine` —— 1/32 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/32 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
