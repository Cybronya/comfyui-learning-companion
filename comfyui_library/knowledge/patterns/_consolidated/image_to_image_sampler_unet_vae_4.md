---
name: image_to_image_sampler_unet_vae_4
type: Image To Image
frequency: 20
level: moderate
coverage: 0.9029
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物国风风格化_2110252503370653697.json, 图片生成/图生图/人物镜头多角度展示_2007372715937767425.json, 图片生成/图生图/人物镜头多角度工作流_1995473495901581313.json, 图片生成/图生图/从模特身上提取衣服_1979103601475883009.json, 图片生成/图生图/全能图片V1平替QwenImageEditLora4步-2D转3D动画皮克斯风格_1963414314948464641.json, 图片生成/图生图/全能图片V1平替QwenImageEditLora4步-3D转毛毡风格_1963417264743755778.json, 图片生成/图生图/动漫 真人转动漫  真人转卡通  真人转漫画_2096490894571687937.json, 图片生成/图生图/动漫 真人转动漫  真人转卡通  真人转漫画_2097045177390166018.json, 图片生成/图生图/动漫 真人转动漫  真人转卡通  真人转漫画_2097051371597033473.json, 图片生成/图生图/动漫转真人 漫画转真人  线稿转真人  线稿上色 去AI感 超真实_2095059334844731393.json, 图片生成/图生图/动漫转真人 漫画转真人  线稿转真人  线稿上色 去AI感 超真实_2095059817814646785.json, 图片生成/图生图/动漫转真人 漫画转真人  线稿转真人  线稿上色 去AI感 超真实_2095069954918928385.json, 图片生成/图生图/动漫转真人 漫画转真人  线稿转真人  线稿上色 去AI感 超真实_2095193503121887233.json, 图片生成/图生图/动漫转真人 漫画转真人  线稿转真人  线稿上色 去AI感 超真实_2102291710595387394.json, 图片生成/图生图/动漫转真人 漫画转真人  线稿转真人  线稿上色 去AI感 超真实_2107768117282828289.json, 图片生成/图生图/动漫转真人 漫画转真人  线稿转真人  线稿上色 去AI感 超真实_2107833844169789441.json, 图片生成/图生图/动漫转真人 漫画转真人  线稿转真人  线稿上色 去AI感 超真实_2108264468500271106.json, 图片生成/图生图/图片编辑 改图_2112431618567794689.json, 图片生成/图生图/最强-人物不变+多角度写真生成【Qwen2511+lora】_2010916855375994882.json, 图片生成/图生图/超牛的一致性人物多角度展示流！_1995001388340064257.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_4

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/人物国风风格化_2110252503370653697.json、图片生成/图生图/人物镜头多角度展示_2007372715937767425.json、图片生成/图生图/人物镜头多角度工作流_1995473495901581313.json、图片生成/图生图/从模特身上提取衣服_1979103601475883009.json、图片生成/图生图/全能图片V1平替QwenImageEditLora4步-2D转3D动画皮克斯风格_1963414314948464641.json…）

- **类型**：Image To Image
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 19/20 个有
- `ImageScaleToTotalPixels` —— 17/20 个有
- `TextEncodeQwenImageEdit` —— 15/20 个有
- `TextEncodeQwenImageEditPlus` —— 14/20 个有
- `PreviewImage` —— 12/20 个有
- `ModelSamplingAuraFlow` —— 11/20 个有
- `PIP_图像联结` —— 11/20 个有
- `CFGNorm` —— 10/20 个有
- `WD14Tagger|pysssss` —— 9/20 个有
- `easy showAnything` —— 9/20 个有
- `Text Multiline` —— 4/20 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 4/20 个有
- `easy promptLine` —— 4/20 个有
- `ImageConcatMulti` —— 1/20 个有
- `SeedVR2LoadDiTModel` —— 1/20 个有
- `SeedVR2LoadVAEModel` —— 1/20 个有
- `SeedVR2VideoUpscaler` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 20 | 64% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 20 | 42% |
| 采样算法 | euler | - | 20 | 60% |
| 调度器 | simple | - | 20 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，20 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，20 个样本，取值分散，一致性仅 42%
- 采样算法 最常用 euler，20 个样本，一致性 60%
- 调度器 最常用 simple，20 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 高发问题（19/20 个样本）：Steps较低可能导致细节不足
