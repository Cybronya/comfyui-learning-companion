---
name: text_to_image_lora_sampler_clip_93
type: Text To Image
frequency: 14
level: strong
coverage: 0.894143
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Seedance2.0Mini文生视频，文字转视频高效直出_2111880856880111618.json, 图片生成/文生图/Z-Image Turbo文生图快速高质量处理工具_2101047351329771521.json, 图片生成/文生图/Z-Image-Turbo文生图｜高速出图质量在线新体验_2105251524116041729.json, 图片生成/文生图/Z-Image基本文生图处理生成工作流工具包_2101786053643431937.json, 图片生成/文生图/Z-image文生图 多风格高质量图片生成_2098860674293260290.json, 图片生成/文生图/Z-image真实文生图｜人像写真美少女高质量生成_2096726231373930498.json, 图片生成/文生图/ZIT基础文生图工作流，高质量文本到图像生成方案_2106810710041911298.json, 图片生成/文生图/krea2基础文生图工作流｜物品摄影人像写真生成_2097777800206970882.json, 图片生成/文生图/krea2基础文生图工作流｜物品摄影人像写真生成_2101478583771422722.json, 图片生成/文生图/z-image文生图工作流｜轻量出图响应快，日常配图随手就能出_2099545132960935937.json, 图片生成/文生图/全能图片G-image-2.5文生图高品质版｜一句话出好图，细节给足_2099479665718153217.json, 图片生成/文生图/小腰精体态曲线塑造 文生图一键生成完美身材比例_2104343399116664834.json, 图片生成/文生图/没有AI味文生图｜Z-image Turbo真实模型工作流_2093450819793408001.json, 图片生成/文生图/没有AI味的模型｜Z-image Tubro文生图一键生成_2093784427087360002.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_93

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/Seedance2.0Mini文生视频，文字转视频高效直出_2111880856880111618.json、图片生成/文生图/Z-Image Turbo文生图快速高质量处理工具_2101047351329771521.json、图片生成/文生图/Z-Image-Turbo文生图｜高速出图质量在线新体验_2105251524116041729.json、图片生成/文生图/Z-Image基本文生图处理生成工作流工具包_2101786053643431937.json、图片生成/文生图/Z-image文生图 多风格高质量图片生成_2098860674293260290.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 13/14 个有
- `ConditioningZeroOut` —— 8/14 个有
- `EmptySD3LatentImage` —— 8/14 个有
- `ModelSamplingAuraFlow` —— 7/14 个有
- `PreviewImage` —— 6/14 个有
- `EmptyImage` —— 2/14 个有
- `CompressImages` —— 1/14 个有
- `LoraLoader` —— 1/14 个有
- `RH_RhartImageG25OfficialTokenSunburstTextToImage` —— 1/14 个有
- `RH_RhartVideoSparkvideo20MiniTextToVideo` —— 1/14 个有
- `SaveVideo` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 14 | 100% |
| 采样算法 | er_sde | - | 14 | 100% |
| 调度器 | beta | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 80 | 80 - 80 | 14 | 100% |
| 高度 | 80 | 80 - 80 | 14 | 100% |
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高发问题（23/14 个样本）：Steps较低可能导致细节不足
