---
name: unknown_workflow_sampler_clip_vae_31
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.898
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/nunchaku-qwen-image with lora_2073405156171018242.json, 图片生成/文生图/nunchaku-qwen-image_2073056140971298817.json, 图片生成/文生图/qwen2512-qwen-lora-文生图工作流_2008018384633466881.json, 图片生成/文生图/qwen2512-qwen-水彩画-文生图工作流_2011342788499087361.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_31

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/nunchaku-qwen-image with lora_2073405156171018242.json、图片生成/文生图/nunchaku-qwen-image_2073056140971298817.json、图片生成/文生图/qwen2512-qwen-lora-文生图工作流_2008018384633466881.json、图片生成/文生图/qwen2512-qwen-水彩画-文生图工作流_2011342788499087361.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 2/4 个有
- `NunchakuQwenImageDiTLoader` —— 2/4 个有
- `UNETLoader` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `EmptyImage` —— 1/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有
- `TextConcat` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 4 | 69% |
| Prompt 约束强度(CFG) | 2 | 1 - 4 | 4 | 42% |
| 采样算法 | res_multistep | - | 4 | 50% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 2，观测区间 1 - 4，4 个样本，取值分散，一致性仅 42%
- 采样算法 最常用 res_multistep，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
