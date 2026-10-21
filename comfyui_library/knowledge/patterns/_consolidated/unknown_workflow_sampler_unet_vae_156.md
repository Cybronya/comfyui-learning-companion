---
name: unknown_workflow_sampler_unet_vae_156
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8752
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CR Prompt Text, ComfyMathExpression, CreateVideo, EasyCache, KSamplerSelect, LoadImage, PathchSageAttentionKJ, RandomNoise, SamplerCustomAdvanced, SaveVideo, ShowAnything|Mie, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/加速版-MiniMax H3 图生视频 首尾帧视频_2091065912949567490.json, 视频生成/文生视频/加速版-MiniMax H3｜图文一键生视频_2084935567606894593.json, 视频生成/文生视频/加速版-MiniMax H3｜多参图像音频极速生视频_2085190320597331969.json, 视频生成/文生视频/加速版-MiniMax H3｜多参图像音频极速生视频_2089636411841540097.json, 视频生成/文生视频/加速版-MiniMax H3｜多参图像音频极速生视频_2091126218266603521.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_156

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/加速版-MiniMax H3 图生视频 首尾帧视频_2091065912949567490.json、视频生成/文生视频/加速版-MiniMax H3｜图文一键生视频_2084935567606894593.json、视频生成/文生视频/加速版-MiniMax H3｜多参图像音频极速生视频_2085190320597331969.json、视频生成/文生视频/加速版-MiniMax H3｜多参图像音频极速生视频_2089636411841540097.json、视频生成/文生视频/加速版-MiniMax H3｜多参图像音频极速生视频_2091126218266603521.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `CreateVideo`
- `EasyCache`
- `KSamplerSelect`
- `LoadImage`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `ShowAnything|Mie`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImpactSwitch` —— 4/5 个有
- `PrimitiveFloat` —— 4/5 个有
- `ResolutionSelector` —— 4/5 个有
- `DF_Int_to_Float` —— 3/5 个有
- `GetVideoComponents` —— 3/5 个有
- `LoadAudio` —— 3/5 个有
- `LoadVideo` —— 3/5 个有
- `MiniMaxH3ReferenceToVideo` —— 3/5 个有
- `MiniMaxH3ImageToVideo` —— 2/5 个有
- `CM_IntToFloat` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `Int` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
