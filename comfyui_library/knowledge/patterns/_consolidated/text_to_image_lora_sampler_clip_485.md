---
name: text_to_image_lora_sampler_clip_485
type: Text To Image
frequency: 4
level: moderate
coverage: 0.98075
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, LoraLoader, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/文生图基础款工作流_1978632798712041473.json, 图片生成/文生图/文生图工作流_1930958208720896001.json, 图片生成/文生图/文生图工作流搭建_2007747002171400193.json, 图片生成/文生图/极速卡通文生图_1919010220243357697.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_485

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/文生图基础款工作流_1978632798712041473.json、图片生成/文生图/文生图工作流_1930958208720896001.json、图片生成/文生图/文生图工作流搭建_2007747002171400193.json、图片生成/文生图/极速卡通文生图_1919010220243357697.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoader`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `RH_Prompter` —— 1/4 个有
- `easy promptConcat` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 896 | 512 - 1024 | 4 | 74% |
| 高度 | 896 | 512 - 1024 | 4 | 74% |
| LoRA 模型强度 | 1 | 0.5 - 1 | 4 | 75% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |
| 采样步数 | 25 | 20 - 30 | 4 | 80% |
| Prompt 约束强度(CFG) | 7.5 | 6 - 8 | 4 | 89% |
| 采样算法 | ddpm | - | 4 | 25% |
| 调度器 | karras | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 896，观测区间 512 - 1024，4 个样本
- 高度 中位数 896，观测区间 512 - 1024，4 个样本
- LoRA 模型强度 中位数 1，观测区间 0.5 - 1，4 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 20 - 30，4 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 7.5，观测区间 6 - 8，4 个样本，取值集中（一致性 89%）
- 采样算法 最常用 ddpm，4 个样本，一致性 25%
- 调度器 最常用 karras，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
