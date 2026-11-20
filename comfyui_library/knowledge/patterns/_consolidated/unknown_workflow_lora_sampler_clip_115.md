---
name: unknown_workflow_lora_sampler_clip_115
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.882
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Instagirl Wan2.2_1954740605987504129.json, 图片生成/文生图/Wan2.2图片生成  文生图_2038151225899749378.json, 图片生成/文生图/Wan2.2文生图_1950935703578419201.json, 图片生成/文生图/图片-文生图-Instagirl_1960284703142129666.json, 图片生成/文生图/文生图Wan2.2 极简+高清_1974421120923340802.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_115

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Instagirl Wan2.2_1954740605987504129.json、图片生成/文生图/Wan2.2图片生成  文生图_2038151225899749378.json、图片生成/文生图/Wan2.2文生图_1950935703578419201.json、图片生成/文生图/图片-文生图-Instagirl_1960284703142129666.json、图片生成/文生图/文生图Wan2.2 极简+高清_1974421120923340802.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
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
- `LoraLoader` —— 3/5 个有
- `easy cleanGpuUsed` —— 3/5 个有
- `Int` —— 2/5 个有
- `LoadImage` —— 2/5 个有
- `SeedVR2` —— 2/5 个有
- `SeedVR2BlockSwap` —— 2/5 个有
- `Anything Everywhere3` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `Text` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 0.6 - 1 | 3 | 78% |
| LoRA 文本强度 | 1 | 0.6 - 1 | 3 | 78% |
| 采样步数 | fixed | - | 5 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 10 | 5 | 89% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler | - | 5 | 60% |
| 重绘幅度 | simple | - | 5 | 60% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 0.6 - 1，3 个样本
- LoRA 文本强度 中位数 1，观测区间 0.6 - 1，3 个样本
- 采样步数 最常用 fixed，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 10，5 个样本，取值集中（一致性 89%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，5 个样本，一致性 60%
- 重绘幅度 最常用 simple，5 个样本，一致性 60%
