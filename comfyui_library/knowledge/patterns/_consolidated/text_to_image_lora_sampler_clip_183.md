---
name: text_to_image_lora_sampler_clip_183
type: Text To Image
frequency: 9
level: strong
coverage: 0.889667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AI字体设计生成工作流｜快速出艺术字效果｜海报标题排版必备工具_2112033407785066497.json, 图片生成/图生图/G image2.5全能系列模型｜单张成本低至7分钱_2098728369797025793.json, 图片生成/图生图/Z-Image turbo文生图｜又快又好秒出高质量图片_2101537574203514882.json, 图片生成/图生图/hqwa001字体生成工作流，图生图精准输出艺术字设计_2112243051635761153.json, 图片生成/图生图/全能图片G image2.5系列 文生图图生图单张成本低至7分钱_2098662218412941313.json, 图片生成/图生图/大理石美甲摆拍工作流｜穿戴甲产品图商拍级出图_2097206536471924738.json, 图片生成/文生图/Anima文生图 高质量图片生成处理工具_2100652917832376321.json, 图片生成/文生图/Anima文生图｜动漫图像生成一键直出创作_2090189762333335553.json, 图片生成/文生图/Anima生图｜文生图动漫风格_2090465768436752386.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_183

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/AI字体设计生成工作流｜快速出艺术字效果｜海报标题排版必备工具_2112033407785066497.json、图片生成/图生图/G image2.5全能系列模型｜单张成本低至7分钱_2098728369797025793.json、图片生成/图生图/Z-Image turbo文生图｜又快又好秒出高质量图片_2101537574203514882.json、图片生成/图生图/hqwa001字体生成工作流，图生图精准输出艺术字设计_2112243051635761153.json、图片生成/图生图/全能图片G image2.5系列 文生图图生图单张成本低至7分钱_2098662218412941313.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 9 个 workflow 都包含：
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
- `SaveImage` —— 7/9 个有
- `LoraLoader` —— 4/9 个有
- `ClownsharKSampler_Beta` —— 3/9 个有
- `EmptySD3LatentImage` —— 2/9 个有
- `LLGPTImage25Generator` —— 2/9 个有
- `LoadAudio` —— 2/9 个有
- `Qwen3ASRLoader` —— 2/9 个有
- `Qwen3ASRTranscribe` —— 2/9 个有
- `SaveText` —— 2/9 个有
- `easy showAnything` —— 2/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
