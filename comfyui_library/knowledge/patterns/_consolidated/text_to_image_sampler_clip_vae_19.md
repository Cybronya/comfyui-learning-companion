---
name: text_to_image_sampler_clip_vae_19
type: Text To Image
frequency: 8
level: weak
coverage: 0.926875
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/z image -turbo_2028112729524936706.json, 图片生成/文生图/z image 仿真人4视图_2093216503607947265.json, 图片生成/文生图/z image 大头照_2090740353145065474.json, 图片生成/文生图/z image 标准生图+宋玉lora_2078831757402660866.json, 图片生成/文生图/z-image-turbo + flux.2文生图细节_2075264814888341506.json, 图片生成/文生图/z-image_1993900399874818049.json, 图片生成/文生图/千问qwen-image-2.1文生图_2108106051034894338.json, 图片生成/文生图/千问qwen-image-2.1文生图_2112373946829066242.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_19

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/z image -turbo_2028112729524936706.json、图片生成/文生图/z image 仿真人4视图_2093216503607947265.json、图片生成/文生图/z image 大头照_2090740353145065474.json、图片生成/文生图/z image 标准生图+宋玉lora_2078831757402660866.json、图片生成/文生图/z-image-turbo + flux.2文生图细节_2075264814888341506.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 7/8 个有
- `UNETLoader` —— 7/8 个有
- `PreviewImage` —— 6/8 个有
- `ConditioningZeroOut` —— 4/8 个有
- `JjkText` —— 3/8 个有
- `solarL_SaveImagesToZip` —— 2/8 个有
- `EnhancedLoadDiffusionModel` —— 1/8 个有
- `FlashVSRNode` —— 1/8 个有
- `LatentUpscaleBy` —— 1/8 个有
- `LoraLoaderBypassModelOnly` —— 1/8 个有
- `RH_LLMAPI_Pro_Node` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 4 - 30 | 8 | 23% |
| Prompt 约束强度(CFG) | 2 | 1 - 4.5 | 8 | 38% |
| 采样算法 | euler | - | 8 | 50% |
| 调度器 | simple | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 896 | 80 - 1920 | 8 | 34% |
| 高度 | 1184 | 80 - 1920 | 8 | 41% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 4 - 30，8 个样本，取值分散，一致性仅 23%
- Prompt 约束强度(CFG) 中位数 2，观测区间 1 - 4.5，8 个样本，取值分散，一致性仅 38%
- 采样算法 最常用 euler，8 个样本，一致性 50%
- 调度器 最常用 simple，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 896，观测区间 80 - 1920，8 个样本，取值分散，一致性仅 34%
- 高度 中位数 1184，观测区间 80 - 1920，8 个样本，取值分散，一致性仅 41%
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
