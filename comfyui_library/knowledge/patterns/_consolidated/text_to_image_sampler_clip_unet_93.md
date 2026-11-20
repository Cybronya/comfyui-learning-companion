---
name: text_to_image_sampler_clip_unet_93
type: Text To Image
frequency: 8
level: moderate
coverage: 0.923
common_nodes: [CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/krea-2文生图_2070065443259375617.json, 图片生成/文生图/krea-文生图-Moebius (Jean Giraud)风格美洲虎捕猎鳄鱼_1962669092442386433.json, 图片生成/文生图/krea2 turbo文生图_2069631042172055554.json, 图片生成/文生图/krea2 turbo文生图_2069632468088606722.json, 图片生成/文生图/krea2 turbo文生图_2069636296083075074.json, 图片生成/文生图/krea2 turbo文生图（最新开源，质量极高，速度极快）_2069769763433304066.json, 图片生成/文生图/krea2-cc风格lora_FEI_2115330409411203074.json, 图片生成/文生图/百度新模型ERNIE-image-turbo_2044765020118061058.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_93

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/krea-2文生图_2070065443259375617.json、图片生成/文生图/krea-文生图-Moebius (Jean Giraud)风格美洲虎捕猎鳄鱼_1962669092442386433.json、图片生成/文生图/krea2 turbo文生图_2069631042172055554.json、图片生成/文生图/krea2 turbo文生图_2069632468088606722.json、图片生成/文生图/krea2 turbo文生图_2069636296083075074.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 7/8 个有
- `JjkText` —— 2/8 个有
- `RH_Translator` —— 2/8 个有
- `ResolutionSelector` —— 2/8 个有
- `ComfySwitchNode` —— 1/8 个有
- `DualCLIPLoader` —— 1/8 个有
- `easy loraStack` —— 1/8 个有
- `easy loraStackApply` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 8 | 100% |
| 高度 | 1536 | 1024 - 1536 | 8 | 84% |
| 采样步数 | 8 | 8 - 30 | 8 | 32% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 8 | 37% |
| 采样算法 | euler | - | 8 | 50% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，8 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1024 - 1536，8 个样本，取值集中（一致性 84%）
- 采样步数 中位数 8，观测区间 8 - 30，8 个样本，取值分散，一致性仅 32%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，8 个样本，取值分散，一致性仅 37%
- 采样算法 最常用 euler，8 个样本，一致性 50%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（7/8 个样本）：Steps较低可能导致细节不足
