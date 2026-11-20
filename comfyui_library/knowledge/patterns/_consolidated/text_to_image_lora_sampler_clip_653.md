---
name: text_to_image_lora_sampler_clip_653
type: Text To Image
frequency: 2
level: weak
coverage: 0.9775
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningKrea2Rebalance, ConditioningZeroOut, EmptyLatentImage, KSampler, Krea2ControlApply, Krea2ControlImageEncode, Krea2ControlLoRALoader, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图图KREA2自动深度分区LoRA工作流_2076613514822774786.json, 图片生成/图生图/深度控制_定制版_ID15_2086650777556307969.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_653

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/图图KREA2自动深度分区LoRA工作流_2076613514822774786.json、图片生成/图生图/深度控制_定制版_ID15_2086650777556307969.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningKrea2Rebalance`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `Krea2ControlApply`
- `Krea2ControlImageEncode`
- `Krea2ControlLoRALoader`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `DepthAnythingV2Preprocessor` —— 1/2 个有
- `Ideogram4PromptBuilderKJ` —— 1/2 个有
- `Krea2RegionalMultiLoRA` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoraLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1472 | - | 2 | 70% |
| 高度 | 1308 | - | 2 | 83% |
| LoRA 模型强度 | 0 | - | 1 | 100% |
| LoRA 文本强度 | 0 | - | 1 | 100% |
| 采样步数 | 9 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1.1 | - | 2 | 91% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1472，样本不足，未给区间，2 个样本
- 高度 中位数 1308，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1.1，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
