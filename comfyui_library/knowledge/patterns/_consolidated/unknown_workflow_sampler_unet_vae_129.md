---
name: unknown_workflow_sampler_unet_vae_129
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.829
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR Text]
members: [图片生成/图生图/2102264547909390337.json, 图片生成/图生图/2102311506384867330.json, 图片生成/图生图/2102380656931196930.json, 图片生成/文生图/Qwen Image 2.1去除ai感_2101954709987872770.json, 图片生成/文生图/qwen image 2.1文生图生_2101747084268498945.json, 数字人/数字人/千问工作流_2102229006685917186.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_129

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/2102264547909390337.json、图片生成/图生图/2102311506384867330.json、图片生成/图生图/2102380656931196930.json、图片生成/文生图/Qwen Image 2.1去除ai感_2101954709987872770.json、图片生成/文生图/qwen image 2.1文生图生_2101747084268498945.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 5/6 个有
- `CR Text` —— 4/6 个有
- `ImageStitch` —— 2/6 个有
- `LoraLoaderModelOnly` —— 2/6 个有
- `孤海注释` —— 2/6 个有
- `EmptyImage` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `PrimitiveBoolean` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 6 | 100% |
| 高度 | 1024 | 560 - 1024 | 6 | 82% |
| 采样步数 | 25 | 25 - 25 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 67% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 560 - 1024，6 个样本，取值集中（一致性 82%）
- 采样步数 中位数 25，观测区间 25 - 25，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 67%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text
