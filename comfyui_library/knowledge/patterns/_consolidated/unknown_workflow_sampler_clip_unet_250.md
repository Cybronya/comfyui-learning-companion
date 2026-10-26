---
name: unknown_workflow_sampler_clip_unet_250
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8986
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, InstructPixToPixConditioning, Joy_caption_two, Joy_caption_two_load, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Canny边缘图-JoyCaption提示词反推_1901884242941648898.json, 图片生成/图生图/FLUX_Depth风格迁移-提示词反推_1901994452205117441.json, 图片生成/图生图/FLUX深度控制（精准风格迁移）_1901904698792632322.json, 图片生成/图生图/新版Redux深度风格迁移_在线生图_2036269106093105153.json, 图片生成/图生图/新版Redux深度风格迁移_在线生图_2039978938105073665.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_250

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Canny边缘图-JoyCaption提示词反推_1901884242941648898.json、图片生成/图生图/FLUX_Depth风格迁移-提示词反推_1901994452205117441.json、图片生成/图生图/FLUX深度控制（精准风格迁移）_1901904698792632322.json、图片生成/图生图/新版Redux深度风格迁移_在线生图_2036269106093105153.json、图片生成/图生图/新版Redux深度风格迁移_在线生图_2039978938105073665.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `InstructPixToPixConditioning`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 4/5 个有
- `CLIPVisionEncode` —— 3/5 个有
- `CLIPVisionLoader` —— 3/5 个有
- `ShowText|pysssss` —— 3/5 个有
- `StyleModelApply` —— 3/5 个有
- `StyleModelLoader` —— 3/5 个有
- `DepthAnything_V2` —— 2/5 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 2/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `Label (rgthree)` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `Canny` —— 1/5 个有
- `DF_Image_scale_to_side` —— 1/5 个有
- `DeepTranslatorTextNode` —— 1/5 个有
- `DepthAnythingV2Preprocessor` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 5 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | normal | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 normal，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
