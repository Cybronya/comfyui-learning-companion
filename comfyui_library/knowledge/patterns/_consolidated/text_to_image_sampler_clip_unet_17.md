---
name: text_to_image_sampler_clip_unet_17
type: Text To Image
frequency: 21
level: strong
coverage: 0.947095
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image增强版_2005571137486680066.json, 图片生成/文生图/Z-image文生图工作流_2075475394177880066.json, 图片生成/文生图/Zimage文生图-基础_2003639567171395585.json, 图片生成/文生图/Zimage文生图工作流-国产、认识中文、认识明星_1954438175747928065.json, 图片生成/文生图/[众馨]最新王炸Z-Image超快速超细节生图_1994245198530150402.json, 图片生成/文生图/aidir-文生图-krea2_2078304053796364290.json, 图片生成/文生图/krea2_文生图_2081989846117216258.json, 图片生成/文生图/krea2文生图_2069618400707567618.json, 图片生成/文生图/krea2文生图_2069962144506011649.json, 图片生成/文生图/wanxia_2086138759858450434.json, 图片生成/文生图/z-image文生图工作流_2001830276877697026.json, 图片生成/文生图/z-image文生图工作流_2002604407730630657.json, 图片生成/文生图/z-image文生图工作流_2009919536497168386.json, 图片生成/文生图/z-image文生图工作流_2101933018976968706.json, 图片生成/文生图/z-image文生图工作流（B02）_2056384805872431106.json, 图片生成/文生图/zimage文生图+lora仙逆姚惜雪_2005983053098991617.json, 图片生成/文生图/zimage文生图+全息翼界lora_2014158819462488066.json, 图片生成/文生图/人物生成（自用）_2094050883234521090.json, 图片生成/文生图/俯视户外Z-image文生图真实人像质感御姐美女_2041474359600091138.json, 图片生成/文生图/厚涂cg插画风格zimage_2005084819052785665.json, 图片生成/文生图/阿清的偶像捏脸工作流_2057382985531478018.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_17

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/文生图/Z-image增强版_2005571137486680066.json、图片生成/文生图/Z-image文生图工作流_2075475394177880066.json、图片生成/文生图/Zimage文生图-基础_2003639567171395585.json、图片生成/文生图/Zimage文生图工作流-国产、认识中文、认识明星_1954438175747928065.json、图片生成/文生图/[众馨]最新王炸Z-Image超快速超细节生图_1994245198530150402.json…）

- **类型**：Text To Image
- **样本数**：21
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 21 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 20/21 个有
- `easy promptList` —— 8/21 个有
- `ZImageLoraModelOnly` —— 4/21 个有
- `FlashVSRNode` —— 1/21 个有
- `GenerateNoise` —— 1/21 个有
- `INTConstant` —— 1/21 个有
- `Image Comparer (rgthree)` —— 1/21 个有
- `LGNoiseInjectionLatent` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 904 - 1600 | 21 | 86% |
| 高度 | 1536 | 720 - 1920 | 21 | 79% |
| 采样步数 | 9 | 8 - 12 | 21 | 88% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.2 | 21 | 94% |
| 采样算法 | euler | - | 21 | 86% |
| 调度器 | simple | - | 21 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 21 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/21 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 904 - 1600，21 个样本，取值集中（一致性 86%）
- 高度 中位数 1536，观测区间 720 - 1920，21 个样本
- 采样步数 中位数 9，观测区间 8 - 12，21 个样本，取值集中（一致性 88%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.2，21 个样本，取值集中（一致性 94%）
- 采样算法 最常用 euler，21 个样本，一致性 86%
- 调度器 最常用 simple，21 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- 高发问题（18/21 个样本）：Steps较低可能导致细节不足
