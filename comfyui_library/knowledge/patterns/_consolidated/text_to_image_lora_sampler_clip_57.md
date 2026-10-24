---
name: text_to_image_lora_sampler_clip_57
type: Text To Image
frequency: 17
level: strong
coverage: 0.860706
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1角色多视图生成，角色一致性设计分镜出图工具_2106135600075202562.json, 图片生成/图生图/Qwen Image 2.1透明图层抠图｜主体分离PNG直出_2103035249222574081.json, 图片生成/图生图/Qwen image 2.1一键模特换装｜服装迁移试衣黑科技｜电商换装省成本_2112088875962290178.json, 图片生成/图生图/Qwen image 2.1人物换脸｜写真级换脸效果自然不穿帮_2111106231317389313.json, 图片生成/图生图/Qwen image 2.1智能换装，图生图服装替换自然贴合_2110528939180515330.json, 图片生成/图生图/Qwen_image_2.1智能换装，图生图服装替换自然贴合_2111273115165749250.json, 图片生成/图生图/Qwen_image_2.1智能换装，服装替换自然贴合图生图_2111952478379003906.json, 图片生成/图生图/qwen image2.1短剧漫剧三视图｜写实人物角色批量出图_2103704294355726338.json, 图片生成/文生图/Qwen Image 2.1图像生成大合集｜文生图图生图反推全都有_2111770424299315201.json, 图片生成/文生图/Qwen Image 2.1图像生成大合集｜文生图海报制作图生图｜一站式出图全家桶_2104759923023372289.json, 图片生成/文生图/Qwen Image 2.1图像编辑｜多场景图片处理全搞定_2106628243129458690.json, 图片生成/文生图/Qwen Image 2.1图像编辑｜文生图图生图全覆盖｜其它图片处理也拿手_2104789567328047105.json, 图片生成/文生图/Qwen Image 2.1生成大合集精简版｜文生图图生图双模式｜日常出图够用了_2104773678444670978.json, 图片生成/文生图/qwen image2.1三视图｜写实人物角色批量出图_2103766316233613313.json, 图片生成/文生图/qwen image2.1写实三视图｜人物角色批量出图 文生图图生图通吃_2104099183790739457.json, 图片生成/文生图/写实角色三视图批量出图 qwen image2.1人物设定一键生成_2104276130005082113.json, 视频生成/图生视频/Qwen_Image_2.1图像生成二十步大合集，全方位图生图能力覆盖_2106178017696505857.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_57

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1角色多视图生成，角色一致性设计分镜出图工具_2106135600075202562.json、图片生成/图生图/Qwen Image 2.1透明图层抠图｜主体分离PNG直出_2103035249222574081.json、图片生成/图生图/Qwen image 2.1一键模特换装｜服装迁移试衣黑科技｜电商换装省成本_2112088875962290178.json、图片生成/图生图/Qwen image 2.1人物换脸｜写真级换脸效果自然不穿帮_2111106231317389313.json、图片生成/图生图/Qwen image 2.1智能换装，图生图服装替换自然贴合_2110528939180515330.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 15/17 个有
- `ResolutionSelector` —— 15/17 个有
- `ComfySwitchNode` —— 14/17 个有
- `PreviewImage` —— 14/17 个有
- `QwenImage21Cache` —— 14/17 个有
- `孤海注释` —— 14/17 个有
- `Anything Everywhere3` —— 11/17 个有
- `LayerUtility: ImageReel` —— 11/17 个有
- `LayerUtility: ImageReelComposit` —— 11/17 个有
- `CR Prompt Text` —— 10/17 个有
- `TextGenerateLTX2Prompt` —— 10/17 个有
- `GetNode` —— 8/17 个有
- `SetNode` —— 8/17 个有
- `ShowText|pysssss` —— 8/17 个有
- `easy setNode` —— 8/17 个有
- `BatchImagesNode` —— 6/17 个有
- `PreviewAny` —— 6/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/17 个有
- `CR Text` —— 4/17 个有
- `Fast Groups Bypasser (rgthree)` —— 4/17 个有
- `ImageConcanate` —— 4/17 个有
- `Latent Switch (JPS)` —— 4/17 个有
- `Seed (rgthree)` —— 4/17 个有
- `easy showAnything` —— 4/17 个有
- `EmptyImage` —— 3/17 个有
- `Int` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 17 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 17 | 100% |
| 采样算法 | er_sde | - | 17 | 100% |
| 调度器 | beta | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |
| 宽度 | 80 | 80 - 80 | 17 | 100% |
| 高度 | 80 | 80 - 80 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 25/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，17 个样本，一致性 100%
- 调度器 最常用 beta，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高发问题（25/17 个样本）：Steps较低可能导致细节不足
