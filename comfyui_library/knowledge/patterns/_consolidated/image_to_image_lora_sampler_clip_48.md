---
name: image_to_image_lora_sampler_clip_48
type: Image To Image
frequency: 6
level: strong
coverage: 0.708
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text Replace, Image Comparer (rgthree), ImageResizeKJv2, KSampler, LoadImage, LoraLoaderModelOnly, PMRF, PathchSageAttentionKJ, PreviewAny, PreviewImage, PrimitiveString, Qwen3_VQA, SaveImage, Text Concatenate, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/wan 2.2 超强细节重绘和高清修复_1992597393449308162.json, 图片生成/图生图/wan 2.2 超强细节重绘，高清修复，修正含糊内容及结构_1988960620106100738.json, 图片生成/图生图/wan_2.2_超强细节重绘，高清修复，修正含糊内容及结构_2097868678569222146.json, 图片生成/图生图/wan_2.2_超强细节重绘，高清修复，修正含糊内容及结构_2099408211622322177.json, 图片生成/图生图/最新超强细节重绘及高清修复_1991312599069601794.json, 图片生成/图生图/细节增强_Wan 2.2 超强细节重绘，高清修复_2034615030871760897.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_48

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/wan 2.2 超强细节重绘和高清修复_1992597393449308162.json、图片生成/图生图/wan 2.2 超强细节重绘，高清修复，修正含糊内容及结构_1988960620106100738.json、图片生成/图生图/wan_2.2_超强细节重绘，高清修复，修正含糊内容及结构_2097868678569222146.json、图片生成/图生图/wan_2.2_超强细节重绘，高清修复，修正含糊内容及结构_2099408211622322177.json、图片生成/图生图/最新超强细节重绘及高清修复_1991312599069601794.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Replace`
- `Image Comparer (rgthree)`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PMRF`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveString`
- `Qwen3_VQA`
- `SaveImage`
- `Text Concatenate`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 9 - 9 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | uni_pc | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 0.12 | 0.12 - 0.12 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 9 - 9，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 0.12，观测区间 0.12 - 0.12，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
