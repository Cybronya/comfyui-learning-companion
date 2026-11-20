---
name: text_to_image_sampler_clip_unet_118
type: Text To Image
frequency: 6
level: weak
coverage: 0.989667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/2031225025554030594.json, 图片生成/文生图/2031284119526711298.json, 图片生成/文生图/LH-DMT版本-2.生图片类-027.Z-Image五列表文生图-NF_2016493212516487169.json, 图片生成/文生图/Qwen2512超强一致性文生图阿里最新开源模型_2011616403639504897.json, 图片生成/文生图/SD放大_2037862505682313218.json, 图片生成/文生图/Z-image 批量生图+SD放大_1994350300851019778.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_118

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/2031225025554030594.json、图片生成/文生图/2031284119526711298.json、图片生成/文生图/LH-DMT版本-2.生图片类-027.Z-Image五列表文生图-NF_2016493212516487169.json、图片生成/文生图/Qwen2512超强一致性文生图阿里最新开源模型_2011616403639504897.json、图片生成/文生图/SD放大_2037862505682313218.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：99%

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
- `ConditioningZeroOut` —— 4/6 个有
- `UpscaleModelLoader` —— 4/6 个有
- `easy promptList` —— 4/6 个有
- `CR Text` —— 3/6 个有
- `ImageUpscaleWithModel` —— 3/6 个有
- `PreviewTextNode` —— 2/6 个有
- `RHHiddenNodes` —— 2/6 个有
- `UltimateSDUpscale` —— 2/6 个有
- `Int` —— 1/6 个有
- `Text` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 30 | 6 | 36% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 6 | 2% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 896 | 720 - 1536 | 6 | 66% |
| 高度 | 1280 | 1024 - 1536 | 6 | 84% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 30，6 个样本，取值分散，一致性仅 36%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，6 个样本，取值分散，一致性仅 2%
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 896，观测区间 720 - 1536，6 个样本
- 高度 中位数 1280，观测区间 1024 - 1536，6 个样本，取值集中（一致性 84%）
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足
