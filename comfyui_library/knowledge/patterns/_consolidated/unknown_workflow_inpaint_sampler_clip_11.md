---
name: unknown_workflow_inpaint_sampler_clip_11
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.822
common_nodes: [CLIPTextEncode, DualCLIPLoader, InpaintModelConditioning, KSampler, LoadImage, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/Flux最强图片去水印_1948191639301947393.json, 平台全量/flux fill扩图工作流（外补）_1981977128180826113.json, 平台全量/flux1-fill-fp8 扩图_2006242487144288258.json, 平台全量/flux图片外扩工作流_1947228119746957313.json, 平台全量/flux局部重绘-提示词，无参考（待优化）_1897229278893789186.json, 平台全量/flux扩图_1980118779764051970.json, 平台全量/flux重绘工作流_1981978210353192961.json, 平台全量/万物消除工作流 去水印去杂物flux一键消除_1918555823164035074.json, 平台全量/上传图片去水印工作流_1987093778001498114.json, 平台全量/局部重绘，提示词换脸，局部修改_1986676099189010433.json, 平台全量/水印去除工作流_2013814844071350274.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_11

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（平台全量/Flux最强图片去水印_1948191639301947393.json、平台全量/flux fill扩图工作流（外补）_1981977128180826113.json、平台全量/flux1-fill-fp8 扩图_2006242487144288258.json、平台全量/flux图片外扩工作流_1947228119746957313.json、平台全量/flux局部重绘-提示词，无参考（待优化）_1897229278893789186.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxGuidance` —— 10/11 个有
- `UNETLoader` —— 10/11 个有
- `DifferentialDiffusion` —— 9/11 个有
- `Image Comparer (rgthree)` —— 9/11 个有
- `JWImageResizeByLongerSide` —— 7/11 个有
- `Anything Everywhere` —— 5/11 个有
- `PreviewImage` —— 5/11 个有
- `ImagePadForOutpaint` —— 4/11 个有
- `ImageToMask` —— 4/11 个有
- `MaskToImage` —— 4/11 个有
- `Convert Masks to Images` —— 1/11 个有
- `EnhancedLoadDiffusionModel` —— 1/11 个有
- `Image Compare (mtb)` —— 1/11 个有
- `InvertMask` —— 1/11 个有
- `LoadImagesFromDir //Inspire` —— 1/11 个有
- `Note _O` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 28 | 11 | 87% |
| Prompt 约束强度(CFG) | 1 | 1 - 10 | 11 | 0% |
| 采样算法 | dpmpp_2m | - | 11 | 64% |
| 调度器 | sgm_uniform | - | 11 | 64% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 28，11 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 10，11 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 dpmpp_2m，11 个样本，一致性 64%
- 调度器 最常用 sgm_uniform，11 个样本，一致性 64%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
