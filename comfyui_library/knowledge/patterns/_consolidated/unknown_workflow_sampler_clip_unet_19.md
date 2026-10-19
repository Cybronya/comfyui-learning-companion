---
name: unknown_workflow_sampler_clip_unet_19
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8655
common_nodes: [CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [LayerUtility: PurgeVRAM V2, Primitive string multiline [Crystools]]
members: [comfyui-workflow-templates-json/hidream_i1_dev.json, comfyui-workflow-templates-json/hidream_i1_fast.json, comfyui-workflow-templates-json/hidream_i1_full.json, 图片生成/文生图/1913248213732683777.json, 图片生成/文生图/1913645697319796738.json, 图片生成/文生图/1920089942221848578.json, 图片生成/文生图/1922361267183374337.json, 图片生成/文生图/1922468199466487809.json, 图片生成/文生图/1923682437421780993.json, 图片生成/文生图/1926961584344584194.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_19

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（comfyui-workflow-templates-json/hidream_i1_dev.json、comfyui-workflow-templates-json/hidream_i1_fast.json、comfyui-workflow-templates-json/hidream_i1_full.json、图片生成/文生图/1913248213732683777.json、图片生成/文生图/1913645697319796738.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingSD3` —— 9/10 个有
- `QuadrupleCLIPLoader` —— 9/10 个有
- `CLIPLoader` —— 1/10 个有
- `CLIPTextEncodeHiDream` —— 1/10 个有
- `LayerUtility: PurgeVRAM V2` —— 1/10 个有
- `Primitive string multiline [Crystools]` —— 1/10 个有
- `T5TokenizerOptions` —— 1/10 个有
- `TeaCache` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | 16 - 50 | 10 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 10 | 26% |
| 采样算法 | lcm | - | 10 | 60% |
| 调度器 | simple | - | 10 | 70% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 28，观测区间 16 - 50，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，10 个样本，取值分散，一致性仅 26%
- 采样算法 最常用 lcm，10 个样本，一致性 60%
- 调度器 最常用 simple，10 个样本，一致性 70%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM V2、Primitive string multiline [Crystools]
