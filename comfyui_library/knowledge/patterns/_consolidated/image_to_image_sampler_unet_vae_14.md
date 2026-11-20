---
name: image_to_image_sampler_unet_vae_14
type: Image To Image
frequency: 12
level: moderate
coverage: 0.892167
common_nodes: [CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/KIWI-qwen-Edit图像转CG动漫_1963550771471273985.json, 图片生成/图生图/KIWI-qwen-Edit图像转CG动漫_1963563706520260610.json, 图片生成/图生图/KIWI-qwen-edit-产品精修_1963557059360952321.json, 图片生成/图生图/KIWI-qwen-edit-衣服提取_1963567265559171074.json, 图片生成/图生图/LH-DMT版本-2.生图片类-023.Z_image_turbo图生图_2016484447947853825.json, 图片生成/图生图/Multiple-angles 一致性多角度_2073250359262404610.json, 图片生成/图生图/Qwen Edit扁平转3D，多材质预设_1960598660016988161.json, 图片生成/图生图/☯️qwen姿态迁移_1972199397960445953.json, 图片生成/图生图/人物动作修改 姿势参考 动作修改_1998944623194165250.json, 图片生成/图生图/🌙千问2509人物姿势强化 完美迁移【最强版】🌙_1978831165643722754.json, 图片生成/图生图/🥯千问2509人物姿势完美迁移【姿势强化】🥯_1971739399983722497.json, 图片生成/图生图/🥯千问Edit 2509版 多图稳定编辑版🥯_1971769285058162689.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_14

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/KIWI-qwen-Edit图像转CG动漫_1963550771471273985.json、图片生成/图生图/KIWI-qwen-Edit图像转CG动漫_1963563706520260610.json、图片生成/图生图/KIWI-qwen-edit-产品精修_1963557059360952321.json、图片生成/图生图/KIWI-qwen-edit-衣服提取_1963567265559171074.json、图片生成/图生图/LH-DMT版本-2.生图片类-023.Z_image_turbo图生图_2016484447947853825.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 11/12 个有
- `LoraLoaderModelOnly` —— 11/12 个有
- `TextEncodeQwenImageEdit` —— 10/12 个有
- `ImageConcanate` —— 8/12 个有
- `PreviewImage` —— 6/12 个有
- `TextEncodeQwenImageEditPlus` —— 6/12 个有
- `CR Text` —— 5/12 个有
- `StringFunction|pysssss` —— 5/12 个有
- `AIO_Preprocessor` —— 4/12 个有
- `Fast Groups Bypasser (rgthree)` —— 4/12 个有
- `RH_Captioner` —— 4/12 个有
- `easy showAnything` —— 4/12 个有
- `ImageConcatMulti` —— 3/12 个有
- `ImitationHueNode` —— 3/12 个有
- `CLIPTextEncode` —— 2/12 个有
- `CR Prompt List` —— 2/12 个有
- `Note Plus (mtb)` —— 2/12 个有
- `ImpactInt` —— 1/12 个有
- `RH_LLMAPI_NODE` —— 1/12 个有
- `SaveImageKJ` —— 1/12 个有
- `StringConcatenate` —— 1/12 个有
- `Text Multiline` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 12 | 49% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 12 | 53% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 92% |
| 重绘幅度 | 1 | 0.6 - 1 | 12 | 89% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，12 个样本，取值分散，一致性仅 49%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，12 个样本
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 0.6 - 1，12 个样本，取值集中（一致性 89%）
- 高发问题（8/12 个样本）：Steps较低可能导致细节不足
