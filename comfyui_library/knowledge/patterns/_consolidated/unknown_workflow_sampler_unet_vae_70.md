---
name: unknown_workflow_sampler_unet_vae_70
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.8495
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/4-9宫图+Minimaxh3导演台（批量短剧专用）_2099703771608735745.json, 视频生成/图生视频/MiniMax H3 多图音频参考工作流_2086330601241661442.json, 视频生成/图生视频/MiniMax H3 导演台多图参考生视频_2085966790018031618.json, 视频生成/图生视频/Minimax图生视频（量化加速版)_2084601874262609921.json, 视频生成/图生视频/Minimax多参生视频(量化加速版)_2084619382487085057.json, 视频生成/图生视频/Minimax多参生视频满血768P二倍速版_2084983011841503233.json, 视频生成/图生视频/i2va_minimax_h3_vaeint8_api_2103863320280391681.json, 视频生成/图生视频/minimax_h3 参考图生视频+sage加速_2084127001375494145.json, 视频生成/图生视频/minimax_h3_全能参考（参考视频输入）_2085193849571463169.json, 视频生成/图生视频/超级融合模型-高质量(10Eros-Max)Minimax BF16参考生视频-加速版-TEST3版_2086762633667108866.json, 视频生成/文生视频/MiniMax-H3-参考生视频_2085243192571686914.json, 视频生成/文生视频/Minimax H3 加速工作流_2085691765964754946.json, 视频生成/文生视频/Minimax H3 多参生视频_2087727061006901250.json, 视频生成/文生视频/Minimax H3文生视频、图生视频、参考生视频、动作迁移、人物替换自由切换，双重加速版_2086132690054639617.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_70

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/4-9宫图+Minimaxh3导演台（批量短剧专用）_2099703771608735745.json、视频生成/图生视频/MiniMax H3 多图音频参考工作流_2086330601241661442.json、视频生成/图生视频/MiniMax H3 导演台多图参考生视频_2085966790018031618.json、视频生成/图生视频/Minimax图生视频（量化加速版)_2084601874262609921.json、视频生成/图生视频/Minimax多参生视频(量化加速版)_2084619382487085057.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 14 个 workflow 都包含：
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
- `CreateVideo` —— 12/14 个有
- `LoadImage` —— 12/14 个有
- `ComfyMathExpression` —— 11/14 个有
- `PathchSageAttentionKJ` —— 11/14 个有
- `PrimitiveFloat` —— 11/14 个有
- `ResolutionSelector` —— 11/14 个有
- `MiniMaxH3ReferenceToVideo` —— 9/14 个有
- `PrimitiveStringMultiline` —— 9/14 个有
- `SaveVideo` —— 8/14 个有
- `EasyCache` —— 7/14 个有
- `VHS_VideoCombine` —— 6/14 个有
- `VHS_LoadVideo` —— 5/14 个有
- `GetVideoComponents` —— 4/14 个有
- `LoadAudio` —— 4/14 个有
- `MiniMaxH3BlockCacheT8` —— 4/14 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/14 个有
- `MiniMaxH3ImageToVideo` —— 3/14 个有
- `SFH3MultimodalDirector` —— 3/14 个有
- `CR Prompt Text` —— 2/14 个有
- `LoraLoaderBypassModelOnly` —— 2/14 个有
- `孤海注释` —— 2/14 个有
- `CM_FloatToInt` —— 1/14 个有
- `Fast Groups Bypasser (rgthree)` —— 1/14 个有
- `GetNode` —— 1/14 个有
- `Int` —— 1/14 个有
- `LoraLoader` —— 1/14 个有
- `ModelAttentionBackend` —— 1/14 个有
- `SetNode` —— 1/14 个有
- `Switch any [Crystools]` —— 1/14 个有
- `VHS_VideoInfo` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 0 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
