---
name: image_to_image_lora_sampler_unet_13
type: Image To Image
frequency: 23
level: strong
coverage: 0.84
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen_Edit_2511多角度_2055560720015732738.json, 图片生成/图生图/Qwen_Edit_2511多角度同出_2056331114276540418.json, 图片生成/图生图/Qwen_Edit_2511改图_2055536614876688385.json, 图片生成/图生图/Qwen_Multiangle_2511图片角度自由控制_2010971058458861569.json, 图片生成/图生图/Qwen_Multiangle_2511图片角度自由控制_2038483773788000257.json, 图片生成/图生图/Qwen_Multiangle_2511自由控制图片角度_2038555716276981761.json, 图片生成/图生图/Qwen_image_Edit_2511_单图编辑_2004473601208315905.json, 图片生成/图生图/Qwen_image_Edit_2511_多图编辑_2004495314616811522.json, 图片生成/图生图/apple sharp高斯泼溅成图_2011269417006534657.json, 图片生成/图生图/apple sharp高斯泼溅成图_2025921551727595521.json, 图片生成/图生图/mutiangle旋转摄像头生成多角度人物图片_2021198244126138369.json, 图片生成/图生图/qwen  分镜 精准镜头视角控制器  模特套图 商品套图_2046923407031275521.json, 图片生成/图生图/qwen  精准镜头控制器 图生图 多视角  Qwen Multiangle Camera_2041768515669069826.json, 图片生成/图生图/qwen  精准镜头控制器 多视角套图  镜头选择_2041695143425744897.json, 图片生成/图生图/qwen  精准镜头控制器 模特套图  镜头选择_2039528560959950849.json, 图片生成/图生图/场景生成多视角_2013145425766780929.json, 图片生成/图生图/场景生成多视角_2101477990000582658.json, 图片生成/图生图/多角度切换相机控制 复刻场景 Qwen 人物产品多角度_2069217388083634178.json, 图片生成/图生图/多角度镜头控制（人像摄影 漫剧镜头 场景）_2050550918256578562.json, 图片生成/图生图/工作流基础系列11-QwenImageEdit2511单图编辑_2004000394919485442.json, 图片生成/图生图/工作流基础系列12-QwenImageEdit2511双图编辑_2004026267299135489.json, 图片生成/图生图/组件系列12-QWEN-EDIT-2511单图编辑_2059098441153859586.json, 图片生成/图生图/组件系列13-QWEN-EDIT-2511多图编辑_2059099538136322050.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_13

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（图片生成/图生图/Qwen_Edit_2511多角度_2055560720015732738.json、图片生成/图生图/Qwen_Edit_2511多角度同出_2056331114276540418.json、图片生成/图生图/Qwen_Edit_2511改图_2055536614876688385.json、图片生成/图生图/Qwen_Multiangle_2511图片角度自由控制_2010971058458861569.json、图片生成/图生图/Qwen_Multiangle_2511图片角度自由控制_2038483773788000257.json…）

- **类型**：Image To Image
- **样本数**：23
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 23 个 workflow 都包含：
- `CLIPLoader`
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
- `FluxKontextMultiReferenceLatentMethod` —— 22/23 个有
- `CFGNorm` —— 20/23 个有
- `PreviewImage` —— 14/23 个有
- `QwenMultiangleCameraNode` —— 14/23 个有
- `easy showAnything` —— 13/23 个有
- `Image Comparer (rgthree)` —— 11/23 个有
- `ImageScaleToTotalPixels` —— 11/23 个有
- `easy promptList` —— 10/23 个有
- `GetNode` —— 8/23 个有
- `SetNode` —— 8/23 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/23 个有
- `CR Text` —— 4/23 个有
- `FluxKontextImageScale` —— 4/23 个有
- `Seed (rgthree)` —— 4/23 个有
- `ImpactMakeAnyList` —— 3/23 个有
- `KepStringList` —— 2/23 个有
- `ReferenceLatent` —— 2/23 个有
- `Text Concatenate` —— 1/23 个有
- `easy string` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 23 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 23 | 100% |
| 采样算法 | euler | - | 23 | 100% |
| 调度器 | simple | - | 23 | 100% |
| 重绘幅度 | 1 | 0.9 - 1 | 23 | 98% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/23 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，23 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，23 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，23 个样本，一致性 100%
- 调度器 最常用 simple，23 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.9 - 1，23 个样本，取值集中（一致性 98%）
- 高发问题（23/23 个样本）：Steps较低可能导致细节不足
