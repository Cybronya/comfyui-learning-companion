---
name: text_to_image_sampler_clip_unet_48
type: Text To Image
frequency: 13
level: strong
coverage: 0.941923
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image_lora  （丝袜版）_1995812666759327745.json, 图片生成/文生图/Z-image基础文生图，zimage文生图_1998203845559902209.json, 图片生成/文生图/Z-image文生图（昆昆）_2044213811187556353.json, 图片生成/文生图/Z-image真实感文生图急速出图_1993918066069356545.json, 图片生成/文生图/Z-image美女IP角色工作流（单图训练的lora）_2008089851932975106.json, 图片生成/文生图/boogu turbo批量文生图_2070386922110930945.json, 图片生成/文生图/boogu turbo文生图批量版_2070336788392144897.json, 图片生成/文生图/boogu turbo文生图批量版_2070422555663622146.json, 图片生成/文生图/boogu turbo文生图批量版_2070469626550644737.json, 图片生成/文生图/krea2文生图批量版_2070339623888441346.json, 图片生成/文生图/krea2文生图批量版_2070388445238878210.json, 图片生成/文生图/krea2文生图批量版_2070421570203508737.json, 图片生成/文生图/krea2文生图批量版_2070468131897827330.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_48

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/Z-image_lora  （丝袜版）_1995812666759327745.json、图片生成/文生图/Z-image基础文生图，zimage文生图_1998203845559902209.json、图片生成/文生图/Z-image文生图（昆昆）_2044213811187556353.json、图片生成/文生图/Z-image真实感文生图急速出图_1993918066069356545.json、图片生成/文生图/Z-image美女IP角色工作流（单图训练的lora）_2008089851932975106.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 11/13 个有
- `PromptBatchQueue` —— 9/13 个有
- `HAIGC_SaveImagesToZip` —— 8/13 个有
- `LoraLoaderModelOnly` —— 4/13 个有
- `CompressImages` —— 1/13 个有
- `Fast Groups Muter (rgthree)` —— 1/13 个有
- `VHS_Unbatch` —— 1/13 个有
- `easy cleanGpuUsed` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1920 | 13 | 73% |
| 高度 | 1536 | 1080 - 1920 | 13 | 86% |
| 采样步数 | 8 | 8 - 10 | 13 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 69% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1920，13 个样本
- 高度 中位数 1536，观测区间 1080 - 1920，13 个样本，取值集中（一致性 86%）
- 采样步数 中位数 8，观测区间 8 - 10，13 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 69%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（10/13 个样本）：Steps较低可能导致细节不足
