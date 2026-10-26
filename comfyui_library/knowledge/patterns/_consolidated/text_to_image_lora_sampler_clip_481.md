---
name: text_to_image_lora_sampler_clip_481
type: Text To Image
frequency: 4
level: strong
coverage: 0.87875
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/千问2.1文生图片支持透明底｜文生图海报制作 商品换背景好帮手_2104051581292466177.json, 图片生成/文生图/千问2.1白底商品图｜商业摄影级纯白底｜电商主图批量生成_2104808797784072193.json, 图片生成/文生图/千问Image2.1文生图中文海报自动扩写提示词可抠图，文生图多合一工具_2103561269214277633.json, 图片生成/文生图/微小字体不崩坏 千问image2.1创意海报文生图_2104312640167305218.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_481

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/千问2.1文生图片支持透明底｜文生图海报制作 商品换背景好帮手_2104051581292466177.json、图片生成/文生图/千问2.1白底商品图｜商业摄影级纯白底｜电商主图批量生成_2104808797784072193.json、图片生成/文生图/千问Image2.1文生图中文海报自动扩写提示词可抠图，文生图多合一工具_2103561269214277633.json、图片生成/文生图/微小字体不崩坏 千问image2.1创意海报文生图_2104312640167305218.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 3/4 个有
- `QwenPERewriteT8` —— 2/4 个有
- `SaveImageAdvanced` —— 2/4 个有
- `Seed (rgthree)` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `Text Multiline` —— 2/4 个有
- `ModelAttentionBackend` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `RH_LLMAPI_Pro_Node` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
