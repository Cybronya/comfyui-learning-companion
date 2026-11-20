---
name: image_to_image_lora_sampler_unet_108
type: Image To Image
frequency: 7
level: moderate
coverage: 0.831286
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QWEN图像编辑lora加速版_1958348241307910145.json, "图片生成/图生图/Qwen Edit 3模型对比（Meitu,原版,R1）_1982061261863174146.json", "图片生成/图生图/Qwen Edit 3模型对比（Meitu,原版,R1）_1982359589297496065.json", 图片生成/图生图/Qwen Edit MeiTu 图像美学及指令遵从增加图像编辑V1_1982105490522030081.json, 图片生成/图生图/Qwen Edit MeiTu 图像美学及指令遵从增加图像编辑V1_1984427493174165506.json, 图片生成/图生图/Qwen Edit+姿势-图像精准编辑控制V1_1961275242461249538.json, 图片生成/图生图/Qwen Edit+深度精准编辑控制V1_1961284446211215362.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_108

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/QWEN图像编辑lora加速版_1958348241307910145.json、图片生成/图生图/Qwen Edit 3模型对比（Meitu,原版,R1）_1982061261863174146.json、图片生成/图生图/Qwen Edit 3模型对比（Meitu,原版,R1）_1982359589297496065.json、图片生成/图生图/Qwen Edit MeiTu 图像美学及指令遵从增加图像编辑V1_1982105490522030081.json、图片生成/图生图/Qwen Edit MeiTu 图像美学及指令遵从增加图像编辑V1_1984427493174165506.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 6/7 个有
- `ImageConcanate` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `AddLabel` —— 4/7 个有
- `ControlNetApplySD3` —— 2/7 个有
- `ControlNetLoader` —— 2/7 个有
- `SetUnionControlNetType` —— 2/7 个有
- `DepthAnything_V2` —— 1/7 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `Note Plus (mtb)` —— 1/7 个有
- `OpenposePreprocessor` —— 1/7 个有
- `TextInput_` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 30 | 7 | 33% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 7 | 53% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| ControlNet 权重 | 1.5 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 30，7 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（8/7 个样本）：Steps较低可能导致细节不足
