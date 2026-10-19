---
name: unknown_workflow_sampler_unet_vae_170
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.721667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/minimax H3 多图生成视频_2086293193284481026.json, 视频生成/图生视频/1953694457269026818.json, 视频生成/文生视频/MiniMax+H3+多图参考+官方提示词模板+提速40%无劣化+真人短剧剧情演绎_2095730598064250881.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_170

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/minimax H3 多图生成视频_2086293193284481026.json、视频生成/图生视频/1953694457269026818.json、视频生成/文生视频/MiniMax+H3+多图参考+官方提示词模板+提速40%无劣化+真人短剧剧情演绎_2095730598064250881.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 2/3 个有
- `EasyCache` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `JjkText` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `PrimitiveFloat` —— 2/3 个有
- `ResolutionSelector` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `VHS_VideoCombine` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy mathInt` —— 1/3 个有
- `easy seed` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
