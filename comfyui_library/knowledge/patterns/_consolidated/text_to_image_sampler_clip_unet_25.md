---
name: text_to_image_sampler_clip_unet_25
type: Text To Image
frequency: 15
level: moderate
coverage: 0.887733
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/2031033876067393537.json, 图片生成/文生图/2031306114851147777.json, 图片生成/文生图/251225001.013. Z image_v3升级版更强提示词理解_2004252074999246849.json, 图片生成/文生图/33号特工：Z-image小钢炮，文生图+本地解码+彩图_2046531810259116033.json, 图片生成/文生图/5.其他类型-6.NSF+-09.Z-image生图002.Z-image批量文生图.json_2021966315602317313.json, 图片生成/文生图/Krea-2 高真实感与卓越美学文生图_2069683043954151426.json, 图片生成/文生图/LH-DMT版本-2.生图片类-029.Z-image智能改词文生图-NF_2016493278639693826.json, 图片生成/文生图/Z-IMAGE-TURBO：文生图 （api 专用）_2034271324402622466.json, 图片生成/文生图/qwen-image（文生多图）_2042897299998773250.json, 图片生成/文生图/qwen-image（文生多图）场景一致＋连贯_2043178581190250498.json, 图片生成/文生图/zimage-turbo-内衣静物拍摄文生图_2042237620306055169.json, 图片生成/文生图/出图最快Z-image_1993923664148185089.json, 图片生成/文生图/强到可怕_一次性多提示词 极速生成多张图_1994041155893608450.json, 图片生成/文生图/（1.2）WH-Z-IMAG最强生图（一次可生多图）_2005272973877673986.json, 图片生成/文生图/🤖强到可怕！Z-image小钢炮来袭！又快又好，爱不释手🤖_1993864367661924353.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_25

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/2031033876067393537.json、图片生成/文生图/2031306114851147777.json、图片生成/文生图/251225001.013. Z image_v3升级版更强提示词理解_2004252074999246849.json、图片生成/文生图/33号特工：Z-image小钢炮，文生图+本地解码+彩图_2046531810259116033.json、图片生成/文生图/5.其他类型-6.NSF+-09.Z-image生图002.Z-image批量文生图.json_2021966315602317313.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImpactInt` —— 13/15 个有
- `ConditioningZeroOut` —— 12/15 个有
- `String Literal` —— 11/15 个有
- `CR Prompt List` —— 10/15 个有
- `easy showAnything` —— 10/15 个有
- `AnyAspectRatio` —— 1/15 个有
- `LayerUtility: PurgeVRAM` —— 1/15 个有
- `LoraLoaderModelOnly` —— 1/15 个有
- `Note Plus (mtb)` —— 1/15 个有
- `TT_img_enc_v2` —— 1/15 个有
- `easy cleanGpuUsed` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | 720 - 1920 | 15 | 57% |
| 高度 | 1280 | 720 - 1920 | 15 | 82% |
| 采样步数 | 9 | 8 - 20 | 15 | 61% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 15 | 57% |
| 采样算法 | res_2s | - | 15 | 60% |
| 调度器 | bong_tangent | - | 15 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 720，观测区间 720 - 1920，15 个样本
- 高度 中位数 1280，观测区间 720 - 1920，15 个样本，取值集中（一致性 82%）
- 采样步数 中位数 9，观测区间 8 - 20，15 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，15 个样本
- 采样算法 最常用 res_2s，15 个样本，一致性 60%
- 调度器 最常用 bong_tangent，15 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（9/15 个样本）：Steps较低可能导致细节不足
