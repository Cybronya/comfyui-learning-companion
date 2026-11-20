---
name: image_to_image_sampler_unet_vae_19
type: Image To Image
frequency: 11
level: weak
coverage: 0.842818
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image-Edit 图生图编辑 _ 12 节点保持人物换装_加配饰_2086660579183386625.json, 图片生成/图生图/Qwen-Image-Edit 真人照片转3D卡通 _ 人物换装_2109096443209404418.json, 图片生成/图生图/Qwen-Image-Edit-2509  万能图像编辑 完胜 全能图片V1 2  Pro_1997925023178457089.json, 图片生成/图生图/Qwen-Image-Edit-2509 图像编辑 图像替换 多图融合 在线免费应用 免费下载部署_1982283626857545730.json, 图片生成/图生图/Qwen-Image-Edit-2509 基础工作流_1971613466534539266.json, 图片生成/图生图/Qwen-Image-Edit-2511_2004929074399248386.json, "图片生成/图生图/Qwen-Image-Edit图像编辑,超强精准控制_1958442372495523841.json", 图片生成/图生图/Qwen-Image-Edit工作流_1953817263986147329.json, 图片生成/图生图/Qwen-Image海报生成工作流_1982450271907389441.json, 图片生成/图生图/说话改图工作流大集合_1971841856017526785.json, 图片生成/文生图/Qwen--海报设计_1965378348828475394.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_19

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-Edit 图生图编辑 _ 12 节点保持人物换装_加配饰_2086660579183386625.json、图片生成/图生图/Qwen-Image-Edit 真人照片转3D卡通 _ 人物换装_2109096443209404418.json、图片生成/图生图/Qwen-Image-Edit-2509  万能图像编辑 完胜 全能图片V1 2  Pro_1997925023178457089.json、图片生成/图生图/Qwen-Image-Edit-2509 图像编辑 图像替换 多图融合 在线免费应用 免费下载部署_1982283626857545730.json、图片生成/图生图/Qwen-Image-Edit-2509 基础工作流_1971613466534539266.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 10/11 个有
- `LoraLoaderModelOnly` —— 9/11 个有
- `TextEncodeQwenImageEdit` —— 7/11 个有
- `TextEncodeQwenImageEditPlus` —— 5/11 个有
- `Fast Groups Bypasser (rgthree)` —— 4/11 个有
- `ConditioningZeroOut` —— 3/11 个有
- `EmptySD3LatentImage` —— 3/11 个有
- `Image Comparer (rgthree)` —— 3/11 个有
- `CLIPTextEncode` —— 2/11 个有
- `LayerUtility: PurgeVRAM` —— 2/11 个有
- `PreviewImage` —— 2/11 个有
- `RH_Nano_Banana_Image2Image` —— 2/11 个有
- `RH_Translator` —— 2/11 个有
- `CR Draw Shape` —— 1/11 个有
- `CR Text` —— 1/11 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有
- `NineGridMosaicNode` —— 1/11 个有
- `PreviewAny` —— 1/11 个有
- `RH_ComfyFluxKontext` —— 1/11 个有
- `RH_Jimeng4_Image2Image` —— 1/11 个有
- `SeargePromptCombiner` —— 1/11 个有
- `SeargePromptText` —— 1/11 个有
- `TextEncodeQwenImageEdit_lrzjason` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 50 | 11 | 20% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 11 | 41% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 0.6 - 1 | 11 | 88% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 50，11 个样本，取值分散，一致性仅 20%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，11 个样本，取值分散，一致性仅 41%
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.6 - 1，11 个样本，取值集中（一致性 88%）
- 高发问题（6/11 个样本）：Steps较低可能导致细节不足
