---
name: unknown_workflow_lora_sampler_clip_104
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8802
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, NunchakuQwenImageDiTLoader, NunchakuQwenImageLoraStack, SDXLEmptyLatentSizePicker+, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Nunchaku-Qwen-Image图生图lora版_1980967720676192257.json, 图片生成/图生图/Nunchaku-Qwen-Image图生图lora版_1987824135525044226.json, 图片生成/图生图/图生图lora版_2016788049157431298.json, 图片生成/文生图/qwen(Nunchaku文生图l）支持lora(极速版）_1982787768378109953.json, 图片生成/文生图/图片用这个_2023321341348290562.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_104

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Nunchaku-Qwen-Image图生图lora版_1980967720676192257.json、图片生成/图生图/Nunchaku-Qwen-Image图生图lora版_1987824135525044226.json、图片生成/图生图/图生图lora版_2016788049157431298.json、图片生成/文生图/qwen(Nunchaku文生图l）支持lora(极速版）_1982787768378109953.json、图片生成/文生图/图片用这个_2023321341348290562.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `NunchakuQwenImageDiTLoader`
- `NunchakuQwenImageLoraStack`
- `SDXLEmptyLatentSizePicker+`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `NunchakuQwenImageLoraLoader` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `LoadImage` —— 3/5 个有
- `PreviewAny` —— 3/5 个有
- `RH_Captioner` —— 3/5 个有
- `ModelSamplingAuraFlow` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `easy promptConcat` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024x1024 (1.0) | - | 5 | 100% |
| 高度 | 1 | 1 - 1 | 5 | 100% |
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | kl_optimal | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | disable | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 最常用 1024x1024 (1.0)，5 个样本，一致性 100%
- 高度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 kl_optimal，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 最常用 disable，2 个样本，一致性 100%
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
