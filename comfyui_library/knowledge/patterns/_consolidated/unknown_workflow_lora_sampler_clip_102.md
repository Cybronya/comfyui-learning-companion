---
name: unknown_workflow_lora_sampler_clip_102
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.6432
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, ComfyUI-Krea2T-Enhancer, ConditioningZeroOut, EmptySD3LatentImage, ImageGrid, ImpactStringSelector, KSampler, PixaromaLoraLoader, PixaromaRunTimer, PixaromaSeed, PixaromaTextJoinTwo, PreviewImage, PrimitiveBoolean, PrimitiveInt, PrimitiveString, PrimitiveStringMultiline, RBG_Smart_Seed_Variance, SaveImage, StrToCombo, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2节点抽卡_2095691750642900994.json, 图片生成/文生图/Krea2极速抽卡1次24张图 [2秒1张] [可控变化] [MJ美学]_2092598493159448578.json, 图片生成/文生图/Krea2极速抽卡1次24张图 [2秒1张] [可控变化] [MJ美学]_2094238103719473154.json, 图片生成/文生图/Krea2极速抽卡1次24张图 [2秒1张] [可控变化] [MJ美学]_2094262936775778305.json, 图片生成/文生图/Krea2极速抽卡1次24张图_[2秒1张]_[可控变化]_[MJ美学]_2094721703443263490.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_102

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Krea2节点抽卡_2095691750642900994.json、图片生成/文生图/Krea2极速抽卡1次24张图 [2秒1张] [可控变化] [MJ美学]_2092598493159448578.json、图片生成/文生图/Krea2极速抽卡1次24张图 [2秒1张] [可控变化] [MJ美学]_2094238103719473154.json、图片生成/文生图/Krea2极速抽卡1次24张图 [2秒1张] [可控变化] [MJ美学]_2094262936775778305.json、图片生成/文生图/Krea2极速抽卡1次24张图_[2秒1张]_[可控变化]_[MJ美学]_2094721703443263490.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：64%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `ComfyUI-Krea2T-Enhancer`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `ImageGrid`
- `ImpactStringSelector`
- `KSampler`
- `PixaromaLoraLoader`
- `PixaromaRunTimer`
- `PixaromaSeed`
- `PixaromaTextJoinTwo`
- `PreviewImage`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveString`
- `PrimitiveStringMultiline`
- `RBG_Smart_Seed_Variance`
- `SaveImage`
- `StrToCombo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 4/5 个有
- `ResolutionSelector` —— 4/5 个有
- `AILab_QwenVL` —— 1/5 个有
- `JjkShowText` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `TTResolutionSelector` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
