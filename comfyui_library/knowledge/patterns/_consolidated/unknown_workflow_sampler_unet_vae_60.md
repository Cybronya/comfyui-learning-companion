---
name: unknown_workflow_sampler_unet_vae_60
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.8506
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/02-04-01-爱小墨-高级流-音画同出-文生视频v1.0_2085907402355990529.json, 视频生成/文生视频/37.MiniMax H3 文生视频_2085360265259995138.json, 视频生成/文生视频/39.MiniMax H3 多参考图生视频_2085360251456548866.json, 视频生成/文生视频/4步MiniMax-H3文生视频-LynnReal-Omni_2099804217237135361.json, 视频生成/文生视频/A-3 MiniMax-H3 文生视频 开源版_2084541355501641730.json, 视频生成/文生视频/A-3_MiniMax-H3_文生视频_开源版_2100205096012443649.json, 视频生成/文生视频/MiniMax H3 FL2VA 文生视频_2085360642407616513.json, 视频生成/文生视频/MiniMax H3 INT8 W4A8 加速_2086411704518406146.json, 视频生成/文生视频/MiniMax H3 Larry Turbo 加速_2086411713435492353.json, 视频生成/文生视频/MiniMax H3 LightX2V Turbo 加速_2086332815146311681.json, 视频生成/文生视频/MiniMax_H3 多参考图生视频（可本地运行）_2084295736807739394.json, 视频生成/文生视频/Minimax H3 - 多参视频生成_2084608321469898754.json, 视频生成/文生视频/Minimax H3 - 多参视频生成_2092164049516711938.json, 视频生成/文生视频/minimaxH3满血版海螺H3_2085024933234692098.json, 视频生成/文生视频/video_minimax_h3_r2v多参考生视频_2084510984789647362.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_60

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/文生视频/02-04-01-爱小墨-高级流-音画同出-文生视频v1.0_2085907402355990529.json、视频生成/文生视频/37.MiniMax H3 文生视频_2085360265259995138.json、视频生成/文生视频/39.MiniMax H3 多参考图生视频_2085360251456548866.json、视频生成/文生视频/4步MiniMax-H3文生视频-LynnReal-Omni_2099804217237135361.json、视频生成/文生视频/A-3 MiniMax-H3 文生视频 开源版_2084541355501641730.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 14/15 个有
- `PrimitiveStringMultiline` —— 12/15 个有
- `LoadImage` —— 9/15 个有
- `MiniMaxH3ImageToVideo` —— 8/15 个有
- `MiniMaxH3ReferenceToVideo` —— 7/15 个有
- `ImageResizeKJv2` —— 3/15 个有
- `LoraLoaderModelOnly` —— 2/15 个有
- `ComfyNumberConvert` —— 1/15 个有
- `ComfySwitchNode` —— 1/15 个有
- `EmptyImage` —— 1/15 个有
- `JjkText` —— 1/15 个有
- `PreviewImage` —— 1/15 个有
- `PrimitiveBoolean` —— 1/15 个有
- `easy int` —— 1/15 个有
- `easy seed` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
