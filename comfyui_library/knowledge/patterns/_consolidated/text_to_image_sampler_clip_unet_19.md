---
name: text_to_image_sampler_clip_unet_19
type: Text To Image
frequency: 14
level: moderate
coverage: 0.938429
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Anima_base_原版基础工作流_2055104883111546881.json, 图片生成/文生图/Anima_base_原版基础工作流_2055127367860932609.json, 图片生成/文生图/Anima动漫生成大模型：一键生成“良子”漫画插图！_2018308287694905346.json, 图片生成/文生图/Anima基础工作流_2018148600248803330.json, 图片生成/文生图/Anima文生图_2021929707570208769.json, 图片生成/文生图/Anima最新动漫文生图模型_2018217761347997698.json, 图片生成/文生图/Beyond Reality Z-image文生图_1999838076270768130.json, 图片生成/文生图/Boogu 文生图_2068696295937765378.json, 图片生成/文生图/Krea2-trubo-文生图_2069750701965791233.json, 图片生成/文生图/Lens-文生图_2058748909492723713.json, 图片生成/文生图/Qwen-2.1 文生图_2104918958309732354.json, 图片生成/文生图/Qwen-image-2.1-文生图_2101847911167520770.json, 图片生成/文生图/Z-Image-Turbo 身材优化+丰满LoRA_2001971849082859521.json, 图片生成/文生图/krea2 Lora文生图加英伟达rtx nodes高清放大_2074689431730221057.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_19

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/Anima_base_原版基础工作流_2055104883111546881.json、图片生成/文生图/Anima_base_原版基础工作流_2055127367860932609.json、图片生成/文生图/Anima动漫生成大模型：一键生成“良子”漫画插图！_2018308287694905346.json、图片生成/文生图/Anima基础工作流_2018148600248803330.json、图片生成/文生图/Anima文生图_2021929707570208769.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 6/14 个有
- `ConditioningZeroOut` —— 3/14 个有
- `Label (rgthree)` —— 3/14 个有
- `LatentUpscaleBy` —— 2/14 个有
- `LoraLoaderModelOnly` —— 2/14 个有
- `QwenImage21Cache` —— 2/14 个有
- `DeepTranslatorCLIPTextEncodeNode` —— 1/14 个有
- `GPTImage2PromptPreview` —— 1/14 个有
- `RTXVideoSuperResolution` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 27.5 | 8 - 40 | 14 | 53% |
| Prompt 约束强度(CFG) | 2.25 | 1 - 5 | 14 | 36% |
| 采样算法 | euler | - | 14 | 57% |
| 调度器 | simple | - | 14 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 1024 | 896 - 1280 | 14 | 90% |
| 高度 | 1216 | 1024 - 1920 | 14 | 79% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 27.5，观测区间 8 - 40，14 个样本
- Prompt 约束强度(CFG) 中位数 2.25，观测区间 1 - 5，14 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，14 个样本，一致性 57%
- 调度器 最常用 simple，14 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 896 - 1280，14 个样本，取值集中（一致性 90%）
- 高度 中位数 1216，观测区间 1024 - 1920，14 个样本
