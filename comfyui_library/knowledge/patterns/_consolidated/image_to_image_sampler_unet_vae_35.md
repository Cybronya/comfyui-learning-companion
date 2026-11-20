---
name: image_to_image_sampler_unet_vae_35
type: Image To Image
frequency: 6
level: strong
coverage: 0.9465
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/印花提取-Qwen-Edit-2511-指定宽高扩图版_2044677933012361218.json, 图片生成/图生图/服装_床品_地毯花纹一键提取_2082687997262262274.json, 图片生成/图生图/👾怪獸-千问Edit单图编辑👾_1979934217855471618.json, 图片生成/文生图/Qwen Edit 2511单图编辑_2073294347310821377.json, 图片生成/文生图/Qwen Edit 2511双图编辑_2073294666874843138.json, 图片生成/文生图/workflow_2073294866825695233.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_35

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/印花提取-Qwen-Edit-2511-指定宽高扩图版_2044677933012361218.json、图片生成/图生图/服装_床品_地毯花纹一键提取_2082687997262262274.json、图片生成/图生图/👾怪獸-千问Edit单图编辑👾_1979934217855471618.json、图片生成/文生图/Qwen Edit 2511单图编辑_2073294347310821377.json、图片生成/文生图/Qwen Edit 2511双图编辑_2073294666874843138.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 6 个 workflow 都包含：
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
- `CR Text` —— 5/6 个有
- `ImageScaleToTotalPixels` —— 4/6 个有
- `Image Comparer (rgthree)` —— 3/6 个有
- `EmptySD3LatentImage` —— 2/6 个有
- `ImageConcatMulti` —— 2/6 个有
- `LoraLoader` —— 2/6 个有
- `DWPreprocessor` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `ImagePadForOutpaint` —— 1/6 个有
- `ImageScale` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 20 | 8 - 20 | 6 | 65% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 6 | 65% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | beta57 | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 8 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 beta57，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
