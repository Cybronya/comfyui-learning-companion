---
name: text_to_image_sampler_clip_unet_75
type: Text To Image
frequency: 7
level: strong
coverage: 0.895857
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/出图最快Z-image_1993923664148185089.json, 图片生成/文生图/强到可怕_一次性多提示词 极速生成多张图_1994041155893608450.json, 图片生成/文生图/文生图-boogu_turbo-模板_2090689514200195074.json, 图片生成/文生图/文生图基础款_2010012252333678593.json, 图片生成/文生图/（1.2）WH-Z-IMAG最强生图（一次可生多图）_2005272973877673986.json, 图片生成/文生图/🚀 开源新王💯王炸💥Z-IMAGE系列 文生图+ 图生图_1993880222367940610.json, 图片生成/文生图/🤖强到可怕！Z-image小钢炮来袭！又快又好，爱不释手🤖_1993864367661924353.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_75

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/出图最快Z-image_1993923664148185089.json、图片生成/文生图/强到可怕_一次性多提示词 极速生成多张图_1994041155893608450.json、图片生成/文生图/文生图-boogu_turbo-模板_2090689514200195074.json、图片生成/文生图/文生图基础款_2010012252333678593.json、图片生成/文生图/（1.2）WH-Z-IMAG最强生图（一次可生多图）_2005272973877673986.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt List` —— 6/7 个有
- `ImpactInt` —— 5/7 个有
- `String Literal` —— 5/7 个有
- `easy showAnything` —— 5/7 个有
- `Text Multiline` —— 2/7 个有
- `Fast Groups Muter (rgthree)` —— 1/7 个有
- `INTConstant` —— 1/7 个有
- `LoadImage` —— 1/7 个有
- `Note Plus (mtb)` —— 1/7 个有
- `RH_Captioner` —— 1/7 个有
- `easy int` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | 720 - 1536 | 7 | 69% |
| 高度 | 1280 | 1024 - 1920 | 7 | 81% |
| 采样步数 | 9 | 4 - 10 | 7 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | res_2s | - | 7 | 57% |
| 调度器 | bong_tangent | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 720，观测区间 720 - 1536，7 个样本
- 高度 中位数 1280，观测区间 1024 - 1920，7 个样本，取值集中（一致性 81%）
- 采样步数 中位数 9，观测区间 4 - 10，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，7 个样本，一致性 57%
- 调度器 最常用 bong_tangent，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
