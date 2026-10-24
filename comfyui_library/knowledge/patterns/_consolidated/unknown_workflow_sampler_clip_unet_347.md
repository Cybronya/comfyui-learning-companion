---
name: unknown_workflow_sampler_clip_unet_347
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.873667
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, InstructPixToPixConditioning, KSampler, LoadImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【上新】Flux canny model example_1860177603104739329.json, 图片生成/图生图/【上新】Flux+depth+lora+example_1860177783379947522.json, 图片生成/图生图/剪纸风格_v1_1882354306815873026.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_347

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/【上新】Flux canny model example_1860177603104739329.json、图片生成/图生图/【上新】Flux+depth+lora+example_1860177783379947522.json、图片生成/图生图/剪纸风格_v1_1882354306815873026.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `InstructPixToPixConditioning`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DepthAnything_V2` —— 2/3 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 2/3 个有
- `Label (rgthree)` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `Canny` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 22 | 3 | 95% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 22，3 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
