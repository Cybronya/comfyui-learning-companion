---
name: image_to_image_lora_sampler_unet_79
type: Image To Image
frequency: 9
level: strong
coverage: 0.924222
common_nodes: [CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/RefineAnything产品重绘_2052274837279784961.json, 图片生成/图生图/edit_2511图像多角度编辑_2009951290171854849.json, 图片生成/图生图/image_qwen_image_edit_2511-单图参考+运镜_2010906708750639106.json, 图片生成/图生图/image_qwen_image_edit_2511_multiangle_camera 尺寸2K限_2019265588102701057.json, 图片生成/图生图/image_qwen_image_edit_2511_multiangle_camera_2010682508362391554.json, 图片生成/图生图/image_qwen_image_edit_2511_multiangle_camera转角度_2018618986367291394.json, 图片生成/图生图/qwen2511改图工作流_2038270042151849986.json, 图片生成/图生图/qwen_edit_2511单图编辑_2077221456840314881.json, 图片生成/图生图/qwen_image_edit_2511多角度图片_2094678732018638850.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_79

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/RefineAnything产品重绘_2052274837279784961.json、图片生成/图生图/edit_2511图像多角度编辑_2009951290171854849.json、图片生成/图生图/image_qwen_image_edit_2511-单图参考+运镜_2010906708750639106.json、图片生成/图生图/image_qwen_image_edit_2511_multiangle_camera 尺寸2K限_2019265588102701057.json、图片生成/图生图/image_qwen_image_edit_2511_multiangle_camera_2010682508362391554.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 8/9 个有
- `FluxKontextImageScale` —— 6/9 个有
- `QwenMultiangleCameraNode` —— 6/9 个有
- `Image Comparer (rgthree)` —— 4/9 个有
- `PreviewImage` —— 4/9 个有
- `图像缩放范围孤海` —— 2/9 个有
- `ComfySwitchNode` —— 1/9 个有
- `ConditioningZeroOut` —— 1/9 个有
- `ImageScaleToMaxDimension` —— 1/9 个有
- `LayerUtility: ImageReel` —— 1/9 个有
- `LayerUtility: ImageReelComposit` —— 1/9 个有
- `PrimitiveString` —— 1/9 个有
- `RefineNodePasteBack` —— 1/9 个有
- `RefineNodePreprocessMask` —— 1/9 个有
- `RefineNodeReferenceImageProcess` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 9 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
