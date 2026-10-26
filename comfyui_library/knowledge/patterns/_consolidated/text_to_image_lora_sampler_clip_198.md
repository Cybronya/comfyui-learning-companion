---
name: text_to_image_lora_sampler_clip_198
type: Text To Image
frequency: 9
level: strong
coverage: 0.750667
common_nodes: [AddNoise, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, ImageScaleBy, KSampler, KSamplerAdvanced, LayerColor: AutoAdjust, LayerFilter: FilmV2, LayerFilter: HDREffects, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, RandomNoise, RepeatLatentBatch, SaveImage, Seed (rgthree), SetNode, ShowText|pysssss, Text Concatenate (JPS), UNETLoader, VAEDecode, VAEEncode, VAELoader, easy positive, easy stylesSelector, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Z参考文生图自选lora_2061648196773965826.json, 图片生成/图生图/Z Image：极致真实的图像，洗图，单图无限裂变_2044574689816743938.json, 图片生成/图生图/Z参考文生图CCD风格_2064560033307914242.json, 图片生成/图生图/Z参考文生图_2061630528536793090.json, 图片生成/文生图/Hui-CCD-nannan_2067420287058141186.json, 图片生成/文生图/Z Image：极致真实的图像，抖音小红书洗图，一键就能拥有，反推出图，文生图，_2044396415601876993.json, 图片生成/文生图/Z纯文生图CCD加强_2064568241581809666.json, 图片生成/文生图/Z纯文生图_2061635410899595265.json, 图片生成/文生图/Z纯文生图自选lora_2061650507298598913.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_198

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/反推提示词/Z参考文生图自选lora_2061648196773965826.json、图片生成/图生图/Z Image：极致真实的图像，洗图，单图无限裂变_2044574689816743938.json、图片生成/图生图/Z参考文生图CCD风格_2064560033307914242.json、图片生成/图生图/Z参考文生图_2061630528536793090.json、图片生成/文生图/Hui-CCD-nannan_2067420287058141186.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 9 个 workflow 都包含：
- `AddNoise`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `ImageScaleBy`
- `KSampler`
- `KSamplerAdvanced`
- `LayerColor: AutoAdjust`
- `LayerFilter: FilmV2`
- `LayerFilter: HDREffects`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `RandomNoise`
- `RepeatLatentBatch`
- `SaveImage`
- `Seed (rgthree)`
- `SetNode`
- `ShowText|pysssss`
- `Text Concatenate (JPS)`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy positive`
- `easy stylesSelector`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `Joy_caption_two_advanced` —— 8/9 个有
- `Joy_caption_two_load` —— 8/9 个有
- `Joy_extra_options` —— 8/9 个有
- `StringFunction|pysssss` —— 8/9 个有
- `easy saveText` —— 7/9 个有
- `CR Prompt List` —— 1/9 个有
- `INTConstant` —— 1/9 个有
- `ImpactSwitch` —— 1/9 个有
- `Int` —— 1/9 个有
- `String Literal` —— 1/9 个有
- `easy boolean` —— 1/9 个有
- `easy ifElse` —— 1/9 个有
- `忽略多组孤海` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 9 | 100% |
| Prompt 约束强度(CFG) | 9 | 9 - 9 | 9 | 100% |
| 采样算法 | 1 | 1 - 1 | 9 | 100% |
| 调度器 | dpmpp_2m | - | 9 | 89% |
| 重绘幅度 | sgm_uniform | - | 9 | 89% |
| 宽度 | 1080 | 1080 - 1088 | 9 | 100% |
| 高度 | 1920 | 1920 - 1920 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 randomize，9 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 9，观测区间 9 - 9，9 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_2m，9 个样本，一致性 89%
- 重绘幅度 最常用 sgm_uniform，9 个样本，一致性 89%
- 宽度 中位数 1080，观测区间 1080 - 1088，9 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
