---
name: text_to_image_lora_sampler_clip_70
type: Text To Image
frequency: 15
level: strong
coverage: 0.8308
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/小说剧本转JSON预处理｜搭配全栈式短剧生成V4.2.1_2094006895131582465.json, 图片生成/反推提示词/小说剧本转标准JSON预处理搭配全栈式短剧生成V4.2.1使用工具_2105783383883345922.json, 图片生成/反推提示词/小说剧本转标准JSON预处理｜搭配全栈式短剧生成V4.2.1_2093770324671287297.json, 图片生成/反推提示词/小说剧本转标准JSON预处理｜搭配全栈式短剧生成_2097941412695330818.json, 图片生成/反推提示词/视频反推出SKILL-LLM提示词｜看片秒拆解运镜与文案_2111279373436407809.json, 图片生成/反推提示词/视频反推出SKILL-LLM，反推提示词一键提取_2111613256925274114.json, 图片生成/图生图/AI视频变现途径汇总｜推理应用持续更新指南_2092001114597187585.json, 图片生成/图生图/Z-Image turbo文生图｜又快又好秒出高质量图片_2101537574203514882.json, 图片生成/图生图/ins风手持特写LoRA｜穿戴甲图生图重绘不翻车_2097146065999974401.json, 图片生成/图生图/九宫格角色多动作生成｜三视图参考角色表演图生图_2095588740323438593.json, 图片生成/图生图/九宫格角色部件生成｜三视图参考角色设计图生图_2095585736509714434.json, 图片生成/图生图/头像特写角色多表情九宫格｜三视图参考角色设计_2095590124624109570.json, 图片生成/图生图/宠物+坐骑生成器九宫格｜带参考图角色设计_2095254229475745794.json, 图片生成/图生图/角色多动作九宫格｜带角色图参考动作设计生成_2095249943421345794.json, 图片生成/图生图/角色部件九宫格生成｜带角色图参考三视图可用_2095247137901731842.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_70

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/反推提示词/小说剧本转JSON预处理｜搭配全栈式短剧生成V4.2.1_2094006895131582465.json、图片生成/反推提示词/小说剧本转标准JSON预处理搭配全栈式短剧生成V4.2.1使用工具_2105783383883345922.json、图片生成/反推提示词/小说剧本转标准JSON预处理｜搭配全栈式短剧生成V4.2.1_2093770324671287297.json、图片生成/反推提示词/小说剧本转标准JSON预处理｜搭配全栈式短剧生成_2097941412695330818.json、图片生成/反推提示词/视频反推出SKILL-LLM提示词｜看片秒拆解运镜与文案_2111279373436407809.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 15 个 workflow 都包含：
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
- `RHLLMChatNode` —— 12/15 个有
- `PreviewAny` —— 10/15 个有
- `SaveImage` —— 9/15 个有
- `PrimitiveStringMultiline` —— 8/15 个有
- `LoadImage` —— 7/15 个有
- `1hew_ImageGridSplit` —— 6/15 个有
- `RH_RhartImageG2OfficialImageToImage` —— 6/15 个有
- `SaveText` —— 4/15 个有
- `easy saveText` —— 3/15 个有
- `EmptySD3LatentImage` —— 2/15 个有
- `GoohaiDisplayAny` —— 2/15 个有
- `LoadVideo` —— 2/15 个有
- `TextEncodeQwenImageEditPlus` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（16/15 个样本）：Steps较低可能导致细节不足
