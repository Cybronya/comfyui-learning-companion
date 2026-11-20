---
name: text_to_image_sampler_clip_unet_171
type: Text To Image
frequency: 4
level: weak
coverage: 0.956
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/【遇见AI】Juggernaut-Z-Image模型和Zturbo  Zbase对比_2054033528748298242.json, 图片生成/文生图/【阡陌】Z-Image最强极速文生图工作流_1993971431174242306.json, 图片生成/文生图/【阡陌】通义千问Qwen-image文生图工作流_1953718095699431426.json, 图片生成/文生图/一键分镜图生图—多视图+多角度+多视角，可自行调整_2095714755485986817.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_171

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/【遇见AI】Juggernaut-Z-Image模型和Zturbo  Zbase对比_2054033528748298242.json、图片生成/文生图/【阡陌】Z-Image最强极速文生图工作流_1993971431174242306.json、图片生成/文生图/【阡陌】通义千问Qwen-image文生图工作流_1953718095699431426.json、图片生成/文生图/一键分镜图生图—多视图+多角度+多视角，可自行调整_2095714755485986817.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 3/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `ModelSamplingAuraFlow` —— 2/4 个有
- `easy promptLine` —— 2/4 个有
- `CFGNorm` —— 1/4 个有
- `CR Seed` —— 1/4 个有
- `CheckpointLoaderSimple` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `Text Multiline` —— 1/4 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 4 - 20 | 4 | 44% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 4 | 0% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 744 | 512 - 1080 | 4 | 74% |
| 高度 | 1152 | 512 - 1920 | 4 | 57% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 4 - 20，4 个样本，取值分散，一致性仅 44%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，4 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 744，观测区间 512 - 1080，4 个样本
- 高度 中位数 1152，观测区间 512 - 1920，4 个样本
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
