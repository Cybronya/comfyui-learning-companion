---
name: unknown_workflow_lora_sampler_unet_179
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.94375
common_nodes: [CLIPLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen-image2.1-产品融图_2108161171131027457.json, 图片生成/图生图/Qwen-image2.1-产品融图_2112741548281655298.json, 图片生成/图生图/Qwen-image2.1-动漫转真人_2107796380067655682.json, 图片生成/图生图/Qwen2.1 漫转真_2103754802361618433.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_179

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen-image2.1-产品融图_2108161171131027457.json、图片生成/图生图/Qwen-image2.1-产品融图_2112741548281655298.json、图片生成/图生图/Qwen-image2.1-动漫转真人_2107796380067655682.json、图片生成/图生图/Qwen2.1 漫转真_2103754802361618433.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `FastCanvas` —— 2/4 个有
- `InspyrenetRembg` —— 2/4 个有
- `FastCanvasTool` —— 1/4 个有
- `YYZPack_yyz_canvasnodeTool` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 40 | 4 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 40，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
