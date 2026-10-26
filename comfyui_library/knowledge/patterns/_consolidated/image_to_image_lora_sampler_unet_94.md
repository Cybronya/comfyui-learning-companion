---
name: image_to_image_lora_sampler_unet_94
type: Image To Image
frequency: 7
level: strong
coverage: 0.904429
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, INTConstant, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, QwenMultiangleCameraNode, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/千问多角度图像编辑_2050499840190234626.json, 图片生成/图生图/多角度改变图片角度和镜头 - Qwen Multiangle Camera_2010967693100326913.json, 图片生成/图生图/多角度改变图片角度和镜头 - Qwen Multiangle Camera_2026477268612161538.json, 图片生成/图生图/手动改变图片角度和镜头--陈晨up99811_2077999684022530049.json, 图片生成/图生图/手动改变图片角度和镜头！Multiple angles Qwen edit 2511_2009495468832727041.json, 图片生成/图生图/手动调整场景角度（免费版）_2010620776700973058.json, 图片生成/图生图/改变图片角度和镜头_2114409077630656514.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_94

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/千问多角度图像编辑_2050499840190234626.json、图片生成/图生图/多角度改变图片角度和镜头 - Qwen Multiangle Camera_2010967693100326913.json、图片生成/图生图/多角度改变图片角度和镜头 - Qwen Multiangle Camera_2026477268612161538.json、图片生成/图生图/手动改变图片角度和镜头--陈晨up99811_2077999684022530049.json、图片生成/图生图/手动改变图片角度和镜头！Multiple angles Qwen edit 2511_2009495468832727041.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `INTConstant`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `QwenMultiangleCameraNode`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VAEDecode` —— 6/7 个有
- `VNCCS_VisualPositionControl` —— 6/7 个有
- `easy promptList` —— 6/7 个有
- `easy showAnything` —— 6/7 个有
- `KepStringLiteral` —— 1/7 个有
- `PreviewAny` —— 1/7 个有
- `StringConcatenate` —— 1/7 个有
- `Text Concatenate` —— 1/7 个有
- `Text Multiline` —— 1/7 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/7 个有
- `VAEDecodeTiled` —— 1/7 个有

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
| 发现KSampler但没有VAEDecode | 1/7 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 5，观测区间 4 - 5，7 个样本，取值集中（一致性 93%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
