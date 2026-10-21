---
name: unknown_workflow_sampler_unet_vae_63
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.88
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 多图音频参考工作流_2086330601241661442.json, 视频生成/图生视频/MiniMax H3 导演台多图参考生视频_2085966790018031618.json, 视频生成/图生视频/Minimax图生视频（量化加速版)_2084601874262609921.json, 视频生成/图生视频/Minimax多参生视频(量化加速版)_2084619382487085057.json, 视频生成/图生视频/Minimax多参生视频满血768P二倍速版_2084983011841503233.json, 视频生成/图生视频/aidir-Minimax_h3_多参考图生视频_2087056895474491393.json, 视频生成/图生视频/i2va_minimax_h3_vaeint8_api_2103863320280391681.json, 视频生成/图生视频/minimaxH3 ref2va多参工作流_2084130906889089025.json, 视频生成/文生视频/MinimaxH3多人物短剧工作流竖屏(提示词优化+量化加速版)_2084915488760619009.json, 视频生成/文生视频/Minimax多人物多参短剧工作流(量化加速版)_2084650866472214530.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_63

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 多图音频参考工作流_2086330601241661442.json、视频生成/图生视频/MiniMax H3 导演台多图参考生视频_2085966790018031618.json、视频生成/图生视频/Minimax图生视频（量化加速版)_2084601874262609921.json、视频生成/图生视频/Minimax多参生视频(量化加速版)_2084619382487085057.json、视频生成/图生视频/Minimax多参生视频满血768P二倍速版_2084983011841503233.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 9/10 个有
- `PathchSageAttentionKJ` —— 9/10 个有
- `ComfyMathExpression` —— 8/10 个有
- `LoadImage` —— 8/10 个有
- `PrimitiveFloat` —— 8/10 个有
- `ResolutionSelector` —— 8/10 个有
- `EasyCache` —— 7/10 个有
- `VHS_VideoCombine` —— 7/10 个有
- `GetVideoComponents` —— 6/10 个有
- `MiniMaxH3ReferenceToVideo` —— 6/10 个有
- `PrimitiveStringMultiline` —— 6/10 个有
- `MiniMaxH3ImageToVideo` —— 3/10 个有
- `SaveVideo` —— 3/10 个有
- `LoadAudio` —— 2/10 个有
- `SFH3MultimodalDirector` —— 2/10 个有
- `AudioCrop` —— 1/10 个有
- `CR Prompt Text` —— 1/10 个有
- `EmptyMiniMaxH3LatentAV` —— 1/10 个有
- `LoraLoader` —— 1/10 个有
- `MiniMaxH3BlockCacheT8` —— 1/10 个有
- `MiniMaxH3SigmaShift` —— 1/10 个有
- `PainterVRAM` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 0 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
