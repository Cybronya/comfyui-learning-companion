---
name: text_to_image_sampler_clip_unet_89
type: Text To Image
frequency: 8
level: strong
coverage: 0.87825
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt List, EmptyLatentImage, ImpactInt, KSampler, SaveImage, String Literal, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/qwen-image（文生多图）_2042897299998773250.json, 图片生成/文生图/qwen-image（文生多图）场景一致＋连贯_2043178581190250498.json, 图片生成/文生图/zimage-turbo-内衣静物拍摄文生图_2042237620306055169.json, 图片生成/文生图/出图最快Z-image_1993923664148185089.json, 图片生成/文生图/强到可怕_一次性多提示词 极速生成多张图_1994041155893608450.json, 图片生成/文生图/（1.2）WH-Z-IMAG最强生图（一次可生多图）_2005272973877673986.json, 图片生成/文生图/🚀 开源新王💯王炸💥Z-IMAGE系列 文生图+ 图生图_1993880222367940610.json, 图片生成/文生图/🤖强到可怕！Z-image小钢炮来袭！又快又好，爱不释手🤖_1993864367661924353.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_89

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/qwen-image（文生多图）_2042897299998773250.json、图片生成/文生图/qwen-image（文生多图）场景一致＋连贯_2043178581190250498.json、图片生成/文生图/zimage-turbo-内衣静物拍摄文生图_2042237620306055169.json、图片生成/文生图/出图最快Z-image_1993923664148185089.json、图片生成/文生图/强到可怕_一次性多提示词 极速生成多张图_1994041155893608450.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt List`
- `EmptyLatentImage`
- `ImpactInt`
- `KSampler`
- `SaveImage`
- `String Literal`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/8 个有
- `Fast Groups Muter (rgthree)` —— 1/8 个有
- `LoadImage` —— 1/8 个有
- `LoraLoaderModelOnly` —— 1/8 个有
- `Note Plus (mtb)` —— 1/8 个有
- `RH_Captioner` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有
- `easy int` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | 720 - 1024 | 8 | 87% |
| 高度 | 1280 | 1280 - 1536 | 8 | 94% |
| 采样步数 | 9.5 | 9 - 20 | 8 | 63% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.5 | 8 | 84% |
| 采样算法 | res_2s | - | 8 | 88% |
| 调度器 | bong_tangent | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 720，观测区间 720 - 1024，8 个样本，取值集中（一致性 87%）
- 高度 中位数 1280，观测区间 1280 - 1536，8 个样本，取值集中（一致性 94%）
- 采样步数 中位数 9.5，观测区间 9 - 20，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.5，8 个样本，取值集中（一致性 84%）
- 采样算法 最常用 res_2s，8 个样本，一致性 88%
- 调度器 最常用 bong_tangent，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（5/8 个样本）：Steps较低可能导致细节不足
