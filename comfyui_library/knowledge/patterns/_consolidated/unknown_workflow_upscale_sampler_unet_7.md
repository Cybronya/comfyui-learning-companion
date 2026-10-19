---
name: unknown_workflow_upscale_sampler_unet_7
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5385
common_nodes: [GoohaiUniversalSlider, KSamplerAdvanced, LayerFilter: GaussianBlur, LoadImage, PreviewImage, SaveImage, SeedVR2Conditioning, SeedVR2PostProcessing, SeedVR2Preprocess, UNETLoader, VAEDecodeTiled, VAEEncodeTiled, VAELoader, VOSR2ModelLoader, VOSR2Upscale, easy imageSizeByLongerSide, 图像缩放V2_孤海, 孤海注释, 忽略多组孤海, 数学运算_孤海]
problems: []
missing: [LayerFilter: GaussianBlur, 图像缩放V2_孤海, 忽略多组孤海, 数学运算_孤海, easy imageSizeByLongerSide]
members: [图片生成/图生图/2099087328559067138.json, 图片生成/图生图/2102331563605323778.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_unet_7

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/2099087328559067138.json、图片生成/图生图/2102331563605323778.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：54%

## 共有节点

全部 2 个 workflow 都包含：
- `GoohaiUniversalSlider`
- `KSamplerAdvanced`
- `LayerFilter: GaussianBlur`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SeedVR2Conditioning`
- `SeedVR2PostProcessing`
- `SeedVR2Preprocess`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `easy imageSizeByLongerSide`
- `图像缩放V2_孤海`
- `孤海注释`
- `忽略多组孤海`
- `数学运算_孤海`

**可变部分**（部分 workflow 才有）：
- `GH_ImageVideoComparer` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | sa_solver | - | 2 | 100% |
| 重绘幅度 | beta57 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 sa_solver，2 个样本，一致性 100%
- 重绘幅度 最常用 beta57，2 个样本，一致性 100%
- 这些节点还没有知识卡，系统对它们的理解有限：LayerFilter: GaussianBlur、图像缩放V2_孤海、忽略多组孤海、数学运算_孤海、easy imageSizeByLongerSide
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
