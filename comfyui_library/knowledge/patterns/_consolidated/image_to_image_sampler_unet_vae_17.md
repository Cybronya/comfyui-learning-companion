---
name: image_to_image_sampler_unet_vae_17
type: Image To Image
frequency: 11
level: strong
coverage: 0.944909
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/增强背景和主图效果_2059630159023656961.json, 图片生成/图生图/材质修改Q2511_2008020062157934594.json, 图片生成/图生图/极速真人转动漫_2061261202520625153.json, 图片生成/图生图/橘-qwen edit 2509 多图编辑基础流_2003471485438181377.json, 图片生成/图生图/正面白底图生成器-qwen-Edit-2509_2031287284074553346.json, 图片生成/图生图/灵魂画手工作流_1972209323231342593.json, 图片生成/图生图/生图-图生成正面白底图-qwen-Edit-2509-8步_2000610701750173697.json, 图片生成/图生图/老孙AI 一键去水印qwen2511_2086304124907380737.json, 图片生成/图生图/老照片修复qwen2511千问2511加速版_2003646847212265474.json, 图片生成/图生图/衣服提取衣服_2058616474121625602.json, 图片生成/图生图/衣服提取衣服qwen2511千问2511加速版_2004402979652468737.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_17

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/增强背景和主图效果_2059630159023656961.json、图片生成/图生图/材质修改Q2511_2008020062157934594.json、图片生成/图生图/极速真人转动漫_2061261202520625153.json、图片生成/图生图/橘-qwen edit 2509 多图编辑基础流_2003471485438181377.json、图片生成/图生图/正面白底图生成器-qwen-Edit-2509_2031287284074553346.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 10/11 个有
- `LoraLoaderModelOnly` —— 10/11 个有
- `ModelSamplingAuraFlow` —— 10/11 个有
- `TextEncodeQwenImageEditPlus` —— 10/11 个有
- `ImageScaleToTotalPixels` —— 8/11 个有
- `ImageConcanate` —— 6/11 个有
- `CR Text` —— 5/11 个有
- `FluxKontextMultiReferenceLatentMethod` —— 5/11 个有
- `PreviewImage` —— 3/11 个有
- `ReferenceLatent` —— 3/11 个有
- `GetImageSizeAndCount` —— 2/11 个有
- `EmptySD3LatentImage` —— 1/11 个有
- `FluxGuidance` —— 1/11 个有
- `LayerFilter: GaussianBlur` —— 1/11 个有
- `MaskToImage` —— 1/11 个有
- `TextEncodeQwenImageEdit` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 11 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 91% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 91%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
