---
name: image_to_image_lora_sampler_unet_128
type: Image To Image
frequency: 5
level: strong
coverage: 0.8872
common_nodes: [CLIPLoader, ConditioningZeroOut, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, PreviewAny, PreviewImage, QwenMultiangleCameraNode, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-edit-2511 多角度镜头切换_2010244411535400962.json, 图片生成/图生图/Qwen-edit-2511 多角度镜头切换_2042268510826536961.json, 图片生成/图生图/Qwen-edit-2511 角度编辑器_2010557074199027714.json, 图片生成/图生图/Qwen-edit-2511_多角度镜头切换_2097142491513450498.json, 图片生成/图生图/Qwen-edit-2511_多角度镜头切换_2097241584365555714.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_128

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen-edit-2511 多角度镜头切换_2010244411535400962.json、图片生成/图生图/Qwen-edit-2511 多角度镜头切换_2042268510826536961.json、图片生成/图生图/Qwen-edit-2511 角度编辑器_2010557074199027714.json、图片生成/图生图/Qwen-edit-2511_多角度镜头切换_2097142491513450498.json、图片生成/图生图/Qwen-edit-2511_多角度镜头切换_2097241584365555714.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `PreviewImage`
- `QwenMultiangleCameraNode`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 4/5 个有
- `LayerUtility: PurgeVRAM V2` —— 4/5 个有
- `SeedVR2` —— 4/5 个有
- `SeedVR2BlockSwap` —— 4/5 个有
- `SeedVR2ExtraArgs` —— 4/5 个有
- `Fast Groups Muter (rgthree)` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `easy promptList` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
