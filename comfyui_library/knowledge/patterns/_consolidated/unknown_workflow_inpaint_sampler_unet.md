---
name: unknown_workflow_inpaint_sampler_unet
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.97
common_nodes: [DualCLIPLoader, InpaintModelConditioning, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX+fill超强无痕扩图（在线运行）_1909981995647102977.json, 图片生成/图生图/FLUX-扩图_1914689252691537922.json, 图片生成/图生图/FLUX.1扩图_2055583012271730689.json, 图片生成/图生图/FLUX1-FILL-DEV-FP16扩图工作流_2032094121422233601.json, 图片生成/图生图/FLUX_FILL 【拒绝加班】一键扩图，快狠准_1955539055988523009.json, 图片生成/图生图/FLUX局部重绘_1914505476695097346.json, 图片生成/图生图/FLUX扩图_1900084516772536321.json, 图片生成/图生图/FLUX无缝扩图+高清放大_1915315024124903426.json, 图片生成/图生图/FLUX无缝扩图+高清放大_1917410405457793026.json, 图片生成/图生图/FLUX无缝扩图-工作流_1913971321963802625.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_unet

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/FLUX+fill超强无痕扩图（在线运行）_1909981995647102977.json、图片生成/图生图/FLUX-扩图_1914689252691537922.json、图片生成/图生图/FLUX.1扩图_2055583012271730689.json、图片生成/图生图/FLUX1-FILL-DEV-FP16扩图工作流_2032094121422233601.json、图片生成/图生图/FLUX_FILL 【拒绝加班】一键扩图，快狠准_1955539055988523009.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 10 个 workflow 都包含：
- `DualCLIPLoader`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DifferentialDiffusion` —— 9/10 个有
- `ImagePadForOutpaint` —— 9/10 个有
- `CLIPTextEncode` —— 7/10 个有
- `FluxGuidance` —— 7/10 个有
- `CLIPTextEncodeFlux` —— 3/10 个有
- `SUPIR_Upscale` —— 3/10 个有
- `ConditioningZeroOut` —— 2/10 个有
- `ImageResize+` —— 2/10 个有
- `DF_Image_scale_to_side` —— 1/10 个有
- `EmptySD3LatentImage` —— 1/10 个有
- `LoadImageFromURL` —— 1/10 个有
- `RH_Translator` —— 1/10 个有
- `SDVM Image List Repeat` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 15 - 25 | 10 | 87% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | normal | - | 10 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 15 - 25，10 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 normal，10 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
