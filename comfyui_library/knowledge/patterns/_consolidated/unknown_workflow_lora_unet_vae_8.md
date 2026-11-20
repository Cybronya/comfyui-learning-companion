---
name: unknown_workflow_lora_unet_vae_8
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8118
common_nodes: [CLIPLoader, DrawMaskOnImage, Image Comparer (rgthree), LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen_image_2.1-无偏移图像智能扩图_2111267209128529922.json, 图片生成/图生图/qwenimage2.1美食静物摄影产品扩图工作流_2110199744910942209.json, 平台全量/Qwen image 2.1-无偏移图像智能扩图_2110171367919415298.json, 平台全量/Qwen image2.1-万物移除_2105132972881047554.json, 平台全量/Qwen image2.1-图像智能扩图_2105105476529770498.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_unet_vae_8

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen_image_2.1-无偏移图像智能扩图_2111267209128529922.json、图片生成/图生图/qwenimage2.1美食静物摄影产品扩图工作流_2110199744910942209.json、平台全量/Qwen image 2.1-无偏移图像智能扩图_2110171367919415298.json、平台全量/Qwen image2.1-万物移除_2105132972881047554.json、平台全量/Qwen image2.1-图像智能扩图_2105105476529770498.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `DrawMaskOnImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImagePadForOutpaint` —— 4/5 个有
- `KSampler` —— 4/5 个有
- `QwenImage21Cache` —— 4/5 个有
- `Seed (rgthree)` —— 4/5 个有
- `ImageScaleToTotalPixels` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `CR Prompt Text` —— 1/5 个有
- `EmptyImage` —— 1/5 个有
- `KSamplerAdvanced` —— 1/5 个有
- `MaskFillHoles` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 40 | 5 | 0% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 40，5 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 40，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
