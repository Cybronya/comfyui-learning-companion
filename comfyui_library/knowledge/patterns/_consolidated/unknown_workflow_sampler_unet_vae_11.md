---
name: unknown_workflow_sampler_unet_vae_11
type: Unknown Workflow
frequency: 22
level: moderate
coverage: 0.834455
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/MiniMax H3 加速版-文生视频_2084834194160701441.json, 图片生成/文生图/MiniMax H3 尾帧图生视频_2084544642758037506.json, 图片生成/文生图/Minimax H3-t2v 创意时装大片文生视频_2084847961032454145.json, 图片生成/文生图/Minimax H3-t2v 官方提示词文生视频_2084933973188366337.json, 图片生成/文生图/video_minimax_h3_t2v_2087382436262006785.json, 图片生成/文生图/【1】文生视频（无参考图模式）video_minimax_h3_i2v_2087195498171158529.json, 数字人/数字人/H3数字人_2092831814367924225.json, 数字人/数字人/MiniMax H3开源 数字人音频驱动&图片跳舞 加速版_2089709883632476162.json, 视频生成/图生视频/H3+音频驱动&图片跳舞！加速版_2099306860540162050.json, 视频生成/图生视频/MiniMax H3开源 数字人音频驱动&图片跳舞 加速版_2089304839850381314.json, 视频生成/图生视频/MiniMax H3开源 数字人音频驱动&图片跳舞 加速版_2089316746447638530.json, 视频生成/图生视频/MiniMax H3开源 音频驱动&图片跳舞 加速版_2087489674502828034.json, 视频生成/图生视频/MiniMax H3开源 音频驱动&图片跳舞 加速版_2087515631137681409.json, 视频生成/图生视频/MiniMax H3开源 音频驱动&图片跳舞 加速版_2094741369498722306.json, 视频生成/图生视频/MiniMax H3开源 音频驱动&图片跳舞 加速版_2094766113983913985.json, 视频生成/图生视频/MiniMax H3开源 音频驱动&图片跳舞 加速版_2099456748556996609.json, 视频生成/图生视频/MiniMax H3开源 音频驱动&图片跳舞 加速版_2099471044871548930.json, 视频生成/图生视频/MiniMax H3开源 音频驱动&图片跳舞 加速版_2110317481368838145.json, 视频生成/图生视频/MiniMax H3开源 音频驱动&图片跳舞 加速版_2110323066374025217.json, 视频生成/图生视频/MiniMaxH3 音频驱动&图片跳舞！加速版！B站艾橘溪_2087001018646220802.json, 视频生成/图生视频/MiniMaxH3数字人_音频驱动&图片跳舞！效果炸裂！_2087444061333581825.json, 视频生成/图生视频/音频驱动图片跳舞加速版｜MiniMax H3_2090000101321302017.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_11

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/文生图/MiniMax H3 加速版-文生视频_2084834194160701441.json、图片生成/文生图/MiniMax H3 尾帧图生视频_2084544642758037506.json、图片生成/文生图/Minimax H3-t2v 创意时装大片文生视频_2084847961032454145.json、图片生成/文生图/Minimax H3-t2v 官方提示词文生视频_2084933973188366337.json、图片生成/文生图/video_minimax_h3_t2v_2087382436262006785.json…）

- **类型**：Unknown Workflow
- **样本数**：22
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 22 个 workflow 都包含：
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
- `PrimitiveStringMultiline` —— 19/22 个有
- `LayerUtility: PurgeVRAM V2` —— 17/22 个有
- `LoadImage` —— 17/22 个有
- `LoraLoaderModelOnly` —— 17/22 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 17/22 个有
- `MiniMaxH3ReferenceToVideo` —— 17/22 个有
- `PathchSageAttentionKJ` —— 17/22 个有
- `LoadAudio` —— 16/22 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 16/22 个有
- `GetNode` —— 15/22 个有
- `PainterVRAM` —— 15/22 个有
- `SetNode` —— 15/22 个有
- `VRAM_Debug` —— 15/22 个有
- `MiniMaxH3ImageToVideo` —— 5/22 个有
- `EasyCache` —— 2/22 个有
- `DF_Int_to_Float` —— 1/22 个有
- `GetImageSize` —— 1/22 个有
- `ImageResizeKJv2` —— 1/22 个有
- `ImageScaleToTotalPixels` —— 1/22 个有
- `Int` —— 1/22 个有
- `JjkText` —— 1/22 个有
- `Label (rgthree)` —— 1/22 个有
- `SolAttnPatch` —— 1/22 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
