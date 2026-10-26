---
name: unknown_workflow_sampler_clip_unet_332
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.9365
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, QwenImageLatentAspectRatio, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/z-image文生图基础lolita_2066807405148721154.json, 图片生成/文生图/z-image文生图基础工作流_2053095025231310849.json, 图片生成/文生图/大玉足文生图_2080343200455286785.json, 图片生成/文生图/新王Z-image 出图更快 更真实_1997156621325385729.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_332

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/z-image文生图基础lolita_2066807405148721154.json、图片生成/文生图/z-image文生图基础工作流_2053095025231310849.json、图片生成/文生图/大玉足文生图_2080343200455286785.json、图片生成/文生图/新王Z-image 出图更快 更真实_1997156621325385729.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `QwenImageLatentAspectRatio`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `1hew_LoadImage` —— 2/4 个有
- `AV_LoraLoader` —— 2/4 个有
- `NunchakuFluxIPAdapterApply` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 9 - 9 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 模型强度 | 0.825 | - | 2 | 79% |
| LoRA 文本强度 | 0.825 | - | 2 | 79% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 9 - 9，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.825，样本不足，未给区间，2 个样本
- LoRA 文本强度 中位数 0.825，样本不足，未给区间，2 个样本
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
