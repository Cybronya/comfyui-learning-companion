---
name: unknown_workflow_upscale_sampler_unet_3
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.780333
common_nodes: [GoohaiUniversalSlider, KSamplerAdvanced, LayerFilter: GaussianBlur, LoadImage, SaveImage, SeedVR2Conditioning, SeedVR2PostProcessing, SeedVR2Preprocess, UNETLoader, VAEDecodeTiled, VAEEncodeTiled, VAELoader, VOSR2ModelLoader, VOSR2Upscale, easy imageSizeByLongerSide, 图像缩放V2_孤海, 数学运算_孤海]
problems: []
missing: []
members: [图片生成/图生图/VOSR2+SEEDVR2 图像极速高清修复_2100956577120477185.json, 图片生成/图生图/VOSR2+SEEDVR2极速高清修复_2099087328559067138.json, 图片生成/图生图/VOSR2+SEEDVR2极速高清修复_2102331563605323778.json, 图片生成/图生图/VOSR2+SEEDVR2极速高清修复_2110573178627121154.json, 图片生成/图生图/VOSR2+SEEDVR2极速高清修复_2111274289356951553.json, 图片生成/图生图/VOSR2+SEEDVR2极速高清修复_2113785678315216898.json, 图片生成/图生图/老孙AI 极速高清修复_2109085132496916482.json, 图片生成/文生图/AI高清修复丨VOSR2＋SeedVR2丨双模型放大·细节增强_2108075849978302466.json, 图片生成/文生图/AI高清修复丨VOSR2＋SeedVR2丨双模型放大·细节增强_2110702654283407361.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_unet_3

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/VOSR2+SEEDVR2 图像极速高清修复_2100956577120477185.json、图片生成/图生图/VOSR2+SEEDVR2极速高清修复_2099087328559067138.json、图片生成/图生图/VOSR2+SEEDVR2极速高清修复_2102331563605323778.json、图片生成/图生图/VOSR2+SEEDVR2极速高清修复_2110573178627121154.json、图片生成/图生图/VOSR2+SEEDVR2极速高清修复_2111274289356951553.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 9 个 workflow 都包含：
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
- `PreviewImage` —— 7/9 个有
- `孤海注释` —— 7/9 个有
- `忽略多组孤海` —— 7/9 个有
- `Image Comparer (rgthree)` —— 6/9 个有
- `GH_ImageVideoComparer` —— 3/9 个有
- `ComfySwitchNode` —— 2/9 个有
- `PrimitiveBoolean` —— 2/9 个有
- `EmptyImage` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | 1 | 1 - 1 | 9 | 100% |
| 调度器 | sa_solver | - | 9 | 100% |
| 重绘幅度 | beta57 | - | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，9 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 调度器 最常用 sa_solver，9 个样本，一致性 100%
- 重绘幅度 最常用 beta57，9 个样本，一致性 100%
