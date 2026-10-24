---
name: image_to_image_sampler_unet_vae_16
type: Image To Image
frequency: 11
level: moderate
coverage: 0.845545
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/印花提取-Qwen-Edit-2511-指定宽高扩图版_2044677933012361218.json, 图片生成/图生图/商品照片生成模特图-电商专用-image_qwen_image_edit_2509_1988199854688133122.json, 图片生成/图生图/图像多角度编辑手动控制更精准_2017089045016350722.json, 图片生成/图生图/图片镜头切换_2016419512840626178.json, 图片生成/图生图/场景多视角_2016036160287543298.json, 图片生成/图生图/场景多视角镜头_2010978287455051777.json, 图片生成/图生图/对镜自拍Qwen2511-multiple-angles多角度工作流+全节点注释_2041417500948172801.json, 图片生成/图生图/自由调节镜头视角无极选择器Qwen2511+image+edit_2034454761310785538.json, 图片生成/图生图/调整镜头方向Qwen 2511_2037043928532262913.json, 图片生成/图生图/镜头控制Qwen_2511_2049396359823892482.json, 图片生成/文生图/Qwen2511多角度可视化控制流可调节_2010509977156329474.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_16

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/印花提取-Qwen-Edit-2511-指定宽高扩图版_2044677933012361218.json、图片生成/图生图/商品照片生成模特图-电商专用-image_qwen_image_edit_2509_1988199854688133122.json、图片生成/图生图/图像多角度编辑手动控制更精准_2017089045016350722.json、图片生成/图生图/图片镜头切换_2016419512840626178.json、图片生成/图生图/场景多视角_2016036160287543298.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 10/11 个有
- `FluxKontextMultiReferenceLatentMethod` —— 9/11 个有
- `ImageScaleToTotalPixels` —— 9/11 个有
- `QwenMultiangleCameraNode` —— 9/11 个有
- `EmptySD3LatentImage` —— 7/11 个有
- `easy promptList` —— 6/11 个有
- `easy showAnything` —— 4/11 个有
- `Fast Groups Bypasser (rgthree)` —— 3/11 个有
- `ShowText|pysssss` —— 2/11 个有
- `ImagePadForOutpaint` —— 1/11 个有
- `ImageScale` —— 1/11 个有
- `KepStringList` —— 1/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有
- `LoraLoader` —— 1/11 个有
- `RH_Nano_Banana2_Image2Image` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |
| 采样步数 | 8 | 4 - 20 | 11 | 39% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 11 | 62% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，11 个样本，取值分散，一致性仅 39%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，11 个样本
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（10/11 个样本）：Steps较低可能导致细节不足
