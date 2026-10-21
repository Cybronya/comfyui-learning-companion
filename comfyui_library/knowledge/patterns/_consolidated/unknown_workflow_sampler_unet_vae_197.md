---
name: unknown_workflow_sampler_unet_vae_197
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.967
common_nodes: [BasicGuider, CLIPLoader, CreateVideo, GetImageSizeAndCount, GrowMask, ImageBlur, ImageCompositeMasked, ImageScaleToTotalPixels, ImageToMask, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoadVideoDepthAnythingModel, MaskToImage, MiniMaxH3ReferenceToVideo, MiniMaxH3VDNExecutionPlanT8Advanced, MiniMaxH3VDNModelComposerT8Advanced, PointsEditor, RandomNoise, SamplerCustomAdvanced, SaveVideo, SeCModelLoader, SeCVideoSegmentation, SetLatentNoiseMask, SolidMask, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VideoDepthAnythingProcess]
problems: []
missing: []
members: [视频生成/文生视频/Mini Max H3｜角色替换_参考编辑（Face Refine 精修版）_2106049462291492865.json, 视频生成/文生视频/Mini Max H3｜角色替换_参考编辑（无声版）_2105985623722119170.json, 视频生成/文生视频/Mini Max H3｜角色替换_参考编辑（标准版）_2105941709917081601.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_197

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/Mini Max H3｜角色替换_参考编辑（Face Refine 精修版）_2106049462291492865.json、视频生成/文生视频/Mini Max H3｜角色替换_参考编辑（无声版）_2105985623722119170.json、视频生成/文生视频/Mini Max H3｜角色替换_参考编辑（标准版）_2105941709917081601.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CreateVideo`
- `GetImageSizeAndCount`
- `GrowMask`
- `ImageBlur`
- `ImageCompositeMasked`
- `ImageScaleToTotalPixels`
- `ImageToMask`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoadVideoDepthAnythingModel`
- `MaskToImage`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3VDNExecutionPlanT8Advanced`
- `MiniMaxH3VDNModelComposerT8Advanced`
- `PointsEditor`
- `RandomNoise`
- `SamplerCustomAdvanced`
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

**可变部分**（部分 workflow 才有）：
- `LoadVideo` —— 2/3 个有
- `VHS_VideoInfoLoaded` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `GetVideoComponents` —— 1/3 个有
- `MiniMaxH3AVDecodeT8` —— 1/3 个有
- `MiniMaxH3AudioConditioningT8` —— 1/3 个有
- `MiniMaxH3AudioMixT8` —— 1/3 个有
- `MiniMaxH3FaceRefineConditioningT8Advanced` —— 1/3 个有
- `MiniMaxH3FaceRefinePlanT8Advanced` —— 1/3 个有
- `MiniMaxH3FaceRefineSamplerT8Advanced` —— 1/3 个有
- `MiniMaxH3FaceRefineStitchAuditT8Advanced` —— 1/3 个有
- `MiniMaxH3OutputTrimT8` —— 1/3 个有
- `MiniMaxH3SafeAVSaveT8Advanced` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
