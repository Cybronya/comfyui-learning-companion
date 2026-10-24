---
name: text_to_image_lora_sampler_clip_445
type: Text To Image
frequency: 4
level: strong
coverage: 0.97375
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/QwenImag文生图_1989221367381889026.json, 图片生成/文生图/QwenImag线上文生图（提供本地API调用）_1986272605315485698.json, 图片生成/文生图/Qwen_Image基础加速工作流_1973965175168569346.json, 图片生成/文生图/Qwen趣味剪纸生成_1962073493561085953.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_445

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/QwenImag文生图_1989221367381889026.json、图片生成/文生图/QwenImag线上文生图（提供本地API调用）_1986272605315485698.json、图片生成/文生图/Qwen_Image基础加速工作流_1973965175168569346.json、图片生成/文生图/Qwen趣味剪纸生成_1962073493561085953.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Text Multiline` —— 3/4 个有
- `easy isMaskEmpty` —— 3/4 个有
- `SaveLatent` —— 2/4 个有
- `easy seed` —— 2/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `ImpactSwitch` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `ModelSamplingAuraFlow` —— 1/4 个有
- `QwenEditResolution` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1536 | 1024 - 1536 | 4 | 84% |
| 高度 | 928 | 928 - 1024 | 4 | 96% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1536，观测区间 1024 - 1536，4 个样本，取值集中（一致性 84%）
- 高度 中位数 928，观测区间 928 - 1024，4 个样本，取值集中（一致性 96%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
