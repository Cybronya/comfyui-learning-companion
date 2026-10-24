---
name: image_to_image_lora_sampler_unet_159
type: Image To Image
frequency: 4
level: weak
coverage: 0.9235
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/视角转换_2092163976900730881.json, 图片生成/图生图/👾怪獸-人物道具场景多视角加速版👾_2058103710215131137.json, 图片生成/文生图/image_qwen_image_edit_2511-文生图_2005074898978570241.json, 图片生成/文生图/多角度拖动控制，水平角度，缩放，仰角控制_2009974189255561218.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_159

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/视角转换_2092163976900730881.json、图片生成/图生图/👾怪獸-人物道具场景多视角加速版👾_2058103710215131137.json、图片生成/文生图/image_qwen_image_edit_2511-文生图_2005074898978570241.json、图片生成/文生图/多角度拖动控制，水平角度，缩放，仰角控制_2009974189255561218.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `QwenMultiangleCameraNode` —— 3/4 个有
- `EmptyLatentImage` —— 2/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `LazySwitchKJ` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `easy promptConcat` —— 1/4 个有
- `easy promptList` —— 1/4 个有
- `ttN text` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 20 | 4 | 27% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 4 | 53% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 796 | - | 2 | 64% |
| 高度 | 1024 | - | 2 | 50% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 20，4 个样本，取值分散，一致性仅 27%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 796，样本不足，未给区间，2 个样本
- 高度 中位数 1024，样本不足，未给区间，2 个样本
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
