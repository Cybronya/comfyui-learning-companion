---
name: text_to_image_upscale_lora_sampler_58
type: Text To Image
frequency: 5
level: strong
coverage: 0.6638
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyLatentImage, JsonExtractString, KSampler, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextGenerate, UNETLoader, VAEDecode, VAELoader, easy isNone, 孤海注释]
problems: []
missing: []
members: [图片生成/图生图/MOSS一键洗图去AI感，再SeedVR2二段超分直出高清_2116390566152986626.json, 图片生成/图生图/一键转国风工笔画风，SeedVR2超分直出高清细节_2116754879606771714.json, 图片生成/图生图/一键重塑电商主图光影质感，SeedVR2超分直出高清_2116756395403071490.json, 图片生成/图生图/灰霾秒变通透大片光影，SeedVR2超分直出高清风光_2117117338444197889.json, 图片生成/图生图/老照片AI高清翻新，五官构图原样保留，SeedVR2超分直出清晰大图_2117115868466466817.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_58

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/MOSS一键洗图去AI感，再SeedVR2二段超分直出高清_2116390566152986626.json、图片生成/图生图/一键转国风工笔画风，SeedVR2超分直出高清细节_2116754879606771714.json、图片生成/图生图/一键重塑电商主图光影质感，SeedVR2超分直出高清_2116756395403071490.json、图片生成/图生图/灰霾秒变通透大片光影，SeedVR2超分直出高清风光_2117117338444197889.json、图片生成/图生图/老照片AI高清翻新，五官构图原样保留，SeedVR2超分直出清晰大图_2117115868466466817.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：66%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `JsonExtractString`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy isNone`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 3/5 个有
- `ImageConcatMulti` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `VAEEncode` —— 2/5 个有
- `GetNode` —— 1/5 个有
- `SetNode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 5 | 100% |
| Prompt 约束强度(CFG) | 1.5 | 1.5 - 1.5 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 0.6 - 1 | 5 | 77% |
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.5，观测区间 1.5 - 1.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.6 - 1，5 个样本
- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
