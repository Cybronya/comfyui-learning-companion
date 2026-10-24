---
name: image_to_image_lora_sampler_unet_43
type: Image To Image
frequency: 12
level: moderate
coverage: 0.978083
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image-Edit实现编辑图片的一致性_1968953423150399489.json, 图片生成/图生图/Qwen-Image-Edit实现编辑图片的一致性_1970349247147241473.json, 图片生成/图生图/Qwen_产品多视角分镜场景_2017587044259733505.json, 图片生成/图生图/qwen-image-edit2511单图编辑--标准版--（必收藏）_2048729771428810754.json, 图片生成/图生图/一键转绘-Qwen-Image-Edit图像编辑_2031200944762916865.json, 图片生成/图生图/人物转3D手办Qwen-Image-Edit图像编辑_1998633582274994178.json, 图片生成/图生图/人物转3D手办Qwen-Image-Edit图像编辑_2013877879095955458.json, 图片生成/图生图/人物转3D手办Qwen-Image-Edit图像编辑_2070417457063485442.json, 图片生成/图生图/位置偏移解决方案-Qwen-Image-Edit_1968671815499436033.json, 图片生成/图生图/超强2D转3D-Qwen-Image-Edit_2020677263766855681.json, 图片生成/文生图/3D转绘-Qwen-Image-Edit图像编辑-Comfy官方_1986720327151595522.json, 图片生成/文生图/3D转绘-Qwen-Image-Edit图像编辑-Comfy官方_1986721390671949825.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_43

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-Edit实现编辑图片的一致性_1968953423150399489.json、图片生成/图生图/Qwen-Image-Edit实现编辑图片的一致性_1970349247147241473.json、图片生成/图生图/Qwen_产品多视角分镜场景_2017587044259733505.json、图片生成/图生图/qwen-image-edit2511单图编辑--标准版--（必收藏）_2048729771428810754.json、图片生成/图生图/一键转绘-Qwen-Image-Edit图像编辑_2031200944762916865.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/12 个有
- `ImageStitch` —— 10/12 个有
- `Text Multiline` —— 8/12 个有
- `TextEncodeQwenImageEditPlus` —— 7/12 个有
- `TextEncodeQwenImageEdit` —— 5/12 个有
- `TextEncodeQwenImageEdit_lrzjason` —— 3/12 个有
- `GroupSwitcher` —— 2/12 个有
- `PrimitiveInt` —— 2/12 个有
- `Text` —— 2/12 个有
- `easy float` —— 2/12 个有
- `easy int` —— 2/12 个有
- `ImageScaleDownToSize` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 20 | 12 | 60% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 12 | 65% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 20，12 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，12 个样本
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（6/12 个样本）：Steps较低可能导致细节不足
