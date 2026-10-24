---
name: text_to_image_lora_sampler_clip_77
type: Text To Image
frequency: 15
level: strong
coverage: 0.887333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Moss简洁文生图流程，图生图搭配玩法不设限_2112692396340375554.json, 图片生成/图生图/Qwen Image 2.1图生图工作流，人像写真风格化图生图处理方案_2106885969646542849.json, 图片生成/图生图/Qwen Image 2.1多图编辑图生图处理生成工具_2102506921529004033.json, 图片生成/图生图/Qwen Image 2.1多图编辑文生图图生图处理工作流_2102089735173926914.json, 图片生成/图生图/Qwen Image 2.1官方原版图生图工作流，通义千问7B DiT轻量高效方案_2103198014163742721.json, 图片生成/图生图/Qwen Image 2.1指定抠图模式图生图处理生成工具_2102459788658569217.json, 图片生成/图生图/Qwen Image 2.1文生图图生图处理生成工作流_2102091301226369025.json, 图片生成/图生图/Qwen Image 2.1文生图图生图处理生成工作流_2102101983669866498.json, 图片生成/图生图/Qwen Image 2.1生图及编辑工作流，支持12张参考图一致性最强开源方案_2107154350245240833.json, 图片生成/图生图/Qwen Image 2.1精准抠图工作流，指哪扣哪的交互式图生图体验_2102816199997480961.json, 图片生成/图生图/Qwen Image 2.1自动分镜短剧分镜生成，图生图快速产出故事板_2102850796370096129.json, 图片生成/图生图/Qwen Image 2.1自动分镜短剧分镜生成，图生图快速产出故事板_2103270132993847297.json, 图片生成/图生图/Qwen Image 2.1自动分镜短剧分镜生成，支持三视图参考的图生图工作流_2102897765192916994.json, 图片生成/图生图/Qwen image 2.1图片编辑｜图生图改图如此简单 指哪改哪_2105534138802593793.json, 图片生成/图生图/千问2.1节日表情包生成｜图生图趣味处理｜节庆斗图素材批量做_2104746467230568450.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_77

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/Moss简洁文生图流程，图生图搭配玩法不设限_2112692396340375554.json、图片生成/图生图/Qwen Image 2.1图生图工作流，人像写真风格化图生图处理方案_2106885969646542849.json、图片生成/图生图/Qwen Image 2.1多图编辑图生图处理生成工具_2102506921529004033.json、图片生成/图生图/Qwen Image 2.1多图编辑文生图图生图处理工作流_2102089735173926914.json、图片生成/图生图/Qwen Image 2.1官方原版图生图工作流，通义千问7B DiT轻量高效方案_2103198014163742721.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 14/15 个有
- `TextEncodeQwenImage21` —— 14/15 个有
- `QwenImage21Cache` —— 13/15 个有
- `ComfySwitchNode` —— 10/15 个有
- `ResolutionSelector` —— 10/15 个有
- `CR Text` —— 6/15 个有
- `SaveImageAdvanced` —— 6/15 个有
- `PreviewImage` —— 3/15 个有
- `PrimitiveStringMultiline` —— 3/15 个有
- `QwenPERewriteT8` —— 2/15 个有
- `CreateBoundingBoxes` —— 1/15 个有
- `EmptyFlux2LatentImage` —— 1/15 个有
- `JjkShowText` —— 1/15 个有
- `MOSSImageLayoutPrompt` —— 1/15 个有
- `Note Plus (mtb)` —— 1/15 个有
- `PreviewAny` —— 1/15 个有
- `SkipLayerGuidanceDiTSimple` —— 1/15 个有
- `easy showAnything` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高发问题（16/15 个样本）：Steps较低可能导致细节不足
