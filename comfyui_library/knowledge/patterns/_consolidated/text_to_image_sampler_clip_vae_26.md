---
name: text_to_image_sampler_clip_vae_26
type: Text To Image
frequency: 6
level: moderate
coverage: 0.754
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, ModelSamplingAuraFlow, RH_Prompter, SaveImage, TextCombinerTwo, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Nunchaku Qwen文生图-极速版_1959819102569312258.json, 图片生成/文生图/Qwen-Image 基本工作流_1987531654463950849.json, 图片生成/文生图/Qwen-Image_1963080046766436353.json, 图片生成/文生图/Qwen文生图-极速版_1957351833759051778.json, 图片生成/文生图/Qwen文生图-极速版_1978645121417760769.json, 图片生成/文生图/Qwen文生图_1972548833475489794.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_26

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Nunchaku Qwen文生图-极速版_1959819102569312258.json、图片生成/文生图/Qwen-Image 基本工作流_1987531654463950849.json、图片生成/文生图/Qwen-Image_1963080046766436353.json、图片生成/文生图/Qwen文生图-极速版_1957351833759051778.json、图片生成/文生图/Qwen文生图-极速版_1978645121417760769.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `ModelSamplingAuraFlow`
- `RH_Prompter`
- `SaveImage`
- `TextCombinerTwo`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/6 个有
- `ImpactSwitch` —— 5/6 个有
- `Int` —— 5/6 个有
- `easy cleanGpuUsed` —— 5/6 个有
- `NunchakuQwenImageDiTLoader` —— 4/6 个有
- `CFGNorm` —— 3/6 个有
- `easy anythingIndexSwitch` —— 3/6 个有
- `LoraLoaderModelOnly` —— 2/6 个有
- `PathchSageAttentionKJ` —— 2/6 个有
- `UnetLoaderGGUF` —— 2/6 个有
- `AddWater_MarkNode` —— 1/6 个有
- `LoadImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 6 | 38% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 6 | 55% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 512 | 512 - 512 | 6 | 100% |
| 高度 | 512 | 512 - 512 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，6 个样本，取值分散，一致性仅 38%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 512，6 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，6 个样本，取值集中（一致性 100%）
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足
