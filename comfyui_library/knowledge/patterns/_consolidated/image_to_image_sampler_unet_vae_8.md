---
name: image_to_image_sampler_unet_vae_8
type: Image To Image
frequency: 17
level: moderate
coverage: 0.983824
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【遇见AI】QWen-image-edit-2511 Qwen Multiangle Camera_2009873163982737410.json, 图片生成/图生图/【遇见AI】Qwen-image-edit 图生图基础_2051187067786407937.json, 图片生成/图生图/人物视角转换_2009456601119334402.json, 图片生成/图生图/人物视角转换_2065426763504775169.json, 图片生成/图生图/人物转3D手办Qwen-Image-Edit图像编辑_1998633582274994178.json, 图片生成/图生图/人物转3D手办Qwen-Image-Edit图像编辑_2013877879095955458.json, 图片生成/图生图/人物转3D手办Qwen-Image-Edit图像编辑_2070417457063485442.json, 图片生成/图生图/千问-3D转绘_1995785923046543362.json, 图片生成/图生图/多角度分镜-qwen edit 2511_2009893386551037953.json, 图片生成/图生图/换脸换装FireRed人物一致性_2031960497838366722.json, 图片生成/图生图/换装换脸FireRed人物一致性_2031963984508751873.json, 图片生成/图生图/超强2D转3D-Qwen-Image-Edit_2020677263766855681.json, 图片生成/文生图/3D转绘-Qwen-Image-Edit图像编辑-Comfy官方_1986720327151595522.json, 图片生成/文生图/3D转绘-Qwen-Image-Edit图像编辑-Comfy官方_1986721390671949825.json, 平台全量/3D转绘-Qwen-Image-Edit_2018861981977026562.json, 平台全量/单图_双图编辑 换装换脸FireRed-Image-Edit  局部重绘 万物迁移_2032278487364538369.json, 平台全量/单图_双图编辑 换装换脸FireRed-Image-Edit  局部重绘 万物迁移_2055090325395386369.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_8

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/【遇见AI】QWen-image-edit-2511 Qwen Multiangle Camera_2009873163982737410.json、图片生成/图生图/【遇见AI】Qwen-image-edit 图生图基础_2051187067786407937.json、图片生成/图生图/人物视角转换_2009456601119334402.json、图片生成/图生图/人物视角转换_2065426763504775169.json、图片生成/图生图/人物转3D手办Qwen-Image-Edit图像编辑_1998633582274994178.json…）

- **类型**：Image To Image
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 17 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 15/17 个有
- `ConditioningZeroOut` —— 14/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 12/17 个有
- `Text Multiline` —— 9/17 个有
- `ImageStitch` —— 7/17 个有
- `FluxKontextMultiReferenceLatentMethod` —— 5/17 个有
- `CR Text` —— 4/17 个有
- `Int` —— 4/17 个有
- `Image Comparer (rgthree)` —— 3/17 个有
- `ImageConcanate` —— 3/17 个有
- `QwenMultiangleCameraNode` —— 3/17 个有
- `Anything Everywhere3` —— 1/17 个有
- `CR Prompt List` —— 1/17 个有
- `LoraLoader` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 40 | 17 | 25% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 17 | 58% |
| 采样算法 | euler | - | 17 | 88% |
| 调度器 | simple | - | 17 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 40，17 个样本，取值分散，一致性仅 25%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，17 个样本
- 采样算法 最常用 euler，17 个样本，一致性 88%
- 调度器 最常用 simple，17 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
