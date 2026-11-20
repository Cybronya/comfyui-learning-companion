---
name: image_to_image_lora_sampler_unet_16
type: Image To Image
frequency: 21
level: strong
coverage: 0.396667
common_nodes: [CFGNorm, CLIPLoader, GetNode, ImageResizeKJv2, JjkText, KSampler, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PrimitiveInt, SaveImage, SetNode, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键生成多镜头+多角度2_2098938629342187522.json, 图片生成/图生图/一键生成多镜头+多角度=Qwen-Multiple-angles_1984963830654648321.json, 图片生成/图生图/一键生成多镜头+多角度=Qwen-Multiple-angles_2042955576895873025.json, 图片生成/图生图/一键生成多镜头+多角度=Qwen-Multiple-angles。好用到爆，超乎你想象！_2031902890029223937.json, 图片生成/图生图/一键生成多镜头+多角度=Qwen-Multiple-angles。好用到爆，超乎你想象！_2041156746311376898.json, 图片生成/图生图/一键生成多镜头+多角度_1997597737426292738.json, 图片生成/图生图/一键生成多镜头+多角度_2012761833446318081.json, 图片生成/图生图/一键生成多镜头+多角度_2019406910067318785.json, 图片生成/图生图/一键生成多镜头+多角度_2020848993571446785.json, 图片生成/图生图/一键生成多镜头+多角度_2069941228808003585.json, 图片生成/图生图/人物多机位视角切换_2009853282759483393.json, 图片生成/图生图/千问Qwen edit 2509BF16原版 图片一键生成多角度、多镜头控制工作流_1986296620218286081.json, 图片生成/图生图/图片多机位切换_1993495709802577921.json, 图片生成/图生图/角度变换生成相同姿势多角度画面_1989894391701622785.json, 图片生成/文生图/文生多图，口令生多图，文字控制模特动作场景，一键生8张_2017673868990750722.json, 平台全量/Qwen-image-edit-2511 模特套图裂变 高一致性多姿生成  不辨真伪BANANA2_2005526073498632193.json, 平台全量/Qwen-image-edit-2511图像编辑  模特裂变 相同姿势多角度 服装穿搭人物一致换装_2005451512845398017.json, 平台全量/SamsaLa AIGC视觉-一致性控制镜头角度_1986637548174929921.json, 平台全量/qwen一键生成相同姿势多角度画面_1988138727916597249.json, 平台全量/一张图片一键生成多角度多镜头 短剧必备_2091165173640949762.json, 平台全量/史上最最强一键生成多角度、多镜头控制工作流_1986823489900507138.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_16

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/图生图/一键生成多镜头+多角度2_2098938629342187522.json、图片生成/图生图/一键生成多镜头+多角度=Qwen-Multiple-angles_1984963830654648321.json、图片生成/图生图/一键生成多镜头+多角度=Qwen-Multiple-angles_2042955576895873025.json、图片生成/图生图/一键生成多镜头+多角度=Qwen-Multiple-angles。好用到爆，超乎你想象！_2031902890029223937.json、图片生成/图生图/一键生成多镜头+多角度=Qwen-Multiple-angles。好用到爆，超乎你想象！_2041156746311376898.json…）

- **类型**：Image To Image
- **样本数**：21
- **可信度**：强结论
- **平均知识覆盖**：40%

## 共有节点

全部 21 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `GetNode`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PrimitiveInt`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 14/21 个有
- `ProcessString` —— 5/21 个有
- `easy promptLine` —— 5/21 个有
- `easy showAnything` —— 5/21 个有
- `Fast Groups Muter (rgthree)` —— 2/21 个有
- `Image Comparer (rgthree)` —— 2/21 个有
- `PreviewImage` —— 2/21 个有
- `EmptySD3LatentImage` —— 1/21 个有
- `Fast Groups Bypasser (rgthree)` —— 1/21 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/21 个有
- `ImageScaleToTotalPixels` —— 1/21 个有
- `孤海注释` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 21 | 88% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 21 | 100% |
| 采样算法 | euler | - | 21 | 100% |
| 调度器 | simple | - | 21 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 21 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 139/21 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，21 个样本，取值集中（一致性 88%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，21 个样本，一致性 100%
- 调度器 最常用 simple，21 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- 高发问题（139/21 个样本）：Steps较低可能导致细节不足
