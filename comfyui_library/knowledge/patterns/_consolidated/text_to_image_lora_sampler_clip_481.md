---
name: text_to_image_lora_sampler_clip_481
type: Text To Image
frequency: 4
level: strong
coverage: 0.952
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/批量去水印v1.0_1997212139112828929.json, 图片生成/图生图/换角度（可以手动调角度）_2017499064656470018.json, 图片生成/图生图/沙雕熊猫头角色qwen_1988475955230498818.json, 平台全量/智能多角度生成_2009549048591687682.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_481

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/批量去水印v1.0_1997212139112828929.json、图片生成/图生图/换角度（可以手动调角度）_2017499064656470018.json、图片生成/图生图/沙雕熊猫头角色qwen_1988475955230498818.json、平台全量/智能多角度生成_2009549048591687682.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `QwenMultiangleCameraNode` —— 2/4 个有
- `ImageResize+` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `RHUploadZip_V2` —— 1/4 个有
- `easy imageConcat` —— 1/4 个有
- `easy imageSize` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1304 | 1280 - 1440 | 4 | 95% |
| 高度 | 1024 | 720 - 1920 | 4 | 57% |
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1304，观测区间 1280 - 1440，4 个样本，取值集中（一致性 95%）
- 高度 中位数 1024，观测区间 720 - 1920，4 个样本
- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
