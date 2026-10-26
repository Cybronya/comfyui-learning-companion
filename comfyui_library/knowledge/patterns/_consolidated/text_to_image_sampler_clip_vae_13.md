---
name: text_to_image_sampler_clip_vae_13
type: Text To Image
frequency: 9
level: weak
coverage: 0.927111
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Nunchaku-Qwen-Image文生图lora版_1982417831478345730.json, 图片生成/文生图/boogu 文生图工作流_2072977078944886785.json, 图片生成/文生图/boogu-base-文生图_2068132811814563841.json, 图片生成/文生图/boogu-文生图_2067591707537002497.json, 图片生成/文生图/boogu. image电商海报_2040459014437347330.json, 图片生成/文生图/boogu_base_example_2068252685769461761.json, 图片生成/文生图/boogu_base_文生图-支持复杂提示词_2069073383496708097.json, 图片生成/文生图/boogu_image_turbo 文生图_2074111380944408578.json, 图片生成/文生图/krea 2 文生图工作流_2079525843776393218.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_13

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Nunchaku-Qwen-Image文生图lora版_1982417831478345730.json、图片生成/文生图/boogu 文生图工作流_2072977078944886785.json、图片生成/文生图/boogu-base-文生图_2068132811814563841.json、图片生成/文生图/boogu-文生图_2067591707537002497.json、图片生成/文生图/boogu. image电商海报_2040459014437347330.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 8/9 个有
- `ConditioningZeroOut` —— 7/9 个有
- `PreviewImage` —— 6/9 个有
- `ResolutionSelector` —— 2/9 个有
- `Anything Everywhere3` —— 1/9 个有
- `NunchakuQwenImageDiTLoader` —— 1/9 个有
- `NunchakuQwenImageLoraLoader` —— 1/9 个有
- `NunchakuQwenImageLoraStack` —— 1/9 个有
- `RTXVideoSuperResolution` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 50 | 9 | 1% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 9 | 31% |
| 采样算法 | euler | - | 9 | 56% |
| 调度器 | sgm_uniform | - | 9 | 44% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 1024 | 512 - 1024 | 9 | 71% |
| 高度 | 1024 | 512 - 1536 | 9 | 63% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 50，9 个样本，取值分散，一致性仅 1%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，9 个样本，取值分散，一致性仅 31%
- 采样算法 最常用 euler，9 个样本，一致性 56%
- 调度器 最常用 sgm_uniform，9 个样本，一致性 44%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 512 - 1024，9 个样本
- 高度 中位数 1024，观测区间 512 - 1536，9 个样本
- 高发问题（6/9 个样本）：Steps较低可能导致细节不足
