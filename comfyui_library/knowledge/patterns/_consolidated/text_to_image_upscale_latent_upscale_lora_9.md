---
name: text_to_image_upscale_latent_upscale_lora_9
type: Text To Image
frequency: 4
level: strong
coverage: 0.82275
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3DurationPlannerT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3OutputTrimT8, MiniMaxH3SafeAVSaveT8Advanced, MiniMaxH3TwoPassAudioAuditT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, MiniMaxH3VDNExecutionPlanT8Advanced, MiniMaxH3VDNModelComposerT8Advanced, MiniMaxH3VDNRefinePlanT8Advanced, PreviewAny, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3 ControlNet Union 2.0视频控制与局部重绘VDN 12步高清版_2108970658804887554.json, 视频生成/图生视频/MiniMax H3 ControlNet Union局部重绘专用工作流 精准控制改图_2109171442880442369.json, 视频生成/图生视频/MiniMax H3通用视频生成VDN 12步高清版 高质量动态生成_2108968961265192961.json, 视频生成/文生视频/H3 VDN 12NFE高质量二采商品展示Hero Shot工作流，文生视频图生视频方案_2108274637418352642.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_9

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 ControlNet Union 2.0视频控制与局部重绘VDN 12步高清版_2108970658804887554.json、视频生成/图生视频/MiniMax H3 ControlNet Union局部重绘专用工作流 精准控制改图_2109171442880442369.json、视频生成/图生视频/MiniMax H3通用视频生成VDN 12步高清版 高质量动态生成_2108968961265192961.json、视频生成/文生视频/H3 VDN 12NFE高质量二采商品展示Hero Shot工作流，文生视频图生视频方案_2108274637418352642.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3DurationPlannerT8`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3OutputTrimT8`
- `MiniMaxH3SafeAVSaveT8Advanced`
- `MiniMaxH3TwoPassAudioAuditT8Advanced`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `MiniMaxH3VDNExecutionPlanT8Advanced`
- `MiniMaxH3VDNModelComposerT8Advanced`
- `MiniMaxH3VDNRefinePlanT8Advanced`
- `PreviewAny`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3AudioConditioningT8` —— 3/4 个有
- `AIO_Preprocessor` —— 2/4 个有
- `ComfyMathExpression` —— 2/4 个有
- `GetVideoComponents` —— 2/4 个有
- `GrowMask` —— 2/4 个有
- `ImageScale` —— 2/4 个有
- `LoadVideo` —— 2/4 个有
- `MaskPreview` —— 2/4 个有
- `MiniMaxH3FunControlNetApply` —— 2/4 个有
- `ModelPatchLoader` —— 2/4 个有
- `PointsEditor` —— 2/4 个有
- `SeCModelLoader` —— 2/4 个有
- `SeCVideoSegmentation` —— 2/4 个有
- `VHS_LoadVideo` —— 2/4 个有
- `VHS_VideoInfoLoaded` —— 2/4 个有
- `Video Slice` —— 2/4 个有
- `LoadAudio` —— 1/4 个有
- `MiniMaxH3ReferenceToVideo` —— 1/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1.4 | - | 2 | 71% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 1.4，样本不足，未给区间，2 个样本
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
