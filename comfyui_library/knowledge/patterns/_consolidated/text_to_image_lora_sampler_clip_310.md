---
name: text_to_image_lora_sampler_clip_310
type: Text To Image
frequency: 7
level: strong
coverage: 0.857571
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/提示词优化Moss image Base文生图 高质量加速版工具_2113782529378578433.json, 图片生成/文生图/文生图MOSS文生图2K极速版｜美少女写实风秒出图_2114228750840852482.json, 图片生成/文生图/自动词优化版Moss-image Sft文生图｜描述更省心_2112412795026370562.json, 平台全量/Flux3-klein文生图提示词增强，创意直出更省心_2118511745106014209.json, 平台全量/Flux3-klein文生图提示词增强，创意直出更省心_2118514382316589057.json, 视频生成/文生视频/MOSS SFT ComfyUI官方版工作流，文生视频基础管线稳定可靠_2114560619595788289.json, 视频生成/文生视频/qwen_image_2.1提示词扩写｜一句话自动扩成专业描述｜文生图更省心_2102309278647406593.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_310

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/提示词优化Moss image Base文生图 高质量加速版工具_2113782529378578433.json、图片生成/文生图/文生图MOSS文生图2K极速版｜美少女写实风秒出图_2114228750840852482.json、图片生成/文生图/自动词优化版Moss-image Sft文生图｜描述更省心_2112412795026370562.json、平台全量/Flux3-klein文生图提示词增强，创意直出更省心_2118511745106014209.json、平台全量/Flux3-klein文生图提示词增强，创意直出更省心_2118514382316589057.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 6/7 个有
- `PrimitiveStringMultiline` —— 6/7 个有
- `PreviewImage` —— 5/7 个有
- `TextGenerate` —— 5/7 个有
- `孤海注释` —— 4/7 个有
- `PreviewAny` —— 3/7 个有
- `easy showAnything` —— 3/7 个有
- `CR Prompt Text` —— 2/7 个有
- `ConditioningZeroOut` —— 2/7 个有
- `EmptyImage` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `MOSSImageBlockCacheT8` —— 1/7 个有
- `MOSSImagePromptEnhancerT8` —— 1/7 个有
- `SkipLayerGuidanceDiTSimple` —— 1/7 个有
- `TextEncodeQwenImage21` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（8/7 个样本）：Steps较低可能导致细节不足
