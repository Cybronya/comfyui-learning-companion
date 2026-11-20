---
name: unknown_workflow_inpaint_clip_unet_4
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.801
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/模特局部修改-Flux_1958484921721503746.json, 图片生成/图生图/灵弦无痕扩图工作流_1932358260127690753.json, 图片生成/图生图/电商图片扩图 FluxOneReward_1992130460604231682.json, 图片生成/图生图/👾怪獸-OneReward局部重绘👾_2014683004244860930.json, 平台全量/002.扩图_2003801675406163970.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_clip_unet_4

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/模特局部修改-Flux_1958484921721503746.json、图片生成/图生图/灵弦无痕扩图工作流_1932358260127690753.json、图片生成/图生图/电商图片扩图 FluxOneReward_1992130460604231682.json、图片生成/图生图/👾怪獸-OneReward局部重绘👾_2014683004244860930.json、平台全量/002.扩图_2003801675406163970.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `InpaintModelConditioning`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `ConditioningZeroOut` —— 3/5 个有
- `ImagePadForOutpaint` —— 3/5 个有
- `CR Text` —— 2/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `DeepTranslatorTextNode` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `ImageAndMaskPreview` —— 1/5 个有
- `KSamplerAdvanced` —— 1/5 个有
- `LayerMask: MaskGrow` —— 1/5 个有
- `easy imageConcat` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 35 | 5 | 0% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | normal | - | 5 | 40% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 35，5 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 normal，5 个样本，一致性 40%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 35，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
