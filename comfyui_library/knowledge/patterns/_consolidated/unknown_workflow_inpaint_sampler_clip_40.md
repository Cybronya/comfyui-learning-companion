---
name: unknown_workflow_inpaint_sampler_clip_40
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.983333
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Fill flux OneReward-image expansion扩图_1966338160613601281.json, 图片生成/图生图/Flux Fill局部重绘_1925507801064599554.json, 图片生成/图生图/OneReward-万物移除_1970488228178522114.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_40

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Fill flux OneReward-image expansion扩图_1966338160613601281.json、图片生成/图生图/Flux Fill局部重绘_1925507801064599554.json、图片生成/图生图/OneReward-万物移除_1970488228178522114.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `RH_Translator` —— 2/3 个有
- `GrowMask` —— 1/3 个有
- `InvertMask` —— 1/3 个有
- `LayerUtility: ExtendCanvas` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LayerUtility: TextBox` —— 1/3 个有
- `LoadImageFromUrl` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `Note Plus (mtb)` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
