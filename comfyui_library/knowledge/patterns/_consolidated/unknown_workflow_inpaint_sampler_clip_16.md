---
name: unknown_workflow_inpaint_sampler_clip_16
type: Unknown Workflow
frequency: 6
level: strong
coverage: 1
common_nodes: [CLIPTextEncode, FluxGuidance, InpaintModelConditioning, KSampler, LoadImage, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/2025-04-15-nunchaku-flux.1-fill_1912069428291301378.json, 图片生成/图生图/FLUX-双截棍局部重绘_1977654014881996802.json, 图片生成/图生图/FLUX局部重绘111_1916028850374119426.json, 图片生成/图生图/FLUX局部重绘_1915624975535898625.json, 图片生成/图生图/Flux-OneReward扩图_1995322323672686594.json, 图片生成/图生图/Nunchaku 加速flux fill无痕扩图_1951927273660338177.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_16

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/2025-04-15-nunchaku-flux.1-fill_1912069428291301378.json、图片生成/图生图/FLUX-双截棍局部重绘_1977654014881996802.json、图片生成/图生图/FLUX局部重绘111_1916028850374119426.json、图片生成/图生图/FLUX局部重绘_1915624975535898625.json、图片生成/图生图/Flux-OneReward扩图_1995322323672686594.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `FluxGuidance`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `NunchakuFluxDiTLoader` —— 5/6 个有
- `ConditioningZeroOut` —— 4/6 个有
- `DifferentialDiffusion` —— 4/6 个有
- `DualCLIPLoader` —— 4/6 个有
- `ImagePadForOutpaintMasked` —— 2/6 个有
- `RH_Translator` —— 2/6 个有
- `ImageToMask` —— 1/6 个有
- `LayerMask: MaskGrow` —— 1/6 个有
- `NunchakuTextEncoderLoader` —— 1/6 个有
- `NunchakuTextEncoderLoaderV2` —— 1/6 个有
- `UNETLoader` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 6 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | normal | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，6 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 normal，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
