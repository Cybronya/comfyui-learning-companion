---
name: text_to_image_lora_sampler_clip_167
type: Text To Image
frequency: 10
level: strong
coverage: 0.85
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/全自动提示词图像编辑 千问image2.1海报改图优化_2104340100669857794.json, 图片生成/图生图/BF16精度Qwen Image 2.1图片编辑，小字不崩的图生图处理方案_2102871104883879938.json, 图片生成/图生图/Qwen Image 2.1一致性保持加图像编辑 角色一致性更强_2109344093791940610.json, 图片生成/图生图/Qwen Image 2.1单图编辑产品展示图生图处理工具_2102489354336821249.json, 图片生成/图生图/Qwen Image 2.1单图编辑流｜局部修改想改哪里改哪里_2108081920897806338.json, 图片生成/图生图/Qwen Image 2.1单图编辑｜图生图局部修改｜一张图也能精修到位_2104763014581940225.json, 图片生成/图生图/Qwen Image 2.1单图编辑｜图生图局部修改｜一张图也能精修到位_2108523054933561346.json, 图片生成/图生图/Qwen Image 2.1单图编辑｜图生图局部修改｜想修哪里修哪里_2107745036996800513.json, 图片生成/图生图/Qwen Image 2.1图像编辑利器｜图生图局部修改一句话搞定_2110685195149074434.json, 图片生成/图生图/Qwen Image 2.1多图编辑｜多参考图融合修改｜批量改图效率翻倍_2104764482592534530.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_167

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/反推提示词/全自动提示词图像编辑 千问image2.1海报改图优化_2104340100669857794.json、图片生成/图生图/BF16精度Qwen Image 2.1图片编辑，小字不崩的图生图处理方案_2102871104883879938.json、图片生成/图生图/Qwen Image 2.1一致性保持加图像编辑 角色一致性更强_2109344093791940610.json、图片生成/图生图/Qwen Image 2.1单图编辑产品展示图生图处理工具_2102489354336821249.json、图片生成/图生图/Qwen Image 2.1单图编辑流｜局部修改想改哪里改哪里_2108081920897806338.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 9/10 个有
- `CR Prompt Text` —— 8/10 个有
- `ComfySwitchNode` —— 8/10 个有
- `ShowText|pysssss` —— 8/10 个有
- `Anything Everywhere3` —— 6/10 个有
- `Seed (rgthree)` —— 6/10 个有
- `CR Text Concatenate` —— 5/10 个有
- `ResizeLongestToNode` —— 5/10 个有
- `TextGenerate` —— 5/10 个有
- `GetNode` —— 2/10 个有
- `Image Comparer (rgthree)` —— 2/10 个有
- `SaveImageAdvanced` —— 2/10 个有
- `SetNode` —— 2/10 个有
- `BatchImagesNode` —— 1/10 个有
- `CompressImages` —— 1/10 个有
- `GetImageSize` —— 1/10 个有
- `QwenPERewriteT8` —— 1/10 个有
- `RHLLMChatNode` —— 1/10 个有
- `Text Multiline` —— 1/10 个有
- `TextGenerateLTX2Prompt` —— 1/10 个有
- `XinbaoImageStandardizer` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（11/10 个样本）：Steps较低可能导致细节不足
