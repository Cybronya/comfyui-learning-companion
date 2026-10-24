---
name: unknown_workflow_sampler_unet_vae_79
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.813727
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, PrimitiveStringMultiline, QwenEditConfigPreparer, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/02-01-03-QwenEdit-基础修图-志佬_2004889499622666241.json, 图片生成/图生图/02-02-02-QwenEdit-双图编辑-志佬_2006656824291889154.json, 图片生成/图生图/2511Qwen Edit  双图编辑_2003855425076379649.json, 图片生成/图生图/Klein 9B 局部重绘  贴回原位——适用于2K 4K大图_2063421100146647042.json, 图片生成/图生图/QE2511 修图换人换物增强一致性lora_2010591123043000322.json, 图片生成/图生图/Qwen2511换装 一致性lora alpha_2010697292533211137.json, 图片生成/图生图/QwenEdit2511提升一致性Lora，适合单角色下使用_2010687188006080514.json, 图片生成/图生图/QwenEdit_2509_Anything2Real+A2R_1991699100773216258.json, 图片生成/图生图/【老金驿站】Qwen2509图像转真实_1989304425208573954.json, 图片生成/图生图/局部重绘无偏移_2109566086395031553.json, 图片生成/文生图/Qwen Edit 2509：风格转换【Anything2Real LoRA模型 】二次元动漫转真人_1991153622583193602.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_79

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/02-01-03-QwenEdit-基础修图-志佬_2004889499622666241.json、图片生成/图生图/02-02-02-QwenEdit-双图编辑-志佬_2006656824291889154.json、图片生成/图生图/2511Qwen Edit  双图编辑_2003855425076379649.json、图片生成/图生图/Klein 9B 局部重绘  贴回原位——适用于2K 4K大图_2063421100146647042.json、图片生成/图生图/QE2511 修图换人换物增强一致性lora_2010591123043000322.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `PrimitiveStringMultiline`
- `QwenEditConfigPreparer`
- `SaveImage`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 10/11 个有
- `QwenEditOutputExtractor` —— 10/11 个有
- `CropWithPadInfo` —— 9/11 个有
- `LoraLoaderModelOnly` —— 9/11 个有
- `QwenEditAdaptiveLongestEdge` —— 8/11 个有
- `ImageScaleBy` —— 7/11 个有
- `Image Comparer (rgthree)` —— 6/11 个有
- `LayerUtility: ImageReel` —— 6/11 个有
- `LayerUtility: ImageReelComposit` —— 6/11 个有
- `PreviewAny` —— 6/11 个有
- `GetImageSize` —— 5/11 个有
- `GetImageSize+` —— 3/11 个有
- `ImageResizeKJv2` —— 3/11 个有
- `GH_CropRestore` —— 2/11 个有
- `GH_MaskCropV2` —— 2/11 个有
- `LayerMask: MaskGrow` —— 2/11 个有
- `ImageConcanate` —— 1/11 个有
- `PrimitiveFloat` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 11 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | beta57 | - | 11 | 64% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 beta57，11 个样本，一致性 64%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（18/11 个样本）：Steps较低可能导致细节不足
