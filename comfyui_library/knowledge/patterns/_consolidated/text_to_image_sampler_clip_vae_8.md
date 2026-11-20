---
name: text_to_image_sampler_clip_vae_8
type: Text To Image
frequency: 14
level: moderate
coverage: 0.964071
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/35logo_2049763229265612802.json, 图片生成/图生图/Qwen-厚涂插画_2005961463678337025.json, 图片生成/图生图/Z-image-base文生图-8步-加速版_2029109565865861122.json, 图片生成/图生图/慕沛灵粉红装扮)_1985298677944172546.json, 图片生成/图生图/梦幻孤独画风Qwen_2007044144136462337.json, 图片生成/文生图/1-Z-image-角色信息+场景出图_2041121891695464449.json, 图片生成/文生图/1-Z-image-角色信息+场景出图_2052377045975486465.json, 图片生成/文生图/2-1-z-image-文生图-角色生成_2061349711671554049.json, 图片生成/文生图/2029542457939075073.json, 图片生成/文生图/2030225062405611521.json, 图片生成/文生图/2030250301340520450.json, 图片生成/文生图/A-14 Z-Image Turbo 特定风格 人像大作 文生图_2096961472139194369.json, 图片生成/文生图/A-15 Krea2 特定风格 人像大作 文生图_2098692058323177474.json, 图片生成/文生图/Krea2 人物LoRA测试—Taslim_2073325908940902401.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_8

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/反推提示词/35logo_2049763229265612802.json、图片生成/图生图/Qwen-厚涂插画_2005961463678337025.json、图片生成/图生图/Z-image-base文生图-8步-加速版_2029109565865861122.json、图片生成/图生图/慕沛灵粉红装扮)_1985298677944172546.json、图片生成/图生图/梦幻孤独画风Qwen_2007044144136462337.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 13/14 个有
- `LoraLoaderModelOnly` —— 11/14 个有
- `ModelSamplingAuraFlow` —— 11/14 个有
- `ConditioningZeroOut` —— 8/14 个有
- `PreviewImage` —— 3/14 个有
- `ResolutionSelector` —— 3/14 个有
- `CR Latent Input Switch` —— 1/14 个有
- `FlashVSRNode` —— 1/14 个有
- `Textbox` —— 1/14 个有
- `UnetLoaderGGUF` —— 1/14 个有
- `easy ifElse` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 720 - 2480 | 14 | 60% |
| 高度 | 1408 | 720 - 2480 | 14 | 70% |
| 采样步数 | 8 | 8 - 20 | 14 | 58% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 14 | 38% |
| 采样算法 | euler | - | 14 | 79% |
| 调度器 | simple | - | 14 | 79% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 720 - 2480，14 个样本
- 高度 中位数 1408，观测区间 720 - 2480，14 个样本
- 采样步数 中位数 8，观测区间 8 - 20，14 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，14 个样本，取值分散，一致性仅 38%
- 采样算法 最常用 euler，14 个样本，一致性 79%
- 调度器 最常用 simple，14 个样本，一致性 79%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（12/14 个样本）：Steps较低可能导致细节不足
