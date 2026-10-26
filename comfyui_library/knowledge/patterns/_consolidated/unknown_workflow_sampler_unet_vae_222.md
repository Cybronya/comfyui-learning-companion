---
name: unknown_workflow_sampler_unet_vae_222
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7812
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/字体动画_MiniMaxH3_2091089391518306306.json, 视频生成/文生视频/文生视频-minimax_h3_t2v_2084183370304675841.json, 视频生成/文生视频/文生视频-minimax_h3_t2v_2084541372161413121.json, 视频生成/文生视频/文生视频-minimax_h3_t2v_2085005368459096065.json, 视频生成/文生视频/海螺文生视频_2085524853020512258.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_222

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/字体动画_MiniMaxH3_2091089391518306306.json、视频生成/文生视频/文生视频-minimax_h3_t2v_2084183370304675841.json、视频生成/文生视频/文生视频-minimax_h3_t2v_2084541372161413121.json、视频生成/文生视频/文生视频-minimax_h3_t2v_2085005368459096065.json、视频生成/文生视频/海螺文生视频_2085524853020512258.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 4/5 个有
- `Text` —— 3/5 个有
- `easy showAnything` —— 3/5 个有
- `孤海注释` —— 2/5 个有
- `Canvas Properties` —— 1/5 个有
- `Font Properties` —— 1/5 个有
- `GetImageSize` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `Text to Image Generator` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
