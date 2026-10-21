---
name: unknown_workflow_sampler_clip_checkpoint_11
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.912167
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, ImpactSwitch, KSampler (Efficient), KSampler Adv. (Efficient), PrimitiveFloat, SaveImage, VAEDecode, VAEEncode, VAELoader, easy positive]
problems: []
missing: []
members: [图片生成/文生图/anima(冥神)_2059802290592243713.json, 图片生成/文生图/anima（育婴龙女）_2060546911119167489.json, 图片生成/文生图/anima（阿宝阿库）_2059812406750175233.json, 图片生成/文生图/ill一采，anima二采样（天气）_2059556474224988161.json, 图片生成/文生图/ill一采，anima二采样（柴郡猫）_2059088000453267458.json, 图片生成/文生图/模型图片测试（迷迭香）_2059812487205314562.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_11

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/anima(冥神)_2059802290592243713.json、图片生成/文生图/anima（育婴龙女）_2060546911119167489.json、图片生成/文生图/anima（阿宝阿库）_2059812406750175233.json、图片生成/文生图/ill一采，anima二采样（天气）_2059556474224988161.json、图片生成/文生图/ill一采，anima二采样（柴郡猫）_2059088000453267458.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `ImpactSwitch`
- `KSampler (Efficient)`
- `KSampler Adv. (Efficient)`
- `PrimitiveFloat`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy positive`

**可变部分**（部分 workflow 才有）：
- `LatentUpscaleBy` —— 3/6 个有
- `LoraLoader` —— 3/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `VAEDecodeTiled` —— 3/6 个有
- `easy promptConcat` —— 3/6 个有
- `PreviewImage` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 30 - 40 | 3 | 87% |
| Prompt 约束强度(CFG) | 22.5 | 5 - 50 | 6 | 19% |
| 采样算法 | 5 | 5 - 5 | 3 | 100% |
| 调度器 | normal | - | 6 | 50% |
| 重绘幅度 | 0.3 | 0.3 - 0.3 | 3 | 100% |
| 宽度 | 1024 | 896 - 1024 | 6 | 94% |
| 高度 | 1024 | 1024 - 1280 | 6 | 89% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，观测区间 30 - 40，3 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 22.5，观测区间 5 - 50，6 个样本，取值分散，一致性仅 19%
- 采样算法 中位数 5，观测区间 5 - 5，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 normal，6 个样本，一致性 50%
- 重绘幅度 中位数 0.3，观测区间 0.3 - 0.3，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 896 - 1024，6 个样本，取值集中（一致性 94%）
- 高度 中位数 1024，观测区间 1024 - 1280，6 个样本，取值集中（一致性 89%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 50，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
