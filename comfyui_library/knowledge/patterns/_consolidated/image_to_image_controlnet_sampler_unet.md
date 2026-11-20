---
name: image_to_image_controlnet_sampler_unet
type: Image To Image
frequency: 9
level: moderate
coverage: 0.849333
common_nodes: [CFGNorm, CLIPLoader, ControlNetApplySD3, ControlNetLoader, ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, SetUnionControlNetType, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Edit 图像编辑 Canny 控制_1968183874985537537.json, 图片生成/图生图/Qwen Edit 图像编辑 Depth 控制_1968182929035788290.json, 图片生成/图生图/Qwen Edit 图像编辑 OpenPose 控制_1968011303954579458.json, 图片生成/图生图/Qwen Edit+姿势-图像精准编辑控制V1_1961275242461249538.json, 图片生成/图生图/Qwen Edit+深度精准编辑控制V1_1961284446211215362.json, 图片生成/图生图/Qwen-Image Edit（姿势随心变）Controlnet控制_1966608414266830850.json, 图片生成/图生图/Qwen-edit-Controlnet控制工作流_1961761519048572929.json, 图片生成/文生图/Qwen Image Edit 千问模型-CN图像编辑 @橘子_SJRJT_1963114897561333762.json, 图片生成/文生图/Qwen 文生图+CN控制 @橘子_SJRJT_1962818248989360130.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_unet

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen Edit 图像编辑 Canny 控制_1968183874985537537.json、图片生成/图生图/Qwen Edit 图像编辑 Depth 控制_1968182929035788290.json、图片生成/图生图/Qwen Edit 图像编辑 OpenPose 控制_1968011303954579458.json、图片生成/图生图/Qwen Edit+姿势-图像精准编辑控制V1_1961275242461249538.json、图片生成/图生图/Qwen Edit+深度精准编辑控制V1_1961284446211215362.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SetUnionControlNetType`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 6/9 个有
- `PreviewImage` —— 6/9 个有
- `OpenposePreprocessor` —— 5/9 个有
- `AIO_Preprocessor` —— 4/9 个有
- `ImageConcatMulti` —— 4/9 个有
- `EmptyLatentImage` —— 3/9 个有
- `JjkText` —— 3/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/9 个有
- `CR Prompt Text` —— 2/9 个有
- `ImageConcanate` —— 2/9 个有
- `CannyEdgePreprocessor` —— 1/9 个有
- `DepthAnythingV2Preprocessor` —— 1/9 个有
- `DepthAnything_V2` —— 1/9 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 1/9 个有
- `EmptySD3LatentImage` —— 1/9 个有
- `FluxKontextImageScale` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 30 | 9 | 29% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 9 | 59% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| ControlNet 权重 | 1.5 | 1.2 - 2 | 9 | 84% |
| 宽度 | 1280 | 1280 - 1280 | 3 | 100% |
| 高度 | 720 | 720 - 720 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 30，9 个样本，取值分散，一致性仅 29%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，9 个样本
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1.5，观测区间 1.2 - 2，9 个样本，取值集中（一致性 84%）
- 宽度 中位数 1280，观测区间 1280 - 1280，3 个样本，取值集中（一致性 100%）
- 高度 中位数 720，观测区间 720 - 720，3 个样本，取值集中（一致性 100%）
