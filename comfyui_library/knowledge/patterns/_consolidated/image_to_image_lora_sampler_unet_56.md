---
name: image_to_image_lora_sampler_unet_56
type: Image To Image
frequency: 10
level: moderate
coverage: 0.8174
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, ReferenceLatent, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen 2511-角色全身侧面站立图_2082270603360428034.json, 图片生成/图生图/Qwen 2511-角色全身正面站立图_2082264674363592706.json, 图片生成/图生图/Qwen 单张图像编辑_2020825475739820033.json, 图片生成/图生图/Qwen-Edit-2511 外部扩图工作流_2091508580599025665.json, 图片生成/图生图/Qwen-Edit-2511_外部扩图工作流_2097157315584675841.json, 图片生成/图生图/Qwen-Edit-2511_外部扩图工作流_2097496668118802434.json, 图片生成/图生图/Qwen-Image-Edit ComfyUI 原生工作流 1图_2089987209536561154.json, 图片生成/图生图/Qwen-Image-Edit ComfyUI 原生工作流 2图_2089986353214873602.json, 图片生成/图生图/Qwen-Image-Edit ComfyUI 原生工作流 3图_2089973995432136705.json, 图片生成/图生图/Qwen-Image-Edit ComfyUI 原生工作流_1971196767998033922.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_56

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Qwen 2511-角色全身侧面站立图_2082270603360428034.json、图片生成/图生图/Qwen 2511-角色全身正面站立图_2082264674363592706.json、图片生成/图生图/Qwen 单张图像编辑_2020825475739820033.json、图片生成/图生图/Qwen-Edit-2511 外部扩图工作流_2091508580599025665.json、图片生成/图生图/Qwen-Edit-2511_外部扩图工作流_2097157315584675841.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ReferenceLatent`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 7/10 个有
- `EmptyLatentImage` —— 6/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/10 个有
- `ImagePadKJ` —— 3/10 个有
- `PreviewImage` —— 3/10 个有
- `YK_LoadImageFromURL` —— 3/10 个有
- `CR Text` —— 2/10 个有
- `GetImageSize` —— 2/10 个有
- `LayerUtility: TextJoin` —— 2/10 个有
- `ResizeImageMaskNode` —— 2/10 个有
- `TTResolutionSelector` —— 2/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 10 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 1680 | 512 - 1680 | 6 | 57% |
| 高度 | 768 | 512 - 768 | 6 | 82% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 1680，观测区间 512 - 1680，6 个样本
- 高度 中位数 768，观测区间 512 - 768，6 个样本，取值集中（一致性 82%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
