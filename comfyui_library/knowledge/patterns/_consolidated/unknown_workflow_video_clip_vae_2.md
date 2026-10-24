---
name: unknown_workflow_video_clip_vae_2
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.949833
common_nodes: [CLIPTextEncode, GetImageSize+, GrowMaskWithBlur, INTConstant, ImageCompositeMasked, ImageResizeKJv2, InspyrenetRembg, InvertMask, LoadImage, MaskToImage, ModelSamplingSD3, PreviewImage, SolidMask, TrimVideoLatent, VAEDecode, VHS_DuplicateMasks, VHS_LoadVideo, VHS_VideoCombine, WanVaceToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MEGA Merge-WAN2.2-AllInOne-参考编辑主体替换_1968838814837952513.json, 视频生成/图生视频/MEGA_V3-WAN2.2-AllInOne-参考编辑主体替换_1969998691601948673.json, 视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-参考编辑主体替换_1968252590028926977.json, 视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-参考编辑主体替换_1982052007592763394.json, 视频生成/文生视频/Wan 2.2-Fun-VACE-参考编辑主体替换_1967629207792738305.json, 视频生成/文生视频/mega-aio-v11+qwenvl参考编辑_1985674481710575617.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_vae_2

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/MEGA Merge-WAN2.2-AllInOne-参考编辑主体替换_1968838814837952513.json、视频生成/图生视频/MEGA_V3-WAN2.2-AllInOne-参考编辑主体替换_1969998691601948673.json、视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-参考编辑主体替换_1968252590028926977.json、视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-参考编辑主体替换_1982052007592763394.json、视频生成/文生视频/Wan 2.2-Fun-VACE-参考编辑主体替换_1967629207792738305.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `GetImageSize+`
- `GrowMaskWithBlur`
- `INTConstant`
- `ImageCompositeMasked`
- `ImageResizeKJv2`
- `InspyrenetRembg`
- `InvertMask`
- `LoadImage`
- `MaskToImage`
- `ModelSamplingSD3`
- `PreviewImage`
- `SolidMask`
- `TrimVideoLatent`
- `VAEDecode`
- `VHS_DuplicateMasks`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVaceToVideo`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 5/6 个有
- `Miaoshouai_Tagger` —— 4/6 个有
- `CLIPLoader` —— 3/6 个有
- `CheckpointLoaderSimple` —— 3/6 个有
- `UNETLoader` —— 3/6 个有
- `AV_VAELoader` —— 2/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `KSamplerAdvanced` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有
- `VAELoader` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 6 | 5 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 6 | 6 | 0% |
| 采样算法 | euler | - | 6 | 50% |
| 调度器 | beta | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 6，5 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 6，6 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，6 个样本，一致性 50%
- 调度器 最常用 beta，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足
