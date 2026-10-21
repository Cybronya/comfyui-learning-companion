---
name: unknown_workflow_upscale_sampler_unet_5
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.678
common_nodes: [GoohaiUniversalSlider, KSamplerAdvanced, LayerFilter: GaussianBlur, LoadImage, SaveImage, SeedVR2Conditioning, SeedVR2PostProcessing, SeedVR2Preprocess, UNETLoader, VAEDecodeTiled, VAEEncodeTiled, VAELoader, VOSR2ModelLoader, VOSR2Upscale, easy imageSizeByLongerSide, 图像缩放V2_孤海, 数学运算_孤海]
problems: []
missing: [LayerFilter: GaussianBlur, 图像缩放V2_孤海, 忽略多组孤海, 数学运算_孤海, easy imageSizeByLongerSide]
members: [图片生成/图生图/2099087328559067138.json, 图片生成/图生图/2102331563605323778.json, 图片生成/文生图/AI高清修复丨VOSR2＋SeedVR2丨双模型放大·细节增强_2108075849978302466.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_unet_5

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/2099087328559067138.json、图片生成/图生图/2102331563605323778.json、图片生成/文生图/AI高清修复丨VOSR2＋SeedVR2丨双模型放大·细节增强_2108075849978302466.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 3 个 workflow 都包含：
- `GoohaiUniversalSlider`
- `KSamplerAdvanced`
- `LayerFilter: GaussianBlur`
- `LoadImage`
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
- `数学运算_孤海`

**可变部分**（部分 workflow 才有）：
- `GH_ImageVideoComparer` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `孤海注释` —— 2/3 个有
- `忽略多组孤海` —— 2/3 个有
- `ComfySwitchNode` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `PrimitiveBoolean` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | sa_solver | - | 3 | 100% |
| 重绘幅度 | beta57 | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 sa_solver，3 个样本，一致性 100%
- 重绘幅度 最常用 beta57，3 个样本，一致性 100%
- 这些节点还没有知识卡，系统对它们的理解有限：LayerFilter: GaussianBlur、图像缩放V2_孤海、忽略多组孤海、数学运算_孤海、easy imageSizeByLongerSide
