---
name: unknown_workflow_video_sampler_unet_6
type: Unknown Workflow
frequency: 28
level: moderate
coverage: 0.855929
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/文生图/INT8 Turbo 4 步加速版_2103075017385922562.json, 图片生成/文生图/Minimax-H3-文生视频(双时钟+8步极速)_2085735853296541698.json, 图片生成/文生图/MinimaxH3 全功能加速工作流_2084250421568299010.json, 数字人/数字人/MiniMax H3-视频复刻-数字人-视频换人、视频换产品、文案不换（保持原视频语音）_2106734702446075906.json, 数字人/数字人/MiniMax H3-视频复刻-数字人-视频换人、视频换产品、视频换文案（替换原视频语音）_2106724867256176641.json, 数字人/数字人/音频驱动-Dasiwa V1-MiniMax H3数字人-加速版_2095011177205166081.json, 数字人/数字人/（company自用）双人数字人15s及15s以内版_2093239293912371202.json, 视频生成/图生视频/(10eros-Max Ref2v加速)Minimax参考生视频V1_2090750346653167618.json, 视频生成/图生视频/(SLA脸部动作稳定版)Minimax-H3开源 参考生视频_2091459862701101057.json, 视频生成/图生视频/(SLA脸部动作稳定版)Minimax-H3开源 参考生视频_2091504849526542337.json, 视频生成/图生视频/(SLA脸部动作稳定版)Minimax-H3开源 参考生视频_2097672335238193153.json, 视频生成/图生视频/(SLA脸部动作稳定版)Minimax参考生视频V1_2091100470646501378.json, 视频生成/图生视频/(b25-49+ema600)MiniMax H3数字人加速版V1_2094796122115108866.json, 视频生成/图生视频/(双时钟-8步高质量极速)Minimax参考生视频V2（老版第一版加速）_2090372869883777026.json, 视频生成/图生视频/(贞贞lora-双时钟-8步)Minimax参考生视频V1_2086638366224900098.json, 视频生成/图生视频/10Eros Beta+Lightx2v正式版Minimax双时钟参考生视频V1_2087368448614682625.json, 视频生成/图生视频/10Eros Beta+Lightx2v正式版Minimax双时钟图生视频V1_2087494589186920449.json, 视频生成/图生视频/10Eros Beta+Lightx2v正式版Minimax双时钟图生视频V1_2088288426880749570.json, 视频生成/图生视频/10Eros Beta版+Lightx2v正式版-Minimax双时钟-图音视频多参生视频-加速版_2087563282352791554.json, 视频生成/图生视频/1图 MINIMAX 单图视频生成_2111253442411974657.json, 视频生成/图生视频/720P双时钟高质量加速 0.8_2088677432479014914.json, 视频生成/图生视频/8步加速_2088996111943032833.json, 视频生成/图生视频/8步高质量极速Minimax H3开源版_2105680108311896065.json, 视频生成/图生视频/8步高质量极速Minimax H3开源版_2108184548386365441.json, 视频生成/图生视频/Dasiwa-MiniMax H3-动态最强-单采-参考生视频_2095105300293574657.json, 视频生成/图生视频/MINIMAX-H3 多图参考短剧一键生成_2085997938811166721.json, 视频生成/图生视频/MiniMax H3 视频复刻：视频编辑、视频翻拍、二创与指定角色替换-长视频直出_2105605446362030081.json, 视频生成/视频生视频/MiniMax H3 视频复刻 角色替换-二创翻拍_2106096378328993794.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_6

> 由 `engine/knowledge_consolidation` 从 28 个 workflow 归纳得出（图片生成/文生图/INT8 Turbo 4 步加速版_2103075017385922562.json、图片生成/文生图/Minimax-H3-文生视频(双时钟+8步极速)_2085735853296541698.json、图片生成/文生图/MinimaxH3 全功能加速工作流_2084250421568299010.json、数字人/数字人/MiniMax H3-视频复刻-数字人-视频换人、视频换产品、文案不换（保持原视频语音）_2106734702446075906.json、数字人/数字人/MiniMax H3-视频复刻-数字人-视频换人、视频换产品、视频换文案（替换原视频语音）_2106724867256176641.json…）

- **类型**：Unknown Workflow
- **样本数**：28
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 28 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 27/28 个有
- `LoraLoaderBypassModelOnly` —— 27/28 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 27/28 个有
- `ResolutionSelector` —— 25/28 个有
- `MiniMaxH3DualClockSamplerT8` —— 24/28 个有
- `CR Prompt Text` —— 22/28 个有
- `ModelAttentionBackend` —— 19/28 个有
- `SolAttnMiniMax` —— 12/28 个有
- `孤海注释` —— 7/28 个有
- `LoadAudio` —— 6/28 个有
- `PrimitiveStringMultiline` —— 5/28 个有
- `VHS_LoadVideo` —— 5/28 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 4/28 个有
- `LoraLoaderModelOnly` —— 3/28 个有
- `Int` —— 2/28 个有
- `LoadVideo` —— 2/28 个有
- `AudioCrop` —— 1/28 个有
- `DA3Inference` —— 1/28 个有
- `DA3Render` —— 1/28 个有
- `LoadDA3Model` —— 1/28 个有
- `ShowAnything|Mie` —— 1/28 个有
- `TimbreAudioLoader` —— 1/28 个有
- `VHS_LoadVideoFFmpeg` —— 1/28 个有
- `VHS_VideoInfo` —— 1/28 个有
- `WujiAudioLoader` —— 1/28 个有
- `easy int` —— 1/28 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
