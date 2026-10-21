---
name: unknown_workflow_sampler_vae_27
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.866556
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: [Seed (rgthree)]
members: [视频生成/图生视频/video_minimax_h3_i2v_first_last_frame_2092171283260862466.json, 视频生成/图生视频/▶▷MiniMaxH3-图生视频_2093020292909195265.json, 视频生成/图生视频/图生视频教学工作流学习班_2091876747317960706.json, 视频生成/图生视频/开源版Minimax H3 图生视频_2089902055870787586.json, 视频生成/图生视频/新手短剧_MiniMax H3 多参考视频生成工作流 v1_0_2106283115156172802.json, 视频生成/图生视频/首尾帧-MiniMaxH3-图生视频-模板_2090038373938458625.json, 视频生成/文生视频/MiniMax_H3_文生视频加速_2099770316435316738.json, 视频生成/文生视频/MiniMax_H3_文生视频加速_2100031727967232001.json, 视频生成/文生视频/文生视频-MiniMaxH3-BV1-模板_2090725747148288002.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_27

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/video_minimax_h3_i2v_first_last_frame_2092171283260862466.json、视频生成/图生视频/▶▷MiniMaxH3-图生视频_2093020292909195265.json、视频生成/图生视频/图生视频教学工作流学习班_2091876747317960706.json、视频生成/图生视频/开源版Minimax H3 图生视频_2089902055870787586.json、视频生成/图生视频/新手短剧_MiniMax H3 多参考视频生成工作流 v1_0_2106283115156172802.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 8/9 个有
- `MiniMaxH3ImageToVideo` —— 8/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/9 个有
- `UNETLoader` —— 8/9 个有
- `ResolutionSelector` —— 6/9 个有
- `Seed (rgthree)` —— 6/9 个有
- `Label (rgthree)` —— 5/9 个有
- `LoadImage` —— 5/9 个有
- `INTConstant` —— 2/9 个有
- `ImageResizeKJv2` —— 2/9 个有
- `Text Multiline` —— 2/9 个有
- `DiffusionModelLoaderKJ` —— 1/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有
- `MiniMaxH3ReferenceToVideo` —— 1/9 个有
- `ModelPreviewOverrideKJ` —— 1/9 个有
- `PrimitiveInt` —— 1/9 个有
- `YK_LoadImageFromURL` —— 1/9 个有
- `easy positive` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：Seed (rgthree)
