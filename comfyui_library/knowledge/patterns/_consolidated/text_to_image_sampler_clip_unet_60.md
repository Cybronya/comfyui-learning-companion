---
name: text_to_image_sampler_clip_unet_60
type: Text To Image
frequency: 8
level: strong
coverage: 0.93875
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image_lora  （丝袜版）_1995812666759327745.json, 图片生成/文生图/boogu turbo文生图_2069610874171641858.json, 图片生成/文生图/boogu turbo文生图_2069633350947663873.json, 图片生成/文生图/boogu turbo文生图_2069634712343244801.json, 图片生成/文生图/boogu turbo文生图急速生图_2069629401351933954.json, 图片生成/文生图/krea2 文生图 无LORA_2093341821593284609.json, 图片生成/文生图/krea2 超真实人物生成2608_2096870221717000194.json, 图片生成/文生图/风格化开源模型krea2_2073230611573207041.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_60

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Z-image_lora  （丝袜版）_1995812666759327745.json、图片生成/文生图/boogu turbo文生图_2069610874171641858.json、图片生成/文生图/boogu turbo文生图_2069633350947663873.json、图片生成/文生图/boogu turbo文生图_2069634712343244801.json、图片生成/文生图/boogu turbo文生图急速生图_2069629401351933954.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 7/8 个有
- `CR Text` —— 6/8 个有
- `LoraLoaderModelOnly` —— 3/8 个有
- `CompressImages` —— 2/8 个有
- `TTResolutionSelector` —— 2/8 个有
- `Fast Groups Muter (rgthree)` —— 1/8 个有
- `VHS_Unbatch` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有
- `忽略多组孤海` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1920 | 8 | 67% |
| 高度 | 1536 | 512 - 1536 | 8 | 72% |
| 采样步数 | 8 | 8 - 10 | 8 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1920，8 个样本
- 高度 中位数 1536，观测区间 512 - 1536，8 个样本
- 采样步数 中位数 8，观测区间 8 - 10，8 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（9/8 个样本）：Steps较低可能导致细节不足
