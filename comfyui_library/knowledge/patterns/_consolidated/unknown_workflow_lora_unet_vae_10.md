---
name: unknown_workflow_lora_unet_vae_10
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.789
common_nodes: [CLIPLoader, DrawMaskOnImage, Image Comparer (rgthree), ImagePadForOutpaint, ImageScaleToTotalPixels, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen_image_2.1-无偏移图像智能扩图_2111267209128529922.json, 图片生成/图生图/qwenimage2.1美食静物摄影产品扩图工作流_2110199744910942209.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_unet_vae_10

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Qwen_image_2.1-无偏移图像智能扩图_2111267209128529922.json、图片生成/图生图/qwenimage2.1美食静物摄影产品扩图工作流_2110199744910942209.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `DrawMaskOnImage`
- `Image Comparer (rgthree)`
- `ImagePadForOutpaint`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `EmptyImage` —— 1/2 个有
- `KSampler` —— 1/2 个有
- `KSamplerAdvanced` —— 1/2 个有
- `QwenImage21Cache` —— 1/2 个有
- `Seed (rgthree)` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 20.5 | - | 2 | 5% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- Prompt 约束强度(CFG) 中位数 20.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 5%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 风险：Prompt 约束强度(CFG) 观测到 40，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
