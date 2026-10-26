---
name: unknown_workflow_controlnet_sampler_clip_10
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.872
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, ControlNetApplySD3, ControlNetLoader, EmptySD3LatentImage, KSampler, LoadImage, ModelSamplingAuraFlow, PreviewImage, SaveImage, SetUnionControlNetType, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image InstantX Controlnet Dwpose高难姿势控制V1_1961735398378639362.json, 图片生成/图生图/Qwen Image 姿势 Controlnet_1967676032595759105.json, 图片生成/文生图/Qwen Image 4步文生图_1977759228209364994.json, 图片生成/文生图/Qwen Image InstantX Controlnet(姿态，边缘，深度)_1960886656419205122.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_10

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen Image InstantX Controlnet Dwpose高难姿势控制V1_1961735398378639362.json、图片生成/图生图/Qwen Image 姿势 Controlnet_1967676032595759105.json、图片生成/文生图/Qwen Image 4步文生图_1977759228209364994.json、图片生成/文生图/Qwen Image InstantX Controlnet(姿态，边缘，深度)_1960886656419205122.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `SetUnionControlNetType`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `SeedVR2BlockSwap` —— 3/4 个有
- `DepthAnything_V2` —— 2/4 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `OpenposePreprocessor` —— 2/4 个有
- `SaveLatent` —— 2/4 个有
- `SeedVR2GGUF` —— 2/4 个有
- `AIO_Preprocessor` —— 1/4 个有
- `Anything Everywhere3` —— 1/4 个有
- `CR Prompt Text` —— 1/4 个有
- `DWPreprocessor` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `LoraLoader` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有
- `Text` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | 0.75 - 1 | 4 | 88% |
| 采样步数 | 8 | 4 - 20 | 4 | 40% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | res_2s | - | 4 | 75% |
| 调度器 | beta57 | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 1，观测区间 0.75 - 1，4 个样本，取值集中（一致性 88%）
- 采样步数 中位数 8，观测区间 4 - 20，4 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，4 个样本，一致性 75%
- 调度器 最常用 beta57，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
