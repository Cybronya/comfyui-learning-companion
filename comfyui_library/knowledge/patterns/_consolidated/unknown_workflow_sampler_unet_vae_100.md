---
name: unknown_workflow_sampler_unet_vae_100
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8343
common_nodes: [BasicGuider, CLIPLoader, LoadImage, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax_H3_强化锁定镜头_音色绑定_2109202394990075906.json, 视频生成/图生视频/Minimax_H3_首帧锁定_固定全景_音色配对修正版_2108927308747857922.json, 视频生成/图生视频/Minimax_h3_超级加速多图参考生视频_2084162807137918977.json, 视频生成/图生视频/Minimax参考生视频-(8步加速-768P)_2085357536189960194.json, 视频生成/图生视频/aidir-Minimax_h3_多参考图生视频_2087056895474491393.json, 视频生成/图生视频/h3  4步多图自用_2088590941430046722.json, 视频生成/图生视频/lightx2v 300%加速 MinimaxH3-多参生视频（图片 视频 声音）_2084269573662142465.json, 视频生成/图生视频/minimax h3多元素参考 生视频工作流_2084531165620432897.json, 视频生成/图生视频/minimaxH3多参考视频工作流_2084285648122499073.json, 视频生成/文生视频/58.MiniMax H3 全能参考加速极简_2087136892977504257.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_100

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/Minimax_H3_强化锁定镜头_音色绑定_2109202394990075906.json、视频生成/图生视频/Minimax_H3_首帧锁定_固定全景_音色配对修正版_2108927308747857922.json、视频生成/图生视频/Minimax_h3_超级加速多图参考生视频_2084162807137918977.json、视频生成/图生视频/Minimax参考生视频-(8步加速-768P)_2085357536189960194.json、视频生成/图生视频/aidir-Minimax_h3_多参考图生视频_2087056895474491393.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 9/10 个有
- `KSamplerSelect` —— 9/10 个有
- `PrimitiveFloat` —— 9/10 个有
- `PrimitiveStringMultiline` —— 8/10 个有
- `ComfyMathExpression` —— 7/10 个有
- `LoadAudio` —— 7/10 个有
- `LoraLoaderModelOnly` —— 7/10 个有
- `CreateVideo` —— 6/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/10 个有
- `SaveVideo` —— 6/10 个有
- `PathchSageAttentionKJ` —— 5/10 个有
- `VHS_LoadVideo` —— 4/10 个有
- `VHS_VideoCombine` —— 4/10 个有
- `Int` —— 3/10 个有
- `EasyCache` —— 2/10 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 2/10 个有
- `PainterVRAM` —— 2/10 个有
- `SpectrumSDXL` —— 2/10 个有
- `CR Prompt Text` —— 1/10 个有
- `Label (rgthree)` —— 1/10 个有
- `MiniMaxH3AddGuide` —— 1/10 个有
- `PlaySound|pysssss` —— 1/10 个有
- `SimpleMath+` —— 1/10 个有
- `TextInput` —— 1/10 个有
- `easy cleanGpuUsed` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
