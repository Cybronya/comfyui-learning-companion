---
name: unknown_workflow_sampler_vae_33
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.86325
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/video_minimax_h3_i2v_first_last_frame_2092171283260862466.json, 视频生成/图生视频/图生视频教学工作流学习班_2091876747317960706.json, 视频生成/图生视频/开源版Minimax H3 图生视频_2089902055870787586.json, 视频生成/图生视频/新手短剧｜MiniMax H3 多参考视频生成工作流 v1.0_2106283115156172802.json, 视频生成/图生视频/首尾帧-MiniMaxH3-图生视频-模板_2090038373938458625.json, 视频生成/文生视频/MiniMax_H3_文生视频加速_2099770316435316738.json, 视频生成/文生视频/MiniMax_H3_文生视频加速_2100031727967232001.json, 视频生成/文生视频/文生视频-MiniMaxH3-BV1-模板_2090725747148288002.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_33

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/video_minimax_h3_i2v_first_last_frame_2092171283260862466.json、视频生成/图生视频/图生视频教学工作流学习班_2091876747317960706.json、视频生成/图生视频/开源版Minimax H3 图生视频_2089902055870787586.json、视频生成/图生视频/新手短剧｜MiniMax H3 多参考视频生成工作流 v1.0_2106283115156172802.json、视频生成/图生视频/首尾帧-MiniMaxH3-图生视频-模板_2090038373938458625.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 8 个 workflow 都包含：
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
- `LoraLoaderModelOnly` —— 7/8 个有
- `MiniMaxH3ImageToVideo` —— 7/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/8 个有
- `UNETLoader` —— 7/8 个有
- `ResolutionSelector` —— 5/8 个有
- `Seed (rgthree)` —— 5/8 个有
- `Label (rgthree)` —— 4/8 个有
- `LoadImage` —— 4/8 个有
- `INTConstant` —— 2/8 个有
- `Text Multiline` —— 2/8 个有
- `DiffusionModelLoaderKJ` —— 1/8 个有
- `ImageResizeKJv2` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `MiniMaxH3ReferenceToVideo` —— 1/8 个有
- `ModelPreviewOverrideKJ` —— 1/8 个有
- `PrimitiveInt` —— 1/8 个有
- `YK_LoadImageFromURL` —— 1/8 个有
- `easy positive` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
