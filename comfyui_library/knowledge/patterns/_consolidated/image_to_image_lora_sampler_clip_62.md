---
name: image_to_image_lora_sampler_clip_62
type: Image To Image
frequency: 6
level: strong
coverage: 0.929
common_nodes: [CLIPLoader_Any, CLIPTextEncode, ConditioningZeroOut, Image Comparer (rgthree), ImageScaleToMaxDimension, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader_Any, VAEDecode, VAEEncode, VAELoader_Any]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Repair and Enlarge人像修复放大  质感恢复 婚纱影楼 修复放大_2117057763405811714.json, 图片生成/图生图/修复放大-flux2-特写版_2116135073291526145.json, 图片生成/图生图/修复放大-flux2-特写版_2116473828607086593.json, 图片生成/图生图/修复放大-flux2-特写版_2116498457811841026.json, 平台全量/修复放大 flux2-特写版 Fixed Zoom in flux2—Close-up Editio_2117787015151443969.json, 平台全量/修复放大-flux2-特写版_1904215035462193153.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_62

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Repair and Enlarge人像修复放大  质感恢复 婚纱影楼 修复放大_2117057763405811714.json、图片生成/图生图/修复放大-flux2-特写版_2116135073291526145.json、图片生成/图生图/修复放大-flux2-特写版_2116473828607086593.json、图片生成/图生图/修复放大-flux2-特写版_2116498457811841026.json、平台全量/修复放大 flux2-特写版 Fixed Zoom in flux2—Close-up Editio_2117787015151443969.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader_Any`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `ImageScaleToMaxDimension`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader_Any`
- `VAEDecode`
- `VAEEncode`
- `VAELoader_Any`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
