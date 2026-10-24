---
name: unknown_workflow_inpaint_sampler_clip_19
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.900667
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSampler, Kontext Inpainting Conditioning, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext-Inpainting_1945406215578951682.json, 图片生成/图生图/Kontext_inpaint 局部重绘_1946925187003478017.json, 图片生成/图生图/Kontext_inpaint 局部重绘_1948639765250867201.json, 图片生成/图生图/kontext-inpaint-局部重绘-实现画面精准控_1944775964113162241.json, 图片生成/图生图/kontext局部重绘_1967544702801154050.json, 图片生成/图生图/kontext遮罩语义局部重绘_1951220872784883713.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_19

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Kontext-Inpainting_1945406215578951682.json、图片生成/图生图/Kontext_inpaint 局部重绘_1946925187003478017.json、图片生成/图生图/Kontext_inpaint 局部重绘_1948639765250867201.json、图片生成/图生图/kontext-inpaint-局部重绘-实现画面精准控_1944775964113162241.json、图片生成/图生图/kontext局部重绘_1967544702801154050.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `Kontext Inpainting Conditioning`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `RH_Translator` —— 3/6 个有
- `GrowMaskWithBlur` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `MaskPreview+` —— 2/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `ImageAndMaskPreview` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `ImageStitch` —— 1/6 个有
- `LayerMask: MaskGrow` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | 28 - 28 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 28，观测区间 28 - 28，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
