---
name: image_to_image_sampler_vae_9
type: Image To Image
frequency: 13
level: strong
coverage: 0.892846
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen 多视图 三视图 图生图  相机镜头控制器_2039644703557165058.json, 图片生成/图生图/qwen 精准镜头控制器 多视图 三视图 图生图_2039526686571634689.json, 图片生成/图生图/分镜角度自由控制_2011281438196371458.json, 图片生成/图生图/利用3D相机优势生成多角度图像_2011263097549365250.json, 图片生成/图生图/利用3D相机优势生成多角度图像_2015060059142754306.json, 图片生成/图生图/千问2511 多角度自由切换_2048567603374858242.json, 图片生成/图生图/千问2511 多角度自由切换_2052587612896022530.json, 图片生成/图生图/单图编辑_Qwen2511_2010642367375740929.json, 图片生成/图生图/多镜头自由切换！Qwen-image edit 2511_2009557606741843969.json, 图片生成/图生图/自由角度和光线调整编辑图片_2036348651290759170.json, 图片生成/图生图/通义Qwen2511 多角度视角自由切换_2015670502123118594.json, 图片生成/图生图/😶‍🌫️千问2511 多角度自由切换🐳_2009500325392158722.json, 平台全量/Qwen2511服装拆解_2016129939401089025.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_9

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/qwen 多视图 三视图 图生图  相机镜头控制器_2039644703557165058.json、图片生成/图生图/qwen 精准镜头控制器 多视图 三视图 图生图_2039526686571634689.json、图片生成/图生图/分镜角度自由控制_2011281438196371458.json、图片生成/图生图/利用3D相机优势生成多角度图像_2011263097549365250.json、图片生成/图生图/利用3D相机优势生成多角度图像_2015060059142754306.json…）

- **类型**：Image To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 11/13 个有
- `LoraLoaderModelOnly` —— 11/13 个有
- `UNETLoader` —— 11/13 个有
- `QwenMultiangleCameraNode` —— 10/13 个有
- `PreviewImage` —— 9/13 个有
- `LayerUtility: ImageReel` —— 7/13 个有
- `LayerUtility: ImageReelComposit` —— 7/13 个有
- `CR Text Concatenate` —— 3/13 个有
- `QwenMultiangleLightningNode` —— 3/13 个有
- `ShowText|pysssss` —— 3/13 个有
- `CR Text` —— 2/13 个有
- `CheckpointLoaderSimple` —— 2/13 个有
- `ImpactMakeAnyList` —— 2/13 个有
- `Note Plus (mtb)` —— 2/13 个有
- `ImageScaleToTotalPixels` —— 1/13 个有
- `LayerUtility: ImageAutoCrop V2` —— 1/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/13 个有
- `Qwen3_VQA_Plus` —— 1/13 个有
- `easy promptConcat` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 13 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 92% |
| 调度器 | simple | - | 13 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，13 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 92%
- 调度器 最常用 simple，13 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
