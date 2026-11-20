---
name: image_to_image_lora_sampler_unet_86
type: Image To Image
frequency: 9
level: strong
coverage: 0.983556
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/静态Q版角色快速生成可传播短视频。_2029188582170173441.json, 视频生成/图生视频/【老金驿站】下一场景Qwen-edit2509生成工作流_1979088227527200769.json, 视频生成/图生视频/一键佩戴饰品+生成讲解视频_1989475956505104385.json, 视频生成/图生视频/一键换图片背景+生成烧菜视频_1987684744014049282.json, 视频生成/图生视频/一键生成和小时候的自己对话_1987671585945489409.json, 视频生成/图生视频/三图参考生成两个人物对话视频_1987680109538816002.json, 视频生成/图生视频/指定人物对话_1987680874936381442.json, 视频生成/图生视频/生成人物视角转换视频_1987676437924745217.json, 视频生成/文生视频/一句话生成和小时候的自己对话_1987677418305556481.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_86

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（平台全量/静态Q版角色快速生成可传播短视频。_2029188582170173441.json、视频生成/图生视频/【老金驿站】下一场景Qwen-edit2509生成工作流_1979088227527200769.json、视频生成/图生视频/一键佩戴饰品+生成讲解视频_1989475956505104385.json、视频生成/图生视频/一键换图片背景+生成烧菜视频_1987684744014049282.json、视频生成/图生视频/一键生成和小时候的自己对话_1987671585945489409.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveVideo` —— 8/9 个有
- `TextEncodeQwenImageEditPlus` —— 8/9 个有
- `EmptySD3LatentImage` —— 7/9 个有
- `RH_Sora2_I2V` —— 7/9 个有
- `SaveImage` —— 6/9 个有
- `PrimitiveStringMultiline` —— 3/9 个有
- `RH_Kling_Video` —— 1/9 个有
- `RH_Translator` —— 1/9 个有
- `TextEncodeQwenImageEdit` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 9 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
