---
name: image_to_image_sampler_clip_unet_77
type: Image To Image
frequency: 6
level: weak
coverage: 0.982833
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z_image_turbo图洗图_2056328304931725313.json, 图片生成/图生图/flux.2-去除水印-标准版-（必收藏）_2056999199815847938.json, 图片生成/图生图/flux2_klein_2077688220808208385.json, 图片生成/图生图/qwen万能lora控图_1960703410297344001.json, 图片生成/图生图/【阡陌】Qwen-Image六合一In Context Controlnet lora精准控制工作流_1960248554344361985.json, 图片生成/文生图/Qwen-Image的union cn_1958888407248351234.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_77

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Z_image_turbo图洗图_2056328304931725313.json、图片生成/图生图/flux.2-去除水印-标准版-（必收藏）_2056999199815847938.json、图片生成/图生图/flux2_klein_2077688220808208385.json、图片生成/图生图/qwen万能lora控图_1960703410297344001.json、图片生成/图生图/【阡陌】Qwen-Image六合一In Context Controlnet lora精准控制工作流_1960248554344361985.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 5/6 个有
- `ReferenceLatent` —— 5/6 个有
- `AIO_Preprocessor` —— 3/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `EmptySD3LatentImage` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `CFGNorm` —— 1/6 个有
- `GoogleTranslator` —— 1/6 个有
- `Image Compare (mtb)` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `String Literal` —— 1/6 个有
- `TextBox` —— 1/6 个有
- `easy seed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | 4 - 30 | 6 | 19% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 6 | 55% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 0.5 - 1 | 6 | 80% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，观测区间 4 - 30，6 个样本，取值分散，一致性仅 19%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，6 个样本
- 高发问题（4/6 个样本）：Steps较低可能导致细节不足
