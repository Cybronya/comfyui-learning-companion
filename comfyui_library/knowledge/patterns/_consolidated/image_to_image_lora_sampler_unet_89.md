---
name: image_to_image_lora_sampler_unet_89
type: Image To Image
frequency: 7
level: strong
coverage: 0.876429
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen edit 2511 多角度生成_2032063580392136705.json, 图片生成/图生图/Qwen image edit2511-JOYS_2004441857839034369.json, 图片生成/图生图/RefineAnything产品重绘_2052274837279784961.json, 图片生成/图生图/产品单图编辑 ｜细节修复、修改文本… ｜+RefineAny 局部优化 LoRA｜Qwen-lmage-Edit-2511_2052579173188816897.json, 图片生成/图生图/修复产品细节（文字）_2087469251488731137.json, 图片生成/图生图/修复人脸、产品、文字、细节。_2089628300737073154.json, 图片生成/图生图/标签替换_2112453904410701826.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_89

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen edit 2511 多角度生成_2032063580392136705.json、图片生成/图生图/Qwen image edit2511-JOYS_2004441857839034369.json、图片生成/图生图/RefineAnything产品重绘_2052274837279784961.json、图片生成/图生图/产品单图编辑 ｜细节修复、修改文本… ｜+RefineAny 局部优化 LoRA｜Qwen-lmage-Edit-2511_2052579173188816897.json、图片生成/图生图/修复产品细节（文字）_2087469251488731137.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
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
- `FluxKontextMultiReferenceLatentMethod` —— 6/7 个有
- `Image Comparer (rgthree)` —— 5/7 个有
- `RefineNodePasteBack` —— 5/7 个有
- `RefineNodePreprocessMask` —— 5/7 个有
- `RefineNodeReferenceImageProcess` —— 5/7 个有
- `PreviewImage` —— 3/7 个有
- `JDC_ResizeFactor` —— 1/7 个有
- `PlaySound|pysssss` —— 1/7 个有
- `QwenMultiangleCameraNode` —— 1/7 个有
- `RMBG` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有
- `图像缩放V2_孤海` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 7 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
