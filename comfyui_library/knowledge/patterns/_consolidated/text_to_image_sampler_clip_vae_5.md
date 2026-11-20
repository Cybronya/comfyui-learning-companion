---
name: text_to_image_sampler_clip_vae_5
type: Text To Image
frequency: 17
level: moderate
coverage: 0.975765
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/35logo_2049763229265612802.json, 图片生成/图生图/Qwen-厚涂插画_2005961463678337025.json, 图片生成/图生图/Z-image-base文生图-8步-加速版_2029109565865861122.json, 图片生成/图生图/慕沛灵粉红装扮)_1985298677944172546.json, 图片生成/图生图/梦幻孤独画风Qwen_2007044144136462337.json, 图片生成/文生图/1-Z-image-角色信息+场景出图_2041121891695464449.json, 图片生成/文生图/1-Z-image-角色信息+场景出图_2052377045975486465.json, 图片生成/文生图/2-1-z-image-文生图-角色生成_2061349711671554049.json, 图片生成/文生图/2029542457939075073.json, 图片生成/文生图/2030225062405611521.json, 图片生成/文生图/A-14 Z-Image Turbo 特定风格 人像大作 文生图_2096961472139194369.json, 图片生成/文生图/A-15 Krea2 特定风格 人像大作 文生图_2098692058323177474.json, 图片生成/文生图/Krea2 人物LoRA测试—Taslim_2073325908940902401.json, 图片生成/文生图/Z-image-turbo文生图3D国漫CG风格_2074209841383567362.json, 图片生成/文生图/Z-image-turbo文生图赛璐璐平涂动漫风格_2077821791761948673.json, 图片生成/文生图/Z-image-turbo文生图超写实真人摄影风格_2076587497584414722.json, 图片生成/文生图/Z-image-turbo文生图超写实真人摄影风格_V2.0_2114235650760339458.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_5

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/反推提示词/35logo_2049763229265612802.json、图片生成/图生图/Qwen-厚涂插画_2005961463678337025.json、图片生成/图生图/Z-image-base文生图-8步-加速版_2029109565865861122.json、图片生成/图生图/慕沛灵粉红装扮)_1985298677944172546.json、图片生成/图生图/梦幻孤独画风Qwen_2007044144136462337.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 16/17 个有
- `ModelSamplingAuraFlow` —— 15/17 个有
- `LoraLoaderModelOnly` —— 14/17 个有
- `ConditioningZeroOut` —— 7/17 个有
- `CR Latent Input Switch` —— 5/17 个有
- `ResolutionSelector` —— 3/17 个有
- `PreviewImage` —— 2/17 个有
- `FlashVSRNode` —— 1/17 个有
- `Textbox` —— 1/17 个有
- `UnetLoaderGGUF` —— 1/17 个有
- `easy ifElse` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 720 - 2480 | 17 | 64% |
| 高度 | 1536 | 720 - 2480 | 17 | 70% |
| 采样步数 | 8 | 8 - 20 | 17 | 60% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 17 | 40% |
| 采样算法 | euler | - | 17 | 59% |
| 调度器 | simple | - | 17 | 82% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 720 - 2480，17 个样本
- 高度 中位数 1536，观测区间 720 - 2480，17 个样本
- 采样步数 中位数 8，观测区间 8 - 20，17 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，17 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 euler，17 个样本，一致性 59%
- 调度器 最常用 simple，17 个样本，一致性 82%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 高发问题（16/17 个样本）：Steps较低可能导致细节不足
