---
name: unknown_workflow_sampler_clip_vae_27
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.933286
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/API - Qwenimage文生图_2066885101774008321.json, 图片生成/文生图/Background_2049065581084680194.json, 图片生成/文生图/Chroma 官方工作流_1922361267183374337.json, 图片生成/文生图/Nunchaku Qwen-Image8步加速_1964993982478602241.json, 图片生成/文生图/Nunchaku-Qwen-2512-文生图_2021106190981271553.json, 图片生成/文生图/Qwen Image 2512 平铺商品摄影｜LoRA 商品棚拍_2091542940056375297.json, 图片生成/文生图/Qwen Image Nanchaku1.0 超级加速-StarAI_1960059347424456705.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_27

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/API - Qwenimage文生图_2066885101774008321.json、图片生成/文生图/Background_2049065581084680194.json、图片生成/文生图/Chroma 官方工作流_1922361267183374337.json、图片生成/文生图/Nunchaku Qwen-Image8步加速_1964993982478602241.json、图片生成/文生图/Nunchaku-Qwen-2512-文生图_2021106190981271553.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 5/7 个有
- `UNETLoader` —— 5/7 个有
- `NunchakuQwenImageDiTLoader` —— 3/7 个有
- `Int` —— 2/7 个有
- `LoraLoader` —— 2/7 个有
- `Note Plus (mtb)` —— 1/7 个有
- `NunchakuQwenImageLoraStackV3` —— 1/7 个有
- `T5TokenizerOptions` —— 1/7 个有
- `Text _O` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 4 - 30 | 7 | 39% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 7 | 36% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 4 - 30，7 个样本，取值分散，一致性仅 39%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，7 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/7 个样本）：Steps较低可能导致细节不足
