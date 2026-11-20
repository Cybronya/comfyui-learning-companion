---
name: image_to_image_sampler_unet_vae_22
type: Image To Image
frequency: 10
level: moderate
coverage: 0.9167
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/flux.2-去除水印-标准版-（必收藏）_2056999199815847938.json, 图片生成/图生图/flux2_klein_2077688220808208385.json, 图片生成/图生图/image_qwen_image_edit[1]_1959997623912574977.json, 图片生成/图生图/image_qwen_image_edit_2509-双图参考+参考色调重打光_2011594156342255617.json, 图片生成/图生图/image_qwen_image_edit_2509-提示词改变主体_1970979185940406274.json, 图片生成/图生图/logo字体修改编辑_1962779203995348993.json, 图片生成/图生图/qwen Edit_2028751468630646786.json, 图片生成/图生图/qwen image edit 4step 单图_1962144621184880641.json, 图片生成/图生图/qwen2509_1997815157244014594.json, 图片生成/图生图/☯️千问QUYI-DIY换装流_1978128358280159234.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_22

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/flux.2-去除水印-标准版-（必收藏）_2056999199815847938.json、图片生成/图生图/flux2_klein_2077688220808208385.json、图片生成/图生图/image_qwen_image_edit[1]_1959997623912574977.json、图片生成/图生图/image_qwen_image_edit_2509-双图参考+参考色调重打光_2011594156342255617.json、图片生成/图生图/image_qwen_image_edit_2509-提示词改变主体_1970979185940406274.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 9/10 个有
- `ModelSamplingAuraFlow` —— 9/10 个有
- `LoraLoaderModelOnly` —— 8/10 个有
- `ImageScaleToTotalPixels` —— 7/10 个有
- `TextEncodeQwenImageEditPlus` —— 5/10 个有
- `TextEncodeQwenImageEdit` —— 4/10 个有
- `EmptySD3LatentImage` —— 3/10 个有
- `CLIPTextEncode` —— 2/10 个有
- `ReferenceLatent` —— 2/10 个有
- `GLM_Vision_ImageToPrompt` —— 1/10 个有
- `GoogleTranslator` —— 1/10 个有
- `ImageScale` —— 1/10 个有
- `LayerUtility: ImageScaleRestore V2` —— 1/10 个有
- `QwenMultiangleCameraNode` —— 1/10 个有
- `StringFunction|pysssss` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | 4 - 20 | 10 | 30% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 10 | 54% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，观测区间 4 - 20，10 个样本，取值分散，一致性仅 30%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，10 个样本
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（8/10 个样本）：Steps较低可能导致细节不足
