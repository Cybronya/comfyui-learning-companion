---
name: text_to_image_controlnet_lora_sampler_5
type: Text To Image
frequency: 5
level: moderate
coverage: 0.8438
common_nodes: [CLIPLoader, CLIPTextEncode, ControlNetLoader, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/87time # 50  通义千问 QW 控制 CN_1970450658602196993.json, 图片生成/图生图/87time # 52 QW 局部重绘_1970447904290861057.json, 图片生成/图生图/87time #52 QW 局部重绘_1965687455661834242.json, 图片生成/图生图/【阡陌】Qwen-Image-ControlNet-Union精准控图工作流_1960641591251787778.json, 图片生成/文生图/Qwen image 2512文生图+CN控制汇总_2006971640961306626.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_lora_sampler_5

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/87time # 50  通义千问 QW 控制 CN_1970450658602196993.json、图片生成/图生图/87time # 52 QW 局部重绘_1970447904290861057.json、图片生成/图生图/87time #52 QW 局部重绘_1965687455661834242.json、图片生成/图生图/【阡陌】Qwen-Image-ControlNet-Union精准控图工作流_1960641591251787778.json、图片生成/文生图/Qwen image 2512文生图+CN控制汇总_2006971640961306626.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ControlNetApplyAdvanced` —— 4/5 个有
- `AIO_Preprocessor` —— 3/5 个有
- `GetImageSize+` —— 3/5 个有
- `DWPreprocessor` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `ModelSamplingAuraFlow` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `CFGNorm` —— 1/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `ControlNetInpaintingAliMamaApply` —— 1/5 个有
- `EmptySD3LatentImage` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `ModelPatchLoader` —— 1/5 个有
- `QwenImageDiffsynthControlnet` —— 1/5 个有
- `SetNode` —— 1/5 个有
- `SetUnionControlNetType` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 5 | 76% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 768 | 768 - 1280 | 5 | 76% |
| 高度 | 1024 | 720 - 1024 | 5 | 87% |
| ControlNet 权重 | 0.925 | 0.85 - 3 | 4 | 36% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 768 - 1280，5 个样本
- 高度 中位数 1024，观测区间 720 - 1024，5 个样本，取值集中（一致性 87%）
- ControlNet 权重 中位数 0.925，观测区间 0.85 - 3，4 个样本，取值分散，一致性仅 36%
- 高发问题（7/5 个样本）：Steps较低可能导致细节不足
