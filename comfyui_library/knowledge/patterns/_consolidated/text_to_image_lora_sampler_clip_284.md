---
name: text_to_image_lora_sampler_clip_284
type: Text To Image
frequency: 7
level: strong
coverage: 0.844143
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveText, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AI字体设计生成工作流｜快速出艺术字效果｜海报标题排版必备工具_2112033407785066497.json, 图片生成/图生图/Qwen Image 2.1 PE提示词强化｜官方优化版｜短句也能写出大片感_2102588489098424321.json, 图片生成/图生图/Qwen Image 2.1提示词强化PE工作流，中文白话输入自动扩写专业提示词出图_2102817681568256001.json, 图片生成/图生图/hqwa001字体生成工作流，图生图精准输出艺术字设计_2112243051635761153.json, 图片生成/图生图/带时间轴的音频转文本 语音内容逐句精准对齐_2104317334918885377.json, 图片生成/图生图/音频转文本带时间轴｜其他实用工具 语音字幕逐句精准对齐_2104072290626527234.json, 视频生成/文生视频/Qwen_Image_2.1提示词强化PE工作流，中文白话输入自动扩写专业提示词出图_2106552276637802498.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_284

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/AI字体设计生成工作流｜快速出艺术字效果｜海报标题排版必备工具_2112033407785066497.json、图片生成/图生图/Qwen Image 2.1 PE提示词强化｜官方优化版｜短句也能写出大片感_2102588489098424321.json、图片生成/图生图/Qwen Image 2.1提示词强化PE工作流，中文白话输入自动扩写专业提示词出图_2102817681568256001.json、图片生成/图生图/hqwa001字体生成工作流，图生图精准输出艺术字设计_2112243051635761153.json、图片生成/图生图/带时间轴的音频转文本 语音内容逐句精准对齐_2104317334918885377.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveText`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 6/7 个有
- `PreviewAny` —— 5/7 个有
- `LoadAudio` —— 4/7 个有
- `QwenPECanvasT8` —— 3/7 个有
- `QwenPERewriteT8` —— 3/7 个有
- `Qwen3ASRLoader` —— 2/7 个有
- `Qwen3ASRLoader_DFT` —— 2/7 个有
- `Qwen3ASRTranscribe` —— 2/7 个有
- `Qwen3ASRTranscribe_DFT` —— 2/7 个有
- `easy showAnything` —— 2/7 个有
- `EmptyImage` —— 1/7 个有
- `PreviewImage` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
