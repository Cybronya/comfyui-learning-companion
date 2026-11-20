---
name: unknown_workflow_lora_unet_vae_8
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.831667
common_nodes: [CLIPLoader, Image Comparer (rgthree), ImageScaleToTotalPixels, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen_image_2.1-无偏移图像智能扩图_2111267209128529922.json, 图片生成/图生图/qwenimage2.1美食静物摄影产品扩图工作流_2110199744910942209.json, 图片生成/图生图/诺亚数字人_Qwen 2.1换脸工作流_2114543156766265345.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_unet_vae_8

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen_image_2.1-无偏移图像智能扩图_2111267209128529922.json、图片生成/图生图/qwenimage2.1美食静物摄影产品扩图工作流_2110199744910942209.json、图片生成/图生图/诺亚数字人_Qwen 2.1换脸工作流_2114543156766265345.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DrawMaskOnImage` —— 2/3 个有
- `ImagePadForOutpaint` —— 2/3 个有
- `KSampler` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `QwenImage21Cache` —— 2/3 个有
- `CR Prompt Text` —— 1/3 个有
- `EmptyImage` —— 1/3 个有
- `KSamplerAdvanced` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 35 | - | 2 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 40 | 3 | 0% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 35，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 40，3 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 40，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
