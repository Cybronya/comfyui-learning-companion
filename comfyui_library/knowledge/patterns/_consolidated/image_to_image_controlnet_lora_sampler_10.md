---
name: image_to_image_controlnet_lora_sampler_10
type: Image To Image
frequency: 3
level: strong
coverage: 0.828667
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ControlNetApplyAdvanced, ControlNetLoader, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen控制+Z_image洗图_1993937974584950785.json, 图片生成/文生图/controlnet—千问教学工作流_1994239870906417154.json, 图片生成/文生图/qwen-毛坯房一键精装图_1994410356925665282.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_lora_sampler_10

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen控制+Z_image洗图_1993937974584950785.json、图片生成/文生图/controlnet—千问教学工作流_1994239870906417154.json、图片生成/文生图/qwen-毛坯房一键精装图_1994410356925665282.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `SetUnionControlNetType` —— 2/3 个有
- `AILab_QwenVL` —— 1/3 个有
- `CR SDXL Aspect Ratio` —— 1/3 个有
- `DWPreprocessor` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `SeedVR2` —— 1/3 个有
- `SeedVR2ExtraArgs` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 10 | 3 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 0.8 | 0.75 - 1 | 3 | 87% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 10，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.8，观测区间 0.75 - 1，3 个样本，取值集中（一致性 87%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
