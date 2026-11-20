---
name: image_to_image_lora_sampler_unet_117
type: Image To Image
frequency: 7
level: strong
coverage: 0.9
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, QwenMultiangleCameraNode, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptList]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/全能生图 千问 2511多角度变换_2012356861068054529.json, 图片生成/图生图/图像多角度编辑手动控制更精准_2017089045016350722.json, 图片生成/图生图/多角度改变图片角度和镜头 - Qwen Multiangle Camera_2010967693100326913.json, 图片生成/图生图/多角度改变图片角度和镜头 - Qwen Multiangle Camera_2026477268612161538.json, 图片生成/图生图/手动改变图片角度和镜头--陈晨up99811_2077999684022530049.json, 图片生成/图生图/手动改变图片角度和镜头！Multiple angles Qwen edit 2511_2009495468832727041.json, 图片生成/图生图/手动调整场景角度（免费版）_2010620776700973058.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_117

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/全能生图 千问 2511多角度变换_2012356861068054529.json、图片生成/图生图/图像多角度编辑手动控制更精准_2017089045016350722.json、图片生成/图生图/多角度改变图片角度和镜头 - Qwen Multiangle Camera_2010967693100326913.json、图片生成/图生图/多角度改变图片角度和镜头 - Qwen Multiangle Camera_2026477268612161538.json、图片生成/图生图/手动改变图片角度和镜头--陈晨up99811_2077999684022530049.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `QwenMultiangleCameraNode`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptList`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 6/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/7 个有
- `VNCCS_VisualPositionControl` —— 6/7 个有
- `easy showAnything` —— 6/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `RH_Nano_Banana2_Image2Image` —— 2/7 个有
- `Text Multiline` —— 2/7 个有
- `ConstrainImage|pysssss` —— 1/7 个有
- `ImageScaleToTotalPixels` —— 1/7 个有
- `MultiTextConcatenate` —— 1/7 个有
- `Text Concatenate` —— 1/7 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 4 - 5 | 7 | 93% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 4 - 5，7 个样本，取值集中（一致性 93%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
