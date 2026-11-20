---
name: text_to_image_controlnet_lora_sampler_14
type: Text To Image
frequency: 3
level: weak
coverage: 0.873667
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, Int, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SetUnionControlNetType, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen姿势、线稿、深度控制三合一_1960639879807983617.json, 图片生成/文生图/Qwen姿势控制V1_1978359834733076482.json, 图片生成/文生图/闽粤纹样-线稿-文生图-纹样模型v3-48G_2022360002404552705.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_lora_sampler_14

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/qwen姿势、线稿、深度控制三合一_1960639879807983617.json、图片生成/文生图/Qwen姿势控制V1_1978359834733076482.json、图片生成/文生图/闽粤纹样-线稿-文生图-纹样模型v3-48G_2022360002404552705.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptyLatentImage`
- `Int`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SetUnionControlNetType`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 2/3 个有
- `ImpactSwitch` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `Textbox` —— 2/3 个有
- `easy int` —— 2/3 个有
- `CFGNorm` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `easy showAnything` —— 1/3 个有
- `ttN text` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 3 | 36% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 3 | 53% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 0.5 - 1 | 3 | 72% |
| 宽度 | 512 | 512 - 1080 | 3 | 62% |
| 高度 | 512 | 512 - 1920 | 3 | 32% |
| ControlNet 权重 | 1 | 0.75 - 1 | 3 | 87% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，3 个样本，取值分散，一致性仅 36%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，3 个样本
- 宽度 中位数 512，观测区间 512 - 1080，3 个样本
- 高度 中位数 512，观测区间 512 - 1920，3 个样本，取值分散，一致性仅 32%
- ControlNet 权重 中位数 1，观测区间 0.75 - 1，3 个样本，取值集中（一致性 87%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
