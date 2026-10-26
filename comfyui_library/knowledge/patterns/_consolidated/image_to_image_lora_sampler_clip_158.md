---
name: image_to_image_lora_sampler_clip_158
type: Image To Image
frequency: 2
level: weak
coverage: 1
common_nodes: [CLIPTextEncode, CR Text, Convert Masks to Images, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, FluxKontextImageScale, GetImageSize+, Image To Mask, ImageAndMaskPreview, ImageScale, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Mask Fill Holes, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, RH_LLMAPI_NODE, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/单图遮罩Kontext+Nunchaku 局部重绘+万物消除替换+扩写_1939172804220633089.json, 图片生成/图生图/最强图像去水印（可加遮罩）Kontext+Nunchaku 局部重绘+万物消除替换+双重高清修复_1942459817787076610.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_158

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/单图遮罩Kontext+Nunchaku 局部重绘+万物消除替换+扩写_1939172804220633089.json、图片生成/图生图/最强图像去水印（可加遮罩）Kontext+Nunchaku 局部重绘+万物消除替换+双重高清修复_1942459817787076610.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Text`
- `Convert Masks to Images`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `GetImageSize+`
- `Image To Mask`
- `ImageAndMaskPreview`
- `ImageScale`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Mask Fill Holes`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `RH_LLMAPI_NODE`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 1/2 个有
- `InvSRSampler` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `LoadInvSRModels` —— 1/2 个有
- `PMRF` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
