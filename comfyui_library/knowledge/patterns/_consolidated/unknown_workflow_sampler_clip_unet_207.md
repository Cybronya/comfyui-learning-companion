---
name: unknown_workflow_sampler_clip_unet_207
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.9765
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/超强文生图Z-image-base_2016185060738732034.json, 图片生成/文生图/超真实文生图 Z-image  zimage   自然真实 没AI感_2046109081471029250.json, 图片生成/文生图/超真实文生图_2044746798295687169.json, 图片生成/文生图/通义千问 Qwen-image文生图丨中文渲染系列出图_1953691322731429889.json, 图片生成/文生图/通义千问Qwen-image文生图_1953143788371906562.json, 图片生成/文生图/通义千问Qwen-image文生图：媲美即梦出图_1952728050552270850.json, 图片生成/文生图/黑森林Flux2文生图_1993588775534133249.json, 平台全量/Qwen-Image参考图风格生成(自动优化提示词)_1985879061081858049.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_207

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/超强文生图Z-image-base_2016185060738732034.json、图片生成/文生图/超真实文生图 Z-image  zimage   自然真实 没AI感_2046109081471029250.json、图片生成/文生图/超真实文生图_2044746798295687169.json、图片生成/文生图/通义千问 Qwen-image文生图丨中文渲染系列出图_1953691322731429889.json、图片生成/文生图/通义千问Qwen-image文生图_1953143788371906562.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 7/8 个有
- `ConditioningZeroOut` —— 4/8 个有
- `CR Text` —— 3/8 个有
- `FluxResolutionNode` —— 2/8 个有
- `CR SDXL Aspect Ratio` —— 1/8 个有
- `Image Filter Adjustments` —— 1/8 个有
- `LoadImage` —— 1/8 个有
- `Lora Loader Stack (rgthree)` —— 1/8 个有
- `RH_LLMAPI_NODE` —— 1/8 个有
- `ShowText` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22.5 | 20 - 50 | 8 | 58% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 8 | 58% |
| 采样算法 | euler | - | 8 | 62% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 22.5，观测区间 20 - 50，8 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，8 个样本
- 采样算法 最常用 euler，8 个样本，一致性 62%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
