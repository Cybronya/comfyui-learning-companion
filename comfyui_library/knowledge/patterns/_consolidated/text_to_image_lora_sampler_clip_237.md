---
name: text_to_image_lora_sampler_clip_237
type: Text To Image
frequency: 3
level: moderate
coverage: 0.979333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z image_绝对美写实人像_2063211868080140290.json, 图片生成/文生图/【极速版】Krea2 Trubo美商极高文生图_V2版_2105216145447014402.json, 视频生成/图生视频/2070438497516875778.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_237

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z image_绝对美写实人像_2063211868080140290.json、图片生成/文生图/【极速版】Krea2 Trubo美商极高文生图_V2版_2105216145447014402.json、视频生成/图生视频/2070438497516875778.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `easy promptLine` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `Int` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `TTResolutionSelector` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `TextInput_` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_2s | - | 3 | 33% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1080 | 512 - 1920 | 3 | 51% |
| 高度 | 1080 | 512 - 1920 | 3 | 51% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，3 个样本，一致性 33%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 512 - 1920，3 个样本
- 高度 中位数 1080，观测区间 512 - 1920，3 个样本
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
