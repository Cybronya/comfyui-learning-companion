---
name: image_to_image_sampler_unet_vae_7
type: Image To Image
frequency: 17
level: weak
coverage: 0.794941
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/ComfyUI_qwen_image姿势控制自动穿戴_1971197174509977602.json, 图片生成/图生图/FLUX-2-Klein-图生图洗图工作流_2015711272569937921.json, 图片生成/图生图/FLUX-2-Klein-图生图洗图工作流_2055150677059489793.json, 图片生成/图生图/FLUX-Klein 3图融合工作流_2014225545059373057.json, 图片生成/图生图/FLUX.2-4b-单图编辑-标准版-（必收藏）_2052395682006347778.json, 图片生成/图生图/Moss image🔺4K高清洗图（注释内有模型和节点下载链接）_2116156612195999746.json, 图片生成/图生图/Z-Image增加真实质感去ai感，真实系_2046044910419185666.json, 图片生成/图生图/ZImage增加真实质感去油腻写实系_2053332475044212738.json, 图片生成/图生图/ZImage增加真实质感去油腻写实系_2057137840416448513.json, 图片生成/图生图/一键转Q版工作流V1_2057651447432572929.json, 图片生成/图生图/一键转Q版工作流V1_2057700323195711490.json, 图片生成/图生图/一键转Q版工作流V1_2059158135604076546.json, 图片生成/图生图/一键转Q版工作流V1_2059531242244231169.json, 图片生成/图生图/一键转Q版工作流V1_2066400918530252802.json, 图片生成/图生图/动漫图一键转Q版图工作流_2057792823910551554.json, 图片生成/图生图/图生图一键转Q版工作流V1_2064508373718102018.json, 图片生成/图生图/真人动漫二次元 一键转Q版_2057794622239371266.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_7

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/ComfyUI_qwen_image姿势控制自动穿戴_1971197174509977602.json、图片生成/图生图/FLUX-2-Klein-图生图洗图工作流_2015711272569937921.json、图片生成/图生图/FLUX-2-Klein-图生图洗图工作流_2055150677059489793.json、图片生成/图生图/FLUX-Klein 3图融合工作流_2014225545059373057.json、图片生成/图生图/FLUX.2-4b-单图编辑-标准版-（必收藏）_2052395682006347778.json…）

- **类型**：Image To Image
- **样本数**：17
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 15/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 14/17 个有
- `ConditioningZeroOut` —— 13/17 个有
- `SeedVR2LoadDiTModel` —— 13/17 个有
- `SeedVR2LoadVAEModel` —— 13/17 个有
- `SeedVR2VideoUpscaler` —— 13/17 个有
- `Image Comparer (rgthree)` —— 12/17 个有
- `ImageScaleToTotalPixels` —— 12/17 个有
- `LoraLoaderModelOnly` —— 12/17 个有
- `easy cleanGpuUsed` —— 11/17 个有
- `CLIPTextEncode` —— 9/17 个有
- `TextEncodeQwenImageEditPlus` —— 9/17 个有
- `Fast Groups Bypasser (rgthree)` —— 8/17 个有
- `GetNode` —— 8/17 个有
- `SetNode` —— 8/17 个有
- `easy imageConcat` —— 8/17 个有
- `Int` —— 3/17 个有
- `ReferenceLatent` —— 2/17 个有
- `孤海注释` —— 2/17 个有
- `BiRefNetRMBG` —— 1/17 个有
- `JjkText` —— 1/17 个有
- `OpenposePreprocessor` —— 1/17 个有
- `PowerfulMaskCrop` —— 1/17 个有
- `SkipLayerGuidanceDiTSimple` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 25 | 17 | 47% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 17 | 58% |
| 采样算法 | euler | - | 17 | 94% |
| 调度器 | sgm_uniform | - | 17 | 47% |
| 重绘幅度 | 1 | 0.45 - 1 | 17 | 71% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 25，17 个样本，取值分散，一致性仅 47%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，17 个样本
- 采样算法 最常用 euler，17 个样本，一致性 94%
- 调度器 最常用 sgm_uniform，17 个样本，一致性 47%
- 重绘幅度 中位数 1，观测区间 0.45 - 1，17 个样本
- 高发问题（15/17 个样本）：Steps较低可能导致细节不足
