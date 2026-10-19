---
name: text_to_image_lora_sampler_clip_160
type: Text To Image
frequency: 6
level: strong
coverage: 0.953333
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, GetImageSizeAndCount, GrowMask, ImageBlur, ImageCompositeMasked, ImageScaleToTotalPixels, ImageToMask, JjkText, KSampler, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoadVideoDepthAnythingModel, LoraLoaderModelOnly, MaskToImage, MiniMaxH3ReferenceToVideo, MiniMaxH3VDNExecutionPlanT8Advanced, MiniMaxH3VDNModelComposerT8Advanced, PointsEditor, RandomNoise, SamplerCustomAdvanced, SaveImage, SaveVideo, SeCModelLoader, SeCVideoSegmentation, SetLatentNoiseMask, SolidMask, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VideoDepthAnythingProcess, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3角色替换参考编辑Face Refine精修版，视频生视频图生视频方案_2106432993144426497.json, 视频生成/图生视频/MiniMax H3角色替换参考编辑无声版，视频生视频图生视频处理工具_2106496570077306881.json, 视频生成/图生视频/MiniMax H3角色替换参考编辑标准版，视频生视频图生视频处理工具_2106434664054480898.json, 视频生成/视频生视频/MiniMax H3角色替换参考编辑Face Refine精修版，视频生视频图生视频方案_2106432993144426497.json, 视频生成/视频生视频/MiniMax H3角色替换参考编辑无声版_视频生视频图生视频处理工具_2106496570077306881.json, 视频生成/视频生视频/MiniMax H3角色替换参考编辑标准版_视频生视频图生视频处理工具_2106434664054480898.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_160

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3角色替换参考编辑Face Refine精修版，视频生视频图生视频方案_2106432993144426497.json、视频生成/图生视频/MiniMax H3角色替换参考编辑无声版，视频生视频图生视频处理工具_2106496570077306881.json、视频生成/图生视频/MiniMax H3角色替换参考编辑标准版，视频生视频图生视频处理工具_2106434664054480898.json、视频生成/视频生视频/MiniMax H3角色替换参考编辑Face Refine精修版，视频生视频图生视频方案_2106432993144426497.json、视频生成/视频生视频/MiniMax H3角色替换参考编辑无声版_视频生视频图生视频处理工具_2106496570077306881.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLatentImage`
- `GetImageSizeAndCount`
- `GrowMask`
- `ImageBlur`
- `ImageCompositeMasked`
- `ImageScaleToTotalPixels`
- `ImageToMask`
- `JjkText`
- `KSampler`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoadVideoDepthAnythingModel`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3VDNExecutionPlanT8Advanced`
- `MiniMaxH3VDNModelComposerT8Advanced`
- `PointsEditor`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SaveVideo`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `SetLatentNoiseMask`
- `SolidMask`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VideoDepthAnythingProcess`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadVideo` —— 4/6 个有
- `VHS_VideoInfoLoaded` —— 4/6 个有
- `Fast Groups Bypasser (rgthree)` —— 2/6 个有
- `GetVideoComponents` —— 2/6 个有
- `MiniMaxH3AVDecodeT8` —— 2/6 个有
- `MiniMaxH3AudioConditioningT8` —— 2/6 个有
- `MiniMaxH3AudioMixT8` —— 2/6 个有
- `MiniMaxH3FaceRefineConditioningT8Advanced` —— 2/6 个有
- `MiniMaxH3FaceRefinePlanT8Advanced` —— 2/6 个有
- `MiniMaxH3FaceRefineSamplerT8Advanced` —— 2/6 个有
- `MiniMaxH3FaceRefineStitchAuditT8Advanced` —— 2/6 个有
- `MiniMaxH3OutputTrimT8` —— 2/6 个有
- `MiniMaxH3SafeAVSaveT8Advanced` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
