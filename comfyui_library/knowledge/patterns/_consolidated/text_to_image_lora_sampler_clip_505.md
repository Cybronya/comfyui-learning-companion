---
name: text_to_image_lora_sampler_clip_505
type: Text To Image
frequency: 3
level: moderate
coverage: 0.972333
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, LoraLoaderModelOnly, PathchSageAttentionKJ, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/K2文生图工作流竖版推荐_2082984803409944578.json, 图片生成/文生图/wan2.2超写实文生图_1970130948895481857.json, 图片生成/文生图/豹豹喵呜制作：K2白玉AIO测试工作流_2082374968163258369.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_505

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/K2文生图工作流竖版推荐_2082984803409944578.json、图片生成/文生图/wan2.2超写实文生图_1970130948895481857.json、图片生成/文生图/豹豹喵呜制作：K2白玉AIO测试工作流_2082374968163258369.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `LayerColor: Brightness & Contrast` —— 2/3 个有
- `LayerFilter: AddGrain` —— 2/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `孤海注释` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 3 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1280 | 1088 - 2160 | 3 | 69% |
| 高度 | 1920 | 1280 - 3840 | 3 | 54% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1280，观测区间 1088 - 2160，3 个样本
- 高度 中位数 1920，观测区间 1280 - 3840，3 个样本
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
