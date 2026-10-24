---
name: unknown_workflow_lora_sampler_clip_201
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.803333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/WAN2.2提升画质的10个窍门_1952624573403607042.json, 图片生成/文生图/Wan2.2图片生成  文生图_2038151225899749378.json, 图片生成/文生图/文生图Wan2.2 极简+高清_1974421120923340802.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_201

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/WAN2.2提升画质的10个窍门_1952624573403607042.json、图片生成/文生图/Wan2.2图片生成  文生图_2038151225899749378.json、图片生成/文生图/文生图Wan2.2 极简+高清_1974421120923340802.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/3 个有
- `SeedVR2` —— 2/3 个有
- `SeedVR2BlockSwap` —— 2/3 个有
- `Anything Everywhere3` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `Note Plus (mtb)` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `Text` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 30 | 3 | 32% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 67% |
| 重绘幅度 | simple | - | 3 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 30，3 个样本，取值分散，一致性仅 32%
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 67%
- 重绘幅度 最常用 simple，3 个样本，一致性 67%
- 风险：Prompt 约束强度(CFG) 观测到 30，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
