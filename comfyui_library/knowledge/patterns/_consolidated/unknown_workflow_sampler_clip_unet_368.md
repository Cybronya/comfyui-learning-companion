---
name: unknown_workflow_sampler_clip_unet_368
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.894667
common_nodes: [CLIPTextEncode, CR SDXL Aspect Ratio, ConditioningZeroOut, DualCLIPLoader, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLUX-krea最新模型文生图更真实_1951086073063612417.json, 图片生成/文生图/FLUX-krea最新模型文生图（真实感无AI味+自动提示词+批量）_1951062054163652610.json, 图片生成/文生图/Flux.1 Krea Dev文生图【逼真质感 无AI味】_1951177482479280130.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_368

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/FLUX-krea最新模型文生图更真实_1951086073063612417.json、图片生成/文生图/FLUX-krea最新模型文生图（真实感无AI味+自动提示词+批量）_1951062054163652610.json、图片生成/文生图/Flux.1 Krea Dev文生图【逼真质感 无AI味】_1951177482479280130.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `RH_LLMAPI_NODE` —— 2/3 个有
- `RH_Translator` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `Display Any (rgthree)` —— 1/3 个有
- `Int` —— 1/3 个有
- `easy compare` —— 1/3 个有
- `easy ifElse` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
