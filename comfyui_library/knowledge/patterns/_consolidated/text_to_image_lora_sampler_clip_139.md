---
name: text_to_image_lora_sampler_clip_139
type: Text To Image
frequency: 11
level: strong
coverage: 0.877455
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1文生图纯净官流40步无PE，搭配技能高质量文本出图方案_2103260563735400450.json, 图片生成/文生图/Qwen image 2.1 turbo文生图 高质量画面稳定直出_2110355293870837762.json, 图片生成/文生图/Qwen image 2.1 turbo文生图｜画质优化LoRA加持_2112451573052952578.json, 图片生成/文生图/Qwen image 2.1文生图美少女特调｜写实风格出图细腻｜二次元真人两相宜_2102246172638408706.json, 图片生成/文生图/Qwen image 2.1文生图角色四视图V1.1 角色设定批量产出_2109347086192963585.json, 图片生成/文生图/qen image 2.1turbo图片编辑，文生图图生图双修_2111229917986910209.json, 图片生成/文生图/qwen image 2.1 rurbo文生图，高清创意直出_2111281294968709122.json, 图片生成/文生图/qwen image 2.1 rurbo文生图，高清创意直出_2111954037758316546.json, 图片生成/文生图/（文生图）qwen image 2.1 rurbo，高清创意直出_2111591580015620098.json, 视频生成/图生视频/Qwen_image_2.1多图编辑int8版｜自带提示词增强｜图生图低显存友好_2104450980506062849.json, 视频生成/图生视频/qwen_image_2.1编辑工作流｜文生图图生图双支持｜日常改图必备款_2102310384794427394.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_139

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1文生图纯净官流40步无PE，搭配技能高质量文本出图方案_2103260563735400450.json、图片生成/文生图/Qwen image 2.1 turbo文生图 高质量画面稳定直出_2110355293870837762.json、图片生成/文生图/Qwen image 2.1 turbo文生图｜画质优化LoRA加持_2112451573052952578.json、图片生成/文生图/Qwen image 2.1文生图美少女特调｜写实风格出图细腻｜二次元真人两相宜_2102246172638408706.json、图片生成/文生图/Qwen image 2.1文生图角色四视图V1.1 角色设定批量产出_2109347086192963585.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 11 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 10/11 个有
- `TextGenerateLTX2Prompt` —— 10/11 个有
- `孤海注释` —— 9/11 个有
- `easy showAnything` —— 8/11 个有
- `KSamplerSelect` —— 6/11 个有
- `ManualSigmas` —— 6/11 个有
- `SamplerCustom` —— 6/11 个有
- `ComfySwitchNode` —— 4/11 个有
- `BatchImagesNode` —— 3/11 个有
- `LoadImage` —— 3/11 个有
- `SaveImageAdvanced` —— 3/11 个有
- `EmptyImage` —— 2/11 个有
- `Fast Groups Bypasser (rgthree)` —— 2/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/11 个有
- `PreviewImage` —— 2/11 个有
- `PrimitiveBoolean` —— 2/11 个有
- `PixaromaRunTimer` —— 1/11 个有
- `PixaromaSeed` —— 1/11 个有
- `QwenImage21Cache` —— 1/11 个有
- `StringConcatenate` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（12/11 个样本）：Steps较低可能导致细节不足
