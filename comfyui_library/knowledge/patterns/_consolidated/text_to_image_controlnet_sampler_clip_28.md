---
name: text_to_image_controlnet_sampler_clip_28
type: Text To Image
frequency: 3
level: moderate
coverage: 0.922333
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, KSampler, LoadImage, PreviewImage, SaveImage, SetUnionControlNetType, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/SDXL文生图基础工作流_2000486653930110978.json, 图片生成/文生图/教学用controlnet控制工作流_1920050306917535746.json, 平台全量/ControlNet_1975549699233026050.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_28

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/SDXL文生图基础工作流_2000486653930110978.json、图片生成/文生图/教学用controlnet控制工作流_1920050306917535746.json、平台全量/ControlNet_1975549699233026050.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SetUnionControlNetType`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `VAELoader` —— 2/3 个有
- `Anything Everywhere3` —— 1/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `DWPreprocessor` —— 1/3 个有
- `FluxGuidance` —— 1/3 个有
- `FluxResolutionNode` —— 1/3 个有
- `Lora Loader Stack (rgthree)` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `RH_Prompter` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `SizeFromPresetsSD15` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 30 | 3 | 84% |
| Prompt 约束强度(CFG) | 5 | 1 - 8 | 3 | 39% |
| 采样算法 | dpmpp_2m | - | 3 | 33% |
| 调度器 | beta | - | 3 | 33% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 768 | 512 - 1280 | 3 | 63% |
| 高度 | 1024 | 512 - 1280 | 3 | 66% |
| ControlNet 权重 | 0.9 | 0.55 - 1 | 3 | 76% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 30，3 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 1 - 8，3 个样本，取值分散，一致性仅 39%
- 采样算法 最常用 dpmpp_2m，3 个样本，一致性 33%
- 调度器 最常用 beta，3 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 512 - 1280，3 个样本
- 高度 中位数 1024，观测区间 512 - 1280，3 个样本
- ControlNet 权重 中位数 0.9，观测区间 0.55 - 1，3 个样本
