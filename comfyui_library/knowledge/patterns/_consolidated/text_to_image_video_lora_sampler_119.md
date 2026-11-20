---
name: text_to_image_video_lora_sampler_119
type: Text To Image
frequency: 6
level: strong
coverage: 0.7485
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, EmptyLatentImage, ImageResizeKJv2, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SAM3_TrackPreview, SAM3_TrackToMask, SAM3_VideoTrack, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/minimax h3角色替换工作流｜数字人换角色动作迁移_2113591073137315841.json, 视频生成/图生视频/H3 Character Swap 1.5 SAM3.1精准替换 VDN8加速工具_2113689229984358402.json, 视频生成/图生视频/H3 Character Swap 1.5升级｜SAM 3.1精准换角色VDN8加速视频替换_2113441647387303937.json, 视频生成/图生视频/H3 Character Swap蒙版版 双人视频角色替换处理工具_2113392745107779586.json, 视频生成/图生视频/H3 Mask替换人物 视频人物替换进阶工具_2099906937986048002.json, 视频生成/图生视频/多人视频人物遮罩替换 简单提示词H3蒙版处理工具_2113753730213568514.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_119

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（数字人/数字人/minimax h3角色替换工作流｜数字人换角色动作迁移_2113591073137315841.json、视频生成/图生视频/H3 Character Swap 1.5 SAM3.1精准替换 VDN8加速工具_2113689229984358402.json、视频生成/图生视频/H3 Character Swap 1.5升级｜SAM 3.1精准换角色VDN8加速视频替换_2113441647387303937.json、视频生成/图生视频/H3 Character Swap蒙版版 双人视频角色替换处理工具_2113392745107779586.json、视频生成/图生视频/H3 Mask替换人物 视频人物替换进阶工具_2099906937986048002.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SAM3_TrackPreview`
- `SAM3_TrackToMask`
- `SAM3_VideoTrack`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `DrawBBoxes` —— 5/6 个有
- `LTXVConcatAVLatent` —— 5/6 个有
- `MVEx_MaskCleanup` —— 5/6 个有
- `MVEx_MaskToLatentSpace` —— 5/6 个有
- `MVEx_SubjectCrop` —— 5/6 个有
- `MVEx_SubjectUncrop` —— 5/6 个有
- `PreviewAnimation` —— 5/6 个有
- `ResizeImageMaskNode` —— 5/6 个有
- `SetLatentNoiseMask` —— 5/6 个有
- `SolidMask` —— 5/6 个有
- `VAEEncode` —— 5/6 个有
- `VAEEncodeAudio` —— 5/6 个有
- `BasicScheduler` —— 4/6 个有
- `GetNode` —— 4/6 个有
- `KSamplerSelect` —— 4/6 个有
- `ModelAttentionBackend` —— 4/6 个有
- `SaveImage` —— 4/6 个有
- `SetNode` —— 4/6 个有
- `MiniMaxH3VDNExecutionPlanT8Advanced` —— 2/6 个有
- `MiniMaxH3VDNModelComposerT8Advanced` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `ImageAndMaskPreview` —— 1/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/6 个有
- `取色器_孤海` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
