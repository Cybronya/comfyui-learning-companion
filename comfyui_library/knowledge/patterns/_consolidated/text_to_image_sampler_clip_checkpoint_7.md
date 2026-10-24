---
name: text_to_image_sampler_clip_checkpoint_7
type: Text To Image
frequency: 13
level: moderate
coverage: 0.984923
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/文生图-SDXL_1979279623626330113.json, 图片生成/文生图/文生图-并放大图片工作流_1934952424287182850.json, 图片生成/文生图/文生图-极速-3D卡通_2101863055092178945.json, 图片生成/文生图/文生图基础款-v1_1980214445693689857.json, 图片生成/文生图/文生图基础款1_1851544019800313857.json, 图片生成/文生图/文生图基础款_1818200162132209665.json, 图片生成/文生图/文生图基础款_1830501484281688065.json, 图片生成/文生图/文生图基础款_1851451030012841985.json, 图片生成/文生图/文生图基础款_1902358353320816641.json, 图片生成/文生图/文生图基础款_1907783762778664961.json, 图片生成/文生图/文生图基础款_1908871520008216577.json, 图片生成/文生图/文生图折纸_1788776494500212738.json, 图片生成/文生图/艺术品高清图-青花龙_1778063653963108354.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_7

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/文生图-SDXL_1979279623626330113.json、图片生成/文生图/文生图-并放大图片工作流_1934952424287182850.json、图片生成/文生图/文生图-极速-3D卡通_2101863055092178945.json、图片生成/文生图/文生图基础款-v1_1980214445693689857.json、图片生成/文生图/文生图基础款1_1851544019800313857.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 3/13 个有
- `UpscaleModelLoader` —— 3/13 个有
- `LoraLoader` —— 2/13 个有
- `VAEEncode` —— 2/13 个有
- `Anything Everywhere3` —— 1/13 个有
- `ArgosTranslateTextNode` —— 1/13 个有
- `PreviewImage` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 512 - 1024 | 13 | 79% |
| 高度 | 1024 | 512 - 1024 | 13 | 82% |
| 采样步数 | 20 | 5 - 30 | 13 | 74% |
| Prompt 约束强度(CFG) | 8 | 2 - 8 | 13 | 76% |
| 采样算法 | dpmpp_2m_sde | - | 13 | 69% |
| 调度器 | karras | - | 13 | 77% |
| 重绘幅度 | 1 | 0.3 - 1 | 13 | 73% |
| LoRA 模型强度 | 0.5 | - | 2 | 100% |
| LoRA 文本强度 | 0.65 | - | 2 | 46% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 768，观测区间 512 - 1024，13 个样本
- 高度 中位数 1024，观测区间 512 - 1024，13 个样本，取值集中（一致性 82%）
- 采样步数 中位数 20，观测区间 5 - 30，13 个样本
- Prompt 约束强度(CFG) 中位数 8，观测区间 2 - 8，13 个样本
- 采样算法 最常用 dpmpp_2m_sde，13 个样本，一致性 69%
- 调度器 最常用 karras，13 个样本，一致性 77%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，13 个样本
- LoRA 模型强度 中位数 0.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.65，样本不足，未给区间，2 个样本，取值分散，一致性仅 46%
