---
name: image_to_image_lora_sampler_unet_58
type: Image To Image
frequency: 10
level: strong
coverage: 0.9187
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/RefineAnything产品重绘_2052274837279784961.json, 图片生成/图生图/image_qwen_image_edit_2511-单图参考+打光_2010914134002503681.json, 图片生成/图生图/image_qwen_image_edit_2511-单图参考+重打光+选视角_2011254283882205186.json, 图片生成/图生图/产品单图编辑 ｜细节修复、修改文本… ｜+RefineAny 局部优化 LoRA｜Qwen-lmage-Edit-2511_2052579173188816897.json, 图片生成/图生图/修复产品细节（文字）_2087469251488731137.json, 图片生成/图生图/修复人脸、产品、文字、细节。_2089628300737073154.json, 图片生成/图生图/利用3D相机优势生成多角度图像_2011263097549365250.json, 图片生成/图生图/利用3D相机优势生成多角度图像_2015060059142754306.json, 图片生成/图生图/标签替换_2112453904410701826.json, 图片生成/图生图/自由角度和光线调整编辑图片_2036348651290759170.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_58

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/RefineAnything产品重绘_2052274837279784961.json、图片生成/图生图/image_qwen_image_edit_2511-单图参考+打光_2010914134002503681.json、图片生成/图生图/image_qwen_image_edit_2511-单图参考+重打光+选视角_2011254283882205186.json、图片生成/图生图/产品单图编辑 ｜细节修复、修改文本… ｜+RefineAny 局部优化 LoRA｜Qwen-lmage-Edit-2511_2052579173188816897.json、图片生成/图生图/修复产品细节（文字）_2087469251488731137.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGNorm`
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
- `ConditioningZeroOut` —— 5/10 个有
- `QwenMultiangleLightningNode` —— 5/10 个有
- `RefineNodePasteBack` —— 5/10 个有
- `RefineNodePreprocessMask` —— 5/10 个有
- `RefineNodeReferenceImageProcess` —— 5/10 个有
- `CR Text Concatenate` —— 4/10 个有
- `Image Comparer (rgthree)` —— 4/10 个有
- `QwenMultiangleCameraNode` —— 4/10 个有
- `FluxKontextImageScale` —— 3/10 个有
- `PreviewImage` —— 3/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
