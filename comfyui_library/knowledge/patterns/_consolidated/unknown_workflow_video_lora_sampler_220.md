---
name: unknown_workflow_video_lora_sampler_220
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.776222
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SCAIL2ScheduledLongVideoWithSAM, SCAIL2SegmentPlanBuilder, ShowText|pysssss, UNETLoader, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/Scail2 TTP多参+内循环+面部强化_2071860174570221570.json, 视频生成/图生视频/Scail2 TTP多参+内循环+面部强化_2072501093262774273.json, 视频生成/图生视频/Scail2 TTP多参+内循环+面部强化人物角色替换_2071400172424351746.json, 视频生成/图生视频/Scail2 多图参考+面部修复 全身跳舞面部不崩 内部自循环 长视频直出_2072215231262191617.json, 视频生成/图生视频/Scail2+动作迁移+多参面+部强化+内循环长视频_2072162271043870721.json, 视频生成/图生视频/Scail2+角色替换+多参面+内循环长视频_2072986209936297986.json, 视频生成/图生视频/Scail2+角色替换+多参面+内循环长视频_2073313220749967360.json, 视频生成/图生视频/Scail2-多图参考+面部修复-全身视频面部不崩-循环长视频直出_2073299453481668610.json, 视频生成/图生视频/Scail2-脸部自适应-姿势迁移-重打光_2071800002871123969.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_220

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/Scail2 TTP多参+内循环+面部强化_2071860174570221570.json、视频生成/图生视频/Scail2 TTP多参+内循环+面部强化_2072501093262774273.json、视频生成/图生视频/Scail2 TTP多参+内循环+面部强化人物角色替换_2071400172424351746.json、视频生成/图生视频/Scail2 多图参考+面部修复 全身跳舞面部不崩 内部自循环 长视频直出_2072215231262191617.json、视频生成/图生视频/Scail2+动作迁移+多参面+部强化+内循环长视频_2072162271043870721.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SCAIL2ScheduledLongVideoWithSAM`
- `SCAIL2SegmentPlanBuilder`
- `ShowText|pysssss`
- `UNETLoader`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `SCAIL2ChunkKeyframeExtractor` —— 8/9 个有
- `SCAIL2KeyframeMatrixViewer` —— 8/9 个有
- `GetImageSize` —— 7/9 个有
- `ImageConcatMulti` —— 7/9 个有
- `MaskToImage` —— 7/9 个有
- `PreviewImage` —— 7/9 个有
- `SCAIL2AlignReferenceFaceToCrop` —— 7/9 个有
- `SCAIL2FaceCompositeBack` —— 7/9 个有
- `SCAIL2HeadTrackCrop` —— 7/9 个有
- `CR Text` —— 5/9 个有
- `Int` —— 5/9 个有
- `SimpleMath+` —— 5/9 个有
- `Fast Groups Bypasser (rgthree)` —— 3/9 个有
- `GetNode` —— 3/9 个有
- `RH_Nano_Banana2_Image2Image` —— 3/9 个有
- `RH_RhartImageG2ImageToImage` —— 3/9 个有
- `SaveImage` —— 3/9 个有
- `SetNode` —— 3/9 个有
- `TTResolutionSelector` —— 3/9 个有
- `CreateVideo` —— 2/9 个有
- `FlashVSR_SM_KSampler` —— 2/9 个有
- `FlashVSR_SM_Model` —— 2/9 个有
- `SaveVideo` —— 2/9 个有
- `easy int` —— 2/9 个有
- `Note Plus (mtb)` —— 1/9 个有
- `PrimitiveStringMultiline` —— 1/9 个有
- `WanAnimatePlus LoraSelectMulti` —— 1/9 个有
- `孤海注释` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1.34378e+09 | - | 2 | 82% |
| Prompt 约束强度(CFG) | randomize | - | 2 | 100% |
| 采样算法 | 2 | - | 2 | 100% |
| 调度器 | 3.5 | - | 2 | 100% |
| 重绘幅度 | 11 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 1.34378e+09，样本不足，未给区间，2 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 最常用 randomize，2 个样本，一致性 100%
- 采样算法 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 1.59208e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
