---
name: unknown_workflow_video_upscale_latent_upscale_27
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.459
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, ImageResizeKJv2, KSamplerSelect, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Best_faceid V1 for ltx2.3_2082528336852635649.json, 视频生成/图生视频/LTX 2.3 打造的人脸一致性与角色保持 LoRA_2083500149866848258.json, 视频生成/图生视频/LTX 2.3 打造的人脸一致性与角色保持 LoRA_2083534814229127169.json, 视频生成/图生视频/LTX2.3 Edit Anything编辑万物编辑视频任何元素视频替换视频修改视频编辑动作迁移_2099063135738097666.json, 视频生成/图生视频/LTX2.3 超高人脸一致性与角色保持 LoRA_2083496691566727169.json, 视频生成/图生视频/LTX2.3-best_faceid_charsheet-人脸高一致性_2083089483041427458.json, 视频生成/图生视频/LTX2.3-best_faceid_ganloss-人脸高一致性_2083196415471345666.json, 视频生成/图生视频/video_ltx2_3_best_charactor_sheet_ganloss_2080574328030191617.json, 视频生成/图生视频/video_ltx2_3_best_faceid_charsheet_ganloss_upscale_2080581115986931714.json, 视频生成/图生视频/video_ltx2_3_best_faceid_ganloss_2080550056238862337.json, 视频生成/图生视频/video_ltx2_3_best_faceid_ganloss_2083097564500549633.json, 视频生成/图生视频/video_ltx2_3_best_faceid_ganloss_upscale_2080566370382729217.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_27

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/Best_faceid V1 for ltx2.3_2082528336852635649.json、视频生成/图生视频/LTX 2.3 打造的人脸一致性与角色保持 LoRA_2083500149866848258.json、视频生成/图生视频/LTX 2.3 打造的人脸一致性与角色保持 LoRA_2083534814229127169.json、视频生成/图生视频/LTX2.3 Edit Anything编辑万物编辑视频任何元素视频替换视频修改视频编辑动作迁移_2099063135738097666.json、视频生成/图生视频/LTX2.3 超高人脸一致性与角色保持 LoRA_2083496691566727169.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：46%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTXIdentityOverlapConditioning` —— 11/12 个有
- `LoadImage` —— 11/12 个有
- `PreviewImage` —— 11/12 个有
- `RMBG` —— 11/12 个有
- `PrimitiveInt` —— 10/12 个有
- `PrimitiveBoolean` —— 9/12 个有
- `BasicScheduler` —— 8/12 个有
- `LTXVAudioVAEDecode` —— 7/12 个有
- `LTXVCropGuides` —— 7/12 个有
- `VAEDecodeTiled` —— 7/12 个有
- `LTXTiledSampler` —— 6/12 个有
- `LTXVLatentUpsamplerTiled` —— 6/12 个有
- `SimpleMath+` —— 3/12 个有
- `Int` —— 2/12 个有
- `孤海注释` —— 2/12 个有
- `GetImageRangeFromBatch` —— 1/12 个有
- `ImageConcanate` —— 1/12 个有
- `LTXVAddGuideMulti` —— 1/12 个有
- `LTXVImgToVideoInplace` —— 1/12 个有
- `LTXVLatentUpsampler` —— 1/12 个有
- `Label (rgthree)` —— 1/12 个有
- `VAEEncode` —— 1/12 个有
- `VHS_LoadVideo` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 12 | 100% |
| 高度 | 25 | 25 - 25 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，12 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，12 个样本，取值集中（一致性 100%）
