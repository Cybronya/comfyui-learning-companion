---
name: unknown_workflow_sampler_clip_unet_396
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.85
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/cfg zero＋细节守护_1904911641337860097.json, 图片生成/文生图/哥特旗袍女孩v3_1932051517409570818.json, 图片生成/文生图/文生图+网红批量生成器_1891742441647812610.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_396

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/cfg zero＋细节守护_1904911641337860097.json、图片生成/文生图/哥特旗袍女孩v3_1932051517409570818.json、图片生成/文生图/文生图+网红批量生成器_1891742441647812610.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Upscale Image` —— 2/3 个有
- `DetailDaemonSamplerNode` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `CFGZeroStarAndInit` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `DetailDaemonGraphSigmasNode` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `Image Filter Adjustments` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `easy stylesSelector` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 720 - 1024 | 3 | 84% |
| 高度 | 1024 | 1024 - 1280 | 3 | 89% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 720 - 1024，3 个样本，取值集中（一致性 84%）
- 高度 中位数 1024，观测区间 1024 - 1280，3 个样本，取值集中（一致性 89%）
