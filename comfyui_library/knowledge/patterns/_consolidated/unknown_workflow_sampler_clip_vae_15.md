---
name: unknown_workflow_sampler_clip_vae_15
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.901
common_nodes: [CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, KSampler, ModelSamplingAuraFlow, SaveImage, Text Multiline, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/38bgb_2049808434131939330.json, 图片生成/文生图/Nunchaku8步加速千问文生图_1962382351810564097.json, 图片生成/文生图/Nunchaku千问文生图_1959849718341906433.json, 图片生成/文生图/Nunchaku千问文生图超快_1959997422854418434.json, 图片生成/文生图/QWen-Image 8步加速_1955523693487296514.json, 图片生成/文生图/QWen-Image 表情包 解锁你的情绪新表达_1955541581090754561.json, 图片生成/文生图/QWen-Image8步加速中文渲染_1955336945507471361.json, 图片生成/文生图/Qwen-Image文生图+提示词优化器_1953302071052333057.json, 图片生成/文生图/中文书法字体设计 - 媲美即梦 - Qwen-Image文生图_1953065521521618946.json, 图片生成/文生图/中文书法字体设计 -文生图-中文字体logo-书法字体设计-艺术字_2021848205499043842.json, 图片生成/文生图/千问Qwen-image中文书法字体设计 - 媲美即梦_2002775003546415106.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_15

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/反推提示词/38bgb_2049808434131939330.json、图片生成/文生图/Nunchaku8步加速千问文生图_1962382351810564097.json、图片生成/文生图/Nunchaku千问文生图_1959849718341906433.json、图片生成/文生图/Nunchaku千问文生图超快_1959997422854418434.json、图片生成/文生图/QWen-Image 8步加速_1955523693487296514.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `Text Multiline`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 8/11 个有
- `easy showAnything` —— 8/11 个有
- `LoraLoaderModelOnly` —— 5/11 个有
- `EmptySD3LatentImage` —— 4/11 个有
- `ConditioningZeroOut` —— 3/11 个有
- `NunchakuQwenImageDiTLoader` —— 3/11 个有
- `RH_LLMAPI_NODE` —— 3/11 个有
- `StringReplace` —— 3/11 个有
- `ImpactInt` —— 1/11 个有
- `TextInput_` —— 1/11 个有
- `easy anythingIndexSwitch` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 11 | 68% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 11 | 61% |
| 采样算法 | euler | - | 11 | 91% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，11 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，11 个样本
- 采样算法 最常用 euler，11 个样本，一致性 91%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
