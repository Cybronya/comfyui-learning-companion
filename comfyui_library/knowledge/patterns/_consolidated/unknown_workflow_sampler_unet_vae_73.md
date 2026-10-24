---
name: unknown_workflow_sampler_unet_vae_73
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.898
common_nodes: [CLIPLoader, KSampler, LoadImage, PreviewImage, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-image2.1-人像多角度生成_2101942834889838593.json, 图片生成/图生图/Qwen-image2.1-人像多角度生成_2108744184894148609.json, 图片生成/图生图/Qwen-image2.1-人像多角度生成_2110187888993456130.json, 图片生成/图生图/Qwen-image2.1-人物转白模_2107713734658584577.json, 图片生成/图生图/Qwen-image2.1-动作迁移2_2107475110847401986.json, 图片生成/图生图/Qwen-image2.1-单图编辑（4步加速）_2102723958306066433.json, 图片生成/图生图/Qwen-image2.1-图像人像+角度操控（AnyAngl-lora）_2105204359549243394.json, 图片生成/图生图/Qwen-image2.1-最佳换头换脸_2102382946584977410.json, 图片生成/图生图/Qwen-image2.1-最佳换头换脸_2105644895645032449.json, 图片生成/图生图/Qwen-image2.1-最佳换头换脸_2105682659937705986.json, 图片生成/图生图/Qwen-image2.1-角色四视图及三视图生成_2103034276039188481.json, 图片生成/图生图/Qwen-image2.1-透明图层抠图_2102747243479658497.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_73

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Qwen-image2.1-人像多角度生成_2101942834889838593.json、图片生成/图生图/Qwen-image2.1-人像多角度生成_2108744184894148609.json、图片生成/图生图/Qwen-image2.1-人像多角度生成_2110187888993456130.json、图片生成/图生图/Qwen-image2.1-人物转白模_2107713734658584577.json、图片生成/图生图/Qwen-image2.1-动作迁移2_2107475110847401986.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/12 个有
- `LoraLoaderModelOnly` —— 9/12 个有
- `CR Prompt Text` —— 4/12 个有
- `QwenMultiangleCameraNode` —— 4/12 个有
- `easy promptList` —— 4/12 个有
- `easy showAnything` —— 4/12 个有
- `EmptyLatentImage` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 6 - 25 | 12 | 59% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 1560 | - | 1 | 100% |
| 高度 | 904 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 6 - 25，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
