---
name: text_to_image_lora_sampler_clip_213
type: Text To Image
frequency: 9
level: strong
coverage: 0.900444
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-image-2.1文生图改版角色资产｜角色设计设定图专供_2112855940704849921.json, 图片生成/图生图/qwen-image-2.1多图编辑创意版｜其它图片处理加其他创意玩法｜改图随心_2102260297569488898.json, 图片生成/图生图/qwen-image-2.1官方图生图｜原版工作流稳定不翻车_2103090972849688577.json, 图片生成/图生图/qwen2.1图片编辑 局部修改指令式操作_2104703919430656001.json, 图片生成/图生图/qwen2.1图片编辑局部修改 指令式操作精准改图_2104975240785915906.json, 图片生成/图生图/qwen_image_2.1单图编辑｜换装无偏移角色一致性_2105234290983399426.json, 图片生成/图生图/千问2.1节日表情包生成｜图生图趣味处理｜节庆斗图素材批量做_2104746467230568450.json, 图片生成/图生图/千问Image2.1图像编辑不偏移版，自动优化提示词可抠图商品换背景工具_2103564372319760385.json, 图片生成/图生图/抠图工作流 精准主体识别透明背景生成一键搞定_2105393800863637505.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_213

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen-image-2.1文生图改版角色资产｜角色设计设定图专供_2112855940704849921.json、图片生成/图生图/qwen-image-2.1多图编辑创意版｜其它图片处理加其他创意玩法｜改图随心_2102260297569488898.json、图片生成/图生图/qwen-image-2.1官方图生图｜原版工作流稳定不翻车_2103090972849688577.json、图片生成/图生图/qwen2.1图片编辑 局部修改指令式操作_2104703919430656001.json、图片生成/图生图/qwen2.1图片编辑局部修改 指令式操作精准改图_2104975240785915906.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 8/9 个有
- `QwenImage21Cache` —— 8/9 个有
- `ResolutionSelector` —— 8/9 个有
- `ComfySwitchNode` —— 7/9 个有
- `SaveImageAdvanced` —— 4/9 个有
- `Image Comparer (rgthree)` —— 3/9 个有
- `Text` —— 3/9 个有
- `PreviewImage` —— 2/9 个有
- `QwenPERewriteT8` —— 2/9 个有
- `ShowText|pysssss` —— 2/9 个有
- `Text Multiline` —— 2/9 个有
- `XinbaoImageStandardizer` —— 2/9 个有
- `1hew_AnySwitchSelect` —— 1/9 个有
- `CR Prompt List` —— 1/9 个有
- `CR Text` —— 1/9 个有
- `JjkShowText` —— 1/9 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/9 个有
- `RunningHub SeedXPro Translator` —— 1/9 个有
- `Seed (rgthree)` —— 1/9 个有
- `easy promptLine` —— 1/9 个有

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

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（11/9 个样本）：Steps较低可能导致细节不足
