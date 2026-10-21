---
name: unknown_workflow_sampler_clip_unet_198
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.954
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSamplerAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-image-蓝色多脑盒-增强随机性版本_1999611975741079553.json, 图片生成/文生图/Z-image文生图（加强随机性）_1999686713578487809.json, 图片生成/文生图/z-image-turbo 无限制模型 + 图形4倍放大 工作流_2018231007891169281.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_198

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-image-蓝色多脑盒-增强随机性版本_1999611975741079553.json、图片生成/文生图/Z-image文生图（加强随机性）_1999686713578487809.json、图片生成/文生图/z-image-turbo 无限制模型 + 图形4倍放大 工作流_2018231007891169281.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/3 个有
- `UpscaleModelLoader` —— 2/3 个有
- `CR Value` —— 1/3 个有
- `ImageSharpen` —— 1/3 个有
- `ImageUpscaleWithModel` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `UltimateSDUpscale` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 928 | 576 - 1080 | 3 | 75% |
| 高度 | 1664 | 1024 - 1920 | 3 | 75% |
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 10 | 9 - 10 | 3 | 95% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | dpmpp_3m_sde | - | 3 | 33% |
| 重绘幅度 | ddim_uniform | - | 3 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 928，观测区间 576 - 1080，3 个样本
- 高度 中位数 1664，观测区间 1024 - 1920，3 个样本
- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，观测区间 9 - 10，3 个样本，取值集中（一致性 95%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_3m_sde，3 个样本，一致性 33%
- 重绘幅度 最常用 ddim_uniform，3 个样本，一致性 67%
