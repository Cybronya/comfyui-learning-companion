---
name: unknown_workflow_inpaint_sampler_clip_33
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.914
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, InpaintModelConditioning, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/FLUX 局部重绘_1894670915769380866.json, 平台全量/Fill局部重绘_在线生图_1894395085402865666.json, 平台全量/Flux Fill图像扩展_在线扩图_1894045000794046466.json, 平台全量/Flux Fill局部扩图_1911731826078220289.json, 平台全量/OneReward-fp8-局部重绘&扩图工作流_1966304229801496578.json, 平台全量/扩图_1860178448928083970.json, 平台全量/扩图加局部修复_1852427248119816193.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_33

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/FLUX 局部重绘_1894670915769380866.json、平台全量/Fill局部重绘_在线生图_1894395085402865666.json、平台全量/Flux Fill图像扩展_在线扩图_1894045000794046466.json、平台全量/Flux Fill局部扩图_1911731826078220289.json、平台全量/OneReward-fp8-局部重绘&扩图工作流_1966304229801496578.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxGuidance` —— 6/7 个有
- `ImagePadForOutpaint` —— 5/7 个有
- `Label (rgthree)` —— 3/7 个有
- `ArgosTranslateTextNode` —— 2/7 个有
- `ConstrainImage|pysssss` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `ShowText|pysssss` —— 2/7 个有
- `Anything Everywhere` —— 1/7 个有
- `CLIPTextEncodeFlux` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `RH_Captioner` —— 1/7 个有
- `YC_SingleTextNode` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 7 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | normal | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，7 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 normal，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
