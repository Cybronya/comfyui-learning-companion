---
name: text_to_image_sampler_clip_unet_117
type: Text To Image
frequency: 6
level: weak
coverage: 0.883833
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Y1-Image_wan2_2_14B_t2v_1960231389213962242.json, 图片生成/文生图/Z-image文生图_1994684914001977346.json, 图片生成/文生图/boogu-base-文生图_2068132811814563841.json, 图片生成/文生图/boogu-文生图_2067591707537002497.json, 图片生成/文生图/极简中文生图工作流_2070152864193925122.json, 图片生成/文生图/电商生成真实人物图片 MagicWanImage_1991348310250467330.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_117

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Y1-Image_wan2_2_14B_t2v_1960231389213962242.json、图片生成/文生图/Z-image文生图_1994684914001977346.json、图片生成/文生图/boogu-base-文生图_2068132811814563841.json、图片生成/文生图/boogu-文生图_2067591707537002497.json、图片生成/文生图/极简中文生图工作流_2070152864193925122.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 5/6 个有
- `ModelSamplingSD3` —— 2/6 个有
- `EmptyHunyuanLatentVideo` —— 1/6 个有
- `RH_Translator` —— 1/6 个有
- `SDXL Resolutions (JPS)` —— 1/6 个有
- `SeargePromptCombiner` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1376 | 6 | 80% |
| 高度 | 1152 | 768 - 1280 | 6 | 83% |
| 采样步数 | 14.5 | 6 - 50 | 6 | 24% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 6 | 36% |
| 采样算法 | euler | - | 6 | 67% |
| 调度器 | simple | - | 6 | 67% |
| 重绘幅度 | 1 | 0.2 - 1 | 6 | 66% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1376，6 个样本
- 高度 中位数 1152，观测区间 768 - 1280，6 个样本，取值集中（一致性 83%）
- 采样步数 中位数 14.5，观测区间 6 - 50，6 个样本，取值分散，一致性仅 24%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，6 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，6 个样本，一致性 67%
- 调度器 最常用 simple，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.2 - 1，6 个样本
- 高发问题（3/6 个样本）：Steps较低可能导致细节不足
