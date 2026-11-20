---
name: image_to_image_sampler_unet_vae_15
type: Image To Image
frequency: 12
level: weak
coverage: 0.85725
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen万能图片编辑图生图全能图片V1平替_2005434060799442945.json, 图片生成/图生图/三图编辑_2067961763567591425.json, 图片生成/图生图/三张图就编辑 ICEdit_LoRA_2015404467323146242.json, 图片生成/图生图/主体抠图与黑白蒙版生成_2052234697593368577.json, 图片生成/图生图/主体抠图与黑白蒙版生成_2061622051689033729.json, 图片生成/图生图/产品单图编辑 ｜细节修复、修改文本… ｜+RefineAny 局部优化 LoRA｜Qwen-lmage-Edit-2511_2052579173188816897.json, 图片生成/图生图/修复产品细节（文字）_2087469251488731137.json, 图片生成/图生图/修复人脸、产品、文字、细节。_2089628300737073154.json, 图片生成/图生图/千问图像编辑_产品材质更换工作流_2106390652362772481.json, 图片生成/图生图/小红书换装_2075185550822301697.json, 图片生成/图生图/标签替换_2112453904410701826.json, 平台全量/产品单图编辑 + 1 张参考图（精细编辑）｜+RefineAny 局部优化 LoRA｜Qwen-lmage-Edit-2511_2052582687495475201.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_15

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/qwen万能图片编辑图生图全能图片V1平替_2005434060799442945.json、图片生成/图生图/三图编辑_2067961763567591425.json、图片生成/图生图/三张图就编辑 ICEdit_LoRA_2015404467323146242.json、图片生成/图生图/主体抠图与黑白蒙版生成_2052234697593368577.json、图片生成/图生图/主体抠图与黑白蒙版生成_2061622051689033729.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 11/12 个有
- `LoraLoaderModelOnly` —— 11/12 个有
- `ModelSamplingAuraFlow` —— 11/12 个有
- `ConditioningZeroOut` —— 7/12 个有
- `FluxKontextImageScale` —— 7/12 个有
- `FluxKontextMultiReferenceLatentMethod` —— 7/12 个有
- `Image Comparer (rgthree)` —— 7/12 个有
- `PreviewImage` —— 6/12 个有
- `RefineNodePasteBack` —— 5/12 个有
- `RefineNodePreprocessMask` —— 5/12 个有
- `RefineNodeReferenceImageProcess` —— 5/12 个有
- `Text Multiline` —— 2/12 个有
- `DuckHideNode` —— 1/12 个有
- `ImageBatchMultiple+` —— 1/12 个有
- `ImageSharpen` —— 1/12 个有
- `YANC.MultilineString` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 20 | 12 | 31% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 12 | 34% |
| 采样算法 | euler | - | 12 | 92% |
| 调度器 | simple | - | 12 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 20，12 个样本，取值分散，一致性仅 31%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，12 个样本，取值分散，一致性仅 34%
- 采样算法 最常用 euler，12 个样本，一致性 92%
- 调度器 最常用 simple，12 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（11/12 个样本）：Steps较低可能导致细节不足
