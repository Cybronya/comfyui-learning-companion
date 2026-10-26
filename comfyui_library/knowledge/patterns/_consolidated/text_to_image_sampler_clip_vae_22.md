---
name: text_to_image_sampler_clip_vae_22
type: Text To Image
frequency: 6
level: moderate
coverage: 0.907333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/z image -turbo_2028112729524936706.json, 图片生成/文生图/z image 仿真人4视图_2093216503607947265.json, 图片生成/文生图/z image 大头照_2090740353145065474.json, 图片生成/文生图/z image 标准生图+宋玉lora_2078831757402660866.json, 图片生成/文生图/z-image_1993900399874818049.json, 图片生成/文生图/z_image_Doodle style 风格工作流_2014354573992927233.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_22

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/z image -turbo_2028112729524936706.json、图片生成/文生图/z image 仿真人4视图_2093216503607947265.json、图片生成/文生图/z image 大头照_2090740353145065474.json、图片生成/文生图/z image 标准生图+宋玉lora_2078831757402660866.json、图片生成/文生图/z-image_1993900399874818049.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/6 个有
- `UNETLoader` —— 5/6 个有
- `PreviewImage` —— 4/6 个有
- `ConditioningZeroOut` —— 3/6 个有
- `JjkText` —— 2/6 个有
- `EnhancedLoadDiffusionModel` —— 1/6 个有
- `FlashVSRNode` —— 1/6 个有
- `LoraLoaderBypassModelOnly` —— 1/6 个有
- `PIP_StringConcatenation` —— 1/6 个有
- `RH_LLMAPI_Pro_Node` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9.5 | 8 - 30 | 6 | 38% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 6 | 43% |
| 采样算法 | euler | - | 6 | 67% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1024 | 768 - 1920 | 6 | 68% |
| 高度 | 1184 | 1024 - 1920 | 6 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9.5，观测区间 8 - 30，6 个样本，取值分散，一致性仅 38%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，6 个样本，取值分散，一致性仅 43%
- 采样算法 最常用 euler，6 个样本，一致性 67%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 768 - 1920，6 个样本
- 高度 中位数 1184，观测区间 1024 - 1920，6 个样本
- 高发问题（3/6 个样本）：Steps较低可能导致细节不足
