---
name: text_to_image_sampler_clip_vae_6
type: Text To Image
frequency: 17
level: weak
coverage: 0.923941
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Nunchaku极速版Z-image文生图_2005527503991177218.json, 图片生成/文生图/Nunchaku超级加速版Z-image文生图v1_2005116765585764354.json, 图片生成/文生图/Ovis-image文生图工作流_1996530154350452738.json, 图片生成/文生图/Qwen2512超强一致性文生图阿里最新开源模型_2011616403639504897.json, 图片生成/文生图/Qwen3超强图片反推_2043616761685221378.json, 图片生成/文生图/Red-Z image Distilled Base加速版文生图V1_2018000841084506113.json, 图片生成/文生图/Super Z-image 3.0文生图_2018000830837825538.json, 图片生成/文生图/Super Z-image 3.0文生图批量跑 浮云2.6_2019676814746066946.json, 图片生成/文生图/Super Z-image 文生图_2018521699486015489.json, 图片生成/文生图/Z-Image Turbo VS De-Turbo VS Re-Turbo对比_2073390583678332930.json, 图片生成/文生图/Z-Image-De-Turbo去蒸馏文生图（CFG3 25步）_1997621234118668290.json, 图片生成/文生图/Z-image-distall-patch文生图_2002052529569579010.json, 图片生成/文生图/Z-image-distall-patch（文生图）写实性lora_2004006107569897473.json, 图片生成/文生图/Z-image文生图人像摄影2K版_1994574159525126145.json, 图片生成/文生图/贞贞lora多重z-image版本对比_2018006131871846401.json, 图片生成/文生图/（贞贞-小情绪版）Z-Image 文生图V1_2001331257915080706.json, 图片生成/文生图/👾怪獸-Z-Image 文生图圣诞特集👾_1996136993329496065.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_6

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/文生图/Nunchaku极速版Z-image文生图_2005527503991177218.json、图片生成/文生图/Nunchaku超级加速版Z-image文生图v1_2005116765585764354.json、图片生成/文生图/Ovis-image文生图工作流_1996530154350452738.json、图片生成/文生图/Qwen2512超强一致性文生图阿里最新开源模型_2011616403639504897.json、图片生成/文生图/Qwen3超强图片反推_2043616761685221378.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

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
- `CR Prompt Text` —— 12/17 个有
- `ConditioningZeroOut` —— 11/17 个有
- `LayerUtility: PurgeVRAM` —— 8/17 个有
- `LoraLoaderModelOnly` —— 7/17 个有
- `easy promptLine` —— 7/17 个有
- `PrimitiveInt` —— 6/17 个有
- `ImageConcatMulti` —— 3/17 个有
- `CR Text` —— 2/17 个有
- `NunchakuZImageDiTLoader` —— 2/17 个有
- `RHHiddenNodes` —— 1/17 个有
- `TextInputNode` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 50 | 17 | 35% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 17 | 0% |
| 采样算法 | euler | - | 17 | 76% |
| 调度器 | simple | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |
| 宽度 | 1080 | 768 - 1920 | 17 | 70% |
| 高度 | 1920 | 1024 - 1920 | 17 | 76% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 50，17 个样本，取值分散，一致性仅 35%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，17 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，17 个样本，一致性 76%
- 调度器 最常用 simple，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 768 - 1920，17 个样本
- 高度 中位数 1920，观测区间 1024 - 1920，17 个样本
