---
name: text_to_image_lora_sampler_clip_211
type: Text To Image
frequency: 9
level: strong
coverage: 0.880556
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PrimitiveBoolean, QwenImage21Cache, RegexMatch, RegexReplace, SaveImage, SplitImageWithAlpha, StringFormat, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1换装V1高一致性无偏移工作流，图生图换装处理工具_2107534818765533186.json, 图片生成/图生图/Qwen Image 2.1换装V2高一致性无偏移工作流，图生图换装处理工具_2107533328957132801.json, 图片生成/图生图/Qwen Image 2.1换装编辑后人物一致性无偏差服装光影匹配原图加LoRA工作流_2107917971644571650.json, 图片生成/图生图/Qwen-Image-2.1换装V1高一致性版｜模特服装一键替换细节不变形_2107301997392257025.json, 图片生成/图生图/Qwen-Image-2.1换装V1高一致性版｜模特服装一键替换细节不变形_2109522026326224898.json, 图片生成/图生图/Qwen-Image-2.1换装V2高一致性版｜服装替换无偏移不跑版型_2107300495013539841.json, 图片生成/图生图/Qwen-Image-2.1换装V2高一致性版｜服装替换无偏移不跑版型_2109522763051520001.json, 图片生成/图生图/Qwen-Image-2.1高一致性换装，服装展示商品替换自如_2110506858170642433.json, 图片生成/图生图/Qwen-Image-2.1高一致性换装，服装展示商品替换自如_2112347931742392321.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_211

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1换装V1高一致性无偏移工作流，图生图换装处理工具_2107534818765533186.json、图片生成/图生图/Qwen Image 2.1换装V2高一致性无偏移工作流，图生图换装处理工具_2107533328957132801.json、图片生成/图生图/Qwen Image 2.1换装编辑后人物一致性无偏差服装光影匹配原图加LoRA工作流_2107917971644571650.json、图片生成/图生图/Qwen-Image-2.1换装V1高一致性版｜模特服装一键替换细节不变形_2107301997392257025.json、图片生成/图生图/Qwen-Image-2.1换装V1高一致性版｜模特服装一键替换细节不变形_2109522026326224898.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveBoolean`
- `QwenImage21Cache`
- `RegexMatch`
- `RegexReplace`
- `SaveImage`
- `SplitImageWithAlpha`
- `StringFormat`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 8/9 个有
- `DF_Integer` —— 8/9 个有
- `Image Compare (mtb)` —— 8/9 个有
- `ImageScaleToTotalPixels` —— 8/9 个有
- `JWImageResizeByLongerSide` —— 8/9 个有
- `PreviewImage` —— 8/9 个有
- `SeedNode` —— 8/9 个有
- `Text` —— 8/9 个有
- `孤海注释` —— 8/9 个有
- `EmptyImage` —— 3/9 个有
- `Image Comparer (rgthree)` —— 1/9 个有
- `JjkShowText` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
