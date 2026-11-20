---
name: unknown_workflow_inpaint_sampler_clip_38
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.942833
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, GrowMaskWithBlur, KSampler, Kontext Inpainting Conditioning, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux_Fill 局部重绘 inpaint_1956571084927717377.json, 图片生成/图生图/Kontext Dev inpaint局部重绘_1946788754485833730.json, 图片生成/图生图/Kontext局部重绘工作流_1949015470310600705.json, 平台全量/Flux Kontext Inpainting 局部重绘_1945371001805000706.json, 平台全量/Kontext_局部重绘-Nunchaku加速_1945001408016076802.json, 平台全量/kontext_dev局部重绘_1954145705826906114.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_38

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Flux_Fill 局部重绘 inpaint_1956571084927717377.json、图片生成/图生图/Kontext Dev inpaint局部重绘_1946788754485833730.json、图片生成/图生图/Kontext局部重绘工作流_1949015470310600705.json、平台全量/Flux Kontext Inpainting 局部重绘_1945371001805000706.json、平台全量/Kontext_局部重绘-Nunchaku加速_1945001408016076802.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `GrowMaskWithBlur`
- `KSampler`
- `Kontext Inpainting Conditioning`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `RH_Translator` —— 5/6 个有
- `UNETLoader` —— 5/6 个有
- `Anything Everywhere3` —— 4/6 个有
- `LayerMask: MaskPreview` —— 4/6 个有
- `Mask Fill Holes` —— 4/6 个有
- `Image Comparer (rgthree)` —— 2/6 个有
- `easy imageConcat` —— 2/6 个有
- `DeepTranslatorTextNode` —— 1/6 个有
- `LoraLoader` —— 1/6 个有
- `NunchakuFluxDiTLoader` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
