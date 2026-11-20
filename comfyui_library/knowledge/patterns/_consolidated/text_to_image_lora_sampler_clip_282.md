---
name: text_to_image_lora_sampler_clip_282
type: Text To Image
frequency: 7
level: strong
coverage: 0.876
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, PrimitiveInt, PrimitiveStringMultiline, RegexExtract, SaveImage, UNETLoader, VAEDecode, VAELoader, YUAN_TXTConvertAny, YUAN_TXTJsonExtractor, YUAN_TXTParagraphSplitter, easy batchAnything, easy forLoopEnd, easy forLoopStart, sch_split_text, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/短剧拍档V11.5 千问qwen image 2.1一键生成人物道具场景资产_2104341680827748353.json, 图片生成/文生图/Krea2版短剧拍档V10.0｜人物道具场景全资产反推提示词图生图_2092557531926327297.json, 图片生成/文生图/image 2版短剧拍档V10.0｜人物道具场景资产一键生成全节点注释_2092554666830811137.json, 图片生成/文生图/场景角色一站式生成 短剧拍档全资产制作支持多图编辑_2098099264600760321.json, 图片生成/文生图/短剧拍档V10.0 Krea2版｜场景角色一键生成全节点注释_2092323335656005634.json, 图片生成/文生图/短剧拍档V11.1一键生成全部资产｜人物道具场景全节点注释_2097936336417284098.json, 图片生成/文生图/短剧拍档资产生成工作流｜人物道具场景一键批量出图_2097851274552233985.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_282

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/反推提示词/短剧拍档V11.5 千问qwen image 2.1一键生成人物道具场景资产_2104341680827748353.json、图片生成/文生图/Krea2版短剧拍档V10.0｜人物道具场景全资产反推提示词图生图_2092557531926327297.json、图片生成/文生图/image 2版短剧拍档V10.0｜人物道具场景资产一键生成全节点注释_2092554666830811137.json、图片生成/文生图/场景角色一站式生成 短剧拍档全资产制作支持多图编辑_2098099264600760321.json、图片生成/文生图/短剧拍档V10.0 Krea2版｜场景角色一键生成全节点注释_2092323335656005634.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RegexExtract`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `YUAN_TXTConvertAny`
- `YUAN_TXTJsonExtractor`
- `YUAN_TXTParagraphSplitter`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `sch_split_text`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `RH_RhartImageG2TextToImage` —— 4/7 个有
- `YuanMultiImage` —— 4/7 个有
- `BasicScheduler` —— 2/7 个有
- `CFGGuider` —— 2/7 个有
- `ComfySwitchNode` —— 2/7 个有
- `KSamplerSelect` —— 2/7 个有
- `PrimitiveBoolean` —— 2/7 个有
- `RandomNoise` —— 2/7 个有
- `SamplerCustomAdvanced` —— 2/7 个有
- `Anything Everywhere3` —— 1/7 个有
- `LoadImage` —— 1/7 个有
- `QwenImage21Cache` —— 1/7 个有
- `ResolutionSelector` —— 1/7 个有
- `Seed (rgthree)` —— 1/7 个有
- `TextEncodeQwenImage21` —— 1/7 个有
- `TextGenerateLTX2Prompt` —— 1/7 个有

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
