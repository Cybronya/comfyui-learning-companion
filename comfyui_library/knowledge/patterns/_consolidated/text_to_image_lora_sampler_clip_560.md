---
name: text_to_image_lora_sampler_clip_560
type: Text To Image
frequency: 3
level: strong
coverage: 0.891
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image_lora  （丝袜版）_1995812666759327745.json, 图片生成/文生图/Z-image文生图奇幻风格_1997646513021104130.json, 图片生成/文生图/krea2文生图+官方LORA_2069978232052600834.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_560

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-image_lora  （丝袜版）_1995812666759327745.json、图片生成/文生图/Z-image文生图奇幻风格_1997646513021104130.json、图片生成/文生图/krea2文生图+官方LORA_2069978232052600834.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
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
- `CR Text` —— 2/3 个有
- `CompressImages` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `ImpactInt` —— 1/3 个有
- `JoinStringMulti` —— 1/3 个有
- `VHS_Unbatch` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1920 | 1024 - 1920 | 3 | 74% |
| 高度 | 1080 | 1080 - 1536 | 3 | 83% |
| 采样步数 | 9 | 8 - 10 | 3 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1920，观测区间 1024 - 1920，3 个样本
- 高度 中位数 1080，观测区间 1080 - 1536，3 个样本，取值集中（一致性 83%）
- 采样步数 中位数 9，观测区间 8 - 10，3 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
