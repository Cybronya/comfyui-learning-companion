---
name: unknown_workflow_sampler_clip_unet_430
type: Unknown Workflow
frequency: 3
level: strong
coverage: 1
common_nodes: [CLIPTextEncode, DualCLIPLoader, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flex.2-preview-文生图_1917071528809136129.json, 图片生成/文生图/Flex.2-preview文生图演示_1916390487366762498.json, 图片生成/文生图/pl-flux_高清工作流_2058795408276672513.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_430

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Flex.2-preview-文生图_1917071528809136129.json、图片生成/文生图/Flex.2-preview文生图演示_1916390487366762498.json、图片生成/文生图/pl-flux_高清工作流_2058795408276672513.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR SDXL Aspect Ratio` —— 2/3 个有
- `Flex2Conditioner` —— 2/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `MZ_Flux1PartialLoad_Patch` —— 1/3 个有
- `Primitive integer [Crystools]` —— 1/3 个有
- `SDXLEmptyLatentSizePicker+` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 25 | 3 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | deis | - | 3 | 67% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 768x1280 (0.6) | - | 1 | 100% |
| 高度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 25，3 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 deis，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
