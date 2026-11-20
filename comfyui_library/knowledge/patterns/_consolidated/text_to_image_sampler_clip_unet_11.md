---
name: text_to_image_sampler_clip_unet_11
type: Text To Image
frequency: 24
level: weak
coverage: 0.818
common_nodes: [Anything Everywhere3, CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Qwen Image 2.1全功能工作流 文生图编辑反推一体工具_2114105118831505410.json, 图片生成/反推提示词/qwen Image 2.1全功能工作流｜文生图反推提示词图生图_2114006893998989313.json, 图片生成/图生图/Qwen Image 2.1 AI短剧漫剧人物三视图，图生图角色一致性设计工具_2103949584014860290.json, 图片生成/图生图/Qwen Image 2.1图像合集人像写真实图生图处理工具_2102543389462982657.json, 图片生成/图生图/Qwen Image 2.1图像生成二十步大合集，全方位图生图能力覆盖_2102828879642714114.json, 图片生成/图生图/Qwen Image 2.1图像生成大合集，场景换装图生图多场景一站式工具_2103254188389130241.json, 图片生成/图生图/Qwen Image 2.1图像生成大合集｜多场景文生图图生图一站搞定_2113572080506724353.json, 图片生成/图生图/Qwen Image 2.1图像生成大合集｜文生图图生图全都有｜收藏一个够用了_2102628402149806081.json, 图片生成/图生图/Qwen Image 2.1工作流合集图生图处理生成工具_2102495775229046786.json, 图片生成/图生图/Qwen Image 2.1工作流合集文生图图生图处理工具_2102555854674419713.json, 图片生成/图生图/Qwen Image 2.1工作流大合集｜图生图多种玩法一网打尽｜新手必存_2102238523955965954.json, 图片生成/图生图/Qwen Image 2.1｜万能输入文生图图生图一体工作流，千问2.1一站式创作_2107281533928300545.json, 图片生成/图生图/Qwen2.1双图版_Flux2Klein自动生成图_2102391245615230977.json, 图片生成/图生图/Qwen2.1双图版｜Flux2Klein自动生成图｜双参考融合效果更自然_2102585557531578370.json, 图片生成/图生图/qwen image2.1短剧漫剧三视图｜写实人物角色批量出图_2103704294355726338.json, 图片生成/文生图/Qwen Image 2.1图像生成大合集｜文生图图生图反推全都有_2111770424299315201.json, 图片生成/文生图/Qwen Image 2.1图像生成大合集｜文生图海报制作图生图｜一站式出图全家桶_2104759923023372289.json, 图片生成/文生图/Qwen Image 2.1图像编辑｜多场景图片处理全搞定_2106628243129458690.json, 图片生成/文生图/Qwen Image 2.1图像编辑｜文生图图生图全覆盖｜其它图片处理也拿手_2104789567328047105.json, 图片生成/文生图/Qwen Image 2.1生成大合集精简版｜文生图图生图双模式｜日常出图够用了_2104773678444670978.json, 图片生成/文生图/qwen image2.1三视图｜写实人物角色批量出图_2103766316233613313.json, 图片生成/文生图/qwen image2.1写实三视图｜人物角色批量出图 文生图图生图通吃_2104099183790739457.json, 图片生成/文生图/写实角色三视图批量出图 qwen image2.1人物设定一键生成_2104276130005082113.json, 视频生成/图生视频/Qwen_Image_2.1图像生成二十步大合集，全方位图生图能力覆盖_2106178017696505857.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_11

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（图片生成/反推提示词/Qwen Image 2.1全功能工作流 文生图编辑反推一体工具_2114105118831505410.json、图片生成/反推提示词/qwen Image 2.1全功能工作流｜文生图反推提示词图生图_2114006893998989313.json、图片生成/图生图/Qwen Image 2.1 AI短剧漫剧人物三视图，图生图角色一致性设计工具_2103949584014860290.json、图片生成/图生图/Qwen Image 2.1图像合集人像写真实图生图处理工具_2102543389462982657.json、图片生成/图生图/Qwen Image 2.1图像生成二十步大合集，全方位图生图能力覆盖_2102828879642714114.json…）

- **类型**：Text To Image
- **样本数**：24
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 24 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 23/24 个有
- `JjkText` —— 23/24 个有
- `LayerUtility: ImageReel` —— 23/24 个有
- `LayerUtility: ImageReelComposit` —— 23/24 个有
- `LoraLoaderModelOnly` —— 23/24 个有
- `PreviewImage` —— 23/24 个有
- `solarL_SaveImagesToZip` —— 23/24 个有
- `ComfySwitchNode` —— 22/24 个有
- `TextGenerateLTX2Prompt` —— 22/24 个有
- `easy setNode` —— 21/24 个有
- `孤海注释` —— 21/24 个有
- `GetNode` —— 20/24 个有
- `SetNode` —— 20/24 个有
- `ShowText|pysssss` —— 19/24 个有
- `PreviewAny` —— 17/24 个有
- `BatchImagesNode` —— 16/24 个有
- `easy showAnything` —— 16/24 个有
- `Fast Groups Bypasser (rgthree)` —— 15/24 个有
- `Seed (rgthree)` —— 14/24 个有
- `EmptyFlux2LatentImage` —— 2/24 个有
- `LoraLoader` —— 2/24 个有
- `RepeatLatentBatch` —— 2/24 个有
- `llama_cpp_instruct_adv` —— 2/24 个有
- `llama_cpp_model_loader` —— 2/24 个有
- `llama_cpp_parameters` —— 2/24 个有
- `EmptyImage` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1024 | 24 | 0% |
| 高度 | 80 | 80 - 1024 | 24 | 0% |
| 采样步数 | 4 | 4 - 20 | 24 | 31% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 24 | 84% |
| 采样算法 | er_sde | - | 24 | 96% |
| 调度器 | beta | - | 24 | 96% |
| 重绘幅度 | 1 | 1 - 1 | 24 | 100% |
| LoRA 模型强度 | 0.4 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 27/24 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1024，24 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，24 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 20，24 个样本，取值分散，一致性仅 31%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，24 个样本，取值集中（一致性 84%）
- 采样算法 最常用 er_sde，24 个样本，一致性 96%
- 调度器 最常用 beta，24 个样本，一致性 96%
- 重绘幅度 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（27/24 个样本）：Steps较低可能导致细节不足
