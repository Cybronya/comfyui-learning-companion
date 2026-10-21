---
name: text_to_image_lora_sampler_clip_55
type: Text To Image
frequency: 14
level: strong
coverage: 0.8775
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: [CR Prompt Text]
members: [图片生成/反推提示词/PE提示词加持 Qwen Image 2.1文生图质量跃升_2104336965058514946.json, 图片生成/反推提示词/qwen2.1文生图｜反推提示词加图生图，套图素材批量产出_2104570933620076545.json, 图片生成/图生图/2102216509333528578.json, 图片生成/图生图/2102227263780642818.json, 图片生成/图生图/2102489354336821249.json, 图片生成/图生图/Qwen Image 2.1 PE图像编辑工作流，人像写真图生图其它图片处理方案_2107212690769928193.json, 图片生成/文生图/PE提示词加持 Qwen Image 2.1文生图质量跃升_2104336965058514946.json, 图片生成/文生图/Qwen 2.1文生图4步加速版｜快节奏出图不影响质量_2103063918653558786.json, 图片生成/文生图/Qwen Image 2.1 PE多宫格生图｜一张出九宫排版素材_2103032143940243457.json, 图片生成/文生图/Qwen Image 2.1 PE文生图工作流，人像写真海报制作文本到图像方案_2107215861605031937.json, 图片生成/文生图/Qwen Image 2.1 PE文生图工作流，高质量文本到图像生成方案_2106466665084055554.json, 图片生成/文生图/Qwen Image 2.1 PE文生图，提示词增强高质量文本到图像生成工作流_2103222827108364290.json, 图片生成/文生图/qwen2.1文生图｜反推提示词加图生图，套图素材批量产出_2104570933620076545.json, 图片生成/文生图/稳定加速Tao版 Qwen Image 2.1 PE文生图加图生图编辑_2104352509451137025.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_55

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/反推提示词/PE提示词加持 Qwen Image 2.1文生图质量跃升_2104336965058514946.json、图片生成/反推提示词/qwen2.1文生图｜反推提示词加图生图，套图素材批量产出_2104570933620076545.json、图片生成/图生图/2102216509333528578.json、图片生成/图生图/2102227263780642818.json、图片生成/图生图/2102489354336821249.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 12/14 个有
- `ComfySwitchNode` —— 12/14 个有
- `QwenImage21Cache` —— 12/14 个有
- `easy showAnything` —— 11/14 个有
- `QwenPERewriteT8` —— 9/14 个有
- `easy cleanGpuUsed` —— 9/14 个有
- `LoadImage` —— 5/14 个有
- `QwenImage21BlockCacheT8` —— 4/14 个有
- `QwenImage21SageAttentionT8` —— 4/14 个有
- `QwenImage21SpectrumT8` —— 4/14 个有
- `RHLLMChatNode` —— 3/14 个有
- `PreviewAny` —— 2/14 个有
- `ResizeLongestToNode` —— 2/14 个有
- `ShowText|pysssss` —— 2/14 个有
- `StringConstantMultiline` —— 2/14 个有
- `StringFunction|pysssss` —— 2/14 个有
- `StringReplace` —— 2/14 个有
- `TextGenerate` —— 2/14 个有

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

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高发问题（15/14 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Prompt Text
