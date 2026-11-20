---
name: unknown_workflow_inpaint_lora_sampler_59
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.922
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【最简】一键替换-换装_换商品_1934875668926636034.json, 图片生成/图生图/删除指定物体_2053105190848479234.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_59

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/【最简】一键替换-换装_换商品_1934875668926636034.json、图片生成/图生图/删除指定物体_2053105190848479234.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AddMaskForICLora` —— 1/2 个有
- `CLIPVisionLoader` —— 1/2 个有
- `FillMaskWithColor` —— 1/2 个有
- `GrowMask` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `MaskPreview+` —— 1/2 个有
- `StyleModelLoader` —— 1/2 个有
- `YC_LG_Redux` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22.5 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1.165 | - | 2 | 86% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 22.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1.165，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
