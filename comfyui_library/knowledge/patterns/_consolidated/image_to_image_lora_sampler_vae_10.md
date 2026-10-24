---
name: image_to_image_lora_sampler_vae_10
type: Image To Image
frequency: 8
level: strong
coverage: 0.8415
common_nodes: [CFGNorm, CLIPLoader, FluxKontextImageScale, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen_image_edit_2511多角度图片_2094678732018638850.json, 图片生成/图生图/分镜角度自由控制_2011281438196371458.json, 图片生成/图生图/千问2511 多角度自由切换_2009636132782350338.json, 图片生成/图生图/千问2511 多角度自由切换_2010655044642807809.json, 图片生成/图生图/千问2511 多角度自由切换_2048567603374858242.json, 图片生成/图生图/千问2511 多角度自由切换_2052587612896022530.json, 图片生成/图生图/千问2511 多角度自由切换（提示词控制）_2009622014679588865.json, 图片生成/图生图/图像角度转变_2042752682758250498.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_vae_10

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/qwen_image_edit_2511多角度图片_2094678732018638850.json、图片生成/图生图/分镜角度自由控制_2011281438196371458.json、图片生成/图生图/千问2511 多角度自由切换_2009636132782350338.json、图片生成/图生图/千问2511 多角度自由切换_2010655044642807809.json、图片生成/图生图/千问2511 多角度自由切换_2048567603374858242.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextImageScale`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageReel` —— 7/8 个有
- `LayerUtility: ImageReelComposit` —— 7/8 个有
- `UNETLoader` —— 7/8 个有
- `QwenMultiangleCameraNode` —— 6/8 个有
- `CR Text` —— 2/8 个有
- `Image Comparer (rgthree)` —— 2/8 个有
- `ImageScaleToMaxDimension` —— 2/8 个有
- `ComfySwitchNode` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `ModelPatchTorchSettings` —— 1/8 个有
- `PathchSageAttentionKJ` —— 1/8 个有
- `PlaySound|pysssss` —— 1/8 个有
- `PrimitiveString` —— 1/8 个有
- `Text Multiline` —— 1/8 个有
- `UnetLoaderGGUF` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 8 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
